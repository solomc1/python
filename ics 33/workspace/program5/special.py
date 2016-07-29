# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.
#the special ball changes colors and moves extremely fast while having the same properties as a prey.

from ball import Ball
import random

class Special(Ball):
    def __init__(self,x,y):
        Ball.__init__(self, x, y)
        self.randomize_color()
        self.set_speed(30)
    
    def update(self):
        Ball.update(self)
        self.randomize_color()

    def __str__(self):
        return 'Special'