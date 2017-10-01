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
    plt.plot(x,y)
    plt.show()

def damp_state(omega_zero, gamma):
    """ Calculates the value of b with damp state (over damped, critically damped and under damped) using omega_zero and gamma."""

    if gamma > 2*omega_zero: # Over Damped
        b = gamma/(2*math.sqrt((gamma**2/4)-omega_zero**2))

        return(b, True)
    elif gamma == 2*omega_zero: # Critically Damped
        b = gamma/2

        return(b, None)
    else: # Under Damped
        b = gamma/(2*math.sqrt(omega_zero**2-(gamma**2/4)))

        return(b, False)

def shm(omega_zero,gamma,timeList):
    """ Calculates displacement using the quadratic equation."""

    # Lists:
    dispList = []

    # Calling function to calculate damp state:
    damp = damp_state(omega_zero,gamma) #Returns b and True (Over), None (Critically), False (Under)

    # If/Else to decide equation for displacement:
    if damp[1] == True: # Over Damped
        p = math.sqrt((gamma**2/4)-omega_zero**2)

        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(math.cosh(p*time)+damp[0]*math.sinh(p*time)))

    elif damp[1] == None: # Under Damped
        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(1+damp[0]*time))

    else:
        w = math.sqrt(omega_zero**2-(gamma**2/4))

        # For loop to solve for displacement and add it to dispList:
        for time in timeList:
            dispList.append(math.exp(-gamma*time/2)*(math.cosh(w*time)+damp[0]*math.sinh(w*time)))

    return(dispList)

def main(userInput):
    """ Calculates t and calls functions to calculate displacement, amplitude and damp state. """

    # List:
    timeList = [0] # Starting with 0

    # User Input:
    userInput = userInput.split(',')
    omega_zero = float(userInput[0])
    gamma = float(userInput[1])

    # Calculating interval:
    interval = ((5*math.pi)/omega_zero)/200

    # Calculating t:
    while len(timeList) < 200: # Create up to 200 values
        timeList.append(timeList[-1]+interval) # Adding interval to the last value in list

    # TODO: create function for amplitude (probably with y axis)
    dispList = shm(omega_zero,gamma,timeList)

    # Plotting the graph:
    graph_plotter(timeList,dispList)

# Asking user for input:
main(input("Write the values of gamma and omega_zero separated by comma (no spaces): "))
