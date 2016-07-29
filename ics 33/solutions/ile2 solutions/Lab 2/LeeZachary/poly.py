class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for poly_tuple in terms:
            coeff = poly_tuple[0]
            power = poly_tuple[1]
            if coeff != 0:
                assert type(coeff) in (int, float), 'Poly.__init__: illegal coefficient type in:' + str(poly_tuple)
                assert type(power) == int and power >= 0, 'Poly.__init__: illegal power in:' + str(poly_tuple)
                assert power not in self.terms, 'Poly.__init__: term has same power as earlier term:' + str(poly_tuple)
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
        poly_params = []
        
        for power, coeff in sorted(self.terms.items(), reverse = True):
            poly_params.append('({}, {})'.format(coeff, power))
            
        return 'Poly(' + ', '.join(poly_params) + ')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return sorted(self.terms, reverse = True)[0]
    
    def __call__(self,arg):
        if type(arg) in (int, float):
            return sum([coeff * (arg**power) for power, coeff in self.terms.items()])
        else:
            raise AssertionError('Poly.__call__: arg is not an int or float: {}'.format(arg))
    

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), reverse = True):
            yield coeff, power  
            

    def __getitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError('Poly.__getitem__: index is not an int or it is less than 0: ' + index)
            

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0:
                del self[index]
            else:
                self.terms[index] = value
        else:
            raise TypeError('Poly.__setitem__: index is not an int or it is less than 0: ' + index)
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                del self.terms[index]
            else:
                pass
        else:
            raise TypeError('Poly.__delitem__: index is not an int or it is less than 0: ' + index)

    def _add_term(self,c,p):
        if type(c) in (int, float) and type(p) == int and p >= 0:
            if p not in self.terms:
                if c != 0:
                    self[p] = c
                else:
                    pass
            else:
                new_c = self[p] + c
                if new_c == 0:
                    del self[p]
                else:
                    self[p] = new_c
                
                
        else:
            raise TypeError('Poly._add_term: c ({}) must be an int or a float \
            and p({}) must be an int greater than or equal to 0.'.format(c, p))
       

    def __add__(self,right):
        if type(right) in (int, float):
            new = eval(repr(self))
            new._add_term(right, 0)
            return new
        elif type(right) == Poly:
            new = eval(repr(self))
            for p, c in right.terms.items():
                new._add_term(c, p)
            return new
        else:
            raise TypeError('Poly.__add__: right must be int, float, or Poly. \
            right ({}) is of type {}'.format(right, type(right)))

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) in (int, float):
            new = eval(repr(self))
            for p, c in new.terms.items():
                new[p] = right * c
            return new
        elif type(right) == Poly:
            new = Poly()
            for s_power, s_coeff in self.terms.items():
                for r_power, r_coeff in right.terms.items():
                    new._add_term(s_coeff * r_coeff, s_power + r_power)
            return new
                
        else:
            raise TypeError('Poly.__add__: right must be int, float, or Poly. \
            right ({}) is of type {}'.format(right, type(right)))
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == Poly:
            equal_terms = True
            for term in self.terms:
                equal_terms = equal_terms and self[term] == right[term]
            return equal_terms and len(self.terms) == len(right.terms)
        elif type(right) in (int, float):
            return len(self.terms) == 1 and self[0] == right
        else:
            raise TypeError('Poly.__eq__: right must be an int, float or Poly. \
            right ({}) is of type {}'.format(right, type(right)))
        

    
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
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()