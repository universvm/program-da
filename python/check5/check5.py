"""
    CheckPoint5: Practical Physics 
	To write a Python program  to display the trajectory and the second to display the relation between final kinetic energy and launch angle.

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

def step_forward(x,y,vx,vy,beta,delta_t):
    """   Do a forward step. """
    return x,y,vx,vy

def acceleration(vx,vy,beta):
    """ Calculate the acceleration. """
    # needed for the calculation of Vy as Vx is constant.
    return(ax,ay)    

def calc_range(vx,vy):
    """ Calculating time to reach the ground and range. """
     
    # Calculate time to reach ground (x = 0):
    td = (2*vy)/9.81

    # Calculating range: 
    range_dist = td*vx

    return(td,range_dist)

def calc_initial(v_initial,theta):
    """ Calculate inital conditions and time to reach the ground. """

    # Calculate velocity x and y:
    vx = v_initial*math.cos(theta)
    vy = v_initial*math.sin(theta)

    # # Calcualte displacement x and y:
    # x = 0 # as x = t * Vx = 0 * Vx = 0
    # y = 0 

    return(vx,vy)

def main(userInput):
    """ Calls functions to parse data input, and calls graph plotter. """

	 # User Input:
    userInput = userInput.split(',')

    # Lists:
    DispListX = [0] # Initial x and y = 0 as x or y = t * Vx or Vy = 0 * Vx or Vy = 0
    DispListY = [0]

    # Converting values to float:
    v_initial = float(userInput[0])
    theta = float(userInput[1])
    beta = float(userInput[2])
    delta_t = float(userInput[3])    

    # Calculating initial conditions:
    vx,vy = calc_initial(v_initial,theta)

    # Calculating range: 
    td,range_dist = calc_range(vx,vy)

    # Printing range:
    print("The range is {0} meters".format(range_dist))

    # Defining temporary variable for while loop:
    t = 0 # initial time = 0

    # While loop to iterate until t = td (i.e. projectile touches the floor):
    while t < td:
        acceleration()

    # Plotting the graph:
    graph_plotter(timeList,powList)

# Asking user for input:
if __name__ == '__main__':
    main(input("Write the magnitude of the initial velocity (m/s), angle (degrees), drag coefficient, step interval (s). Comma separated (no spaces): "))

		