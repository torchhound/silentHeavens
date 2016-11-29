import geojson
from flask_mongoalchemy import MongoAlchemy
from coordGen import coordGen
from nameGen import nameGen

app.config['MONGOALCHEMY_DATABASE'] = 'repository'
db = MongoAlchemy(app)

coordinates = []
names = []
'''
class Star(object):
	def __init__(self, x, y, z, name, starType):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
		self.type = starType

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name, 'type': self.starType)}
'''
class StarSystem(object): #metadata about planets, asteroids, comets, and stations
	def __init__(self, x, y, z, name, planets, asteroids, comets, stations, jumpGate):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
		self.planets = planets
		self.asteroids = asteroids
		self.comets = comets
		self.stations = stations
		self.jumpGate = jumpGate

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name, 'asteroids': self.asteroids, 'comets': self.comets, 'planets': self.planets, 'stations': self.stations, "jumpGate": self.jumpGate)}
'''
class Planet(object):
	def __init__(self, x, y, z, name, moons):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
		self.moons = moons

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name, 'moons': self.moons)}
'''
class Blackhole(object):
	def __init__(self, x, y, z, name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name)}
'''
class Station(object):
	def __init__(self, x, y, z, name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name)}

class JumpGate(object):
	def __init__(self, x, y, z, name, output):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
		self.output = output

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name, 'output': self.output)}
'''
class AsteroidField(object):
	def __init__(self, x, y, z, name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name

	@property
	def __geo_interface__(self):
		return {'type': 'Feature', 'coordinates': (self.x, self.y, self.z), 'properties': ('name': self.name)}

def coordCheck(x, y, z):
	global coordinates
	tup = (x, y, z)
	if tup in coordinates:
		return False
	else:
		coordinates.append(tup)

def nameCheck(name):
	global names
	if name in names:
		return False
	else:
		names.append(name)

def addStarSystem(starSystem): #not sure about this
	try:
		starSystem.save()
	except Exception as e:
		print(e)
		pass #return False?

def main(): #10k star systems


if __name__ == "__main__":
	main()