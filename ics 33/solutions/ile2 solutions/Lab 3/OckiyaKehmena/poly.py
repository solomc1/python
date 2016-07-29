class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            assert (type(x[0]) == int or type(x[0]) == float), 'Poly.__init__(): Coefficient must be numeric >= 0'
            assert type(x[1]) == int and x[1] >= 0, "Poly.__init__(): Power must be integer >= 0"
            if x[0] != 0:
                assert x[1] not in self.terms, "Poly.__init__(): A power was repeated and already in polynomial"
                self.terms[x[1]] = x[0]
            
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
        repr_str = ""
        b = list(self.terms.keys())
        for x in b:
            if x != b[-1]:
                repr_str += "({x}, {y}),".format(x=self.terms[x],y=x)
            else:
                repr_str += "({x}, {y})".format(x=self.terms[x],y=x)
        return "Poly({rstr})".format(rstr=repr_str)
    
    def __len__(self):
        return max(list(self.terms.keys())) if len(list(self.terms.keys())) > 0 else 0
    
    def __call__(self,arg):
        result = 0
        for x in self.terms:
            result += self.terms[x]*(arg**x)
        return result
    

    def __iter__(self):
        return iter(sorted([(self.terms[x],x) for x in self.terms], key=(lambda x: x[1]), reverse=True))


    def __getitem__(self,index):
        if index >= 0 and type(index) == int:
            return self.terms[index] if index in self.terms else 0
        raise TypeError("Poly.__getitem__(): Index must be integer > 0")
            

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0 and index in self.terms:
                self.terms.pop(index)
            elif value != 0:
                self.terms[index] = value
            return
        raise TypeError("Poly.__setitem__(): Invalid index/value detected. Must be sensible.")

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                self.terms.pop(index)
            return
        raise TypeError("Poly.__setitem__(): Invalid index detected. Must be sensible.")
            

    def _add_term(self,c,p):
        if type(c) in [int, float] and type(p) == int and p >= 0:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                sum = self.terms[p] + c
                if sum != 0:
                    self.terms[p] = sum
                else:
                    self.terms.pop(p)
            return
        raise TypeError("Poly._add_term(): Coefficient must be numeric; Power must be int >= 0")
       

    def __add__(self,right):
        if type(right) in [int, float]:
            p = Poly((0,0))
            #p.__dict__ = self.__dict__.copy()
            #p._add_term(right, 0)
            for x in self.terms:
                p._add_term(self.terms[x],x)
            p._add_term(right, 0)
            return p
        elif type(right) == Poly:
            p = Poly((0,0))
            for x in self.terms:
                p._add_term(self.terms[x],x)
            #p.__dict__ = self.__dict__.copy()
            for x in right.terms:
                p._add_term(right.terms[x], x)
            return p
        else:
            raise TypeError("Poly.__add__(): Can only add Poly + (int or float or Poly)")

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) in [int, float]:
            product = Poly((1,0))
            for x in self.terms:
                product._add_term(self.terms[x]*right,x)
            product._add_term(-1,0)
            return product
        elif type(right) == Poly:
            product = Poly((1,0))
            for x in right.terms:
                for y in self.terms:
                    product._add_term((self.terms[y]*right.terms[x]), (y + x))
            product._add_term(-1,0)
            return product
        else:
            raise TypeError("Poly.__mul__(): Can only mul Poly * (int or float or Poly)")
        
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) in [int, float]:
            if len(self) == 0:
                return self(1) == right
            else:
                return False
        if type(right) == Poly:
            return self.terms == right.terms
        else:
            raise TypeError("Poly.__eq__(): Can only == Poly == (int or float or Poly)")

    
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