class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            assert type(x[0]) in [int,float] , 'Poly.__init__: Illegal power in' + str(x)
            assert type(x[1]) is int, 'Poly.__init__: Illegal power in' + str(x)
            assert x[1]>= 0, 'Poly.__init__: Illegal power in' + str(x)
            assert x[1] not in self.terms, 'Poly.__init__: Illegal power in' + str(x)
            if x[0] != 0:
                self.terms[x[1]] = x[0]
            
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
        return 'Poly({})'.format(','.join('('+ str(y) +','+ str(x) +')' for x,y in self.terms.items()))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    def __call__(self,arg):
        total = 0
        assert type(arg) in [int,float], "Poly.__call__: Illegal type " + type(arg) + ' must be int or float'
        for power,coeff in self.terms.items():
            total += coeff*(arg**power)
        return total
    def __iter__(self):
        for x,y in sorted(self.terms.items(), reverse = True): 
            yield y,x

    def __getitem__(self,index):
        if type(index) is  not int:
            raise TypeError("Poly.__getitem__: Illegal type " + str(type(index))+" must be an integer")
        elif index < 0:
            raise TypeError("Poly.__getitem__: Illegal index " + str(index)+" must be >= 0")
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0              

    def __setitem__(self,index,value):
        if type(index) is  not int:
            raise TypeError("Poly.__setitem__: Illegal type " + str(type(index))+" must be an integer")
        elif index < 0:
            raise TypeError("Poly.__setitem__: Illegal index " + str(index)+" must be >= 0")
        if value == 0:
            if index in self.terms.keys():
                self.__delitem__(index)
        else:
            self.terms[index] = value
        
             

    def __delitem__(self,index):
        if type(index) is  not int:
            raise TypeError("Poly.__detitem__: Illegal type " + str(type(index))+" must be an integer")
        elif index < 0:
            raise TypeError("Poly.__detitem__: Illegal index " + str(index)+" must be >= 0")
        if index in self.terms.keys():
            del self.terms[index]

    def _add_term(self,c,p):
        if type(p) is  not int:
            raise TypeError("Poly._add_term: Illegal type " + str(type(p))+" must be an integer")
        elif(type(c) not in [int,float]):
            raise TypeError("Poly._add_term: Illegal type " + str(type(c))+" must be an numeric")
        elif p < 0:
            raise TypeError("Poly._add_term: Illegal coefficent " + str(p)+" must be >= 0")
        if p in self.terms.keys():
            new_sum = c + self.terms[p]
            if new_sum == 0:
                del self.terms[p]
            else:
                self.terms[p] = new_sum
        elif c != 0:
            self.terms[p] = c

    def __add__(self,right):
        if type(right) == Poly:
            p = Poly()
            for power,coef in self.terms.items():
                p._add_term(coef,power)
            for coef,power in right:
                p._add_term(coef,power)
            return p
        elif type(right) in [int,float]:
            p = Poly((right,0))
            for key,value in self.terms.items():
                p._add_term(value,key)
            return p
        else:
            raise TypeError('Poly.__add__ unordable Types' + str(type(right)) + 'with Poly')
    
    def __radd__(self,left):
        if type(left) in [int,float]:
            p = Poly((left,0))
            for key,value in self.terms.items():
                p._add_term(value,key)
            return p
        else:
            raise TypeError('Poly.__add__ unordable Types' + str(type(left)) + 'with Poly')
            
    

    def __mul__(self,right):
        if type(right) == Poly:
            p = Poly()
            for power,cof in self.terms.items():
                for coef,pow2 in right:
                    p._add_term(cof*coef,power+pow2)
            return p
        elif type(right) in [int,float]:
            p = Poly()
            for key,value in self.terms.items():
                p._add_term(right*value,key)
            return p
        else:
            raise TypeError('Poly.__mul__ unordable Types' + str(type(right)) + 'with Poly')
    

    def __rmul__(self,left):
        if type(left) in [int,float]:
            p = Poly()
            for key,value in self.terms.items():
                p._add_term(left*value,key)
            return p
        else:
            raise TypeError('Poly.__mul__ unordable Types' + str(type(left)) + 'with Poly')
    

    def __eq__(self,right):
        if type(right) is Poly:
            if(len(self) != len(right)):
                return False
            for i in self.terms.keys():
                if self.terms[i] != right[i]:
                    return False
            return True
        elif type(right) in [int,float]:
            return (False if len(self) != 0 else (False if 0 not in self.terms.keys() else self.terms[0] == right))
        else:
            raise TypeError('Poly.__eq__ unordable Types' + str(type(right)) + 'with Poly')
        

    
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