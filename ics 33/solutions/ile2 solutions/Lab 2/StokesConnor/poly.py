class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for tuple in terms:
            power = tuple[1]
            coefficient = tuple[0]
            assert type(coefficient) in (int, float), "Poly.__init__: Coefficient was {}, should be either int or float.".format(type(coefficient))
            assert type(power) == int, "Poly.__init__: Power was {}, should be an int.".format(type(power))
            assert power >= 0, "Poly.__init__: Power ({}) must be equal to or greater than 0.".format(power)
            assert power not in self.terms, "Poly.__init__: Power({}) already in the polynomial, and cannot be repeated.".format(power)
            
            if coefficient != 0:
                self.terms[power] = coefficient
        
        # Fill in the rest of this method, using *terms to intialize self.terms

            
    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. Notice that it assumes that
    #   every Poly object stores a dict whose keys are powers and whose
    #   associated values are coefficients. This function does not depend
    #   on any other method in this class being written correctly.   
    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        return_str = ""
        for power in self.terms.keys():
            return_str += "({},{}),".format(self.terms[power],power)
        return "Poly(" + return_str[:-1] + ")"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for power in self.terms.keys():
            coeff = self.terms[power]
            new_arg = arg ** power
            total += new_arg * coeff

        return total
    

    def __iter__(self):
        pairs = sorted(self.terms.items(),reverse=True)
        class poly_iter:
            def __init__(self):
                self.iterable = pairs
                self.n = 0
            def __next__(self):
                to_return = self.n
                try:
                    self.n += 1
                    return (self.iterable[to_return][1],self.iterable[to_return][0])
                except:
                    raise StopIteration
        return poly_iter()
                

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError("Poly.__getitem__: index ({}) was of type {}, must be of type int.".format(index,type(index)))
        if index < 0:
            raise TypeError("Poly.__getitem__: index({}) must be of value 0 or greater.".format(index))
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
                 

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError("Poly.__setitem__: index ({}) was of type {}, must be of type int.".format(index,type(index)))
        if index < 0:
            raise TypeError("Poly.__setitem__: index ({}) must be of value 0 or greater.".format(index))
        if type(index) not in (int,float):
            raise TypeError("Poly.__setitem__: value ({}) was of type {}, must be of type int or float.".format(value,type(value)))
        
        if value == 0:
            del self[index]
            
        else:
            self.terms[index] = value
        
        return None
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError("Poly.__setitem__: index ({}) was of type {}, must be of type int.".format(index,type(index)))
        if index < 0:
            raise TypeError("Poly.__setitem__: index ({}) must be of value 0 or greater.".format(index))
        
        if index not in self.terms:
            return None
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("Poly._add_term: coefficient ({}) was of type {}, must be of type int or float".format(type(c), c))
        if type(p) is not int:
            raise TypeError("Poly._add_term: power ({}) was of type {}, must be of type int".format(type(p), p))
        if p < 0:
            raise TypeError("Poly._add_term: power ({}) must not be less than zero.".format(p))
        
        if p not in self.terms and c != 0:
            self[p] = c
        
        else:
            new_sum = self[p] + c
            if new_sum == 0:
                del self[p]
            else:
                self[p] = new_sum
        return None
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Poly.__add__: right operand ({}) was of type {}, must be of type Poly, int, or float".format(right, type(right)))

        return_poly = Poly()
        
        if type(right) in (int,float):
            right = Poly((right,0))
        
        for power in self.terms.keys():
            return_poly._add_term(self.terms[power], power)
        
        for power in right.terms.keys():
            return_poly._add_term(right.terms[power], power)
            
        return return_poly
    
    def __radd__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError("Poly.__radd__: left operand ({}) was of type {}, must be of type Poly, int, or float".format(left, type(left)))
        
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Poly.__mul__: right operand ({}) was of type {}, must be of type Poly, int, or float".format(right, type(right)))
        
        return_poly = Poly()
        
        if type(right) in (int,float):
            right = Poly((right,0))
            
        for power in self.terms.keys():
            for right_power in right.terms.keys():
                if self.terms[power] == 0:
                    coeff = right.terms[right_power]
                elif right.terms[right_power] == 0:
                    coeff = self.terms[power]
                else:
                    coeff = self.terms[power] * right.terms[right_power]
                
                return_poly._add_term(coeff,power + right_power)
                
        return return_poly
        
    

    def __rmul__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError("Poly.__rmul__: left operand ({}) was of type {}, must be of type Poly, int, or float".format(left, type(left)))
        return self * left

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Poly.__eq__: right operand ({}) was of type {}, must be of type Poly, int, or float".format(right, type(right)))
        
        if type(right) in (int, float):
            right = Poly((right,0))
        
        for power in self.terms.keys():
            if self[power] != right[power]:
                return False
        
        return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    
    '''p1 = Poly((1,1),(2,0))
    p2 = Poly((3,2),(2,1),(1,0))
    
    print(p1 * p2)'''
    '''print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print(p(2))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
    print('  list collecting iterator results:',[t for t in p])
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')'''
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()