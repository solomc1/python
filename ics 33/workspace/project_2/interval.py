# Kevin Wong, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


# I used the following imports; feel free to add others
from goody import type_as_str
from math import sqrt


class Interval:
    
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    @staticmethod
    def min_max(min, max = None):
        assert type(min) == int or type(min) == float, 'Parameter min is not a numeric type1'
        assert type(max) == int or type(max) == float or max == None, 'Parameter max is not a numeric type'
        if max == None:
            return Interval(min, min)
        assert min < max, 'Min cannot be greater than max'
        return Interval(min, max)
    
    @staticmethod
    def mid_err(middle, error = 0):
        assert type(middle) == int or type(middle) == float, 'Parameter min is not a numeric type'
        assert type(error) == int or type(error) == float, 'Parameter max not a numeric type'
        assert error >= 0, 'Error cannot be negative'
        return Interval(middle - error, middle + error)
    
    def best(self):
        return (self.min+self.max)/2
    
    def error(self):
        return (self.max-self.min)/2
    
    def relative_error(self):
        return abs(self.error()/self.best())*100
    
    def __repr__(self)->str:
        return "Interval("+str(self.min)+","+str(self.max)+")"
    
    def __str__(self)->str:
        return (str(self.best())+"(+/-"+str(abs(self.error()))+")")
    
    def __bool__(self)->bool:
        return self.min != self.max
    
    def __pos__(self):
        return Interval(self.min,self.max)
    
    def __neg__(self):
        return Interval(-self.min,-self.max)
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min+other),(self.max+other)))
        elif type(other) == type(self):
            return (Interval((self.min+other.min),(self.max+other.max)))
        else:
            raise TypeError("Cannot add Interval with anything other than int, float, or interval")
    
    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min+other),(self.max+other)))
        elif type(other) == type(self):
            return (Interval((self.min+other.min),(self.max+other.max)))
        else:
            raise TypeError("Cannot add Interval with anything other than int, float, or interval")
    
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min-other),(self.max-other)))
        elif type(other) == type(self):
            return (Interval((self.min-other.max),(self.max-other.min)))
        else:
            raise TypeError("Cannot subtract Interval with anything other than int, float, or Interval")
        
    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return (Interval((other-self.max),(other-self.min)))
        elif type(other) == type(self):
            return (Interval((other.min-self.max),(other.max-self.min)))
        else:
            raise TypeError("Cannot subtract Interval with anything other than int, float, or Interval")
        
    
    def __mul__(self,other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min*other),(self.max*other)))
        elif type(other) == type(self):
            a = self.min
            b = self.max
            c = other.min
            d = other.max
            return (Interval((min(a*c,a*d,b*c,b*d)),(max(a*c,a*d,b*c,b*d))))
        else:
            raise TypeError("Cannot multiply Interval with anything other than int, float, or Interval")
        
    def __rmul__(self,other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min*other),(self.max*other)))
        elif type(other) == type(self):
            a = self.min
            b = self.max
            c = other.min
            d = other.max
            return (Interval((min(a*c,a*d,b*c,b*d)),(max(a*c,a*d,b*c,b*d))))
        else:
            raise TypeError("Cannot multiply Interval with anything other than int, float, or Interval")

    
    def __truediv__(self,other):
        if type(other) == int or type(other) == float:
            return (Interval((self.min/other),(self.max/other)))
        elif type(other) == type(self):
            a = self.min
            b = self.max
            c = other.min
            d = other.max
            if c<=0 and d>=0:
                raise ZeroDivisionError("Cannot divide by zero")
            return (Interval((min(a/c,a/d,b/c,b/d)),(max(a/c,a/d,b/c,b/d))))
        else:
            raise TypeError("Cannot multiply Interval with anything other than int, float, or Interval")
        
    def __rtruediv__(self,other):
        if type(other) == int or type(other) == float:
            if self.min<=0 and self.max>=0:
                raise ZeroDivisionError("Cannot divide by zero")
            return (Interval((other/self.max),(other/self.min)))      
        elif type(other) == type(self):
            c = self.min
            d = self.max
            a = other.min
            b = other.max
            if self.min<=0 and self.max>=0:
                raise ZeroDivisionError("Cannot divide by zero")
            return (Interval((max(a/c,a/d,b/c,b/d),(min(a/c,a/d,b/c,b/d)))))
        else:
            raise TypeError("Cannot multiply Interval with anything other than int, float, or Interval")
          
          
    def __pow__(self,other):
        if type(other)!=int:
            raise TypeError("Can only exponentiate Interval by an integer")
        result = self
        if other == 0:
            return Interval(1.0,1.0)
        elif other < 0:
            result = (1/self)
            for x in range(abs(other)-1):
                result *= (1/self)
        else:
            for x in range(other-1):
                result *= self
        return result
    
    def __eq__(self,other):
        if type(other) == int or type(other) == float:
            return False
        elif type(other) == type(self):
            return (self.min == other.min and self.max == other.max)
        else:
            raise TypeError("Can only compare Interval with int, float, or Interval")
        
    def __gt__(self, other):
        assert hasattr(Interval, 'compare_mode'), "compare_mode invalid"
        assert Interval.compare_mode in ('conservative','liberal'), "compare_mode invalid"
        if Interval.compare_mode == 'conservative':
            if type(other) == int or type(other) == float:
                return self.max > other
            elif type(other) == type(self):
                return (self.min > other.max)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
        else:
            if type(other) == int or type(other) == float:
                return self.max > other
            elif type(other) == type(self):
                return (self.max > other.max)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
            
    def __lt__(self, other):
        assert hasattr(Interval, 'compare_mode'), "compare_mode invalid"
        assert Interval.compare_mode in ('conservative', 'liberal'), "compare_mode invalid"
        if Interval.compare_mode == 'conservative':
            if type(other) == int or type(other) == float:
                return self.max < other
            elif type(other) == type(self):
                return (self.max < other.min)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
        else:
            if type(other) == int or type(other) == float:
                return self.min < other
            elif type(other) == type(self):
                return (self.min < other.min)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")

    
    def __ge__(self, other):
        assert hasattr(Interval, 'compare_mode'), "compare_mode invalid"
        assert Interval.compare_mode in ('conservative','liberal'), "compare_mode invalid"
        if Interval.compare_mode == 'conservative':
            if type(other) == int or type(other) == float:
                return self.min >= other
            elif type(other) == type(self):
                return (self.min >= other.max)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
        else:
            if type(other) == int or type(other) == float:
                return self.max >= other
            elif type(other) == type(self):
                return (self.max >= other.max)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
            
    def __le__(self, other):
        assert hasattr(Interval, 'compare_mode'), "compare_mode invalid"
        assert Interval.compare_mode in ('conservative', 'liberal'), "compare_mode invalid"
        if Interval.compare_mode == 'conservative':
            if type(other) == int or type(other) == float:
                return self.max <= other
            elif type(other) == type(self):
                return (self.max <= other.min)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
        else:
            if type(other) == int or type(other) == float:
                return self.min <= other
            elif type(other) == type(self):
                return (self.min <= other.min)
            else:
                raise TypeError("Can only compare Interval with int, float, or Interval")
            
    def __abs__(self):
        if self.min > 0:
            return Interval(abs(self.min),abs(self.max))
        elif self.max < 0:
            return Interval(abs(self.max),abs(self.min))
        else:
            if abs(self.min) >= abs(self.max):
                return Interval(0.0,abs(self.min))
            else:
                return Interval(0.0,abs(self.max))
            
    def sqrt(self):
        return Interval(sqrt(self.min),sqrt(self.max))
    
    def __setattr__(self,name,value):
        assert name in ('min','max') and name not in self.__dict__, "Interval object is immutable"
        self.__dict__[name] = value
        
if __name__ == '__main__':
     
    #put code here to test Interval directly

    import driver
    driver.driver()
