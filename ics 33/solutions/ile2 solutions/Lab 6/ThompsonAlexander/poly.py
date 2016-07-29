class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms: #x is the (coefficient, power) tuple
            power = x[1]
            coef = x[0]
            assert type(power) is int and power >= 0, 'Poly.__init__: illegal power in: ' + str(x)
            assert type(coef) in (int, float), 'Poly.__init__: illegal coefficient in: ' + str(x)
            assert power not in self.terms.keys(), 'Poly.__init__: illegal power in: ' + str(x)
            if coef != 0:
                self.terms[power] = coef
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
        class_str = 'Poly('
        if len(self.terms) == 0:
            return 'Poly()'
        for x in self.terms.items():
            class_str += '(' + str(x[1]) + ',' + str(x[0])+'),'
        class_str = class_str[:-1]+')'
        return class_str
    
    def __len__(self):
        if len(self.terms) > 0:
            return max(self.terms.keys())
        return 0
    
    def __call__(self,arg):
        total = 0
        if len(self.terms) > 0:
            for power, coefficient in self.terms.items():
                term = coefficient*(arg**power)
                total += term
        return total
    

    def __iter__(self):
        for x in sorted(self.terms.items(), reverse=True):
            yield (x[1],x[0])

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: illegal index: '+str(index))
        return 0 if index not in self.terms else self.terms[index]
            
    def __setitem__(self,index,value):
        if type(index) is not int or index < 0 or type(value) not in (float, int):
            raise TypeError('Poly.__setitem__: illegal arguments: index='+str(index)+', value='+str(value))
        if value == 0 and index in self.terms:
            self.terms.pop(index)
        elif value == 0 and index not in self.terms:
            return
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: illegal index: '+str(index))
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(p) is not int or p < 0 or type(c) not in (float, int):
            raise TypeError('Poly._add_term: illegal arguments: c='+str(c)+', p='+str(p))
        if c == 0:
            return
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms and c + self.terms[p] == 0:
            self.terms.pop(p)
        else:
            self.terms[p] += c
        
    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__add__: illegal argument: right='+str(right))
        result = Poly()
        for p1, c1 in self.terms.items():
            result._add_term(c1,p1)
        if type(right) in (int, float):
            result._add_term(right, 0)
        else:
            for p1, c1 in right.terms.items():
                result._add_term(c1,p1)
        return result
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__mul__: illegal argument: right='+str(right))
        result = Poly()
        if type(right) in (int, float):
            for p, c in self.terms.items():
                result._add_term(c*right, p)
        else:
            for p1, c1 in self.terms.items():
                for p2, c2 in right.terms.items():
                    result._add_term(c1*c2, p1+p2)
        return result
    
    def __rmul__(self,left):
        return self.__mul__(left)

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__: illegal argument: right='+str(right))
        if type(right) in (int, float):
            return len(self.terms.values()) == 1 and 0 in self.terms.keys() and self.terms[0] == right
        else:
            for p1, c1 in self.terms.items():
                if p1 not in right.terms.keys() or right.terms[p1] != c1:
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