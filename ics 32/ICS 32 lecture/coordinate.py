class Coordinate:
    def __init__ (self, frac_x: float, frac_y: float,self, abs_x, abs_y, abs_size_x: int, abs_size_y:int):
        if frac_x != None:
            self._frac_x = frac_x
            self._frac_y = frac_y

        else:
            self._frac_x = abs_x / abs_size_x
            self._frac_y = abs_y / abs_size_y

    def frac(self) -> (float, float):
        return self._frac_x, self._fracy_y

    def abs(self, abs_size_x: int, abs_size_y: int) -> (int,int):
        return int(self._frac_x * abs_size_x), int(self._frac_y * abs_size_y)

def from_frac(frac_x: float, frac_y: float):
    return Coordinatefrac_x, frac_y, None, None, None, None)

def from_abs(abs_x: int, abs_y: int, abs_size_x:int, abs_size_y:int):
    return Coordinate(None, None, abs_x, abs_y, abs_size_x, abs_size_y)
