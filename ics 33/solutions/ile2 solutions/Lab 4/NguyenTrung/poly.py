import math

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) in (int,float), 'coefficent must be int or float'
            assert type(i[1]) is int and i[1] >= 0
            assert i[1] not in self.terms, 'double times appear'
            if i[0] != 0:
                self.terms[i[1]] = i[0]
        
        
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
        return 'Poly('+str(str(v,k) for [v,k] in self.terms.items())+')'

    
    def __len__(self):
        if len(self.terms) != 0:
            return max(self.terms)
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
#         assert arg in (int,float), 'wrong arg'
        for i in self.terms:
            result += math.pow(arg,i)*self.terms[i]
        return int(result)
    

    def __iter__(self):
        it = iter(self.terms)
        for i in reversed(sorted(it)):
            yield (self.terms[i],i)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('wrong index type')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('wrong index type')
        elif value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('wrong index type')
        elif index in self.terms:
            del self.terms[index]
        else:
            pass
            

    def _add_term(self,c,p):
        if type(c) not in (int,float) and type(p) is not int and p >= 0:
            raise TypeError('wrong c or p')
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if (self.terms[p] + c) == 0:
                del self.terms[p]
            else:
                self.terms[p] += c
       

    def __add__(self,right):
        newPoly = Poly()
        if type(right) is Poly:
            for i in right.terms:
                newPoly._add_term(i, right.terms[i] + self.terms[i])
#         elif type(right) is int:
#                 newPoly._add_term(i, right.terms[i] + right)
        return newPoly

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()