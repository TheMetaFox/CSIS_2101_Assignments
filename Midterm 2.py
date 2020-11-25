#File:    Question14.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 26, 2020

# This program's functionis to calculate the area of a triangle.

def main():
    nJoshua = int(input("Please enter a Positive Integer: "))

    nsum = 0
    for i in range(0, (nJoshua+1)*-1, -1):
        nsum = i+nsum
    print(nsum)

    nsum = 0
    j = 0
    while j > nJoshua*-1:
        nsum += j
        j += -1
    print(nsum)


