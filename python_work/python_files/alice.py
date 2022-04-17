# def count_words(filename):
	# """Count the approximate number of words in a file."""
	# try:
		# with open(filename, 'rb') as file_object:
			# contents = file_object.read()
	# except FileNotFoundError:
		# msg = "Sorry, the file " + filename + " does not exist."
	# else:
		# # Count the approximate number of words in the files
		# words = contents.split()
		# num_words = len(words)
		# print("The file " + filename + " has about " + str(num_words) + " words.")


# filename = 'alice_in_wonderland.txt'
# count_words(filename)

# def count_words(filename):
	# """Count the approximate number of words in a file."""
	# try:
		# with open(filename, 'rb') as file_object:
			# contents = file_object.read()
	# except FileNotFoundError:
		# pass # nothing happend
	# else:
		# # Count the approximate number of words in the files
		# words = contents.split()
		# num_words = len(words)
		# print("The file " + filename + " has about " + str(num_words) + " words.\n")
		# number_alice = str(words).lower().count('alice')
		# print(str(number_alice) + " number of alice appears in the" + filename)

# filename = 'alice_in_wonderland.txt'
# count_words(filename)


# def count_words(filename):
	# """Count the approximate number of words in a file."""
	# try:
		# with open(filename, 'rb') as file_object:
			# contents = file_object.read()
	# except FileNotFoundError:
		# pass # nothing happend
	# else:
		# # Count the approximate number of words in the files
		# words = contents.split()
		# num_words = len(words)
		# lines = ''
		# for line in words:
			# lines += str(line)
		# lines.replace('b', '\t')
		# print(lines.replace('b', ' '))
		# # print("The file " + filename + " has about " + str(num_words) + " words.\n")
		# # number_alice = str(words).lower().count('alice')
		# # print(str(number_alice) + " number of alice appears in the" + filename)



def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, 'rb') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass # nothing happend
	else:
		print(contents)

filename = 'alice_in_wonderland.txt'
count_words(filename)

