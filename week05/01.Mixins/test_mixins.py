import unittest
from mixins import *
class TestMixinsFromAndToJsonAndXml(unittest.TestCase):

	def test_when_returns_json_file_from_class_object(self):
		p = Panda(name="Ivo",age = 20)
		expected_result = """{
    "type": "Panda",
    "dict": {
        "name": "Ivo",
        "age": 20
    }
}"""


		self.assertEqual(p.to_json(indent = 4),expected_result)

	def test_when_returns_class_object_from_json_file(self):
		p = Panda(name="Ivo",age = 20)
		l = p.to_json()
		l = str(l)
		expected_result = Panda(name='Ivo', age=20)
		self.assertEqual(Panda.from_json(l),expected_result)

	def test_when_returns_xml_file_from_class_object(self):
		p = Panda(name="Ivo",age = 20)
		expected_result = "<Panda><name>Ivo</name><age>20</age></Panda>"
		self.assertEqual(p.to_xml(),expected_result)

	def test_when_returns_class_object_from_xml_file(self):
		p = Panda(name="Ivo",age = 20)
		l = p.to_xml()
		l = str(l)
		#print(from_xml(l))
		expected_result = Panda(name='Ivo', age=20)
		self.assertEqual(Panda.from_xml(l),expected_result)


if __name__ == '__main__':
	unittest.main()
