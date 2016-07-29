class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in [int, float]
            assert type(term[1]) == int and term[1] >=0
            if term[1] in self.terms.keys():
                assert False
            else:
                if term[0] == 0:
                    pass
                else:
                    self.terms[term[1]] = term[0]
        
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
        polys = ''
        for power, coeff in self.terms.items():
            polys += '({},{}),'.format(coeff, power)
        polys = polys.rstrip(',')
        return 'Poly({})'.format(polys)

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return (max(self.terms.keys()))
    
    def __call__(self,arg):
        total = 0
        for power, coeff in self.terms.items():
            if power == 0:
                total += (coeff)
            else:
                total += (coeff*arg**power)
        return total
    

    def __iter__(self):
        terms = list(self.terms.keys())
        terms.sort(reverse = True)
        for term in terms:
            yield (self.terms[term], term)
            
        
            

    def __getitem__(self,index):
        if not type(index) == int:
            raise TypeError
        if index < 0 : 
            raise TypeError
        return self.terms[index] 
            

    def __setitem__(self,index,value):
        if not type(index) == int:
            raise TypeError
        if index<0:
            raise TypeError
        self.terms[index] = value
        if value == 0:
            del self.terms[index]
            

    def __delitem__(self,index):
        if not type(index) == int:
            raise TypeError
        if index<0:
            raise TypeError
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not type(p) == int:
            raise TypeError
        if p<0:
            raise TypeError
        if type(c) not in (int,float):
            raise TypeError
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        
       

    def __add__(self,right):
        if type(right) not in (Poly, int,float):
            raise TypeError
        result = Poly()
        if type(right) in (int, float):
            right = Poly((right, 0))
        for power,coeff in self.terms.items():
            result._add_term(coeff,power)
        for power, coeff in right.terms.items():
            result._add_term(coeff, power)
        return result

    
    def __radd__(self,left):
        if type(left) not in (Poly, int,float):
            raise TypeError
        result = Poly()
        if type(left) in (int, float):
            left = Poly((left, 0))
        for power,coeff in self.terms.items():
            result._add_term(coeff,power)
        for power, coeff in left.terms.items():
            result._add_term(coeff, power)
        return result
    

    def __mul__(self,right):
        if type(right) not in (Poly, int,float):
            raise TypeError
        result = Poly()
        if type(right) in (int, float):
            right = Poly((right, 0))
        for power, coeff in self.terms.items():
            for rpower, rcoeff in right.terms.items():
                result._add_term(coeff*rcoeff, power+rpower)
        return result
    

    def __rmul__(self,left):
        if type(left) not in (Poly, int,float):
            raise TypeError
        result = Poly()
        if type(left) in (int, float):
            left = Poly((left, 0))
        for power, coeff in self.terms.items():
            for lpower, lcoeff in left.terms.items():
                result._add_term(coeff*lcoeff, power+lpower)
        return result
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) == Poly:
            return self.terms.items() == right.terms.items()
        else:
            right = Poly((right,0))
            return self.terms.items() == right.terms.items()




if __name__ == '__main__':
#     Some simple tests; you can comment them out and/or add your own before
#     the driver is called.
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