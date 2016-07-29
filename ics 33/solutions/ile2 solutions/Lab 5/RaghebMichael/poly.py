class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {power:coefficient for coefficient,power in terms if coefficient != 0}
        #print(self.terms)
        for power,coefficient in self.terms.items():
            #print(power)
            assert type(coefficient) in [int, float], 'Coefficient is not int or float.'
            assert type(power) == int, 'Power is not an integer.'
            assert power >= 0, 'Power is not greater than or equal to 0.'
            #if power in self.terms.keys(): raise AssertionError("You can't repeat powers.")
           
        
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
        repr_poly = ''
        for power, coefficient in self.terms.items():
            repr_poly += ',({},{})'.format(coefficient, power)
        return 'Poly({})'.format(repr_poly[1:])

    
    def __len__(self):
        return max((power for power in self.terms.keys())) if self.terms else 0
    
    def __call__(self,arg):
        term_sum = 0
        for power, coefficient in self.terms.items():
            term_sum += coefficient * ((arg)**power)
        return term_sum
    

    def __iter__(self):
        two_tuples = sorted(((power, coefficient) for power, coefficient in self.terms.items()), reverse = True)
        two_tuples = ((coefficient, power) for power, coefficient in two_tuples)
        for term_tuple in two_tuples:
            yield term_tuple
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index is not int or is below 0.')
        if index not in self.terms.keys(): return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('The power is either not an integer or is less than zero.')
        if value == 0 and index in self.terms.keys():
            del self.terms[index]
        else:
            self.terms.update({index:value})

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The power is either not an integer or is less than zero.')
        if index in self.terms.keys(): del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [float, int]:
            raise TypeError('Power is not an int or a float.')
        if type(p) != int or p < 0:
            raise TypeError('Power is either not an int or is less than 0.')
        if p not in self.terms.keys() and c != 0:
            self.terms.update({p:c})
        elif p in self.terms.keys():
            if c + self.terms[p] == 0:
                del self.terms[p]
            else:
                self.terms.update({p:c + self.terms[p]})
        

    def __add__(self,right):
        if type(right) == Poly:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient, power)
            for power, coefficient in right.terms.items():
                new_poly._add_term(coefficient, power)
            return new_poly
        if type(right) in [int, float]:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient, power)
            new_poly._add_term(right, 0)
            return new_poly

    
    def __radd__(self,left):
        if type(left) in [float, int]:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient, power)
            new_poly._add_term(left, 0)
            return new_poly
    

    def __mul__(self,right):
        if type(right) == Poly:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                for power2, coefficient2 in right.terms.items():
                    new_poly._add_term(coefficient * coefficient2, power + power2)
            return new_poly
        if type(right) in [float, int]:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient * right, power)
            return new_poly
    

    def __rmul__(self,left):
        if type(left) in [float, int]:
            new_poly = Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient * left, power)
            return new_poly
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        if type(right) in [float, int]:
            return self.terms[0] == right
        raise TypeError('The Right operand is not a Poly, int, or float.')
    
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