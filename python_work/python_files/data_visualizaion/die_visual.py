from die import Die
import pygal

# # Creat a D6
# die = Die()

# # Make some rolls, and store result in a list.
# results = []
# for roll_num in range(1000):
	# result = die.roll()
	# results.append(result)

# # Analyze the results
# frequencies = []
# for value in range(1, die.num_sides+1): # loop six times 
	# frequency = results.count(value) # count how many sides in the results
	# frequencies.append(frequency)
# # print(frequencies)

# # Visualize the results.
# hist = pygal.Bar()

# hist.title = "Results of rolling one D6 1000 times"
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6', frequencies)
# hist.render_to_file('die_visual.svg')


# # Creat two D6 dice.
# die_1 = Die()
# die_2 = Die()

# # Make some rolls, and store result in a list.
# results = []
# for roll_num in range(1000):
	# result = die_1.roll() + die_2.roll()
	# results.append(result)

# # Analyze the results
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1): # loop six times 
	# frequency = results.count(value) # count how many sides in the results
	# frequencies.append(frequency)
# # print(frequencies)

# # Visualize the results.
# hist = pygal.Bar()

# hist.title = "Results of rolling two D6 1000 times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6 + D6', frequencies)
# hist.render_to_file('die_visual.svg')

# Creat a D6 and D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store result in a list.
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1): # loop six times 
	frequency = results.count(value) # count how many sides in the results
	frequencies.append(frequency)
# print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
	'13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

