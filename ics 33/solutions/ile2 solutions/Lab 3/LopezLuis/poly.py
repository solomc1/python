class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self._terms = terms
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for tup in terms:
            if tup[0] == 0:
                pass
            if type(tup[0]) not in [int,float]:
                raise AssertionError('Poly.__init__: illegal coefficient, not an int or float')
            if type(tup[1]) is not int:
                raise AssertionError('Poly.__init__: illegal power, not of the int type')
            if tup[1] < 0:
                raise AssertionError('Poly.__init__: illegal power, not greater than or equal to 0')  
            if tup[1] not in self.terms.keys():
                self.terms[tup[1]] = tup[0]
            else:
                raise AssertionError('Poly.__init__: illegal power, it has been set for a previous coefficient')
                
                
            
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
        return 'Poly'+str(self._terms)

    
    def __len__(self):
        if self.terms.items() == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        sum = 0
        if type(arg) in [int,float]:
            for k,v in self.terms.items():
                sum += v*arg**k
            return sum
    

    def __iter__(self):
        for k in self._terms:
            yield k
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__getitem__: the index was not the type int')
        if index < 0:
            raise TypeError('Poly.__getitem__: the index was less than 0')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms.get(index)
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Poly.__setitem__: the index is not the type int')
        if index < 0:
            raise TypeError('Poly.__setitem__: the index is less than 0')
        if value == 0:
            if value in self.terms.values():
                self.terms.pop(value)
        else:
            self.terms[index] = value   

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__setitem__: the index is not the type int')
        if index < 0:
            raise TypeError('Poly.__setitem__: the index is less than 0')
        else:
            if index in self.terms.keys():
                self.terms.pop(index) 
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Poly._add_term: the coefficient was not of the int or float type')
        if type(p) is not int:
            raise TypeError('Poly._add_term: the power was not of the int type')
        if p < 0:
            raise TypeError('Poly._add_term: the power cannot be less than zero')
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        if p in self.terms.keys():
            self.terms[p] + c
            if self.terms[p] == 0:
                self.terms.pop(p)

    def __add__(self,right):
        pass

    
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
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()