# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):
    timer = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.counter = Pulsator.timer

    def update(self, p):
        eaten = Black_Hole.update(self,p)
        for _ in eaten:
            self.radius += 1
        self.counter -= 1
        if self.counter == 0:
            self.radius -= 1
            self.counter = Pulsator.timer
        elif self.radius == 0:
            model.remove(self)
        return eaten

    def __str__(self):
        return 'Pulsator'