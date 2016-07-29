class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coefficient, power in terms:
            assert type(coefficient) in [int, float], "illegal coefficient in : ({}, {})".format(coefficient, power)
            assert type(power) == int and power >= 0, "illegal power in : ({}, {})".format(coefficient, power)
            assert power not in self.terms, "duplicate power given : ({}, {})".format(coefficient, power)
            
            if coefficient != 0:
                self.terms[power] = coefficient
        
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
        return "Poly({})".format(", ".join("({}, {})".format(coefficient, power) for power, coefficient in self.terms.items()))

    
    def __len__(self):
        return max(self.terms) if len(self.terms) > 0 else 0
    
    def __call__(self,arg):
        assert type(arg) in [int, float], "illegal type for call : ({})".format(type(arg))
        return sum([c * arg ** p for p, c in self.terms.items()])

    def __iter__(self):
        for p, c in sorted(self.terms.items(), key = lambda x: x[0], reverse = True):
            yield (c, p)

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("illegal index: ({}),  must be of type int and greater than 0".format(index))
        if index in self.terms:
            return self.terms[index]
        return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("illegal power: ({}), must be of type int and greater than 0".format(index))
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("illegal index: ({}),  must be of type int and greater than 0".format(index))
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError("illegal coefficient in : ({}, {}), must be int or float".format(c, p))
        if type(p) != int or p < 0:
            raise TypeError("illegal power in : ({}, {}),  must be of type int and greater than 0".format(c, p))
        
        if p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        elif c != 0:
            self.terms[p] = c
            

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("unsupported operand type(s) for +: 'Poly' and '{}'".format(type(right)))
        
        result = eval(repr(self))
        if type(right) != Poly:
            right = Poly((right, 0))
        for p, c in right.terms.items():
            result._add_term(c, p)
        return result


    def __radd__(self,left):
        if type(left) not in [int, float]:
            raise TypeError("unsupported operand type(s) for +: '{}' and 'Poly'".format(type(left)))
        
        result = eval(repr(self))
        result._add_term(left, 0)
        return result
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("unsupported operand type(s) for *: 'Poly' and '{}'".format(type(right)))
        
        result = Poly()
        if type(right) != Poly:
            right = Poly((right, 0))
        for p1, c1 in self.terms.items():
            for p2, c2 in right.terms.items():
                result._add_term(c2 * c1, p2 + p1)
        return result
    

    def __rmul__(self,left):
        if type(left) not in [int, float]:
            raise TypeError("unsupported operand type(s) for *: '{}' and 'Poly'".format(type(left)))
        
        result = Poly()
        for p, c in self.terms.items():
            result._add_term(c * left, p)
        return result

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("unsupported relational operand type(s) for ==: 'Poly' and '{}'".format(type(right)))
        
        if type(right) != Poly:
            right = Poly((right, 0))
        
        for p2, c2 in right.terms.items():
            for p1, c1 in self.terms.items():
                if p1 != p2 or c1 != c2:
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
    print(Poly((1,1),(2,0)) == Poly((1,1),(2,0)))
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()