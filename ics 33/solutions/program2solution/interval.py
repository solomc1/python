from goody import type_as_str
from math import sqrt


class IntervalError(Exception):
    def __init__(self,message=None):
        Exception.__init__(self,message)

class Interval:
    def __init__(self,min_val,max_val):
        assert min_val <= max_val, 'Interval.__init__ min_val(" > max_val: '+str(min_val)
        self.min,self.max = min_val,max_val

    @staticmethod
    def min_max(min_val,max_val=None):
        assert type(min_val) in [int,float], 'Interval.min_max min_val is not numeric: '+str(min_val)
        assert type(max_val) in [type(None), int,float], 'Interval.min_max max_val is not numeric: '+str(max_val)
        assert max_val == None or min_val <= max_val, 'Interval.min_max min_val('+str(min_val)+') > max_val('+str(max_val)+')'
        return Interval(min_val, (max_val if max_val != None else min_val))
    
    @staticmethod
    def mid_err(mid_val,error=0):
        assert type(mid_val) in [int,float], 'Interval.mid_err mid_val is not numeric: '+str(mid_val)
        assert type(error) in [type(None), int,float], 'Interval.mid_err error is not numeric: '+str(error)
        assert error >= 0, 'Interval.mid_err error('+str(error)+') <0'
        return Interval(mid_val-error,mid_val+error)
    

    # Helper Methods
    def _includes0(self):
        return self.min <= 0 <= self.max

   
    @staticmethod
    def _order2(a,b):
        return min(a,b),max(a,b)

    
    @staticmethod
    def _order4(a,b,c,d):
        return min(a,b,c,d),max(a,b,c,d)

     
    @staticmethod
    def _validate_arithmetic_arguments(l,r,op):
        if type(l) not in [int,float,Interval] or type(r) not in [int,float,Interval]:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+type_as_str(l)+'\' and \''+type_as_str(r)+'\'')        
 

    @staticmethod
    def _validate_relational_arguments(l,r,op):
        if type(l) not in [int,float,Interval] or type(r) not in [int,float,Interval]:
            raise TypeError('unorderable types: ' +
                            type_as_str(l)+'()' + op + type_as_str(r)+'()')        
 
    def best(self):
        return (self.min+self.max)/2
 
    
    def error(self):
        return (self.max-self.min)/2

    
    def relative_error(self):
        return abs(100*self.error()/self.best())
    
   
    def __repr__(self):
        return 'Interval('+str(self.min)+','+str(self.max)+')'


    def __str__(self):
        return str(self.best())+'(+/-'+str(self.error())+')'

    
    def __bool__(self):
        return self.min < self.max


    def __pos__(self):
        return self

    
    def __neg__(self):
        return Interval(*Interval._order2(-self.min,-self.max))


    def __add__(self,right):
        Interval._validate_arithmetic_arguments(self,right,'+')
        if type(right) in [int,float]:
            return Interval(self.min+right, self.max+right)
        else:
            return Interval(self.min+right.min,self.max+right.max)

     
    def __radd__(self,left):
        Interval._validate_arithmetic_arguments(left,self,'+')
        # called only if left is not Interval
        return Interval(left+self.min, left+self.max)

 
    # Note reversal of min/max compared to +
    def __sub__(self,right):
        Interval._validate_arithmetic_arguments(self,right,'-')
        if type(right) in [int,float]:
            return Interval(self.min-right, self.max-right)
        else:
            return Interval(self.min-right.max,self.max-right.min)

     
    def __rsub__(self,left):
        Interval._validate_arithmetic_arguments(left,self,'-')
        # called only if left is not Interval
        return Interval(left-self.max, left-self.min)
 
   
    def __mul__(self,right):
        Interval._validate_arithmetic_arguments(self,right,'*')
        if type(right) in [int,float]:
            return Interval(*Interval._order2(self.min*right,self.max*right))
        else:
            return Interval(*Interval._order4(self.min*right.min,
                                            self.min*right.max,
                                            self.max*right.min,
                                            self.max*right.max,
                                            ))
     

    def __rmul__(self,left):
        Interval._validate_arithmetic_arguments(left,self,'*')
        # called only if left is not Interval
        return Interval(*Interval._order2(left*self.min,left*self.max))
 

    def __truediv__(self,right):
        Interval._validate_arithmetic_arguments(self,right,'/')
        if type(right) in [int,float]:
            return Interval(*Interval._order2(self.min/right,self.max/right))
        else:
            if right._includes0():
                raise ZeroDivisionError('Interval.__truediv__ right interval contains 0:'+str(right))
            return Interval(*Interval._order4(self.min/right.min,
                                            self.min/right.max,
                                            self.max/right.min,
                                            self.max/right.max,
                                            ))
    
     
    def __rtruediv__(self,left):
        Interval._validate_arithmetic_arguments(left,self,'/')
        # called only if left is not Interval
        if self._includes0():
            raise ZeroDivisionError('Interval.__rtruediv__ right interval contains 0:'+str(self))
        return Interval(*Interval._order2(left/self.min,left/self.max))
    
    
    def __pow__(self,right):
        if type(right) is not int:
            raise TypeError('unsupported operand type(s) for **'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')        
        mult = (self if right >= 0 else 1/self)
        answer = Interval(1.,1.)
        for _ in range(abs(right)):
            answer *= mult
        return answer
    
    def __eq__(self,right):
        Interval._validate_relational_arguments(self,right,'==')
        return type(right) is Interval and \
          self.min == right.min and self.max== right.max

     
    def __neq__(self,right):
        Interval._validate_relational_arguments(self,right,'!=')
        return type(right) is not Interval or \
          self.min != right.min or self.max != right.max

     
    def __lt__(self,right):
        self._validate_relational_arguments(self,right,'<')
        assert 'compare_mode' in Interval.__dict__, 'Interval.__lt__ compare_mode not specified'
        assert Interval.compare_mode in ['conservative','liberal'],  'Interval.__lt__ compare_mode illegal:'+str(Interval.compare_mode)
        if type(right) in [int,float]:
            if Interval.compare_mode == 'liberal':
                return self.best() < right
            else:
                return self.max < right
        else:
            if Interval.compare_mode == 'liberal':
                return self.best() < right.best()
            else:
                return self.max < right.min

     
    def __gt__(self,right):
        self._validate_relational_arguments(self,right,'>')
        assert 'compare_mode' in Interval.__dict__, 'Interval.__gt__ compare_mode not specified'
        assert Interval.compare_mode in ['conservative','liberal'],  'Interval.__gt__ compare_mode illegal:'+str(Interval.compare_mode)
        if type(right) in [int,float]:
            if Interval.compare_mode == 'liberal':
                return self.best() > right
            else:
                return self.min > right
        else:
            if Interval.compare_mode == 'liberal':
                return self.best() > right.best()
            else:
                return self.min > right.max
     
    def __le__(self,right):
        self._validate_relational_arguments(self,right,'<=')
        assert 'compare_mode' in Interval.__dict__, 'Interval.__le__ compare_mode not specified'
        assert Interval.compare_mode in ['conservative','liberal'],  'Interval.__le__ compare_mode illegal:'+str(Interval.compare_mode)
        if type(right) in [int,float]:
            if Interval.compare_mode == 'liberal':
                return self.best() <= right
            else:
                return self.max <= right
        else:
            if Interval.compare_mode == 'liberal':
                return self.best() <= right.best()
            else:
                return self.max <= right.min
     
    def __ge__(self,right):
        self._validate_relational_arguments(self,right,'>=')
        assert 'compare_mode' in Interval.__dict__, 'Interval.__ge__ compare_mode not specified'
        assert Interval.compare_mode in ['conservative','liberal'],  'Interval.__ge__ compare_mode illegal:'+str(Interval.compare_mode)
        if type(right) in [int,float]:
            if Interval.compare_mode == 'liberal':
                return self.best() >= right
            else:
                return self.min >= right
        else:
            if Interval.compare_mode == 'liberal':
                return self.best() >= right.best()
            else:
                return self.min >= right.max
    
    
    def __abs__(self):
        if self._includes0():
            return Interval(0.,max(abs(self.min),abs(self.max)))
        else:
            return Interval(*Interval._order2(abs(self.min),abs(self.max)))

    def sqrt(self):
        return Interval(sqrt(self.min),sqrt(self.max))
     
    def __setattr__(self,a,v):
        assert 'max' not in self.__dict__, 'Interval.__setattr__ attempted to reset attribute'
        self.__dict__[a] = v

     
#     
#     # no iadd, isub imul itrudiv ipow
# 
    
    
if __name__ == '__main__':
    
    import driver
    driver.driver()
