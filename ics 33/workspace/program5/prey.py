# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.

# Prey exists so that we can call isinstance(x,Prey) to
#   recognize whether an object is descended from Prey


from mobilesimulton import Mobile_Simulton


class Prey(Mobile_Simulton):
    def __init__(self,x,y,width,height,angle,speed):
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)