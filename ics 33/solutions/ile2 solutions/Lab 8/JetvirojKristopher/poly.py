class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to initialize self.terms
        for term in terms:
            assert type(term) is tuple and len(term) == 2, 'Poly.__init__: illegal term (must be a 2-tuple) : '+str(term)
            assert type(term[0]) in (int, float), 'Poly.__init__: illegal coefficient in : '+str(term)
            assert type(term[1]) is int and term[1] >= 0, 'Poly.__init__: illegal power in : '+str(term)
            assert term[1] not in self.terms, 'Poly.__init__: repeated power in : '+str(term)
            if term[0] != 0:
                self.terms[term[1]] = term[0]
    
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
        return 'Poly({terms})'.format(terms = ','.join('({c},{p})'.format(c=c,p=p) for p,c in self.terms.items()))
    
    def __len__(self):
        return (max(self.terms) if len(self.terms) != 0 else 0)
    
    def __call__(self,arg):
        if type(arg) in (int, float):
            return sum(c*arg**p for p,c in self.terms.items())
        else:
            raise TypeError('Poly.__call__: arg('+str(arg)+') must be an int or float')
    
    def __iter__(self):
        def gen(terms):
            for p,c in sorted(terms.items(), reverse = True):
                yield (c,p)
        return gen(dict(self.terms))

    def __getitem__(self,index):
        if type(index) is int and index >= 0:
            return (self.terms[index] if index in self.terms else 0)
        else:
            raise TypeError('Poly.__getitem__: index('+str(index)+') must be a non-negative int')
    
    def __setitem__(self,index,value):
        if type(index) is int and index >= 0:
            if value != 0:
                self.terms[index] = value
            elif index in self.terms:
                del self.terms[index]
        else:
            raise TypeError('Poly.__setitem__: index('+str(index)+') must be a non-negative int')
    
    def __delitem__(self,index):
        if type(index) is int and index >= 0:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError('Poly.__delitem__: index('+str(index)+') must be a non-negative int')
    
    def _add_term(self,c,p):
        if type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: p('+str(p)+') must be a non-negative int')
        if type(c) not in (int, float):
            raise TypeError('Poly._add_term: c('+str(c)+') must be an int or float')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
    
    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__add__: right('+str(right)+') must be an int, float, or Poly')
        new_poly = Poly(*(term for term in self))
        if type(right) in (int, float):
            new_poly._add_term(right, 0)
        elif type(right) is Poly:
            for term in right:
                new_poly._add_term(*term)
        return new_poly
    
    def __radd__(self,left):
        return self + left
    
    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__mul__: right('+str(right)+') must be an int, float, or Poly')
        new_poly = Poly()
        if type(right) in (int, float):
            for term in self:
                new_poly._add_term(term[0] * right, term[1])
        elif type(right) is Poly:
            for l_p,l_c in self.terms.items():
                for r_p,r_c in right.terms.items():
                    new_poly._add_term(l_c * r_c, l_p + r_p)
        return new_poly
    
    def __rmul__(self,left):
        return self * left
    
    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__: right('+str(right)+') must be an int, float, or Poly')
        if type(right) in (int, float):
            return len(self) == 0 and self.terms.get(0,0) == right
        elif type(right) is Poly:
            return  self.terms == right.terms
    
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