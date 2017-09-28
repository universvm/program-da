"""
    CheckPoint1: Practical Physics 
    Aim: Calculate the volume of a sphere + print radius and surphase area of sphere in m and m^2

    Author: Leonardo Castorina

"""

# Modules:
import math


# Functions:
def saCalc_sphere(rad): 
    """ Calculates the surface area of a sphere in m**2 using volume as argument"""

    # Sphere Surface Area: sa = 4 * pi * r**2
    surface_a = 4*math.pi*math.pow(rad,2)

    # Result:
    print("The surface area of the sphere is {0} m**2".format(surface_a))

def radCalc_sphere(volume):
    """ Calculates the radius of a sphere in m using volume as an argument"""

    print("Your volume input is {0} mm**3".format(volume)) # reminding the user its volume input

    # Calculate Radius: cube root of ( volume * (3/4) / pi )
    radius = float(3)/float(4)*volume*(1/math.pi) # using float for Python 2 Division
    radius = radius**(float(1)/float(3)) # cube root
    radius = radius*math.pow(10,-3) # converting into meters

    # Result:
    print("The radius of the sphere is {0} m ".format(radius))
    
    # Calling function to calculate surface area:
    saCalc_sphere(radius)

    

# Asking user for radius input:
volInput = float(input("Write the volume of the sphere in mm**3: "))

# Calling calculator function using radius input:
radCalc_sphere(volInput)

#feedback no concatenated functions
