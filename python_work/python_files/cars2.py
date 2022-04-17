""" A class that can be used to represnet a car."""
class Car():
	""" simple attempt to respresent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# print("\n")
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# print("\n")









class ElectricCar(Car):
	"""Respresnet aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery_size = 70
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-Kwh battery")

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
	
