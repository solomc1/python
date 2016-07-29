import re

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coeff,power in terms:
            assert type(coeff) in [int,float]
            assert type(power) in [int]
            assert power >=0, 'Power must be greater than or equal to 0.'
            assert power not in self.terms.keys(), 'Power already exists.'
            if coeff == 0:
                pass
            else:
                self.terms[power] = coeff
        
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
        
        return 'Poly(' + ','.join([str(item) for item in self.terms.items()]) + ')'

    
    def __len__(self):
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for power,coeff in self.terms.items():
            result += coeff*(arg**power)
        return result
    

    def __iter__(self):
        
        ordered = sorted(self.terms, reverse=True)
        for power in ordered:
            yield (self.terms[power],power)
            

    def __getitem__(self,index):
        
        if type(index) != int or index < 0:
            raise TypeError
        
        if index not in self.terms.keys():
            return 0
        
        return self.terms[index]
            

    def __setitem__(self,index,value):
        
        power = index
        coeff = value
         
        if type(power) != int or power < 0:
            raise TypeError
         
        else:
            if coeff == 0:
                if power in self.terms.keys:
                    del self.terms[power]
            else:
                self.terms[power] = coeff
        
    def __delitem__(self,index):
        
        if type(index) != int or index < 0:
            raise TypeError
        
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        
        assert type(c) in [int,float]
        assert type(p) == int and p >= 0
        
        if p not in self.terms.keys():
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        for r_power,r_coeff in right.terms.items():
            self._add_term(r_coeff,r_power)
        return self

    
    def __radd__(self,left):
        self.__add__(left)
        return self
    

    def __mul__(self,right):
        return self
    

    def __rmul__(self,left):
        
        self.__mul__(left)
        return self

    def __eq__(self,right):
        
        return str(self) == str(right)

        for power,coeff in self.terms.items():
            try:
                if coeff != right.terms[power]:
                    return False
            except:
                return False

    
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