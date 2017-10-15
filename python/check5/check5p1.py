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

def calc_acc(vx,vy,beta):
    """ Calculate horizontal and vertical acceleration. """

    # Calculate magnitude of velocity:
    vmag = math.sqrt((vx**2)+(vy**2))

    # Calculate ax:
    ax = -beta*(vmag**2)*vx

    # Calculate ay:
    ay = -beta*(vmag**2)*vy-9.81

    return(ax,ay)

def step_forward(x,y,vx,vy,beta,delta_t):
    """   Do a forward step """

    # Calculate the acceleration of the previous step:
    ax,ay = calc_acc(vx,vy,beta)

    # Calculate the new vx and vy: 
    vx = vx+ax*delta_t
    vy = vy+ay*delta_t

    # Calculate the new x and y: 
    x = x+delta_t*vx
    y = y+delta_t*vy #Accounting for -gt
    
    return(x,y,vx,vy)

def calc_initial(v_initial,theta):
    """ Calculate inital conditions and time to reach the ground. """

    # Calculate velocity x and y:
    vx = v_initial*math.cos(theta)
    vy = v_initial*math.sin(theta)

    return(vx,vy)

def main(userInput):
    """    Main program to read in from terminal, do itteration, and plot out graph """
    
    # User Input:
    userInput = userInput.split(',')

    # Converting values to float:
    v_initial = float(userInput[0])
    theta = float(userInput[1])*math.pi/180 # Converting Theta to radians
    beta = float(userInput[2])
    delta_t = float(userInput[3])    

    # Calculating initial conditions:
    vx,vy = calc_initial(v_initial,theta)

    # Displacement lists:
    dispListX = [0]
    dispListY = [0]

    # First step (with previous x and y: 
    x,y,vx,vy = step_forward(dispListX[-1],dispListY[-1],vx,vy,beta,delta_t)

    # Appending X and Y values from first step: 
    dispListX.append(x)
    dispListY.append(y)

    # Continue steps until it touches the floor (y = 0):
    while dispListY[-1] > 0: 

        # Doing a step forward:
        x,y,vx,vy = step_forward(x,y,vx,vy,beta,delta_t)

        # Appending to lists: 
        dispListX.append(x)
        dispListY.append(y)

    # Printing range: (x value when y = 0)
    print("The range is {0} meters".format(dispListX[-1]))

    # Plotting the graph:
    graph_plotter(dispListX,dispListY)

# Asking user for input:
if __name__ == '__main__':
    main(input("Write the magnitude of the initial velocity (m/s), angle (degrees), drag coefficient, step interval (s). Comma separated (no spaces): "))
