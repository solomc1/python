
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for i in terms:
            if i[0] == 0:
                pass
            elif not isinstance(i[0], (int, float)):
                raise AssertionError('Coefficient must be either int or float value')
            elif not (i[1] >= 0):
                raise AssertionError('Power must be an int whose value is >= 0')
            elif type(i[1]) != int:
                raise AssertionError('Power must be an int whose value is >= 0')
            else:
                self.terms[i[1]] = i[0]
                
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
        for i in self.terms:
            return 'Poly((' + str(i) + ',' + str(self.terms[i]) +'))'

    def __len__(self):
        if len(self.terms) == 0:
            length = 0
        else:
            keys = self.terms.keys()
            length = max(keys)
        return length
                    
    
    def __call__(self,arg):
        solution = 0 
        for i in self.terms:
            solution += self.terms[i]*(arg^i)
        return solution
            
    def __iter__(self):
        iterable = iter(self.terms)
        list = set()
        for i in iterable:
            list.add((self.terms[i], i))
            for i in list:
                yield i
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Argument must be int')
        elif index < 0:
            raise TypeError('Argument must be < 0')
        else:
            for i in self.terms:
                if i == index:
                    return self.terms[i]
            
    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Power argument must be int')
        elif index < 0:
            raise TypeError('Power argument must be > 0')
        elif value == 0:
            del self.terms[value]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Power argument must be int')
        elif index < 0:
            raise TypeError('Power argument must be > 0')
        else:
            for i in self.terms:
                if i == index:
                    del self.terms[i]
            

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