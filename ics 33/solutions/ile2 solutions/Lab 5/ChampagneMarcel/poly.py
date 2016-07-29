class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if type(term[0]) in [int,float] and type(term[1]) == int:
                if term[1] < 0:
                    raise AssertionError("Poly.__init__: illegal power in:",term)
                if term[1] != self.terms.keys():
                    if term[0] != 0:
                        self.terms[term[1]] = term[0]
                else:
                    raise AssertionError("Poly.__init__: repeating term:",term)
            else: 
                raise AssertionError("Poly.__init__: illegal type in:",term)
        
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
        return 'Poly'+str( tuple((v,k) for k,v in self.terms.items()) )

    
    def __len__(self):
        if len(list(self.terms.keys())) == 0:
            return 0
        else:
            power = 0
            for key in self.terms.keys():
                if key > power:
                    power = key
            return power
                
    
    def __call__(self,arg):
        val_sum = 0
        for k,v in self.terms.items():
            val_sum += v*arg**k
        return val_sum
            
    

    def __iter__(self):
        temp = [(v,k) for k,v in self.terms.items()]
        for term in temp:
            yield term
            

    def __getitem__(self,index):
        if index in self.terms.keys():
            return self.terms[index]
        elif type(index) != int or index < 0:
            raise TypeError("Invalid index for Poly__getitem__:",index)
        else:
            return 0
            

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError("Invalid power for Poly__setitem__:",index)
        self.terms[index] = value
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            raise TypeError("Invalid power for Poly__delitem__:",index)
            

    def _add_term(self,c,p):
        if type(c) in [int,float] and type(p) == int and p >= 0:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p] += c
                if self.terms[p] == 0:
                    del self.terms[p]       
        else:
            raise TypeError("Invalid terms for Poly__delitem__:",c,p) 
            
            
       

    def __add__(self,right):
        pass
#         new_poly = []
#         if type(right) == Poly:
#             for k,v in self.terms.items():
#                 if k in right.terms.keys():
#                     new_poly.append((v+right.terms[k],k))
#                 else:
#                     new_poly.append((v,k))
#         return Poly(*tuple(new_poly))

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return list(self.terms.items()).sort() == list(right.terms.items()).sort()
        elif type(right) in [int,float]:
            return list(self.terms.items())[0][1] == [right]
        else:
            raise TypeError("Invalid comparison between Poly and",type(right))

    
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