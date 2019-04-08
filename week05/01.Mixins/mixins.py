import json
from collections import namedtuple
import xml.etree.ElementTree as ET
class Jsonable:
	def to_json(self, indent = 4):
		result = {}
		result.update({'type': str(self.__class__.__name__)})
		result.update({'dict':self.__dict__})
		into_json_format = json.dumps(result, indent = indent)
		return str(into_json_format)

	@classmethod
	def from_json(cls, json_string):
		dictionary = json.loads(json_string)
		obj = dictionary['type']
		d_named = namedtuple(obj, dictionary["dict"].keys())(*dictionary["dict"].values())
		return d_named


class Xmlable:
	def to_xml(self):
		result = ""
		result += "<"+str(self.__class__.__name__)+">"
		for d in self.__dict__:
			result +=  "<"+d+">" + str(self.__dict__[d]) + "</"+d+">" 
		result += "</"+str(self.__class__.__name__)+">"
		return result

	@classmethod
	def from_xml(cls, xml_string):
		root = ET.fromstring(xml_string)
		dictionary = {}
		for child in root:
			dictionary[child.tag]= child.text
		obj = root.tag
		d_named = namedtuple(obj, dictionary.keys())(*dictionary.values())
		return d_named

class Panda(Jsonable, Xmlable):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __eq__(self, other):
		return self.name == other.name and self.age == other.age
