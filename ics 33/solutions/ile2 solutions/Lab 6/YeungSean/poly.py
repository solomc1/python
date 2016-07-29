class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for k,v in terms:
            if type(k) not in [int,float]:
                raise AssertionError('Poly.__init__:illegal coefficient in : {}'.format(Poly))
            elif type(v) != int or v < 0:
                raise AssertionError('Poly.__init__:illegal power in : {}'.format(Poly))
            else:
                self.terms[v] = k
        
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
        return 'Poly{}'.format(tuple([(v,k) for k,v in self.terms.items()]))

    
    def __len__(self):
        highest = 0 
        for k,v in self.terms.items():
            if k > highest:
                highest = k
        return highest
    
    def __call__(self,arg):
        value = 0
        for k,v in self.terms.items():
            value += v*(arg**k)
        return value  
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield (v,k) 
            

    def __getitem__(self,index):
        for k,v in self.terms.items():
            if type(index) == int and index >= 0: 
                if index == k:
                    return v
            else:
                raise TypeError("Incorrect type or negative power")
            
            

    def __setitem__(self,index,value):
        for k,v in self.terms.items():
            if type(index) == int and index >= 0: 
                return (v,k)
            else:
                raise TypeError("Incorrect type or negative power")
            

    def __delitem__(self,index):
        for k,v in self.terms.items():
            if type(index) == int and index >= 0: 
                if index == k:
                    del k,v
            else:
                raise TypeError("Incorrect type or negative power")
            

    def _add_term(self,c,p):
        for k,v in self.terms.items():
            if type(c) in [int,float] and type(p) in [int,float] and p >= 0: 
                if p == k:
                    return (v+c,k)       
            else:
                raise TypeError("Incorrect type or negative power")
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) in [Poly, int, float]:
            for k,v in self.terms.items():
                return v == right
        else:
            raise TypeError('{} is an incorrect type.'.format(right))

    
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