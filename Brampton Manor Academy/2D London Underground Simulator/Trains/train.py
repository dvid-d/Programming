import pygame, controls

class Train():
    def __init__(self, type, customer_satisfaction):
        self.type = "" #Automatic or user train
        self.customerSatisf = customer_satisfaction #on a scale