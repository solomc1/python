class Poly:
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            assert type(c) in [int,float], 'Poly.__init__: illegal coefficient in term ' + str((c,p))
            assert type(p) is int and p >= 0 and p not in self.terms, 'Poly.__init__: illegal power in term: ' + str((c,p))
            if c != 0:
                self.terms[p] = c
            
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
        return 'Poly'+str(tuple( (c,p) for p,c in self.terms.items()))
    

    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms)
    

    def __call__(self,arg):
        return sum(self.terms[p] * arg**p for p in self.terms)

    
    def __iter__(self):
        for p,c in sorted(self.terms.items(),reverse=True):
            yield (c,p)

            
    def __getitem__(self,index):
            if type(index) is not int or index < 0:
                raise TypeError('Poly.__getitem__: index('+str(index)+') not int or < 0')
            else:    
                return self.terms.get(index,0) # if index is not a key, returns 0

            
    def __setitem__(self,index,value):
            if type(index) is not int or index < 0:
                raise TypeError('Poly.__setitem__: index('+str(index)+') not int or < 0')
            if value != 0:
                self.terms[index] = value
            elif index in self.terms:
                del self.terms[index]

            
    def __delitem__(self,index):
            if type(index) is not int or index < 0:
                raise TypeError('Poly.__delitem__: index('+str(index)+') not int or < 0')
            if index in self.terms:
                del self.terms[index]

            
    def _add_term(self,c,p):
        if type(c) not in [int,float] or type(p) is not int or p < 0:
            raise TypeError('Poly.___add_terms__: illegal coefficient('+str(c)+') or power ('+str(p)+')')
        if p in self.terms:
            self[p] += c
            if self[p] == 0:
                del self[p]
        elif c != 0:
            self[p] = c

       
    def __add__(self,right):
        result = eval(repr(self))      # Many ways to initialize result to Poly(self)
        if type(right) in [int,float]:
            result._add_term(right,0)
        elif type(right) is Poly:
            for c,p in right:
                result._add_term(c,p)
        else:
            raise TypeError('Poly.__add__: cannot add Poly with '+str(right))
        return result

    
    def __radd__(self,left):
        return self+left  # use commutative property

    
    def __mul__(self,right):
        if type(right) in [int,float]:
            return Poly(*[(c*right,p) for c,p in self])
        elif type(right) is Poly:
            result = Poly()
            for c1,p1 in self:
                for c2,p2 in right:
                    result._add_term(c1*c2,p1+p2)
            return result
        else:
            raise TypeError('Poly.__mul__: cannot multiply Poly by '+str(right))

    
    def __rmul__(self,left):
        return self*left  # use commutative property

    
    def __eq__(self,right):
        if type(right) in [int,float]:
            return self == Poly((right,0))
        if type(right) is Poly:
            return self.terms == right.terms
        else:
            raise TypeError('Poly.__eq__: cannot compute equality of Poly and '+str(right))
    
    
    
    
    
    
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