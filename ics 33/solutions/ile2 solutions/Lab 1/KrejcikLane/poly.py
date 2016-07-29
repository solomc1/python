class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for a,b in terms:
            if type(a) not in [int,float]:
                raise AssertionError('Poly.__init__: type('+a+') not int or float' )
            elif type(b) is not int:
                raise AssertionError('Poly.__init__: illegal power in: ({},{})').format(a,b)
            elif b < 0:
                raise AssertionError('Poly.__init__: power'+b+'is negative; invalid')
#             for x,y in terms:
#                 if y == b:
#                     raise AssertionError('Poly.__init__: cannot have two values with the same powers')
        for c,p in terms:
            self.terms[p] = c
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
#         if len(self.terms) == 2:
#             return 'Poly(({},{})'.format(self.terms.values(),self.terms.keys())
        slist = list(self.terms.items())
        return 'Poly('+','.join(str((c,p)) for p,c in slist)+')'

    
    def __len__(self):
        highest = 0
        for i in self.terms.keys():
            if i > highest:
                highest = i
        return highest
    
    def __call__(self,arg):
        sum = 0
        for p,c in list(self.terms.items()):
            sum += (c*arg)**p
        return sum
    
    @staticmethod
    def _gen(x):
        slist = list(sorted(x.items()))
        for p,c in slist.reverse():
            yield (c,p)

    def __iter__(self):
        return Poly._gen(dict(self.terms))
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: '+index+'is not int or is negative')
        for p,c in self.terms:
            if p == index:
                return c

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: '+index+'is not int or is negative')
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: '+index+'is not int or is negative')
        else:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Poly._add_term: type('+c+') is not int or float')
        elif type(p) is not int or p<0:
            raise TypeError('Poly._add_term: type('+p+') is not int or is negative')
        if type(p) is not Poly and c != 0:
            self.terms[p] = c
        elif type(p) is Poly:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__add__: type(right) is not of Poly, int or float type')
        if type(right) in [int,float]:
            return Poly._add_term(int,0)
        elif type(right) is Poly:
            return self.terms + right

    
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Poly.__radd__: type(left) is not of Poly, int or float type')
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__mul__: type(right) is not of Poly, int or float type')
    

    def __rmul__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('Poly.__rmul__: type(left) is not of Poly, int or float type')
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__eq__: type(right) is not of Poly, int or float type') 
        if type(right) is Poly:
            for each in self.terms:
                for i in right:
                    if each == i:
                        if self.terms[each] != right[i]:
                            return False
            return True
        if type(right) in [int,float]:
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