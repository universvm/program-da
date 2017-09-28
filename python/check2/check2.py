"""
    CheckPoint2: Practical Physics 
    Aim: To solve for x using the quadratic equation, given a, b and c.

    Author: Leonardo Castorina

"""

# Modules:
import math


# Functions:
def discr_calc(a, b, c):
    """ Calculates the discriminant using a, b and c"""

    discriminant = "Do the math"

    return(discriminant)

def main(inValues):
    """ Calculates x using the quadratic equation."""

    # Split input by comma:
    inValues = inValues.split(",")

    # Defining a, b and c + conversion to float:
    if len(inValues) == 3:
        a = float(inValues[0])
        b = float(inValues[1])
        c = float(inValues[2])
    else: # Error
        print('ERROR: You gave {0} values. You need to define a, b and c!'.format(len(inValues)))

    # Printing the details to the user:
    print("The equation is:\n {0}x**2 + {1}x + {2}".format(a, b, c)) 

    # Calling function to calculate discriminant:
    d = discr_calc(a, b, c)

    # Calculating -b/2a
    negB_2a = -b/(2*a)

    # If/Else for number of solutions from d:
    if d == float(0): # One real number solution
        return(negB_2a*d)
    elif d > 0: # Two real solutions
        return(negB_2a*d, negB_2a*-d)    
    else: # 2 Imaginary solutions
        # TODO: Changing d into i
        return('{0} +/- {1}'.format(negB_2a, d))

# Asking user for input:
main(input("Write the values of a, b and c separated by comma (no spaces): "))
