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
    plt.title("Log power of a circuit measured at 25 kHz")

    # Adding labels for axes:    
    plt.xlabel("Time")
    plt.ylabel("Power")

    # Show plot:
    plt.show()

def logpower(voltage,current):
    """ Calculates the value of p from voltage and current"""

    # Lists:
    powList = []

    # For loop to calculate power:
    for i in range(len(voltage)): # For each item in the length of voltage
        power = math.log(float(voltage[i])*float(current[i])) # Log base e of V * I
        powList.append(power) # appending calculated value to list

    # Return the list of power:
    return(powList)

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

    # Lists:
    timeList = [0]

    # Performing Log Calculations:
    powList = logpower(data_lists[0],data_lists[1])

    # Calculating time interval:
    hertz_reciprocal = float(1)/float(25000)

    # Calculating timeList:
    while len(timeList) < len(powList): # Create the same n. of values as power values
        timeList.append(timeList[-1]+hertz_reciprocal) # Adding interval to the last value in list

    # Plotting the graph:
    graph_plotter(timeList,powList)

# Asking user for input:
if __name__ == '__main__':
    main(input("Write the name of the file to parse (sample or short): "))

		