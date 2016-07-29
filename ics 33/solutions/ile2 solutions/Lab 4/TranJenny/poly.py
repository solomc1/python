class Poly:
    
    def __init__(self,*terms):
        
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for stuff in terms:
            power = stuff[1]
            coef = stuff[0]
            self.terms[power] = coef
        for keys in self.terms:
            if type(keys) not in [int, float]:
                raise AssertionError("Coefficient must be an int of float")

            
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
        rstring = ''
        for keys in self.terms:
            rstring +='('+str(self.terms[keys])+','+str(+keys)+')'
        return 'Poly('+rstring+')'

    
    def __len__(self):
        largest = 0
        for keys in self.terms:
            largest = max(self.terms.keys())
        return largest
    
    def __call__(self,arg):
        total = 0
        for keys in self.terms:
            power_cal = arg**keys
            mul_cal = power_cal * self.terms[keys]
            total += mul_cal
        return total
    

    def __iter__(self):
        list_tup= []
        for keys in self.terms:
            list_tup += [sorted(self.terms,key = self.terms[keys])]
            
            

    def __getitem__(self,index):
        if type(index) not in [int] or index <0:
            raise TypeError("type(index) must be an integer and greater than 0")
        else:
            for keys in self.terms:
                if index in self.terms.keys():
                    return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) not in [int] or index <0:
            raise TypeError("type(index) must be an integer and greater than 0")
        
            

    def __delitem__(self,index):
        for key,val in self.terms.items():
            if index == val:
                del val
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError("coefficient must be an integer or a float")
        if type(p) not in [int] or type(p) < 0:
            raise TypeError("power must be an int and must be greater than 0")
        
        
       

    def __add__(self,right):
        pass
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(self) != Poly and type(right) not in [int,float]:
            raise TypeError("One operand must be a Poly and the other operand is a Poly or a numberic (int or float)")
        elif type(self) not in [int,float] and type(right) != Poly:
            raise TypeError("One operand must be a Poly and the other operand is a Poly or a numberic (int or float)")
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
    print('  list collecting iterator results:',)
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