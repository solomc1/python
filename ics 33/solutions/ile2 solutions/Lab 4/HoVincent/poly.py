class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x,y in terms:
            assert type(x) in (int, float), "Poly.__init__: coefficent not an int or float: {}".format(x)
            assert type(y) == int and y >= 0, "Poly.__init__: coefficent not a positive int : {}".format(x)
            if y in self.terms:
                if self.terms[y] != 0:
                    raise AssertionError("Poly.__init__: this power already appears with another non-zero coefficient : {}".format(x))
            if x != 0:
                self.terms[y] = x
            
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
        result = []
        for terms in self.terms.items():
            result.append((terms[1], terms[0]))
        return "Poly{}".format(tuple(result))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        temp = []
        for term in self.terms:
            temp.append(term)
        return max(temp)
            
    
    def __call__(self,arg):
        assert type(arg) in (int, float), "Poly.__call__"
        result = 0
        
        for pow, coe in self.terms.items():
            result += coe *(arg ** pow)
            
        return result
            

    def __iter__(self):
        temp = []
        for pow, coe in self.terms.items():
            temp.append((coe, pow))
            
        for term in sorted(temp, key = lambda x: x[1], reverse = True):
            yield term
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Power is not a positive integer: {}".format(index))
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Power is not a positive integer: {}".format(index))
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Power is not a positive integer: {}".format(index))
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Coefficient is not type int or float: {}".format(c))
        if type(p) != int or p < 0:
            raise TypeError("Power is not a positive integer: {}".format(p))
        if c != 0 and p not in self.terms:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c != 0:
                self.terms[p]= self.terms[p] + c
            else:
                self.terms.pop(p)

        
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Unsupported operand: Poly() + {}()'.format(type(right)))
        result = Poly()
        if type(right) == Poly:
            for p, c in self.terms.items():
                for pow, coe in right.terms.items():
                    if p == pow:
                        result._add_term(c + coe, p)
            for p,c in self.terms.items():
                if p not in result.terms:
                    result._add_term(c,p)
            for p,c in right.terms.items():
                if p not in result.terms:
                    result._add_term(c,p)
        
        else:
            for p,c in self.terms.items():
                if p == 0:
                    result._add_term(right + c, p)
                else:
                    result._add_term(c,p)
        return result
                        
    
    def __radd__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Unsupported operand: {}() + Point()'.format(type(left)))
        result = Poly()
        for p,c in self.terms.items():
                if p == 0:
                    result._add_term(left + c, p)
                else:
                    result._add_term(c,p)
        return result
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Unsupported operand: Poly() * {}()'.format(type(right)))
        result = Poly()
    
        if type(right) == Poly:
            for p, c in self.terms.items():
                for pow, coe in right.terms.items():
                    result._add_term(p + pow, c * coe)
        else:
            for p,c in self.terms.items():
                result._add_term(c * right, p)
        
        return result

    def __rmul__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Unsupported operand: {}() * Poly()'.format(type(left)))
        result = Poly()
        for p, c in self.terms.items():
                result._add_term(c*left, p)
        return result
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Unorderable operator: Poly() == {}()'.format(type(right)))
        if type(right) == Poly:
            for p,c in self.terms.items():
                if right.terms[p] != c:
                    return False
        else:
            for p,c in self.terms.items():
                if p > 0:
                    return False
                elif self.terms[p] != right:
                    return False
        return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()