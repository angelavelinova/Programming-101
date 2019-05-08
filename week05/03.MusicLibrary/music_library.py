import datetime
import random
import json
import mutagen
import os

class Song:

	def __init__(self, title, artist, album, length):
		self.title = title
		self.artist = artist
		self.album = album
		self.length = length

	@property
	def is_valid_length(self):
		i = 0
		while i < len(self.length):
			if not self.length[i].isdigit() and not self.length[i] == ':':
					return False
			i += 1

		array = self.length.split(':')
		i = 0
		while i < len(array):
			if array[i] < '0' or array[i] > '59':
				return False
			i += 1
		if len(array) == 2:
			if int(array[0]) >= 0 and int(array[1]) > 0 and int(array[1]) < 60:
					return True

		if len(array) == 3:
			if int(array[0]) > 0 and int(array[1]) > 0 and int(array[1]) < 60 and int(array[2]) > 0 and int(array[2]) < 60:
					return True

	def __str__(self):
		if self.is_valid_length:
			return "{} {} '{}' {}".format(self.title, self.artist, self.album, self.length)
		raise Exception("Invalid length !!!")

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length

	def __hash__(self):
		return hash((self.title, self.artist, self.album, self.length))
	
	def get_length(self, seconds = False, minutes = False, hours = False):
		time_parts = self.length.split(':')
		if len(time_parts) == 2:
			length_in_seconds = int(time_parts[1]) + int(time_parts[0])*60
			length_in_minutes = int(time_parts[0])
			length_in_hours = 0
		if len(time_parts) == 3:
			length_in_hours = int(time_parts[0])
			length_in_minutes = int(time_parts[0])*60 + int(time_parts[1])
			length_in_seconds = int(time_parts[2]) + int(length_in_minutes*60)
		if seconds:
			return length_in_seconds
		if minutes:
			return length_in_minutes
		if hours:
			return length_in_hours
		else:
			return(str(self.length))

class Playlist:

	def __init__(self, name, repeat=False, shuffle=False):
		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle
		self.songs = []
		self.songs_location = {}
		self.song_ind = 0

	def add_song(self, song):
		if isinstance(song, Song):
			self.songs.append(song)
		return self.songs

	def remove_song(self, song):
		i = 0
		while self.songs[i] != song:
			i += 1
		j = i
		while j < len(self.songs)-1:
			self.songs[j]=self.songs[j+1]
			j += 1

		self.songs = self.songs[0:len(self.songs)-1]
		return self.songs

	def total_length(self):
		total = ""
		hours = 0
		minutes = 0
		seconds = 0
		for i in range(0, len(self.songs)):
			current_time_array = self.songs[i].length.split(':')
			if len(current_time_array)==2:
				minutes += int(current_time_array[0])
				seconds += int(current_time_array[1])
			if len(current_time_array)==3:
				hours += int(current_time_array[0])
				minutes += int(current_time_array[1])
				seconds += int(current_time_array[2])
		s = seconds % 60
		new_m = (seconds - s)//60
		minutes += new_m
		m = minutes % 60
		new_h = (minutes - m)//60
		hours += new_h
		if hours > 0:
			total += str(hours) + ":"
		total += str(m) + ":" + str(s)

		return total

	def artists(self):
		data = []
		for i in range(0, len(self.songs)):
			artist = self.songs[i].artist
			song = self.songs[i].title
			data.append((artist, song))
		hist = {}
		for i in data:
			hist[i] = hist.get(i,0)+1
		result_hist = {}
		for i in hist:
			result_hist[i[0]] = hist[(i[0],i[1])]

		return result_hist

	def next_song(self):
		if self.song_ind == len(self.songs) - 1:
			if self.repeat == True:
				self.song_ind = 0

		if self.shuffle == True:
			self.song_ind = random.randint(0, len(self.songs)-1)
			
		return self.songs[self.song_ind]


	def print_playlist(self):
		print("| ", "Artist ", " | ", "       Song       ", " | ", " Length ", "  |" )
		print("|", "--------", " | ", "------------------", " | ", "--------", "  |" )
		for i in range(0,len(self.songs)):
			res = "| " + str(self.songs[i].artist)+ "   |  "
			title_space = len("------------------")- len(str(self.songs[i].title))
			res += str(self.songs[i].title)
			while title_space > 0:
				res += " "
				title_space -= 1
			res += "  |   "

			title_space = len("-------- ")- len(str(self.songs[i].length))
			res += str(self.songs[i].length)
			while title_space > 0:
				res += " "
				title_space -= 1
			res += " |"

			print(res)


	def save(self):
		d = {}
		for i in range(0, len(self.songs)):
			data = {}
			data["title"] = self.songs[i].title
			data["artist"] = self.songs[i].artist
			data["album"] = self.songs[i].album
			data["length"] = self.songs[i].length
			d[i] = data
		
		filename = ""
		for i in range(0, len(self.name)):
			if self.name[i]==" ":
				filename += "-"
			else:
				filename += self.name[i]
		filename += ".json"
		with open(filename,'w') as f:
			json.dump(d,f)
		return filename

	@classmethod
	def load(file_name):
		with open(file_name, 'r') as f:
			content = json.load(f)
			playlist = Playlist(content["name"])
			for song in content["songs"]:
				new_song = Song(
					artist=song["artist"], title=song["title"], album=song["album"], length=song["length"])
				playlist.add_song(new_song)
			return playlist

	def add_location(self, song, location):
		self.songs_location[song] = location


class MusicCrawler:

	def __init__(self, path):
		self.path = path

	def get_info(self, data):
		song_data = {}
		song_data["artist"] = data.get(["ARTIST"].text[0], "Unknown")
		song_data["album"] = data.get(["ALBUM"].text[0], "Unknown")
		song_data["title"] = data.get(["TITLE"].text[0], "Unknown")
		try:
			song_data["length"] = str(
				datetime.timedelta(seconds=data.info.length//1))[2:]
		except:
			song_data["length"] = "Unknown"
		return song_data

	def generate_playlist(self, name):
		playlist = Playlist(name)
		songs = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith(".mp3")]
		for song in songs:
			data = mutagen.File(self.path + "/" + song)
			info = self.get_info(data)
			new_song = Song(
				artist=info["artist"], title=info["title"], album=info["album"], length=info["length"])
			playlist.add_song(new_song)
			playlist.add_location(new_song, self.path + "/" + song)
		return playlist
