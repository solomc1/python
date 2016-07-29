class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in [float, int], "Poly.__init__: illegal coefficient in: {}".format(term)
            assert type(term[1]) == int and term[1] >= 0, "Poly.__init__: illegal power in: {}".format(term)
            if term[0] != 0:
                assert term[1] not in self.terms, "Poly.__init__: power {} already in polynomial".format(term[1])
                self.terms[term[1]] = term[0]
                          
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
        return "Poly({})".format(','.join(['('+str(v)+','+str(k)+')' for k, v in self.terms.items()]))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return sorted(self.terms,reverse=True)[0]
    
    
    def __call__(self,arg):
        assert type(arg) in [int, float], "Poly.__call__: invalid argument; must be int or float"
        return eval(self.__str__().replace('x', '*('+str(arg)+')').replace('^', '**'))


    def __iter__(self):
        for k, v in sorted(self.terms.items(),reverse=True):
            yield (v, k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: index must and integer and >= 0')
        elif index in self.terms:
            return self.terms[index]
        return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: index must and integer and >= 0')
        elif index in self.terms and value == 0:
            del self.terms[index]
        elif value != 0:   
            self.terms[index] = value
        

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitem__: index must and integer and >= 0')
        elif index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Poly._add_term: coefficient must and integer or float')
        elif type(p) != int or p < 0:
            raise TypeError('Poly._add_term: power must and integer and >= 0')
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]   
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__add__: invalid type for operand +: ' + type(self) + ' and '
                            + type(right))
        result = eval(self.__repr__())
        if type(right) == Poly:
            for p, c in right.terms.items():
                result._add_term(c, p)
            return result
        result._add_term(right, 0)
        return result
        
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__mul__: invalid type for operand *: ' + type(self) + ' and '
                            + type(right))
        elif type(right) == Poly:
            result = Poly()
            for p1, c1 in self.terms.items():
                for p2, c2 in right.terms.items():
                    result._add_term(c1*c2, p1+p2)
            return result
        result = eval(self.__repr__())
        for i in result.terms:
            result[i] *= right
        return result
                       

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__eq__: invalid type for operand ==: ' + type(self) + ' and '
                            + type(right))
        elif type(right) == Poly:
            return self.terms == right.terms
        return len(self.terms) == 1 and self.terms[0] == right
    
    
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