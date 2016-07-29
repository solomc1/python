class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}  
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        s = set()
        for c, p in terms:
            if not isinstance(c, (int, float)) or not isinstance(p, (int)):
                raise AssertionError('Coefficient or Power not if type int')
            
            elif p <0:
                raise AssertionError('Power is negative')
            
            elif c != 0:
                self.terms[p] = c

            
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
        
        return 'Poly('+','.join(str(i) for i in self.terms)+')'

    
    def __len__(self):
        
        if len(self.terms) == 0:
            return 0
        
        else:
            return len(self.terms) -1
    
    def __call__(self,arg):
        
        if not isinstance(arg, (int, float)):
            raise AssertionError('Arg not if type int or float')
        
        else:
            
            l = list()
            
            for k, v in self.terms.items():
                l.append(k*arg**v)
                
            return sum(l)
    

    def __iter__(self):
        
        for k, v in self.terms.items():
            yield v, k

    def __getitem__(self,index):
        
        if type(index) != int or index <0:
            raise TypeError('index is not of type int')
        
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        
        if index < 0:
            raise TypeError('index is less than 0')
        
        elif type(index) != int:
            raise TypeError('index not of type int)')
        
        else:
            self.terms[index] = value 
            

    def __delitem__(self,index):
        pass  

    def _add_term(self,c,p):
        pass  
       

    def __add__(self,right):
        pass 
    
    def __radd__(self,left): 
        pass 

    def __mul__(self,right):
        
        return Poly(right*t for t in self.terms)

    def __rmul__(self,left):
        
        return Poly(left*t for t in self.terms)
    

    def __eq__(self,right):
        
        return self.terms == right.terms 

    
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