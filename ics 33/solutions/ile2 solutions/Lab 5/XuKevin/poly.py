class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coef,power in terms:
            if type(coef) not in [int, float]:
                raise AssertionError('Coefficient not an int or float: coef is type ' + repr(type(coef)))
            if type(power) != int or power < 0:
                raise AssertionError('Power must be an int >= 0: pow = ' + repr(pow))
            if power in self.terms:
                raise AssertionError('Power: ' + repr(power) + ' specified twice')
            if coef != 0:
                self.terms[power] = coef

            
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
        terms = []
        for power,coef in self.terms.items():
            terms.append((coef, power))
        terms_str = ''
        for tup in terms:
            terms_str += str(tup) + ','
        terms_str = terms_str[:-1]
        return 'Poly(' + terms_str + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = int()
        for power,coef in self.terms.items():
            result += arg**power * coef
        return result
    

    def __iter__(self):
        for power, coef in sorted(self.terms.items(), reverse=True):
            yield (coef, power)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int < 0: index = ' + repr(index))
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int < 0: index = ' + repr(index))
        if value == 0 and index in self.terms:
            del self.terms[index]
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int < 0: index = ' + repr(index))
        elif index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
                raise TypeError('Coefficient not an int or float: c is type ' + repr(type(c)))
        if type(p) != int or p < 0:
                raise TypeError('Power must be an int >= 0: p = ' + repr(p))
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Invalid type: right must be an integer, a float, or a Poly')
        elif type(right) == Poly:
            new_p = Poly()
            for p,c in self.terms.items():
                new_p._add_term(c, p)
            for p,c in right.terms.items():
                new_p._add_term(c, p)
        else:
            new_p = self
            new_p._add_term(right, 0)
        return new_p

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Invalid type: right must be an integer, a float, or a Poly')
        elif type(right) == Poly:
            new_p = Poly()
            for p1,c1 in self.terms.items():
                for p2,c2 in right.terms.items():
                    new_p._add_term(c1*c2, p1+p2)
        else:
            new_p = Poly()
            for p,c in self.terms.items():
                new_p._add_term(c*right, p)
        return new_p
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Invalid type: right must be an integer, a float, or a Poly')
        if type(right) == Poly:
            return len(self) == len(right) and self[len(self)] == right[len(self)]
        else:
            return len(self) == 0 and self[0] == right

    
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