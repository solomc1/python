# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

from simulton import Simulton
from random import randint

class Circle(Simulton):
    def __init__(self, x, y, r, c):
        self.radius = r
        self.color = c
        Simulton.__init__(self, x, y, 2*self.radius, 2*self.radius)

    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius, fill=self.color)
        
    def randomize_color(self):
        self.color = self.random_color()
    
    def random_color(self):
        colors = ['Green', 'Red','Blue','Orange','Yellow','Purple','Black','White']
        return colors[randint(0,7)]