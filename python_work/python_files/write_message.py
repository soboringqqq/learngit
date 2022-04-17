# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
	# file_object.write("I love programming.\n") # write to file only in string
	# file_object.write("I love creating new games.\n")
	
filename = 'programming.txt'

with open(filename, 'a') as file_object: # appending a file add at the end of the file
	file_object.write("I also love finding meaing in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

