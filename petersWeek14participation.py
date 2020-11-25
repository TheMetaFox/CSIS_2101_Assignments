#File: petersWeek14participation.py
#Project: Week 14 Participation CSIS 2101
#Author: Joshua Peters
#Version: 1.0 11/22/2020

from petersWeek14partClass import *

def main():
    shape1 = Shape("Magenta", True)
    shape2 = Shape("Cerulean", False)

    print("Shape 1\n" + "-------------\n" + str(shape1))
    print("\n\nShape 2\n" + "-------------\n" + str(shape2))

    triangle1 = Triangle("Coquelicot", True, 5.0, 4.0)

    print("\n\nTriangle\n" + "-------------\n" + str(triangle1))

    print("Triangle area:", str(triangle1.calc_triangle_area()))
