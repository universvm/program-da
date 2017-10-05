"""
    CheckPoint4: Practical Physics 
	To write a Python program to read in data from a text file in a specified format, perform some simple processing and display the output using pyplot.

    Author: Leonardo Castorina

"""
# Modules:
import math
import matplotlib.pyplot as plt

# Functions:
def graph_plotter(x,y):
    # Plotting x and y:
    plt.plot(x,y)

    # Adding title: 
    # TODO: FIX LABELS
    plt.title("Amplitude of a damped simple harmonic oscillator over time")

    # Adding labels for axes:    
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # Show plot:
    plt.show()

def logpower(voltage,current):
    """ Calculates the value of p from """

        return(b, -1, w)

def file_parser(fileInput):
	""" Parses the values in the file and returns volList and curList."""
	
	# Lists:
	volList = []
	curList = []

	# For loop to parse the data:
	for line in fileInput:
		# Ignoring the comments:
		if line.startswith('#'):
			continue
		else:
			# Creating a list by splitting by ' , ':
			line = line.split(' , ')

			# Appending the values to the lists:
			volList.append(line[0])
			curList.append(line[1])
	
	# Return the 2 list:
	return(volList,curList)		

def main(userInput):
    """ Calls functions to parse data files, logpower and graph plotter """

    # Opening file:
	data_file = open('data/{0}.txt'.format(userInput), 'r')

    # Parsing User Input:
    data_lists = file_parser(data_file)

    # Performing Log Calculations:
    logpower(data_lists[0],data_lists[1]) 
   
    # Calculating interval:
    interval = ((5*math.pi)/omega_zero)/pointsToPlot

    # Calculating t:
    while len(timeList) < pointsToPlot: # Create up to "pointsToPlot" values
        timeList.append(timeList[-1]+interval) # Adding interval to the last value in list

    # Calculate displacement/amplitude: 
    dispList = shm(omega_zero,gamma,timeList)

    # Plotting the graph:
    graph_plotter(timeList,dispList)

# Asking user for input:
if __name__ == '__main__':
	main(input("Write the name of the file to parse (sample or short): "))

		