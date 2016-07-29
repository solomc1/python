class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i in terms:
            if i[0] != 0:
                if type(i[0]) is not int and type(i[0]) is not float:
                    raise AssertionError('coefficient must be int or float')
                if type(i[1]) is not int or i[1] < 0:
                    raise AssertionError('power must be int greater than or equal to 0')
                if i[1] in self.terms:
                    raise AssertionError('power cannot appear as a later term if it appears as as earlier term')
                self.terms[i[1]] = i[0]
            
            
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
        return 'Poly({})'.format(*self.terms.items())

    
    def __len__(self):
        if self == Poly():
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        sums = 0
        for i in self.terms.items():
            sums += i[1] * arg**i[0]
        return sums
    

    def __iter__(self):
        for i in sorted(self.terms.items(), reverse = True):
            yield (i[1], i[0])
            

    def __getitem__(self,index):
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('power must be int greater than or equal to 0')
        self.terms[index] = value
        if value == 0:
            del self.terms[index]

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('power must be int greater than or equal to 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('coefficient must be int or float')
        if type(p) is not int or p < 0:
            raise TypeError('power must be int greater than or equal to 0')
        if p not in self.terms.keys():
            self.terms[p] = c
        else:
            self.terms[p] += c
        if self.terms[p] == 0:
            del self.terms[p]
        
       

    def __add__(self,right):
        new_poly = Poly()
        for p,c in self.terms.items():
            new_poly._add_term(c,p)
        if type(right) == Poly:
            for p,c in right.terms.items():
                new_poly._add_term(c, p)
            return new_poly
        if type(right) == int or type(right) == float:
            new_poly._add_term(right, 0)
            return new_poly

    
    def __radd__(self,left):
        new_poly = Poly()
        for p,c in self.terms.items():
            new_poly._add_term(c,p)
        if type(left) == Poly:
            for p,c in left.terms.items():
                new_poly._add_term(c, p)
            return new_poly
        if type(left) == int or type(left) == float:
            new_poly._add_term(left, 0)
            return new_poly
            
    

    def __mul__(self,right):
        new_poly = Poly()
        for p,c in self.terms.items():
            new_poly._add_term(c,p)
        if type(right) == Poly:
            new_terms = []
            items = list(self.terms.items())
            for i in items:
                for i in right.terms.items():
                    new_terms.append(i)
            for i in items:
                for i2 in new_terms:
                    new_poly._add_term(i[1], i[0]+i2[0])
                    new_poly._add_term(i[1]*i2[1], i[0])
            return new_poly
        elif type(right) == int or type(right) == float:
            for i in self.terms.items():
                new_poly._add_term(i[1]*right-i[1], i[0])
            return new_poly
                
    

    def __rmul__(self,left):
        new_poly = Poly()
        for p,c in self.terms.items():
            new_poly._add_term(c,p)
        if type(left) == Poly:
            new_terms = []
            items = list(self.terms.items())
            for i in items:
                for i in left.terms.items():
                    new_terms.append(i)
            for i in items:
                for i2 in new_terms:
                    new_poly._add_term(i[1], i[0]+i2[0])
                    new_poly._add_term(i[1]*i2[1], i[0])
            return new_poly
        elif type(left) == int or type(left) == float:
            for i in self.terms.items():
                new_poly._add_term(i[1]*left-i[1], i[0])
            return new_poly
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms.keys() == right.terms.keys() and self.terms.values() == right.terms.values()
        elif type(right) == int or type(right) == float:
            return self.terms[0] == right
        else:
            raise TypeError('arg must be Poly or int or float')
    
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