#File:    triangleInputPeters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 26, 2020

# This program's functions is to calculate the area of a triangle.

import math

def triangleInput():
    a,b,c = eval(input("Input the three sides of your triangle: "))

# Asks for another input if current imput is invalid
    while isValid(a,b,c) == False:
        a,b,c = eval(input("Invalid Input, please input the three sides of \
your triangle: "))

# Displays the area of the triangle
    print("The area of your triangle is:", calcArea(a,b,c))


# This Function checks if sum of any two sides is greater than the third side 
def isValid(a,b,c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False

# This Function calculates the area of the tiangle
def calcArea(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
