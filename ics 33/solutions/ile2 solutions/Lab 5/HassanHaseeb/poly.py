class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for coef, pow in terms:
            assert type(coef) in [int, float]
            assert type(pow) in int
            assert pow > 0            
            assert pow in self.terms.keys
            assert coef in self.terms.values
            
        
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
        p = eval(Poly(self))
        return 'Poly('+p+')'

    
    def __len__(self):
        powers = []
        if self.terms.key != None:
            for i in self.terms.key:
                powers.append(i)
        return max(powers)
            
    
    def __call__(self,arg):
        if type(arg) in [int, float]:
            p.replace('x', arg)
            return eval(p)
                
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) in [int] or index<0:
            return self.terms[index]
        elif index not in self.terms.keys:
            return int(0)
        else:
            raise TypeError;'index is not a type int'

            

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        if type(index) in [int] or index >= 0:
            self.terms.remove[index]
        else:
            raise TypeError; 'either type is not int or index < 0'
            

    def _add_term(self,c,p):
        if type(c) not in [int, float] and type(p) not in [int, float]:
            raise TypeError; 'type of coeficient and power are not ints or floats' 
        pass
       

    def __add__(self,right):
        if type(right) not in [int, float]:
            raise TypeError; 'type of right is not an int or float'
        else:
            pass

    
    def __radd__(self,left):
        if type(left) not in [int, float]:
            raise TypeError; 'type of left is not an int or float'
        else:
            pass

    def __mul__(self,right):
        if type(right) not in [int, float]:
            raise TypeError ;'type of right is not an int or float'
        else:
            pass

    def __rmul__(self,left):
        if type(left) not in [int, float]:
            raise TypeError ;'type of left is not an int or float'
        else:
            pass

    def __eq__(self,right):
        if type(right) in [int or float]:
            for coef,pow in self.terms:
                if self.terms[pow] == right.terms[pow] and self.terms[coef] == right.terms[coef]:
                    return True
                if self.terms[pow] != right.terms[pow] or self.terms[coef] != right.terms[coef]:
                    return False
        else:
            raise TypeError; 'the argument is not a type int or float'
        

    
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