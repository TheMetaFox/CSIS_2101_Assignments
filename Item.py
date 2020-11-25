#File:    Item.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 November 8, 2020

class Item:
    def __init__(self, price, weightInOunces, description, quantity=1):
        self.price = price
        self.wIO = weightInOunces
        self.desc = description
        self.quant = quantity


    def __str__(self):
        string =(str(self.price)+" each for "+str(self.quant)+" "+self.desc)
        return string


    def get_order_price(self):
        self.orderPrice = self.price * self.quant
        return self.orderPrice
    def get_order_weight_in_ounces(self):
        self.orderwIO = self.wIO * self.quant
        return self.orderwIO
    def get_order_description(self):
        return self.desc
    def get_order_quantity(self):
        return self.qunat


    def set_quantity(self, quantity):
        self.quant = quantity
