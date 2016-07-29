class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        t = iter(terms)
        for i in t:
            if type(i[1]) not in [int,float]:
                raise AssertionError( "Poly.__init__: illegal power in: (" + str(i) + ")")
#             elif type(j) is int and j>=0:
#                 raise AssertionError(str(j) + " is not bigger than 0 and " + str(type(j)) + "is not an int")
            elif i in self.terms:
                if i[0] != 0:  
                    raise AssertionError("Poly.__init__:illegal power in: " + str(type(i)))
                elif i[0] == 0:
                    pass
            else:
                self.terms[i[1]] = i[0] 
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
        t = set()
        for i in self.terms:
            t.add((i,self.terms[i]))
        return 'Poly(' + str(t) + ')'
    
    def __len__(self):
        max = 0
        for i in self.terms:
            if i == 0:
                max = 0
            elif i > max:
                max = i
        return max
    
    def __call__(self,arg):
        c = int(arg)
        if type(c) not in [int,float]:
            raise AssertionError("Poly.__call__: error in " + str(arg) + " is not an int or float")
        else:
            ans = 0
            for i in self.terms:
                ans += (self.terms[i] * (c**i))
            return ans

    def __iter__(self):
        #t = iter(self)
#         for i in self:
#             if i in ['-','+']:
#                 pass
#             elif i == 'x':
#                 pass
        pass
            

    def __getitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError('Poly.__getitem__: illegal ' +str(index) + ' is not an int or not > 0')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) not in int or index < 0:
            raise TypeError('Poly.__setitem__: illegal ' +str(index) + ' is not an int or not > 0')
        elif value == 0:
            value.clear()
        else:
            pass
            

    def __delitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError('Poly.__delitem__: illegal ' +str(index) + ' is not an int or not > 0')
        elif index in self.terms:
            self.terms[index].clear()
            index.clear()
        
            

    def _add_term(self,c,p):
        if c not in [int,float]:
            raise TypeError('Poly._add_term: illegal ' +str(c) + ' is not an int or float')
        elif p not in [int,float]:
            raise TypeError('Poly._add_term: illegal ' +str(p) + ' is not an int or float')
        elif p not in Poly and c != 0:
            self.terms[p] = c
        elif p in Poly and c in Poly:
            c + self.terms[p]
       

    def __add__(self,right):
        if right not in [int.float]:
            raise TypeError('Poly.__add__: illegal' + str(right) + 'is not an int or float')

    
    def __radd__(self,left):
        if left in [int.float]:
            raise TypeError('Poly.__radd__: illegal' + str(left) + 'is not an int or float')
    

    def __mul__(self,right):
        if right not in [int.float]:
            raise TypeError('Poly.__mul_: illegal' + str(right) + 'is not an int or float')
    

    def __rmul__(self,left):
        if left not in [int,float]:
            raise TypeError('Poly.__rmul__:illegal' + str(left) + 'is not an int or float')
    

    def __eq__(self,right):
        if right not in [int.float]:
            raise TypeError('Poly.__eq__: illegal' + str(right) + 'is not an int or float')

    
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