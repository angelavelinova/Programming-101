import unittest
from car_racing import *
class TestCarRace(unittest.TestCase):

	def test_when_opens_valid_json_file_and_returns_object_from_type_data(self):
		inf = read_json()
		self.assertEqual(inf, {'people': [{'name': 'Ivo', 'car': 'Opel', 'model': 'Astra', 'max_speed': 240}, {'name': 'Rado', 'car': 'Pegeout', 'model': '107', 'max_speed': 180}, {'name': 'Slavqna', 'car': 'Opel', 'model': 'Meriva', 'max_speed': 300}, {'name': 'Pavlin', 'car': 'AUDI', 'model': 'R8', 'max_speed': 380}]})

	def test_when_creates_object_from_type_car(self):
		a = Car("BMW", 320,160)
		self.assertIsInstance(a,Car)

	def test_when_creates_object_from_type_driver(self):
		c = Car("BMW", 320,160)
		a = Driver("John", c)
		self.assertIsInstance(a,Driver)

	def test_when_creates_object_from_type_race(self):
		c = Car("BMW", 320,140)
		a = Driver("John", c)
		r = Race(a,0.7)
		self.assertIsInstance(r,Race)

	def test_when_creates_object_from_type_championship(self):
		ch = Championship("ch1", 3)
		self.assertIsInstance(ch,Championship)



if __name__ == '__main__':
	unittest.main()
