class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            if type(c) not in [int,float]:
                raise AssertionError('The type of coefficient is a unsupported operand type:' + str(c))
            if type(p) != int:
                raise AssertionError('The type of power is a unsupported operand type:' + str(c))
            if p < 0:
                raise AssertionError('The power must be a positive integer:' + str(p))
            self.terms[p] = c
#             for po,co in self.terms.items():
#                 if p in self.terms.keys() and co >= 0:
#                     raise AssertionError('Power is repeated and coefficient is not negative' + str(po) + str(p)) 
                
                
            
            
            
        
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
        a = ''
        for c,p in self.terms.items():
            a += ('('+str(p)+','+str(c)+')')
        return 'Poly('+a+')'
            

    
    def __len__(self):
        a = list(self.terms.keys())
        return max(a)
    
    def __call__(self,arg):
        if len(self.terms.items()) == 0:
            return 0
        x=0
        for c,p in self.terms.items():
            if p != 0:
                x += p*(arg**c)
            else:
                x += c
        return x
            
    def __iter__(self):
        for c,p in self.terms.items():
            yield (p,c)
            

    def __getitem__(self,index):
        if type(index) != int and index <0:
            raise TypeError('The index must be positive and a integer' + str(index))
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int and index <0:
            raise TypeError('The index must be positive and a integer' + str(index))
        
        
        
            

    def __delitem__(self,index):
        if type(index) != int and index <0:
            raise TypeError('The index must be positive and a integer' + str(index))
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('The type of coefficient is a unsupported operand type:' + str(c))
        if type(p) != int:
            raise TypeError('The type of power is a unsupported operand type:' + str(c))
        if p < 0:
            raise TypeError('The power must be a positive integer:' + str(p))
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        if p in self.terms.keys():
            a = self.terms[p] + c
            if a == 0:
                del self.terms[p]
            else:
                a
            
       

    def __add__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('The type of the right object/integer is a unsupported operand type' + str(right))
        b = self
        if type(right) == Poly:
            for c,p in right.terms.items():
                b._add_term(p,c)
        else:
            b.terms[0]
            
        
        return b
    
            

    
    def __radd__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError('The type of the right object/integer is a unsupported operand type' + str(left))
        a = self
        for c,p in left.terms.items():
            a._add_term(p,c)
        return a
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('The type of the right object/integer is a unsupported operand type' + str(right))
        list_1 = []
        list_2 = []
        for a,b in self.terms.items():
            list_1.append((a,b))
        for c,d in self.terms.items():
            list_2.append((c,d))
        if type(right) == Poly:
            return list_1 == list_2
        else:
            for i in self.terms.values():
                i = right
            
            
            
        

    
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