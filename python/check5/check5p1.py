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
    plt.title("Projectile Motion Trajectory")

    # Adding labels for axes:    
    plt.xlabel("Displacement x (m)")
    plt.ylabel("Displacement y (m)")

    # Show plot:
    plt.show()

def step_forward(vx,vy,ax,ay,delta_t,td):
    """   Do a forward step. """

    # Lists:
    dispListX = [0] # Initial x and y = 0 as x or y = t * Vx or Vy = 0 * Vx or Vy = 0
    dispListY = [0]
    
    # Defining temporary variable for while loop:
    t = 0 # initial time = 0

    # While loop to iterate until t = td (i.e. projectile touches the floor):
    while t < td:
        # Euler methods for x and y:
        x = dispListX[-1]+delta_t*(vx+ax*t)
        y = dispListY[-1]+delta_t*(vy+ay*t) #Accounting for -gt

        # Append to lists:
        dispListX.append(x)
        dispListY.append(y)

        # Add time interval to t:
        t = t + delta_t

    return(dispListX,dispListY)

def calc_acc(vx,vy,beta):
    """ Calculate horizontal and vertical acceleration. """

    # Calculate magnitude of velocity:
    vmag = math.sqrt((vx**2)+(vy**2))

    # Calculate ax:
    ax = -beta*vmag*vx

    # Calculate ay:
    ay = -beta*vmag*vy-9.81

    return(ax,ay)

def calc_range(vx,vy):
    """ Calculate time to reach the ground and range. """
     
    # Calculate time to reach ground (x = 0):
    td = (2*vy)/9.81

    # Calculate range: 
    range_dist = td*vx

    # Return td and range:
    return(td,range_dist)

def calc_initial(v_initial,theta):
    """ Calculate inital conditions and time to reach the ground. """

    # Calculate velocity x and y:
    vx = v_initial*math.cos(theta)
    vy = v_initial*math.sin(theta)

    return(vx,vy)

def main(userInput):
    """ Calls functions to parse data input, and calls graph plotter. """

	 # User Input:
    userInput = userInput.split(',')

    # Converting values to float:
    v_initial = float(userInput[0])
    theta = float(userInput[1])*math.pi/180 # Converting Theta to radians
    beta = float(userInput[2])
    delta_t = float(userInput[3])    

    # Calculating initial conditions:
    vx,vy = calc_initial(v_initial,theta)

    # Calculating range: 
    td,range_dist = calc_range(vx,vy)

    # Printing range:
    print("The range is {0} meters".format(range_dist))

    # Calculate acceleration:
    ax,ay = calc_acc(vx,vy,beta)

    # Step forward until the projectile touches the floor (td):
    dispListX,dispListY = step_forward(vx,vy,ax,ay,delta_t,td)

    # Plotting the graph:
    graph_plotter(dispListX,dispListY)

# Asking user for input:
if __name__ == '__main__':
    main(input("Write the magnitude of the initial velocity (m/s), angle (degrees), drag coefficient, step interval (s). Comma separated (no spaces): "))

		