
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}

        for term in terms:#term is one 2-tuple, 1st val is coeff, 2nd is power
            coeff = term[0]
            power = term[1]
            self.terms[term[1]] = term[0]
            if terms[1] in self.terms:
                if self.terms[terms[0]] !=0:
                    raise AssertionError('Power appeared earlier without a coefficient of 0')
            assert type(term[0])  in [int,float] and term[0] != 0, 'invalid type for coefficient'
            if type(term[1]) != int: # If the power is not an int, raise assertionerror
                raise AssertionError('invalid type for power')
            assert term[1] >= 0, 'Power value is not greater than or equal to 0' #check if power is >= 0
        
            
        
        
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
        # Want key and value as a pair Poly( (3,2), (-2,1), (4,0) )
        return 'Poly( ' + str(self.terms.items()) + ' )'
        
        
            
    

    
    def __len__(self):

        l = []
        for k in self.terms:
            l.append(k)
        return max(l)
    
    def __call__(self,arg):
        for k in self.terms:
            return self.terms[k] * (arg**k)
            
            
        
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('illegal index value')
        if index not in self.terms():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError('illegal index value')
        self.terms.update(index = value)
        
        if value == 0:
            self.terms.pop[self.terms[index]]
        
            

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('illegal index value')
        self.terms.pop(index)
        
            

    def _add_term(self,c,p):
        pass
       

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