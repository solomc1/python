import goody

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for a,c in self.terms.items():
            assert(a == int or a == float)
            assert(type(c) is int)
            assert(c >= 0)
            if c[0] < c[:-1]:
                raise AssertionError
             
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
        return str(self.terms)

    
    def __len__(self):
        for a in self.terms.keys():
            if int(a) == 0:
                return 0
            else:
                return a
    
    def __call__(self,arg):
        value = 0
        for a,b in self.terms.items():
            value = a*(arg**b)
        return value
    

    def __iter__(self):
        return iter(sorted([a,b] for a,b in self.terms.items(),reverse = True))
           

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError
        if index < 0:
            raise TypeError
        else:
            for c,b in (self.terms.items()):
                if index != b:
                    return 0
                else:
                    return c
        
            
            

    def __setitem__(self,index,value):
        if type(index) is not int and index < 0:
            print(goody.type_as_str(index))
        if value == 0:
            return self.terms.keys.pop([value])
            
            

    def __delitem__(self,index):
        if type(index) is not int and index < 0:
            print(goody.type_as_str(index))
        else:
            for a,b in (self.terms.items()):
                if index in b:
                    return (self.terms.pop[a:index])
                else:
                    pass

    def _add_term(self,c,p):
        if type(c) and type (p) is not int or float and p < 0:
            print('C or P is not an int or a float or P < 0')
        else:
            if p not in self.terms.items() and p != 0:
                return self.terms.add([c,p])
            elif p in self.terms.items():
                return self.terms.add([c,p])
            
                
            
       

    def __add__(self,right):
#        value = 0
#        for a,b in self.terms.items():
#            for c,d in right.items():
#                if b == d:
#                    value = 
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