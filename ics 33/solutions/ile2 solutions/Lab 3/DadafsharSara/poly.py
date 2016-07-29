class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for key,val in terms:
            if type(key,val) != int or float:
                raise TypeError('Not an int or float value')
            elif type(key,val) == int or float:
                self.terms[val] = key
            else:
                ###can continue only if is not equal to 0
                if val == 0:
                    pass
                elif val > 0 and key >= 0:
                    self.terms[val] = key
        
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
        return(str(self))

    def __len__(self):
        return max(self.terms.key())
    
    def __call__(self,arg):
        
        #p = x
        
        #return p
        pass
    
    def __iter__(self):
        def generate(iterable):
            for value in iterable:
                yield value
        return generate(self.terms)
            

    def __getitem__(self,index):
        if type(index) != int and index < 0:
            raise TypeError('Index is not an int and/or is less than zero.')
        elif index not in Poly:
            return(0)

    def __setitem__(self,index,value):
        if type(index) != int and index < 0:
            raise TypeError('Not an int and/or less than zero')
        elif index == 0:
            if index in self.terms:
                del index   

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        if type(c) != int or float and type(p) != int and p < 0:
            raise TypeError('coefficient was not an int or float and/or power was not int and/or was less than 0')
        else:
            if p not in c:
                if p != 0:
                    self.term[p] = c
                    
            elif p in c:
                
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
        if type(right) != Poly or int or float:
            raise TypeError('was not poly, int, or float.') 
        else:
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