"""
    CheckPoint3: Practical Physics 
    Explore the behaviour of a damped simple harmonic oscillator for a range of damping coefficients

    Author: Leonardo Castorina

"""

# Modules:
import math


# Functions:
def damp_state(omega_zero, gamma):
    """ Calculates the value of b with damp state (over damped, critically damped and under damped) using omega_zero and gamma"""

    if gamma > 2*omega_zero: # Over Damped
    	b = gamma/(2*math.sqrt((gamma**2/4)-omega_zero**2))

		return(b, True)
	elif gamma == 2*omega_zero: # Critically Damped
		b = gamma/2

		return(b, None)
	else: # Under Damped
		 b = gamma/(2*math.sqrt(omega_zero**2-(gamma**2/4)))

		 return(b, False)

def shm(omega_zero,gamma,t):
    """ Calculates displacement using the quadratic equation."""

    # Calling function to calculate discriminant:
    d = discr_calc(a, b, c)

    # If/Else for number of solutions from d:
    if d == float(0): # One real number solution
        result = (-b+math.sqrt(d))/(2*a)

        # Result:
        return(result)
    elif d > 0: # Two real solutions
        try:
            result1 = (-b+math.sqrt(d))/(2*a)
            result2 = (-b-math.sqrt(d))/(2*a)

            # Result:
            return(result1, result2)    
        except ZeroDivisionError: # Linear equation
            result = -c/b

            return(result)
    else: # 2 Imaginary solutions
        negB_2a = -b/(2*a)

        #Change d to positive to calculate the root
        d_2a = math.sqrt(-d)/(2*a)

        # Result:
        return('{0} +/- {1}i'.format(negB_2a, d_2a))

TODO: MAIN Function with 
    # Printing the details to the user:
    print("Your values are:\n gamma = {0}; omega_zero = {1}".format(omega_zero, gamma)) 
    and calling smh
# Asking user for input:
print(main(input("Write the values of a, b and c separated by comma (no spaces): ")))
