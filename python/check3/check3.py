"""
    CheckPoint3: Practical Physics 
    Explore the behaviour of a damped simple harmonic oscillator for a range of damping coefficients

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
    plt.title("Amplitude of a damped simple harmonic oscillator over time")

    # Adding labels for axes:    
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # Show plot:
    plt.show()

def damp_state(omega_zero, gamma):
    """ Calculates the value of b with damp state (over damped, critically damped and under damped) using omega_zero and gamma."""

    if gamma > 2*omega_zero: # Over Damped
        p = math.sqrt((0.25*gamma**2)-omega_zero**2)
        b = gamma/(2*p)

        return(b, 1, p)
    elif gamma == 2*omega_zero: # Critically Damped
        b = gamma/2

        return(b, 0)
    else: # Under Damped
        w = math.sqrt(omega_zero**2-(0.25*gamma**2))
        b = gamma/(2*w)

        return(b, -1, w)

def shm(omega_zero,gamma,timeList):
    """ Calculates displacement using the quadratic equation."""

    # Lists:
    dispList = []

    # Calling function to calculate damp state:
    damp = damp_state(omega_zero,gamma) #Returns b and True (Over), None (Critically), False (Under)
    print(damp)
    # If/Else to decide equation for displacement:
    if damp[1] == 1: # Over Damped
        p = damp[2]

        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(math.cosh(p*time)+(damp[0]*math.sinh(p*time))))

    elif damp[1] == 0: # Critical Damped
        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(1+damp[0]*time))

    else: # Under Damped
        w = damp[2]

        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(math.cos(w*time)+(damp[0]*math.sin(w*time))))

    return(dispList)

def main(userInput):
    """ Calculates t and calls functions to calculate displacement, amplitude and damp state. """

    # List:
    timeList = [0] # Starting with 0

    # User Input:
    userInput = userInput.split(',')

    # Float conversion: 
    if len(userInput) == 3: 
        gamma = float(userInput[0])
        omega_zero = float(userInput[1])
        pointsToPlot = float(userInput[2])
    else:
        print("ERROR: You need to give gamma, omega zero and the number of points to plot!")

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
main(input("Write the values of gamma, omega zero and points to plot separated by comma (no spaces): "))
