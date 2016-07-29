class Poly:
    
    
    def __init__(self,*terms):
        #terms = 2-tuples
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coeff, power in terms:
            assert type(coeff) in [int, float], 'Coefficient is of inappropriate type'
            assert type(power) is int and power >= 0, 'Power must be an int >= 0'
            assert power not in self.terms.keys(), 'Power already exists in the polynomial'
            if coeff < 0 and power in self.terms.keys():
                self.terms[power] = coeff
            self.terms[power] = coeff

            
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
        poly_rep = 'Poly({})'
        inner_string = ''
        for power in self.terms.keys():
            inner_string += '({},{}),'.format(self.terms[power], power)
        return poly_rep.format(inner_string)[:-1]+')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys()) 
    
    def __call__(self,arg):
        sum = 0
        for power in self.terms.keys():
            if power == 0:
                sum += self.terms[power]
            else:
                arithmetic = self.terms[power]*(arg**power)
                sum += arithmetic
        return sum

    def __iter__(self):
        for power in self.terms.keys():
            if power > power+1:
                yield (self.terms[power], power)
                
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Argument passed is of incorrect type or is < 0')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index] 
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Argument passed is of incorrect type or is < 0')
        elif value == 0 and value in self.terms.values():
            del(self.terms[value])
        else:
            self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Argument passed is of incorrect type or is < 0')
        else:
            del(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) not in [int, float] and type(p) is not int and p >= 0:
            raise TypeError('Arguments passed are of incorrect types or is < 0')
        else:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p] = self.terms[p]+c
                if self.terms[p] == 0:
                    del(self.terms[p])
                

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Operands are of incorrect type')
        elif type(right) is Poly:
            for power in right.terms.keys():
                self._add_term(right.terms[power], power)
            return self
        elif type(right) in [int, float]:
            self._add_term(right, 0)
            return self
            
            
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        product = 0
        if type(right) not in [Poly, int, float]:
            raise TypeError('Operands are of incorrect type')
        if type(right) is Poly:
            for power in self.terms.keys():
                for r_power in right.terms.keys():
                    self._add_term(right.terms[power], r_power)
            return self
        elif type(right) in [int, float]:
            for power in self.terms.keys():
                self._add_term(right, 0)
            return self

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Argument passed is of incorrect type or is < 0')
        elif type(right) is Poly:
            return self.terms == right.terms
        elif type(right) in [int, float]:
            return right == self.terms

    
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