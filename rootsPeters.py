#File:    rootsPeters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 September 25, 2020

# This program's function is to find two roots of a quadratic equation.
# Quadratic equation: ax^2 + bx + c = 0
# Quadratic formula: (-b +/- sqrt(b^2 - 4ac)/2a

import math

def main():
# assigns user input as variables
    a,b,c = eval(input("Type in the a, b, & c value for your equation \
separated by commas: "))

# calls the calculation of the discriminate
    disc = calcDisc(a,b,c)

# calculates and displays the roots or not
    if validateDisc(disc) == True:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("The roots of the equation:", root1, root2)
    else:
        print("The square root of a negative number cannot be determinded.")

# calculates the discriminate
def calcDisc(a,b,c):
    disc = b**2 - 4*a*c
    return disc

# makes sure the equation is solvable
def validateDisc(disc):
    if disc < 0:
        return False;
    else:
        return True;
