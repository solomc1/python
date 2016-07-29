class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:
            coeff = x[0]
            power = x[1]
            assert type(coeff) in (int,float), "Coefficient must be int or float"
            assert (type(power) == int) and (power >= 0), "Power must be positive int or zero int"
            assert power not in self.terms, "Cannot repeat a power "
            if coeff != 0:
                self.terms[power] = coeff

        
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
        param = ''
        for x in self.terms.items():
            param += '('+str(x[1])+','+str(x[0])+')'+','
        return 'Poly({})'.format(param[:-1])

    
    def __len__(self):
        highest = 0
        for p,c in self.terms.items():
            if p > highest:
                highest = p
        return highest
    
    def __call__(self,arg):
        sum = 0
        for p,c in self.terms.items():
            sum += c*(arg**p)
        return sum
    

    def __iter__(self):
        for p in sorted(self.terms.keys(),reverse = True):
            yield (self.terms[p],p)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Index must be a positive integer")
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Power must be a positive integer")
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Power must be a positive integer")
        if index in self.terms:
            self.terms.pop(index)

    def _add_term(self,c,p):
        if type(p) != int or p < 0 or (type(c) not in (int,float)):
            raise TypeError("Power must be a positive integer")
        if p not in self.terms and c!=0:
            self.__setitem__(p,c)
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.__delitem__(p)
        

    def __add__(self,right):
        new = Poly()
        for p,c in self.terms.items():
            new._add_term(c,p)
        if type(right) in (int,float):
            new._add_term(right,0)
        elif type(right) == type(self):
            for p,c in right.terms.items():
                new._add_term(c,p)
        else:
            raise TypeError("Can only add Polynomial by int or float or another Polynomial")
        return new

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        new = Poly()
        if type(right) in (int,float):
            for p,c in self.terms.items():
                new._add_term(c,p)
            for p in new.terms.keys():
                new.terms[p] *= right
        elif type(right) == type(self):
            for p,c in self.terms.items():
                for rp,cp in right.terms.items():
                    new._add_term(c*cp,p+rp)
        else:
            raise TypeError("Can only add Polynomial by int or float or another Polynomial")
        return new
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) in (int,float):
            for v in self.terms.values():
                return v == right
        elif type(right) == type(self):
            return self.terms == right.terms
        else:
            raise TypeError("Can only compare Polynomial by int or float or another Polynomial")

    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()