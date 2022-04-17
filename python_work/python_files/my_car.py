#from cars2 import Car, ElectricCar # import multiple class

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

import cars2 # import entire module

my_new_car = cars2.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = cars2.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
