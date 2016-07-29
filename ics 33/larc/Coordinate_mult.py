import Coordinate

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self, right):
        if type(right) != Coordinate:
            raise TypeError("Right is not a Coord")

        else:
            return Coordinate(self.x*right, self.y*right)

     def __rmul__(self, left):
        return self.__mul__(left) # most efficiently correct
        
