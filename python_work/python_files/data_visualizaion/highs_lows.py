import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_2018_full.csv'
# with open(filename) as f:
	# reader = csv.reader(f)
	# header_row = next(reader)
	# #print(header_row)
	
	# for index, column_header in enumerate(header_row):
		# print(index, column_header)

# Get high temperatures from file.

# filename = 'sitka_weather_2018_simple.csv'
filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	for row in reader:
		# handel no empty data in csv
		try:
			current_date =datetime.strptime(row[2], "%Y-%m-%d")
			high = int(row[4])
			low = int(row[6])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			
		# current_date = datetime.strptime(row[2], "%Y-%m-%d")
		# dates.append(current_date)
		
		# high = int(row[5])
		# highs.append(high)
		
		# low = int(row[6])
		# lows.append(low)

	#print(highs)
	
# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue') # plot second data
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # fill between two data 

#plt.fill_between(dates, highs, facecolor='blue', alpha=0.1)

# Format plot.
# plt.title("Daily high and low temperature, July 2018", fontsize=24)
plt.title("Daily high and low temperature, - 2018\n Death Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
