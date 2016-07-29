# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from circle import Circle
import model

class Black_Hole(Circle):
    def __init__(self,x,y):
        Circle.__init__(self, x, y, 10, 'Black')

    def update(self,p):
        result = set()
        target = model.find(p)
        for value in target:
            if self.contains(value.get_location()):
                result.add(value)
        return result

    def contains(self,xy):
        return self.distance(xy) < self.radius

    def __str__(self):
        return 'Black_Hole'