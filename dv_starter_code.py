import matplotlib.pyplot as plt # import portion of library we want to use

# data
months = ['May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'March', 'April']
total_rainfall = [<your total monthly rainfall goes here>] # comma separated list of decimal values
average_temp = [<your average monthly temperature in degrees F goes here>] # comman separated list of decimal values

color = 'blue' # color for axis labels for total rainfall 
fig, ax1 = plt.subplots() # generate a figure with one axis
ax1.set_xlabel('Month') # x-axis label
ax1.set_ylabel('Total Rainfall (inches)') # left y-axis
ax1.bar(months, total_rainfall, color=color) # generate a bar graph of total_rainfall
ax1.tick_params(axis='y', labelcolor=color) # place tick marks with values on left y-axis

ax2 = ax1.twinx() # generate another y-axis to appear on the right side - shares the same x-axis

color = 'red'
ax2.set_ylabel('Average Temperature (F)')
ax2.plot(months, average_temp, linestyle='--', marker='o', color=color) # plot points w/ markers and dashed connected line
ax2.tick_params(axis='y', labelcolor=color) # place tick marks with values on right y-axis

plt.title("Total Rainfall and Average Temperature - Allentown Area 2024") # title the graph
fig.tight_layout() # makes figure fit nicely in area
plt.show() # creates the final graph

