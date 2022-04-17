import matplotlib.pyplot as plt

# input_x = [0, 4]
# input_y = [1, 1]  
# plt.scatter(2, 4) # plot a point 
# plt.plot(input_x, input_y) # plot a x axis line
# plt.show()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)

# plt.scatter(x_values, y_values,edgecolor='none', s=40) # no edgecolor 

# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40) # change color

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) # color map

plt.axis([0, 1100, 0, 1100000])

#plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight') # save figure
