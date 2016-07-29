class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for p in terms:
            assert type(p[0]) in (int, float), 'Poly.__init__: illegal coefficient in :' + str(p)
            assert type(p[1]) == int and p[1] >= 0, 'Poly.__init__: illegal power in :' + str(p)
            if p[1] not in self.terms:
                if p[0] != 0:
                    self.terms[p[1]] = p[0]
            else:
                if p[0] != 0:
                    raise AssertionError('Poly.__init__: illegal power in :' + str(p))
                
            
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
        return 'Poly(' + ','.join(['('+ str(v) + ',' + str(k) + ')' for k,v in self.terms.items()]) + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for x in self.terms:
            term = self.terms[x] * (arg ** x)
            result += term
        return result
    

    def __iter__(self):
        for x in sorted(self.terms, reverse = True):
            yield (self.terms[x], x)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Invalid index: either not a int or < 0: ' + str(index))
        else:
            if index not in self.terms.keys():
                return 0
            elif index >= 0:
                return self.terms[index]
            else:
                raise TypeError('Invalid index: not in dictionary: ' + str(index))
        

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Invalid index: either not a int or < 0: ' + str(index))
        if value == 0:
            if index in self.terms.keys():  
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Invalid index: either not a int or < 0: ' + str(index))
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Invalid power: either not a int or < 0: ' + str(p))
        if type(c) not in (int, float):
            raise TypeError('Invalid coefficient: either not a int or float: ' + str(c))
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        else:
            new_c = self.terms[p] + c
            if new_c != 0:
                self.terms[p] = new_c
            else:
                del self.terms[p]
            
           

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid operand type for +: ' + str(type(right)))
        if type(right) in (int, float):
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y], y)
            p._add_term(right, 0)
            return p
        else:
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y], y)
            for x in right.terms.keys():
                p._add_term(right.terms[x], x)
            return p

    
    def __radd__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Invalid operand type for +: ' + str(type(left)))
        if type(left) in (int, float):
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y], y)
            p._add_term(left, 0)
            return p
        else:
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y], y)
            for x in left.terms.keys():
                p._add_term(left.terms[x], x)
            return p
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid operand type for *: ' + str(type(right)))
        if type(right) in (int, float):
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y] * right, y)
            return p
        else:
            p = Poly()
            for y in self.terms.keys():
                for x in right.terms.keys():
                    p._add_term(self.terms[y] * right.terms[x], y + x)
            return p
    

    def __rmul__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Invalid operand type for *: ' + str(type(left)))
        if type(left) in (int, float):
            p = Poly()
            for y in self.terms.keys():
                p._add_term(self.terms[y] * left, y)
            return p
        else:
            p = Poly()
            for y in self.terms.keys():
                for x in left.terms.keys():
                    p._add_term(self.terms[y] * left.terms[x], y + x)
            return p
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid operand type for *: ' + str(type(right)))
        if type(right) in (int, float):
            return right in self.terms.values()
        else:
            for x in self.terms:
                for y in right.terms:
                    return y == x and self.terms[x] == right.terms[y]


    
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