class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert type(t[0]) in [int,float], 'coefficient must be int/float'
            assert type(t[1]) is int and t[1] >= 0, 'power must be int and >= 0'
            if t[0] in self.terms.values() and t[1] != 0:
                raise AssertionError('power cannot appear in a later term with a non-0 coefficient')
            if t[0] != 0:
                self.terms[t[1]] = t[0]
        
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
        return 'Poly{}'.format(tuple(zip(self.terms.keys(), self.terms.values())))
              
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(self.terms)
    
    def __call__(self,arg):
        print(self.terms)
        result = 0
        for k,v in self.terms.items():
            result += v*(arg**k)
        return result

    def __iter__(self):
        for k,v in self.terms.items():
#         for k,v in sorted(self.terms.items(), key=(lambda p: p[1],-p[0])):
            yield (v,k)
            
    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be >= 0')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
              

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be >= 0')
        if value == 0 and value in self.terms.values():
            if self.terms[index] == value: 
                del self.terms[index]
        self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be >= 0')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError('power must be an int')
        if p < 0:
            raise TypeError('power must be >= 0')
        if type(c) not in [int,float]:
            raise TypeError('coefficient must be int/float')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
#         if p in self.terms.keys():
#             self.terms[p] += c
       

    def __add__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('operand must be Poly,int,or float')
        if type(right) in [int,float]:
            pass

    
    def __radd__(self,left):
        if type(left) not in [int,float]:
            raise TypeError('operand must be int,or float')
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('operand must be Poly,int,or float')
        if type(right) in [int,float]:
            pass

    def __rmul__(self,left):
        if type(left) not in [int,float]:
            raise TypeError('operand must be int,or float')
    

    def __eq__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('operand must be Poly,int,or float')
        if type(right) in [int,float]:
            for k,v in self.terms.items():
                return v == 0 and k == right
        if type(right) is Poly:
            if len(right) == len(self):
                for i in range(len(self)):
                    return right.terms.items() == self.terms.items()
    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()