# try: # try-except block
	# print(5/0)
# except ZeroDivisionError:
	# print("You can't divide by zero!")

# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit")

# while True:
	# first_number = input("\nFirst number: ")
	# if first_number == 'q':
		# break
	# second_number = input("\nSecond number: ")
	# if second_number == 'q':
		# break
	# answer = int(first_number) / int(second_number)
	# print(answer)

# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit")

# while True:
	# first_number = input("\nFirst number: ")
	# if first_number == 'q':
		# break
	# second_number = input("\nSecond number: ")
	# try:
		# answer = int(first_number) / int(second_number) # the only code cause an exception to be rised in the try block
	# except ZeroDivisionError:
		# print("You can't divide by 0!")
	# else:
		# print(answer)
		
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	try:
		answer = int(first_number) / int(second_number) # the only code cause an exception to be rised in the try block
	except ZeroDivisionError:
		print("You can't divide by 0!")
	except ValueError: # rised a value error using except to avoid traceback
		print("Pleas enter a value")
	else:
		print(answer)
