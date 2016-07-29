class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coef,power in terms:
            assert type(coef) in (int,float), 'Coefficient is not an int or float'
            assert type(power) is int and power >= 0, 'Illegal power in {}'.format((coef,power))
            if coef != 0:
                if power in self.terms and self.terms[power] != 0: assert False, 'Repeat key'
                self.terms[power] = coef            
        
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
        return 'Poly({args})'.format(args = ','.join('('+str(coef)+','+str(power)+')' for power,coef in self.terms.items()))
                                      
       
    def __len__(self):
        return max(self.terms.keys()) if len(self.terms) != 0 else 0
    
    def __call__(self,arg):
        ans = 0
        for power in self.terms:
            ans += self.terms[power] * (arg**power)
        return ans    

    def __iter__(self):
        for power in sorted(self.terms, reverse = True):
            yield (self.terms[power],power)          

    def __getitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError("Illegal index in getitem")
        return self.terms[index] if index in self.terms else 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0: raise TypeError("Illegal index in setitem")
        if value != 0:  self.terms[index] = value
        elif index in self.terms: del self.terms[index]
        
    def __delitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError("Illegal index in delitem")
        if index in self.terms: del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("Illegal coefficient " +str(c))
        elif type(p) is not int or p < 0:
            raise TypeError("Illegal power "+str(p))
        elif p in self.terms:
            self.terms[p]+=c
            if self.terms[p] == 0: del self.terms[p]
        elif c != 0:
            self.terms[p] = c  

    def __add__(self,right):
        if type(right) not in (Poly,int,float): raise TypeError("Illegal operand "+str(right))
        #create a copy of self
        self_copy = Poly()
        
        if type(right) is Poly:
            for power in self.terms:
                if power in right.terms:
                    self_copy._add_term(self.terms[power] + right.terms[power], power)
                else:
                    self_copy._add_term(self.terms[power],power)
        else:
            self_copy._add_term(right,0)

        return self_copy
    
    def __radd__(self,left):
        if type(left) not in (Poly,int,float): raise TypeError("Illegal value " + str(left))
        return left + self
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float): raise TypeError("Illegal operand "+str(right))
        #create a copy of self
        self_copy = Poly()
        
        if type(right) is Poly:
            for pow1 in self.terms:
                for pow2 in right.terms:
                    self_copy._add_term(self.terms[pow1] * right.terms[pow2], pow1+pow2)
        else:
            for power in self.terms:
                self_copy._add_term(self.terms[power]*right,power)
        
        return self_copy
    

    def __rmul__(self,left):
        if type(left) not in (Poly,int,float): raise TypeError("Illegal operand " + str(left))
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float): raise TypeError("Illegal operand " +str(right))
        
        if type(right) is Poly:
            if all([ key1 == key2 for key1, key2 in zip(self.terms.keys(),right.terms.keys())]):
                return True

    
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