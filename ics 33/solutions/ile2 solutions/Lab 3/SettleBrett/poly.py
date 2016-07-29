class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for (c, p) in terms:
            assert type(c) in (int, float), "Coefficient must be an int or a float"
            assert type(p) == int and p >=0, "Power must be a positive integer or 0"
            assert p not in self.terms, "That power has already been created"
            if c != 0:
                self.terms[p] = c
        
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
        return "Poly(%s)" % ", ".join(["(%s, %s)" % (c, p) for p, c in self.terms.items()])

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        s = 0
        for c, p in self:
            s += c * (arg ** p)
        return s
    

    def __iter__(self):
        for p, c in sorted(self.terms.items(), key = lambda f: -f[0]):
            yield (c, p)
            

    def __getitem__(self,index):
        self.check_index(index)
        return self.terms[index] if index in self.terms else 0
            
    def __setitem__(self,index,value):
        self.check_index(index)
        if type(value) not in (float, int):
            raise TypeError("The new coefficient must be a number")
        if value == 0:
            if index in self.terms:
                del self.terms[index]
            return
        self.terms[index] = value
        
    def check_index(self, ind):
        if type(ind) != int or ind < 0:
            raise TypeError("Index must be an positive integer")
        
    def __delitem__(self,index):
        self.check_index(index)
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        assert type(c) in (int, float), "Coefficient must be an int or a float"
        assert type(p) == int and p >= 0, "Power must be a positive integer or 0"
        if c == 0:
            return
        if p not in self.terms:
            self.terms[p] = c
        else:
            self.terms[p] = (self[p] + c) if p in self.terms else c
        if self.terms[p] == 0:
            del self.terms[p]
       

    def __add__(self,right):
        if type(right) in (int, float):
            ret = Poly(*[couple for couple in self])
            ret.terms[0] = (self.terms[0] + right) if 0 in self.terms else right
            return ret
        elif type(right) == Poly:
            ret = Poly(*[couple for couple in self])
            for c, p in right:
                ret._add_term(c, p)
            return ret
        else:
            raise TypeError("Cannot add a polynomial to type %s" % type(right))
        

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) in (int, float):
            return Poly(*[(c * right, p) for c, p in self])
        elif type(right) == Poly:
            ret = Poly()
            for c, p in self:
                for c2, p2 in right:
                    ret._add_term(c * c2, p + p2)
            return ret
        else:
            raise TypeError("Cannot multiply a polynomial by type %s" % type(right))
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) in (int, float):
            return list(self.terms.keys()) == [0] and self[0] == right
        elif type(right) == Poly:
            return right.terms == self.terms
        else:
            raise TypeError("Comparison can only be between Polynomials and numbers/Polynomials")
        

    
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