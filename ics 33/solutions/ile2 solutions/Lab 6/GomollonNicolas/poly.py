# Nicolas Gomollon, Lab 6

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coeff, power in terms:
            assert type(coeff) in (int, float), "Poly.__init__: illegal coefficient in : {}".format((coeff, power))
            assert (type(power) is int) and (power >= 0), "Poly.__init__: illegal power in : {}".format((coeff, power))
            assert power not in self.terms, "Poly.__init__: power({}) can only be defined once".format(power)
            if coeff != 0: self.terms[power] = coeff
        
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
        return "Poly({})".format(', '.join((str((coeff, power)) for power, coeff in self.terms.items())))

    
    def __len__(self):
        if len(self.terms) == 0: return 0
        return max(self.terms)
    
    def __call__(self,arg):
        return sum([(coeff * (arg ** power)) for power, coeff in self.terms.items()])
    

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), reverse=True):
            yield (coeff, power)
            

    def __getitem__(self,index):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__getitem__: illegal index : {}".format(index))
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__setitem__: illegal index : {}".format(index))
        if (value != 0):
            self.terms[index] = value
        elif index in self.terms:
            self.terms.pop(index)
        return None
            

    def __delitem__(self,index):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__delitem__: illegal index : {}".format(index))
        if index in self.terms:
            self.terms.pop(index)
        return None
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Poly._add_term: illegal coefficient in : {}".format((c, p)))
        if (type(p) is not int) or (p < 0):
            raise TypeError("Poly._add_term: illegal power in : {}".format((c, p)))
        if (c != 0) and (p not in self.terms):
            self[p] = c
        elif (p in self.terms):
            self[p] += c
        return None
        
       

    def __add__(self,right):
        if type(right) is Poly:
            new_terms = dict(self.terms)
            for power, coeff in right.terms.items():
                if power in new_terms:
                    if (new_terms[power] + coeff) != 0:
                        new_terms[power] += coeff
                    else:
                        new_terms.pop(power)
                else:
                    new_terms[power] = coeff
            return Poly(*[(coeff, power) for power, coeff in new_terms.items()])
        elif type(right) in (int, float):
            new_terms = [(coeff, power) for power, coeff in self.terms.items() if power > 0]
            new_terms += [(self[0] + right, 0)]
            return Poly(*new_terms)
        raise TypeError("Poly.__add__: illegal operand : {}".format(right))

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) is Poly:
            new_terms = {}
            for p1, c1 in self.terms.items():
                for p2, c2 in right.terms.items():
                    new_p = p1 + p2
                    new_c = c1 * c2
                    if new_p in new_terms:
                        new_terms[new_p] += new_c
                    else:
                        new_terms[new_p] = new_c
            return Poly(*[(coeff, power) for power, coeff in new_terms.items()])
        elif type(right) in (int, float):
            new_terms = dict(self.terms)
            for power, coeff in new_terms.items():
                new_terms[power] *= right
            return Poly(*[(coeff, power) for power, coeff in new_terms.items()])
        raise TypeError("Poly.__mul__: illegal operand : {}".format(right))
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) is Poly:
            return self.terms == right.terms
        elif type(right) in (int, float):
            if (len(self.terms) == 1) and (len(self) == 0):
                return self.terms[0] == right
            return False
        raise TypeError("Poly.__eq__: illegal operand : {}".format(right))

    
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