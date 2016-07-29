class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            if p in self.terms:
                raise AssertionError("Poly.__init__: power cannot appear as a later term")
        
            assert type(c) in (int, float), "Poly.__init__: invalid coefficient type in : {}".format(terms)
            assert type(p) is int and p >= 0, "Poly.__init__: illegal power in : ({},{})".format(c,p)
            if c == 0:
                pass            
            else:
                self.terms[p] = c
#         print(self.terms)
                
            
        
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
            
        for i in range(len(self.terms)):
            for t in self.terms.items():
                
                return "Poly({})".format(t)

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0 
        return max(self.terms.keys())
             
    
    def __call__(self,arg):
        v=0
        for p,c in self.terms.items():
            v += c*arg**p
        return v
    

    def __iter__(self):
#         for c,p in self.terms.items():
#             yield p,c
        def gen(iterable):
            for c,p in iterable:
                yield p,c
                
        return gen(self.terms.items())
        
    
    
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: illegal index : {}".format(index))
        else:
            for p,c in self.terms.items():
                if index == p:
                    return c
                if index not in self.terms.keys():
                    return 0
        
        
    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__setitem__: illegal power")
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
            else:
                pass
        else:
            self.terms.update({index:value})
                     

    def __delitem__(self,index):
        if index in self.terms:
            self.terms.pop(index)
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__: illegal power")
            

    def _add_term(self,c,p):
#         for pow,cf in self.terms.items():
        if type(c) not in (int, float):
            raise TypeError("Poly._add_term: illegal coefficient: {}".format(c))
        if type(p) != int and p < 0:
            raise TypeError("Poly._add_term: illegal power: {}".format(p))
        
        
        if p in self.terms.items() and c !=0:
            self.terms.update({p:c})
            return self.terms
            
        if p in self.terms.items():
            for pow,cf in self.terms.items():
                if c + cf == 0:
                    self.terms.pop(pow) 
                    return self.terms
                else:
                    self.terms.update({p:c+cf})
                    return self.terms
            

    def __add__(self,right):
        for p,c in self.terms.items():
            for rp,rc in right:
                if type(right) == Poly:
                    if rp in self.terms:
                        return Poly(rp, rc+c)
                elif type(right) in (int, float):
                    pass          
                    
            
        else:
            raise TypeError("Poly.__add__: unsupported operand type(s) for +: {}".format(type(right)))
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Poly.__eq__: unsupported operand type(s) for ==")
        else:
            if type(right) == Poly:
                for p,c in self.terms.items():
                    for rp,rc in right:
                        if p == rp: 
                            return c == rc
                        else:
                            return False
            elif type(right) in (float, int):
                for p,c in self.terms.items():
                    if p == 0:
                        return c == right
                    

    
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
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()