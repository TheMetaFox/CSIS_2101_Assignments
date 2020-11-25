#File:    FishMainclass.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 November 5, 2020

class Fish:
    def __init__(self, nm=0, wt=0, ln=0, ppu=0):
        self.name = nm
        self.weight = wt
        self.length = ln
        self.ppu = ppu

    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_len(self):
        return self.length
    def get_ppu(self):
        return self.ppu

    def set_name(self, nm):
        self.name = nm
    def set_weight(self, wt):
        self.weight = wt
    def set_length(self, ln):
        self.length = ln
    def set_ppu(self, ppu):
        self.ppu = ppu

    def calc_price(self, ppu):
        price = int(self.weight) * int(self.length) * float(ppu)
        return price
        
    




 

"""
class Fish:
    def __init__(self, nm, wt, ln, ppu):
        self.__name = nm
        self.__weight = wt
        self.__length = ln
        self.__ppu = ppu
        self.__typ = "Sea Fish"


    def calc_price(self, ppu):
        price = self.__weight * self.__length * ppu
        return price

# Accessors (get) and Mutators (set)
    def get_name(self):        
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_len(self):
        return self.__length
    def get_typ(self):
        return self.__typ

    def set_name(self, nm):
        self.__name = nm
    def set_weight(self, wt):
        self.__weight = wt
    def set_length(self, ln):
        self.__length = ln
    def det_typ(self, typ):
        self.__typ = typ
"""
