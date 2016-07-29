class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        # Quick value check before we start manipulating data
        for c, p in terms:
            if type(c) not in (int, float):
                raise AssertionError(
                        'Poly.__init__: illegal coefficient in ({}, {})'.format(c, p))
            if type(p) != int:
                raise AssertionError(
                        'Poly.__init__: illegal power in ({}, {})'.format(c, p))
            if p < 0:
                raise AssertionError(
                        'Poly.__init__: power in ({}, {}) is less than 0'.format(c, p))
        
        for c, p in terms:
            if c == 0:
                pass
            else:
                if p in self.terms:
                    raise AssertionError(
                            'Poly.__init__: power {} already defined'.format(p))
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
        polygon_terms = ''
        
        for k,v in self.terms.items():
            polygon_terms += '({},{}),'.format(v, k)
        
        polygon_terms = polygon_terms[:-1]
        
        return 'Poly({})'.format(polygon_terms)

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        
        for k,v in self.terms.items():
            total += v * arg**k
        
        return total
    

    def __iter__(self):
        def gen(d):
            for k in sorted(d.keys(), reverse=True):
                yield (d[k], k)
        
        return gen(self.terms)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError(
                    'Poly.__getitem__: illegal power {}'.format(index))
        if index < 0:
            raise TypeError(
                    'Poly.__getitem__: power {} is less than 0'.format(index))
        
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError(
                    'Poly.__setitem__: illegal power {}'.format(index))
        if type(value) not in (int, float):
            raise TypeError(
                    'Poly.__setitem__: illegal coefficient {}'.format(value))
        if index < 0:
            raise TypeError(
                    'Poly.__setitem__: power {} is less than 0'.format(index))
        
        if value == 0:
            try:
                del self.terms[index]
            except KeyError:
                pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError(
                    'Poly.__delitem__: illegal power {}'.format(index))
        if index < 0:
            raise TypeError(
                    'Poly.__delitem__: power {} is less than 0'.format(index))
        
        
        if index in self.terms:
            del self.terms[index]    

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError(
                    'Poly._add_term: illegal coefficient {}'.format(c))
        if type(p) != int:
            raise TypeError(
                    'Poly._add_term: illegal power {}'.format(p))
        if p < 0:
            raise TypeError(
                    'Poly._add_term: power {} is less than 0'.format(p))
        
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            new_c = self.terms[p] + c
            
            if new_c == 0:
                del self.terms[p]
            else:
                self.terms[p] = new_c

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError(
                    'Poly.__add__: illegal value {}'.format(right))
        
        if type(right) != Poly:
            right = Poly((right, 0))
        
        new_poly = Poly()
        
        for c,p in self:
            new_poly._add_term(c, p)
        
        for c,p in right:
            new_poly._add_term(c, p)
        
        return new_poly
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError(
                    'Poly.__mul__: illegal value {}'.format(right))
        
        if type(right) != Poly:
            right = Poly((right, 0))
        
        new_poly = Poly()
        
        for c1, p1 in self:
            for c2, p2 in right:
                new_poly._add_term(c1*c2, p1+p2)
        
        return new_poly

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        # I'm not sure why we need to raise a TypeError here.
        # With the built-in data types, if we perform an equality check
        # on non-like types, it simply returns False, which seems like the
        # logical thing to do. After all, an illegal data type, (say, a str)
        # would definitely NOT be equal to to a Poly, right? 
        #
        # But hey, specs are specs :P
        if type(right) not in (Poly, int, float):
            raise TypeError(
                    'Poly.__eq__: illegal value {}'.format(right))
        
        if type(right) != Poly:
            right = Poly((right, 0))
            
        if len(self) != len(right):
            return False
        
        if self.terms.keys() != right.terms.keys():
            return False
        
        for k in self.terms.keys():
            if self[k] != right[k]:
                return False
        
        return True

    
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