class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coeff, power in terms:
            assert type(coeff) in (int, float), "Poly.__init__: illegal coeff type in " + str(terms)
            if coeff != 0:
                assert type(power) is int and power >= 0, "Poly.__init__: illegal power type in " + str(terms)
                assert power not in self.terms.keys(), "Poly.__init__: coefficient for power " + str(power) + " specified twice"
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
        return "Poly(" + "".join("({},{}),".format(coeff, power) for power, coeff in self.terms.items())[:-1] + ")"

    
    def __len__(self):
        return 0 if self.terms == {} else max(self.terms.keys())
    
    def __call__(self,arg):
        return sum(coeff * (arg ** power) for power, coeff in self.terms.items())

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), key=lambda term: term[0], reverse=True): yield (coeff, power)

    def __getitem__(self,index):
        if type(index) is not int: raise TypeError("Poly.__getitem__: given power is not an integer")
        elif index < 0: raise TypeError("Poly.__getitem__: given power is not nonnegative")
        return self.terms.get(index, 0)
            
    def __setitem__(self,index,value):
        if type(index) is not int: raise TypeError("Poly.__setitem__: given power is not an integer")
        elif index < 0: raise TypeError("Poly.__setitem__: given power is not nonnegative")
        self.terms[index] = value
        if not value: del self.terms[index]
        
    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError("Poly.__delitem__: given power is not an integer")
        elif index < 0:
            raise TypeError("Poly.__delitem__: given power is not nonnegative")
        if index in self.terms: del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int, float): raise TypeError("Poly._add_term: illegal coeff type")
        if type(p) is not int or p < 0: raise TypeError("Poly._add_term: illegal power type")
        
        self.terms[p] = self.terms.get(p, 0) + c
        if self.terms[p] == 0: del self.terms[p]

    def __add__(self,right):
        copy = eval(repr(self))
        if type(right) in (float, int):
            copy._add_term(right, 0)
            return copy
        elif type(right) is Poly:
            for poly, coeff in right.terms.items(): copy._add_term(coeff, poly)
            return copy
        raise TypeError("Poly.__add__: type of right operand is not int, float, or Poly type")
    
    def __radd__(self,left):
        if type(left) in (float, int, Poly):  return self + left
        raise TypeError("Poly.__radd__: type of left operand is not int, float, or Poly type")
    

    def __mul__(self,right):
        result = Poly()
        if type(right) in (float, int):
            for power, coeff in self.terms.items(): result._add_term(coeff * right, power)
            return result
        elif type(right) is Poly:
            for r_power, r_coeff in right.terms.items():
                for power, coeff in self.terms.items():
                    result._add_term(r_coeff * coeff, power + r_power)
            return result
        raise TypeError("Poly.__mul__: type of right operand is not int, float, or Poly type")

    def __rmul__(self,left):
        if type(left) in (float, int, Poly): return self * left
        raise TypeError("Poly.__rmul__: type of left operand is not int, float, or Poly type")
    

    def __eq__(self,right):
        if type(right) in (float, int, Poly):
            return self.terms == ({0: right} if type(right) in (int, float) else right.terms)
        raise TypeError("Poly.__eq__: the value being compared to is not of type Poly, int or float")

    
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