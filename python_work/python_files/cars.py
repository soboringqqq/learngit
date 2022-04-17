cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
a = 'mushrooms' in requested_toppings # check items is in the list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users: # check items is not in the list
	print(user.title() + ", you can post a response if you wish.")

