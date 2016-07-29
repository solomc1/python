class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coefficient, power in terms:
            assert coefficient == int or float, 'Coefficient must be an int or float value'
            assert power >= 0, 'Power cannot be a negative number'
            if power in self.terms.keys():
                print('Illegal, power', power,'is already in the dictionary')
            else:
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
        return 'Poly('+ ','.join(str(tuples) for tuples in self.terms.items()),')'

    
    def __len__(self):
        power_list = []
        for powers in self.terms.keys():
            power_list.append(powers)
        return max(power_list)
    
    def __call__(self,arg):
        pass
    

    def __iter__(self):
        for tuples in self.terms.items():
            return sorted(tuples,reverse = True)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError ('Index is must be a number matching a power from the polynomial')
        elif index < 0:
            raise TypeError ('The power of the polynomial should not be less than 0')
        elif index not in self.terms.keys():
            return 0
        for index, value in self.terms.items():
            return value
            
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError ('Index value must be an integer')
        elif index < 0:
            raise TypeError ('The power of the polynomial should not be less than 0')
        elif value == 0:
            del self.terms[index]
            
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError ('Index value must be an integer')
        elif index < 0:
            raise TypeError ('The power of the polynomial should not be less than 0')
        if index in self.terms.keys():
            del self.terms[index]
            
            

    def _add_term(self,c,p):
        if type(c)  not in [int or float]:
            raise TypeError ('Coefficient must be numeric')
        if type(p) != int >=0:
            raise TypeError('Power must be an int greater than or equal 0')
        if p not in self.terms.keys() and c != 0:
           self.terms[p] = c
        elif p in self.terms.keys():
            if c == 0:
                del self.terms[p]
            else:
                self.terms[p] += c
           

    def __add__(self,right):
        if type(right) == Poly:
            self._add_term(Poly) + right._add_term(Poly)
        elif type(right) in [int,float]:
            self._add_term(Poly) + right

    
    def __radd__(self,left):
        if type(left) == Poly:
            left._add_term(Poly) + self._add_term(Poly)
        elif type(left) in [int,float]:
            left + self._add_term(Poly)
    

    def __mul__(self,right):
        if type(right) == Poly:
            self._add_term(Poly) * right._add_term(Poly)
        elif type(right) in [int,float]:
            self._add_term(Poly) * right
            

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            len(Poly) == len(right)
        elif type(right) in [int, float]:
            len(Poly) == right

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
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
    print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()