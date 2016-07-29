class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i,j in self.terms:
            if type(i) not in  (int,float):
                raise AssertionError('Poly.__init__: Illegal coeffcient in: (' + str(i)
                                     + ',' + str(j) +')')
            elif j <= 0:
                raise AssertionError('Poly.__init__: Illegal power in: (' + str(i)
                                     + ',' + str(j) +')')
    
                 
                
            
            
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
        return str(self)

    
    def __len__(self):
        for k in self.terms.values():
            if k != 0:
                return self.terms.values[1]
            else:
                return 0
    
    def __call__(self,arg):
        pass
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        elif index < 0:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        elif index not in self.terms.key():
            return 0
        else:
            return self.terms(index)

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        elif index < 0:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        elif value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        elif index < 0:
            raise TypeError('Poly.__getitem__: Invalid index(' +str(index)+')')
        else:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            if p <= 0:
                raise TypeError('Poly._add_term: Invalid coefficient and power(' + 
                                str(c) +','+str(p))

    def __add__(self,right):
        if type(right) == (int or float):
            return (self + right)
        elif type(right) == Poly:
            return (self.poly + self.right)
        else:
            raise TypeError('Poly.__add__: Invalid Type('+str(right)+')')

    
    def __radd__(self,left):
        return self + left

    def __mul__(self,right):
        if type(right) == (int or float):
            return (self * right)
        elif type(right) == Poly:
            return (self.poly * self.right)
        else:
            raise TypeError('Poly.__mul__: Invalid Type('+str(right)+')')
   
    def __rmul__(self,left):
        return self * left
       
    def __eq__(self,right):
        if type(right) == (int or float):
            return (self == right)
        elif type(right) == Poly:
            return (self.poly == self.right)
        else:
            raise TypeError('Poly.__eq__: Invalid Type('+str(right)+')')
        
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