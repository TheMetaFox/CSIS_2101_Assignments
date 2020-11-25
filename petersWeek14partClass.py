#File: petersWeek14partClass.py
#Project: Week 14 Participation CSIS 2101
#Author: Joshua Peters
#Version: 1.0 11/22/2020


class Shape:
    def __init__(self, clr, filled):
        self.color = clr
        self.transparent = filled

    def __str__(self):
        shape_str = ""
        shape_str += "Shape's color: " + self.color +\
                     "\nTransparency: " + str(self.transparent)
        return shape_str

    def get_color(self):
        return self.color

    def is_transparent(self):
        return self.transparent

    def set_color(self, cl):
        self.color = cl

    def set_transparent(self, f):
        self.transparent = f

class Triangle(Shape):
    def __init__(self, clr, filled, hgt, wdth):
        Shape.__init__(self, clr, filled)
        self.height = hgt
        self.width = wdth

    def set_height(self, h):
        self.height = h

    def set_width(self, w):
        self.width = w

    def calc_triangle_area(self):
        return self.height * self.width * 1/2
