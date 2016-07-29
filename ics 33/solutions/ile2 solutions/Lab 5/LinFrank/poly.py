class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for c,p in terms:
            assert type(c) in (int, float)
            assert type(p) == int and p >= 0
            if p in self.terms.keys():
                assert self.terms[p] == 0,'Poly.__init__: cannot have two same powers'
            if c != 0:
                self.terms[p] = c
        
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
        terms_str = ''
        for k,v in self.terms.items():
            terms_str += '('+str(v)+','+str(k)+')'
        return 'Poly('+terms_str+')'

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        solution = 0
        for power,coefficient in self.terms.items():
            solution += coefficient * (arg ** power)
        return solution
    

    def __iter__(self):
        def _gen(terms):
            for power,coefficient in sorted(terms.items(), reverse = True):
                yield (coefficient, power)
        return _gen(self.terms)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError( 'Poly.__getitem__: index must be an int greater than 0:' + str(index))
        if index in self.terms:
            return self.terms[index]
        elif index not in self.terms:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError( 'Poly.__setitem__: index must be an int greater than 0:' + str(index))
        if value == 0 and (index in self.terms):
            del self.terms[index]
        if value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError( 'Poly.__delitem__: index must be an int greater than 0:' + str(index))
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if not type(c) in (int, float):
            raise TypeError
        if type(p) != int or p < 0:
            raise TypeError
        if (p not in self.terms) and (c != 0):
            self.terms[p] = c
        elif p in self.terms:
            potential_new_c = self.terms[p] + c
            if potential_new_c == 0:
                del self.terms[p]
            else:
                self.terms[p] = potential_new_c
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__add__: can only add types Poly with int, float, Poly')
        sum_poly = Poly()
        for power, coefficient in self.terms.items():
            sum_poly._add_term(coefficient, power)
        if type(right) in (int, float):
            sum_poly._add_term(right, 0)
        elif type(right) == Poly:
            for rpower, rcoefficient in right.terms.items():
                sum_poly._add_term(rcoefficient, rpower)
        return sum_poly

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__mul__: can only multiply types Poly with int, float, Poly')
        product_poly = Poly()
        for power, coefficient in self.terms.items():
            product_poly._add_term(coefficient, power)
        if type(right) in (int, float):
            for power, coefficient in self.terms.items():
                product_poly[power] = coefficient*right

        return product_poly
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__eq__: can only compare types Poly with int, float, Poly')
        if type(right) == Poly:
            for power in right.terms.keys():
                if power not in self.terms or self.terms[power] != right[power]:
                    return False
            return True
        if type(right) in (float, int):
            if len(self.terms.items()) != 1:
                return False
            elif tuple(self.terms.items())[0] != 0:
                return False
            elif tuple(self.terms.items())[1] == right:
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()