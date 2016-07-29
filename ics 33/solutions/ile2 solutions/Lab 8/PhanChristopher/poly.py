class Poly:
    
    def __init__(self,*terms) -> None:
        '''
        > self.terms is a dictionary 
            > keys are *powers* of x 
            > values are *coefficients* of x
        '''
        self.terms = {}
        if len(terms) == 0:
            return
        else:
            for coefficient,power in terms:
                #--------------------
                assert type(coefficient) == int
                assert type(power) == int
                assert power >= 0
                assert power not in self.terms
                #--------------------
                if coefficient == 0:
                    pass
                else:
                    self.terms[power] = coefficient
                #--------------------
        return
    
    def __str__(self) -> str:
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self) -> str:
        '''
        Can Do Better
        '''
        s = "Poly("
        for x in self.terms.items():
            s += str((x[1],x[0]))
            s +=","
        s = s.rstrip(",")
        s += ")"
        return s

    
    def __len__(self):
        '''
        Can Do Better
        '''
        length = 0
        for key in self.terms:
            for check in self.terms:
                if key>=check:
                    length = key
                else:
                    length = 0
        return length
    
    def __call__(self,arg:int or float):
        '''
        Can Do Better
        '''
        term = 0
        if type(arg) == int or type(arg) == float:
            for key,value in self.terms.items():
                term += value*(arg**key)
            return term
        else:
            raise TypeError("arg was not an int or float object")
    

    def __iter__(self):
        '''
        Can Do Better
        '''
        l = sorted(self.terms.items(),reverse=True)
        for t in l:
            yield (t[1],t[0])
            

    def __getitem__(self,index):
        '''
        Can Do Better
        '''
        if type(index) == int:
            if index >= 0:
                if index in self.terms:
                    return self.terms[index]
                else:
                    return 0
            else:
                raise TypeError("Incorrect Input")
        else:
            raise TypeError("Incorrect Input")

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0:
                if index in self.terms:
                    del self.terms[index]
                # equavelent to self.terms.__delitem__(index)
            else:
                self.terms[index] = value
        else:
            raise TypeError("Incorrect Input")
            

    def __delitem__(self,index) -> None:
        '''
        Is it this simple?
        '''
        if type(index) == int and index >= 0:
            if index in self.terms:
                self.terms.__delitem__(index)
        else:
            raise TypeError("Incorrect Input")
        return

    def _add_term(self,c,p) -> None:
        if type(c) == int or type(c) == float:
            if type(p) == int and p > 0:
                if p not in self.terms and p <= 0:
                    self.terms[p] = c
                elif p in self.terms and p <= 0:
                    self.terms[p] += c
                    if self.terms[p] == 0:
                        del self.terms[p]
            else:
                raise TypeError("Power is either not an int or negative")
        else:
            raise TypeError("Coefficient is neither a float or int object")
        return

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