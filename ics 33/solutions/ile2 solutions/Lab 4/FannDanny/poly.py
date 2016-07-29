class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coeff, power in terms:
            if power != 0 and coeff in self.terms.values():
                raise AssertionError('Poly.__init__: term '+str((coeff,power))+' has power '+str(power)+' that is in an earlier coefficient')
            elif coeff == 0:
                pass
            else:
                self.terms[power] = coeff
        for i in terms:
            assert type(i[0]) in [int, float], "Poly.__init__: term "+str(i)+" has coefficient"+str(i[0])+" that is not an int or float"
            assert type(i[1]) is int, "Poly.__init__: term "+str(i)+" has power"+str(i[1])+" which is not an int"
            assert i[1] >= 0, "Poly.__init__: term "+str(i)+" has power "+str(i[1])+" that is less than 0"
            
                
             
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
        return 'Poly('+str([(key,value) for key, value in self.terms.items()])+')'

    
    def __len__(self):
        if len(self.terms) > 0:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        term_eval = 0
        for power, coeff in self.terms.items():
            term_eval += coeff*(arg**power)
        return term_eval
    

    def __iter__(self):
        pow_sort = sorted(self.terms.items(), key = lambda x: x[0], reverse = True)
        i_sort = iter(pow_sort)
        while True:
            try:
                yield next(i_sort)
            except StopIteration:
                break

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__getitem__: index '+str(index)+' is not an int')
        elif index < 0:
            raise TypeError('Poly.__getitem__: index '+str(index)+' is less than 0')
        else:
            for power, coeff in self.terms.items():
                if index == power:
                    return coeff
        return 0
    
    def __setitem__(self,index,value):
        if type(value) is not int:
            raise IndexError('Poly.__setitem__: value '+str(value)+' is not an int')
        elif value < 0:
            raise IndexError('Poly.__setitem__: value '+str(value)+' is less than 0')
        elif index == 0:
            for power, coeff in self.terms.items():
                if power == value:
                    del(self.terms[coeff])
        else:
                self.terms[index] = value
        
            
    def __delitem__(self,index):
        if type(index) is not int:
            raise IndexError('Poly.__delitem__: index '+str(index)+' is not an int')
        elif index < 0:
            raise IndexError('Poly.__delitem__: index '+str(index)+' is less than 0')
        
        for power, coeff in self.terms.items():
            if power == index:
                del(self.terms[coeff])
            else:
                pass

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Poly._add_term: coefficient '+str(c)+' is not an int or float')
        if type(p) is not int:
            raise TypeError('Poly._add_term: power '+str(p)+' is not an int')
        if p < 0:
            raise TypeError('Poly._add_term: power '+str(p)+' is less than 0')
        if p in self.terms.values() and p != 0:
            for power, coeff in self.terms.items():
                if power == p:
                    new_coeff = coeff + c
                    if new_coeff == 0:
                        del(self.terms[p])
                    else:
                        del(self.terms[p])
                        self.terms[p] = new_coeff
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
            
        
    
    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__add__: operand '+str(right)+' is not a Poly or numeric type')
        new_poly = Poly()
        if type(right) == Poly:
            for power, coeff in self.terms.items():
                new_poly[coeff] = power
            for power, coeff in right.terms.items():
                new_poly._add_term(coeff, power)
        elif type(right) in [int, float]:
            new_poly._add_term(right, 0)
        return new_poly
                  
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Poly.__add__: operand '+str(left)+' is not a Poly or numeric type')
        else:
            return left + self

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__mul__: operand '+str(right)+' is not a Poly or numeric type')
        new_poly = Poly()
        if type(right) == Poly:
            for power_self, coeff_self in self.terms.items():
                for power_right, coeff_right in right.terms.items():
                    new_coeff = coeff_self * coeff_right
                    new_power = power_self + power_right
                    new_poly._add_term(new_coeff, new_power)
        elif type(right) in [int, float]:
            for power, coeff in self.terms.items():
                new_coeff = coeff*right
                new_poly._add_term(new_coeff, power)
        return new_poly
                

    def __rmul__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Poly.__mul__: operand '+str(left)+' is not a Poly or numeric type')
        else:
            return left * self

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__eq__: operand '+str(right)+' is not a Poly or numeric type')
        if type(right) == Poly:
            if len(self) != len(right):
                return False
            else:
                for coeff in self.terms.keys():
                    if self.terms[coeff] != self.right[coeff]:
                        return False
        elif type(right) in [int, float]:
            if self.terms.keys() == 0:
                if self.terms.values() != right:
                    return False
        return True
            
                    
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()