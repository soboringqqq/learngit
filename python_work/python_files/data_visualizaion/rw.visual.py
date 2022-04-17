import matplotlib.pyplot as plt

from random_walk import RandomWalk

# # Make a  random walk, and plot the points. generate onece
# rw = RandomWalk()
# rw.fill_walk()

# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

# Keep making new walks, as long as the program is active.
# while True:
	# rw = RandomWalk()
	# rw.fill_walk()

	# plt.scatter(rw.x_values, rw.y_values, s=15)
	# plt.show()
	
	# keep_running = input("Make another walk? (y/n): ")
	# if keep_running == 'n':
		# break

# # Color map each points
# while True:
	# rw = RandomWalk()
	# rw.fill_walk()
	
	# point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		# edgecolor='none', s=15)
	# plt.show()
	
	# keep_running = input("Make another walk? (y/n): ")
	# if keep_running == 'n':
		# break
		

# # start walk and end walk
# while True:
	# rw = RandomWalk()
	# rw.fill_walk()
	
	# point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		# edgecolor='none', s=15)
	
	# # Emphasize the first and last points
	# plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
		# s=100)
		
	# plt.show()
	
	# keep_running = input("Make another walk? (y/n): ")
	# if keep_running == 'n':
		# break
		
# cleaning up the axes
while True:
	rw = RandomWalk()
	rw.fill_walk()
	
	plt.figure(figsize=(10, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=15)
	
	# Emphasize the first and last points
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
		s=100)
	
	# Remove the axes.
	#plt.axes().get_xaxis().set_visible(False)
	#plt.axes().get_yaxis().set_visible(False)
	
	plt.axis('off')
		
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break


