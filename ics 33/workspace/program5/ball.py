# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

from prey import Prey
from circle import Circle

class Ball(Prey, Circle):
    def __init__(self,x,y):
        Circle.__init__(self, x, y, 5, 'Blue')
        Prey.__init__(self, x, y, 2*self.radius, 2*self.radius, 0, self.radius)
        self.randomize_angle()

    def update(self):
        self.move()

    def __str__(self):
        return 'Ball'