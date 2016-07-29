class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        if terms:
            for term in terms:
                power = term[1]
                coeff = term[0]
                if type(coeff) in (int, float) and (type(power) == int and power >= 0):
                    if power in self.terms and coeff != 0:
                        raise AssertionError('Poly.__init__: same power cannot appear as later term')
                    elif coeff == 0:
                        pass
                    else:
                        self.terms[power] = coeff
                else:
                    raise AssertionError
        
        
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
        pair = ''
        for power, coeff in self.terms.items():
            pair += '('+str(coeff)+','+str(power)+'),'
        pair = pair.strip(',')
        return 'Poly('+pair+')'

    
    def __len__(self):
        if self.terms:
            return sorted(self.terms.items(), reverse=True)[0][0]
        else:
            return 0
    
    def __call__(self,arg):
        value = 0
        for power, coeff in self.terms.items():
            value += coeff*(arg**power)
        return value
    

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), reverse=True):
            yield coeff, power
            

    def __getitem__(self,index):
        if type(index) == int and index >=0:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]
        else:
            raise TypeError
            

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0:
                if index in self.terms.keys():
                    del self.terms[index]
            else:
                self.terms[index] = value
        else:
            raise TypeError
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError
            

    def _add_term(self,c,p):
        if type(c) in (int, float) and type(p) == int and p >= 0:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                if self.terms[p] + c == 0:
                    del self.terms[p]
                else:
                    self.terms[p] = self.terms[p] + c
        else:
            raise TypeError
       

    def __add__(self,right):
        new = Poly()
        if type(right) == Poly:
            for p, c in right.terms.items():
                new._add_term(c, p)
            for p, c in self.terms.items():
                new._add_term(c, p)
        elif type(right) in (int, float):
            new._add_term(right, 0)
            for p, c in self.terms.items():
                new._add_term(c, p)
        else:
            raise TypeError
        return new

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        new = Poly()
        if type(right) == Poly:
            if right.terms:
                new = self
                for p, c in right.terms.items():
                    if c == 0:
                        for power, coeff in new.terms.items():
                            new.terms[power] = new.terms[power] * c
                    else:
                        for power, coeff in new.terms.items():
                            new.terms[power + p] = new.terms[power]
                            #del new.terms[power]
        elif type(right) in (int, float):
            for power, coeff in new.terms.items():
                new.terms[power] = coeff * right
        else:
            raise TypeError
        return new
                        
                    
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms

    
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