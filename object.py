# a class is a recipe
# an object is the food you made with the recipe
# the recipe can be used lots, and lots of times

# our blueprint for making cars is called car
class Car(object):
	# whenever we start making a new car, __init__ will run
	# we always pass self first
	def __init__(self):
		# self is special
		# self refers to this object
		self.make = "Chevy"
		self.model = "Sonic"
		self.year = 2013
	def changeModel(self,newModel):
		self.model = newModel
myCar = Car()
print myCar.make
print myCar.year
print myCar.model
yourCar = Car()
yourCar.make = "Ford"
yourCar.model = "Mustang"
yourCar.year = 2018
print yourCar.make
print yourCar.model
print yourCar.year
yourCar.changeModel("bentley")
print yourCar.model


