# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from circle import Circle
from random import randint

class Floater(Prey, Circle):
    def __init__(self,x,y):
        Circle.__init__(self, x, y, 5, 'Red')
        Prey.__init__(self, x, y, 2*self.radius, 2*self.radius, 0, self.radius)
        self.randomize_angle()

    def update(self):
        random_num= randint(1,100)
        if random_num < 30:
            difference = randint(-5,6)
            new_speed = self._speed + difference/10
            if 3<new_speed<7:
                self.set_speed(new_speed)    
            new_angle = self._angle + difference/10
            self.set_angle(new_angle)
        self.move()

    def __str__(self):
        return 'Floater'