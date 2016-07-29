class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for coefficient, power in terms:
            assert type(coefficient) in (int, float), 'coefficient {} must be int or float'.format(str(coefficient))
            assert type(power) is int and power >= 0, 'power {} must be int and >=0'.format(str(power))
            if coefficient == 0:
                pass
            else:
                assert power not in self.terms, 'power {} already assigned value in terms'.format(str(power))
                self.terms[power] = coefficient
            
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
        return 'Poly('+','.join('('+str(coefficient)+','+str(power)+')' 
                                for power, coefficient in self.terms.items())+')'


    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())

   
    def __call__(self,arg):
        total = 0
        for power, coefficient in self.terms.items():
            total += coefficient*arg**power
        return total
    

    def __iter__(self):
        for power, coefficient in reversed(sorted(self.terms.items())):
            yield coefficient, power
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: index {} must be int and >=0'.format(str(index)))
        else:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: index {} must be int and >=0'.format(str(index)))
        else:
            if value == 0:
                if index in self.terms:
                    del self.terms[index]
            else:
                self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: index {} must be int and >=0'.format(str(index)))
        else:
            if index not in self.terms:
                pass
            else:
                del self.terms[index]    


    def _add_term(self,c,p):
        if type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: power {} must be int and >=0'.format(str(p)))
        if type(c) not in (int, float):
            raise TypeError('Poly._add_term: coefficient {} must be int or float'.format(str(c)))
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                if self.terms[p] + c == 0:
                    del self.terms[p]
                else:
                    self.terms[p] += c

       
    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__add__: unsupported operand {} for +'.format(str(right)))
        result = eval(repr(self))
        if type(right) is Poly:
            for power, coefficient in right.terms.items():
                result._add_term(coefficient, power)
        else:
            result._add_term(right, 0)
        return result

    
    def __radd__(self,left):
        if type(left) not in (int, float):
            raise TypeError('Poly.__radd__: unsupported operand {} for +'.format(str(left)))
        result = eval(repr(self))
        result._add_term(left, 0)
        return result
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__mul__: unsupported operand {} for *'.format(str(right)))
        if type(right) is Poly:
            result = Poly()
            for power, coefficient in self.terms.items():
                for r_power, r_coefficient in right.terms.items():
                    result._add_term(coefficient*r_coefficient, power+r_power)
        else:
            result = eval(repr(self))
            for power in result.terms:
                result.terms[power] *= right
        return result
    

    def __rmul__(self,left):
        if type(left) not in (int, float):
            raise TypeError('Poly.__rmul__: unsupported operand {} for *'.format(str(left)))
        result = eval(repr(self))
        for power in result.terms:
            result.terms[power] *= left
        return result
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__: unorderable types Poly and {}'.format(str(type(right))))
        if type(right) is Poly:
            return self.terms.items() == right.terms.items()
        else:
            return list(self.terms.keys()) == [0] and self.terms[0] == right

    
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