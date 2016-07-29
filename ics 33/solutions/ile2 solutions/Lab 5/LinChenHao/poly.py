class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {p:c for c,p in terms if p!= 0}
        for p, c in self.terms.items():
            assert type(c) in {int,float}
            assert type(p) == int
            assert p >= 0 
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
        repp =  ''
        for p, c in self.terms.items():
            repp += '{(),()}'.format(c,p)
        return 'Poly({})'.format[1:]

    
    def __len__(self):
        return max((p for p in self.terms.keys()))
    
    
    def __call__(self,arg):
        result = 0
        for p, c in self.terms.items():
            result += c * ((arg)**p)
        return result
    

    def __iter__(self):
        tup = sorted(((c,p) for p , c in self.terms.items()), reverse = True)
        tup = ((c,p) for p, c in tup)
        for ttup in tup:
            yield tup
       

            

    def __getitem__(self,index):
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if value < 0 or type(value) != int:
            raise TypeError('your value must be an integer that is greater than 0')
        if index ==0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be an integer or greater than 0')
        if index in self.terms.keys():
            del self.terms[index]
            
            

    def _add_term(self,c,p):
        if type(c) not in  [float, int]:
            raise TypeError('the coefficient has to a float or an integer')
        if type(p) != int or p >= 0 :
            raise TypeError('power number needs to be an integer and be 0 or greater than 0')
        if p in self.terms:
            self.terms[0] += c
            if self.terms[p] == 0:
                del self.terms[p]           
        if p not in self.terms and c != 0:
            self.terms[p] = c
        
        
       

    def __add__(self,right):
        if right == Poly:
            new_poly = Poly()
            for p , c in self.terms.items()
            

    
    def __radd__(self,left):
        if left not in (int, float):
            return TypeError('left  must be a poly, int or float')
    

    def __mul__(self,right):
        if right not in (Poly, int, float)
            return TypeError(' right be a poly, int or float')

    def __rmul__(self,left):
        if left not in (Poly, int, float)
            return TypeError('left must be a poly, int or float')
    

    def __eq__(self,right):
        if right not in (Poly, int, float)
            return TypeError('right must be a poly, int or float')

    
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