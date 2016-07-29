class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coef, pow in terms:
            assert type(coef) in [int, float], ("Assertion Error: value", coef, "does not comply")
            assert type(pow) == int, ("Assertion Error: value", pow, "not an int")
            assert pow >= 0, ("Assertion Error: value", pow, "is not a positive number")
            
            if coef != 0:
                self.terms[pow] = coef
            else:
                pass
        
        
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
        result = 'Poly(({}),({}),({}))'.format(i for i in self.terms.items())
        return(result)

    
    def __len__(self):
        maxlist = []
        if self.terms.items() == None:
            return 0
        else:
            for k,v in self.terms.items():
                maxlist.append(k)
        return max(maxlist)
            
        
    
    def __call__(self,arg):
        if type(arg) not in [int, float]:
            raise TypeError("Poly.__call__: arg", arg, "not an int or float")
        return
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield(v,k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: index", index, "is invalid")
        if index not in self.terms.keys():
            return(0)
        else:
            for k,v in self.terms.items():
                if index == v:
                    return(k)

            

    def __setitem__(self,pow,coef):
        if type(pow) not in [int, float] or pow < 0:
            raise TypeError("Poly.__setitem__: Illegal power:", str(pow))
        else:
            self.terms[pow] = coef
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__: index", index, "is invalid")
        else:
            for item in self.terms.items():
                if index in item:
                    self.terms[item[-1]] = []
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError("Poly._add_term ", c, "not an int or float")
        if type(p) != int or p < 0:
            raise TypeError("Poly._add_term ", p, "not valid")
        
        if p not in self.terms.values():
            if c != 0:
                self.terms[p] = c
      
       

    def __add__(self,right):
        if type(right) not in [Poly, int]:
            raise TypeError
        if type(right) == int:
            return self._add_term(right, 0)
        if type(right) == Poly:
            for i,m in right:
                self._add_term(i,m)
            

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError
        
        if type(right) == Poly:
            return self == right
        elif type(right) == int:
            if len(self.terms.items()) == 1:
                for i in self.terms.values():
                    return i == right
            else:
                return False
                


    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()