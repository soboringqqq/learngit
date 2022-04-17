from die import Die
import pygal


# Creat two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store result in a list.
results = []
results_die_1 = []
results_die_2 = []
two_side_die_1_2 = 0
two_side_die_2_2 = 0
two_side_die_1_3 = 0
two_side_die_1_1 = 0
two_side_die_2_3 = 0
two_side_die_2_1 = 0
for roll_num in range(1000):
	result_die_1 = die_1.roll()
	result_die_2 = die_2.roll()
	
	results_die_1.append(result_die_1)
	results_die_2.append(result_die_2)
	
	result = result_die_1 + result_die_2
	results.append(result)
	# analysis the side from each dice
	if result == 2:
		if result_die_1 == 1:
			two_side_die_1_2 += 1
		if result_die_2 == 1:
			two_side_die_2_2 += 1
			
	if result == 3:
		if result_die_1 == 1:
			two_side_die_1_3 += 1
		else:
			two_side_die_1_1 += 1
			
			
				
			
print('side 1 from dice 1 is ' + str(two_side_die_1_2), '\n')
print('side 1 from dice 2 is ' + str(two_side_die_2_2), '\n')
print('side 1 from dice 1 is ' + str(two_side_die_1_3), '\n')
print('side 2 from dice 1 is ' + str(two_side_die_1_1), '\n')

print('side 2 from dice 2 is ' + str(two_side_die_1_3), '\n')
print('side 1 from dice 2 is ' + str(two_side_die_1_1), '\n')

# Analyze the results
frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for value in range(2, max_sides+1): # loop six times 
	frequency = results.count(value) # count how many sides in the results
	frequencies.append(frequency)
#print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

# print(len(results))






# frequencies_1 = []
# for value_1 in range(1, die_1.num_sides+1):
	# frequency_1 = results_die_1.count(value_1)
	# frequencies_1.append(frequency_1)

# print(frequencies_1, '\n')

# frequencies_2 = []
# for value_2 in range(1, die_2.num_sides+1):
	# frequency_2 = results_die_2.count(value_2)
	# frequencies_2.append(frequency_2)

# print(frequencies_2, '\n')

