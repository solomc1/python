class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term_tuple in terms:
            # Meet the following assertions
            assert type(term_tuple[0]) in (int, float), 'Poly.__init__: the coef in ' + str(term_tuple) + ' is not a int or float'
            assert type(term_tuple[1]) is int, 'Poly.__init__: the power in ' + str(term_tuple) + ' is not an int'
            assert term_tuple[1] >= 0, 'Poly.__init__: the power in ' + str(term_tuple) + ' is not greater or equal to 0 ' 
            
            # Meet the last assertion
            if term_tuple[1] != 0 and term_tuple[1] in self.terms.values():
                raise AssertionError('Poly.__init__: the power in ' + str(term_tuple) + ' has already been used for a previous term')  
            
            # Only add a a term if its coef isn't 0
            if term_tuple[0] != 0:
                self.terms[term_tuple[1]] = term_tuple[0] 
            
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
        return 'Poly(' + ','.join([str(t) for t in self.terms.items()])+')'

    
    def __len__(self): 
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return max(self.terms.values())
        
    
    def __call__(self,arg):
        total = 0
        for item in self.terms.items():
            total += item[0] * (arg ** item[1])
        return total 
    

    def __iter__(self):
        for item in sorted(list(self.terms.items())): # I need to sort this so that the powers are decreasing
            yield (item[0], item[1])
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('the index is not an integer or is less than 0')
        
        for item in self.terms.items():
            if item[1] == index:
                return item[0]
        return 0 # Only happens when the argument is not a power in terms
            

    def __setitem__(self,index,value): # index: coef , value: power
        if type(value) is not int or value < 0:
            raise TypeError('the index is not an integer or is less than 0')
        if index == 0:
            del self.terms[0]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('the coef is not an int or float')
        if type(p) is not int or p < 0:
            raise TypeError('the power is not an int or is less than 0')
        if p not in self.terms.values() and c != 0:
            self.terms[c] = p
        elif p in self.terms.values():
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