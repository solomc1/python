# A Hunter is both Mobile_Simulton and Pulsator; it updates
#   as a Pulsator, but also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.

from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import model

class Hunter(Pulsator,Mobile_Simulton):
    vision_range = 200
    speed = 5
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,self.get_dimension()[0],self.get_dimension()[1],0,self.speed)
        self.randomize_angle()

    def update(self,p):
        eaten = Pulsator.update(self,p)
        visible = model.find((lambda world_obj: isinstance(world_obj, Prey) and self.distance(world_obj.get_location()) <= Hunter.vision_range))
        closest = None
        closest_dist = 0
        for obj in visible:
            if closest == None:
                closest = obj
                closest_dist = self.distance(closest.get_location())
            elif self.distance(obj.get_location()) < closest_dist:
                closest = obj
                closest_dist = self.distance(closest.get_location())
        
        if closest != None:
            (closest_x, closest_y) = closest.get_location()
            new_x = closest_x - self._x
            new_y = closest_y - self._y
            theta = atan2(new_y,new_x)
            self.set_angle(theta)
        self.move()
        
        return eaten

    def __str__(self):
        return 'Hunter'