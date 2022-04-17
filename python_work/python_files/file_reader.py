# with open('pi_digits.txt') as file_object: # read entire file
	# contents = file_object.read()
	# #print(contents)
	# print(contents.rstrip())

# filename = 'pi_digits.txt'

# with open(filename) as file_object: # read line by line
	# for line in file_object:
		# #print(line)
		# print(line.rstrip())


# filename = 'pi_digits.txt'

# with open(filename) as file_object: # make list of the file
	# lines = file_object.readlines()

# for line in lines:
	# print(line.rstrip())

# with open(filename) as file_object: # make list of the file
	# lines = file_object.readlines()

# pi_string = ''
# for line in lines:
	# pi_string += line.strip()
	
# print(pi_string)
# print(len(pi_string))

# with open(filename) as file_object: # uisng numerical value in the file
	# lines = file_object.readlines()

# pi_number = 0
# for line in lines:
	# pi_number += float(line.strip())
	
# print(str(pi_number))
# print(len(str(pi_number)))

filename = 'pi_million_digits.txt'

# with open(filename) as file_object: # make list of the file
	# lines = file_object.readlines()

# pi_string = ''
# for line in lines:
	# pi_string += line.strip()
	
# print(pi_string[:52] + "...") # read first 50 decimal places
# print(len(pi_string))

with open(filename) as file_object: # make list of the file
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()
	
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")

