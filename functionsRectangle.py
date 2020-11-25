#File:    functionsRectangle.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 16, 2020

# This program's function is to determine whether a rectange is short or long.

def main():
    length = float(input("What is the length of your rectange?"))
    width = float(input("What is the width of your rectange?"))

    if (length/width >= 2) or (width/length >= 2):
        print("This rectangle is long.")
    else:
        print("This rectangle is short.")

    calcArea(length,width)
    calcPerimeter(length,width)

def calcArea(length,width):
    area = length * width
    print("The area of the rectangle is", area)


def calcPerimeter(length,width):
    perimeter = (length + width) * 2
    print("The perimeter of the rectangle is", perimeter)
