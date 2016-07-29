class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        #t[0] = coefficient t[1] == power
        for t in terms:
            assert type(t[1]) == int, 'Power must be an int'
            assert type(t[0]) == int or type(t[0]) == float, "Type of coefficient must be an int or a float"
            assert t[1] >= 0, 'Power cannot be negative'
            assert t[1] not in self.terms, 'There cannot be two coefficients for the same power'
            if t[0] != 0:
                self.terms[t[1]] = t[0]
            
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
        return 'Poly(' + ','.join([str((i[1], i[0])) for i in self.terms.items()]) + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms)
    
    def __call__(self,arg):
        poly_sum = 0
        for k,v in self.terms.items():
            poly_sum += (v * arg ** k)
        return poly_sum
    

    def __iter__(self):
        for k in sorted(self.terms, reverse = True):
            yield (self.terms[k], k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("The index must be an non-negative integer")
        elif index not in self.terms:
            return 0
        else: 
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("The index must be an non-negative integer")
        elif value == 0:
            if index in self.terms:
                del self.terms[index]
        else: 
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("The index must be an non-negative integer")
        elif index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError("The power must be an non-negative integer")
        elif type(c) != float and type(c) != int:
            raise TypeError("The coefficient must be a float or an integer")
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                if self.terms[p] == -c:
                    del self.terms[p]
                else:
                    self.terms[p] += c
       

    def __add__(self,right):
        new_poly = Poly()
        if type(right) == int or type(right) == float:
            for term in self.terms:
                new_poly._add_term(self.terms[term], term)
            new_poly._add_term(right, 0)
            return new_poly
        elif type(right) == Poly:
            for term in self.terms:
                new_poly._add_term(self.terms[term], term)
            for term in right.terms:
                new_poly._add_term(right.terms[term], term)
            return new_poly
        else:
            raise TypeError("Can only add a Poly by an int, a float, or a Poly")


    
    def __radd__(self,left):
        new_poly = Poly()
        if type(left) == int or type(left) == float:
            for term in self.terms:
                new_poly._add_term(self.terms[term], term)
            new_poly._add_term(left, 0)
            return new_poly
        else:
            raise TypeError("Can only add a Poly by an int, a float, or a Poly")
    

    def __mul__(self,right):
        new_poly = Poly()
        if type(right) == int or type(right) == float:
            for term in self.terms:
                new_poly._add_term(self.terms[term] * right, term)
            return new_poly
        elif type(right) == Poly:
            if len(right.terms) == 0:
                return 0
            else:
                for k,v in self.terms.items():
                    for p,c in right.terms.items():
                        new_poly._add_term(v * c, k + p)
                return new_poly
        else:
            raise TypeError("Can only multiply a Poly by an int, a float, or a Poly")

    def __rmul__(self,left):
        new_poly = Poly()
        if type(left) == int or type(left) == float:
            for term in self.terms:
                new_poly._add_term(self.terms[term] * left, term)
            return new_poly
        else:
            raise TypeError("Can only multiply a Poly by an int, a float, or a Poly")
    

    def __eq__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError("The right expression must be an int or a float or a Poly")
        else:
            if type(right) == Poly:
                if self.terms == right.terms:
                    for k, v in self.terms.items():
                        if v != right[k]:
                            return False
                    return True
                else:
                    return False
            else:
                if len(self.terms) == 1 and 0 in self.terms:
                    if self.terms[0] == right:
                        return True
                else:
                    return False
            
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