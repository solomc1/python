class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        previous = []
        for i,j in terms:
            assert type(i) in [int, float] and type(j) in [int,float], i+' or '+j+' is not an integer or float'   
            assert j >= 0, j+' is not greater than 0'
            if i != 0:
                assert j not in previous, j+' appeared as a later term when with a non-zero coefficient'
                previous.append(j)
                self.terms[j] = i
            
            
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
        t = []
        for i in self.terms.items():
            t.append(i)
        return 'Poly({a})'.format(a = t)

    def __len__(self):
        max = 0
        for i in self.terms:
            if self.terms.get(i) > max:
                max = self.terms.get(i)
        return max
    
    def __call__(self,arg):
        return str(self).replace('x', '*{a}'.format(a = arg))
    

    def __iter__(self):
        lt = []
        for i in self.terms:
            pass
        pass
            

    def __getitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError('Not in integer or greater than 0')
        if index not in (self.terms):
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) not in [int] or index < 0:
            raise TypeError('Not in integer or greater than 0')
        if value == 0:
            self.terms.pop(index)
        if index not in (self.terms):
            return 0
        return self.terms[index]  

    def __delitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError('Not in integer or greater than 0')
        if index not in (self.terms):
            return 0
        if index in self.terms.keys():
            self.terms.pop(index)
        return self.terms[index]

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Not a Polynomial, integer, or float')

    
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Not a Polynomial, integer, or float')
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Not a Polynomial, integer, or float')
    

    def __rmul__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Not a Polynomial, integer, or float')
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Not a polynomial')
        if type(right) in [int, float]:
            return right in [self.terms.keys()]
        else:
            return self.terms == right.terms

    
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
#    print('  list collecting iterator results:',[t for t in p])
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