import unittest
from music_library import *
class TestMusicLibrary(unittest.TestCase):
	songs = []
	def setUp(self):
		self.q = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:50")
		self.code_songs = Playlist(name="Code song", repeat=True, shuffle = True)
		self.mc = MusicCrawler("mymusic.json")

	def test_when_returned_object_is_from_class_Song(self): 
		self.assertIsInstance(self.q, Song)

	def test_when_returns_length_of_a_song(self): 
		self.assertEqual(self.q.get_length(), '3:50')
		self.assertEqual(self.q.get_length(seconds = False, minutes = False, hours = True), 0)
		self.assertEqual(self.q.get_length(seconds = False, minutes = True, hours = False), 3)
		self.assertEqual(self.q.get_length(seconds = True, minutes = False, hours = False), 230)

	def test_when_returned_object_is_from_class_Playlist(self): 
		self.assertIsInstance(self.code_songs, Playlist)

	def test_when_add_song(self):
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.add_song(self.q)
		self.assertEqual(str(a),"[Odin Manowar 'The Sons of Odin' 3:50, Odin Manowar 'The Sons of Odin' 3:50]")

	def test_when_remove_song(self):
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.remove_song(self.q)
		self.assertEqual(str(a),"[Odin Manowar 'The Sons of Odin' 3:50]")

	def test_when_returns_hist_of_artists_in_a_playlist(self):
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.add_song(self.q)
		self.assertEqual(self.code_songs.artists(),{'Manowar': 2})

	def test_when_returns_next_song(self):
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.add_song(self.q)
		self.assertEqual(str(self.code_songs.next_song()),"Odin Manowar 'The Sons of Odin' 3:50")

	def test_when_returns_total_length_of_a_playlist(self):
		a = self.code_songs.add_song(self.q)
		a = self.code_songs.add_song(self.q)
		self.assertEqual(self.code_songs.total_length(),"7:40")

	def test_when_returned_object_is_from_class_MusicCrawler(self): 
		self.assertIsInstance(self.mc, MusicCrawler)

if __name__ == '__main__':
	unittest.main()
