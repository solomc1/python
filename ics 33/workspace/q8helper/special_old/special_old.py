

#the special object is invincible to black holes, pulsator, or hunter. when the special object gets near any prey objects, it will be attached to the end of it,
# similar to a snake. Any predator objects, however can still consume the attachments. Since it is a special object, 
from math import sin, cos
from ball import Ball
from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton
import model

class Chain_Parent(object):
    next = None
    def __str__(self):
        return 'Chain_Parent'

class Special(Black_Hole, Mobile_Simulton, Chain_Parent):
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 2*self.radius, 2*self.radius, 0, 5)
        self.randomize_angle()
        self.color = 'Orange'
        self.end_of_chain = self

    def update(self, p):
        to_eat = Black_Hole.update(self,p)
        eaten = set()
        for obj in to_eat:
            if not isinstance(obj,Chain_Link):
                eoc = self.end_of_chain
                chain_x, chain_y = eoc.get_location()
                chain_angle = eoc.get_angle()
                
                new_x = chain_x - eoc.radius*cos(chain_angle)
                new_y = chain_y - eoc.radius*sin(chain_angle)
                
                new_link = Chain_Link(new_x, new_y, self.end_of_chain)
                new_link.change_location(-new_link.radius, -new_link.radius)
                
                self.end_of_chain = new_link
                model.add(new_link)
                eaten.add(obj)
        
        self.move()
        return eaten

    def __str__(self):
        return 'Special'

class Chain_Link(Ball, Chain_Parent):
    def __init__(self, x, y, parent):
        Ball.__init__(self, x, y)
        self.next = parent
        self.set_angle(parent.get_angle())
        self.color = 'Green'
        
    def update(self):
        next_x, next_y = self.next.get_location()
        next_angle, next_radius = self.next.get_angle(), self.next.radius
        new_x = next_x - next_radius*cos(next_angle) - self.radius*cos(next_angle)
        new_y = next_y - next_radius*sin(next_angle) - self.radius*sin(next_angle)
        self.set_location(new_x, new_y)
        self.set_angle(next_angle)

    def __str__(self):
        return 'Chain_Link'
