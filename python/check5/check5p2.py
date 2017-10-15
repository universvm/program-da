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
    plt.title("Projectile Motion Kinetic Energy Ratio over different values of Theta")

    # Adding labels for axes:    
    plt.xlabel("Theta (radians)")
    plt.ylabel("Ratio of Kf/Ki")

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
    beta = float(userInput[1])
    delta_t = float(userInput[2])    

    # Lists: 
    kineticList = []
    thetaList = []

    # Theta initial: 
    theta = 0 

    # While theta is less than 90 degrees: 
    while theta < math.pi/2: 
        # Calculating initial conditions:
        vxi,vyi = calc_initial(v_initial,theta)
        # Initial displacement:
        x = 0
        y = 0

        # First step (with previous x and y: 
        x,y,vxf,vyf = step_forward(x,y,vxi,vyi,beta,delta_t)

        # Continue steps until it touches the floor (y = 0):
        if theta == 0: 
            # Initially projectile does not lift off the ground
            vxf = vxi
            vyf = vyi
        else:    
            while y > 0: 
                # Doing a step forward:
                x,y,vxf,vyf = step_forward(x,y,vxf,vyf,beta,delta_t)

        # Calculating the Kf and Ki:
        kf = vxi**2+vyi**2
        ki = vxf**2+vyf**2

        # Calculating the Kf/Ki:
        ratio_kfki = kf/ki

        # Appending to list: 
        kineticList.append(ratio_kfki)
        thetaList.append(theta)

        # Incrementing theta for while loop
        theta = theta + math.pi/40

    # Plotting the graph:
    graph_plotter(thetaList,kineticList)

# Asking user for input:
if __name__ == '__main__':
    main(input("Write the magnitude of the initial velocity (m/s), angle (degrees), drag coefficient, step interval (s). Comma separated (no spaces): "))
