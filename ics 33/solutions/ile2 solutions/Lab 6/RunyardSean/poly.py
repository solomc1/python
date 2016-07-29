import math
from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
             assert abs(term[0]) not in [int, float], 'Coefficient was not an int or a float'
             assert term[1] >= 0, 'Power was not greater than 0'
             if term[1] in self.__dict__:
                 raise AssertionError('Term was already in dictionary')
             coef = term[0] 
             powers = term[1]
             self.terms[coef] = powers
            
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
        return 'Poly(' + str(self.terms.items()) + ')'

    
    def __len__(self):
        for val in sorted(self.terms.values(), reverse = True):
            print(val)
            return val

    
    def __call__(self,arg):
        call_sum = 0
        for k,v in self.terms.items():
            call_sum += k*(arg**v)
        return call_sum
    

    def __iter__(self):
        def _gen(self):
            for i in sorted(self.items(), reverse = True):
                yield i
            
        return _gen(self.terms)

    def __getitem__(self,index):
        if index != int or index < 0:
            raise TypeError('Insufficient index')
        elif index not in self.__dict__:
            return 0
        else:
            return self.__dict__[index]
            

    def __setitem__(self,index,value):
        if type(val) != int or val < 0:
            raise TypeError('Power value not acceptable')
        else:
            self.__dict__[index] = value
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Right was not an appropriate value')
        else:
            pass

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Right was not an appropriate value')
        else:
            pass

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Right was not an appropriate value')
        else:
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
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()