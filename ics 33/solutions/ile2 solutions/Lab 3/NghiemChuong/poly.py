from goody import irange, type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.co = terms[0]
        self.power = terms[1]
    
        
        assert type_as_str(self.co) not in ['int','float'] or (type(self.power) is int and self.power <0), AssertionError
#         Fill in the rest of this method, using *terms to intialize self.terms
        
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
        return 'Poly({})'.format(self.terms)
    
    def __len__(self):
        return len(self.terms)
    
    def __call__(self,arg):
        return  arg

    def __iter__(self):
        pass
        
    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError
        else:
            return self.terms[index]
    

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        if type(c) is int and type(p) is int: 
            return self.co + c, self.power + p
        
#         else:
#             return self.terms + 
       

    def __add__(self,right):
        if type(right) is not Poly:
            return self + right 
        else:
            return self + right
    
    def __radd__(self,left):
        return self + left 
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) is Poly:
            return self.terms ==  right

    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()