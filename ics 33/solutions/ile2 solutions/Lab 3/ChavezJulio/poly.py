class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if term[0] == 0:
                pass
            else:
                self.terms[term[1]] = term[0]

        # Fill in the rest of this method, using *terms to intialize self.terms
        for key, value in self.terms.items():
            if type(key) != int:
                raise AssertionError()
            elif type(value) != int and type(value) != float:
                raise AssertionError()
            elif key < 0:
                raise AssertionError()
            else:
                pass
                
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
        if self.terms.keys() == set():
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = str(self).replace('x', '*'+str(arg))
        return eval(result)
        
    

    def __iter__(self):
        def _gen(iterable):
            for k,v in iterable.items():
                yield (v,k)
        return _gen(self.terms)
            

    def __getitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError()
        if index not in self.terms.keys():
            return 0
        elif type(index) is int and index > 0:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        return
            

    def __delitem__(self,index):
        pass
            

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