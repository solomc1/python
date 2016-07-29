class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for co, power in terms:
            assert type(co) == int or type(co) == float, "coefficients must be an int or a float"
            assert type(power) == int and power >= 0, "power must be nonnegative integer"
            assert power not in self.terms.keys(), "duplicate powers now allowed"  
            if co == 0:
                continue
            self.terms[power] = co
        
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
        result = []
        for p, c in self.terms.items():
            result.append('{}'.format((c, p)))
        return "Poly({})".format(','.join(result))
            
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for p,c in self.terms.items():
            result += (c*arg**p)
        return result
    

    def __iter__(self):
        result = []
        power = sorted(self.terms.keys(), reverse = True)
        for p in power:
            result.append((self.terms[p], p))
        return iter(result)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("index must be a nonnegative integer")
        
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("index must be a nonnegative integer")
        if type(value) != int and type(value) != float:
            raise TypeError("coefficient must be a integer or float")
        if index not in self.terms.keys() and value == 0:
            pass
        elif index in self.terms.keys() and value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value    

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("index must be a nonnegative integer")
        elif index in self.terms.keys():
            del self.terms[index]
        
    def _add_term(self,c,p):
        if type(c) != float and type(c) != int:
            raise TypeError("coefficient must be int or float")
        if type(p) != int or p < 0:
            raise TypeError("power must be a nonnegative number")
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if c != 0:
                self.terms[p] += c
            else:
                del self.terms[p]


    def __add__(self,right):
        if type(self) == type(right):
            result = eval(repr(self))
            for p,c in right.terms.items():
                result._add_term(c,p)
            return str(result)
        elif type(right) == float or type(right) == int:
            r = Poly((right, 0))
            return str(self + r)
        else:
            raise TypeError("operand must be a float, int, or Polynomial in order to add")
            
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(self) == type(right):
            result = Poly()
            products = []
            for p,c in self.terms.items():
                for k,v in right.terms.items():
                    products.append((p+k,c*v))
            for p,c in products:
                result._add_term(c,p)
            return str(result)
        elif type(right) == int or type(right) == float:
            result = eval(repr(self))
            if right == 0:
                return 0
            else:
                for p in result.terms.keys():
                    result.terms[p] *= right
                return str(result)
        else:
            raise TypeError("operand must be a float, int, or Polynomial in order to multiply")
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == type(self):
            return self.terms == right.terms
        elif type(right) == int:
            if len(self.terms) > 1:
                return False
            elif len(self.terms) == 1 and 0 in self.terms.keys():
                return right == self.terms[0]
            elif len(self.terms) == 0:
                return 0 == right
        else:
            raise TypeError("unable to compare {} and {}".format(type(self), type(right)))
                

    
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