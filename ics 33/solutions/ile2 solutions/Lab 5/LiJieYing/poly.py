class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            if type(c) not in (int,float):
                raise AssertionError('coefficient must be an int or float value')
            elif p<0 or type(p) != int:
                raise AssertionError('power must be an int that is greater than or equal to 0')
            elif terms.count(p)>1 :
                raise AssertionError('power cannot appears a a later term if it appears as an earlier term')
            elif c != 0:
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
        start = 'Poly('
        for k,v in self.terms.items():
            start+= '('+str(k)+','+str(v)+'),'
        return start.strip(',')+')'

    
    def __len__(self):
        return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += int(v)*(arg**int(k))
        return total
                
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield (v,k)
            
            

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Index has to be an int and great than or equal to zero')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError('Index has to be an int and great than or equal to zero')
#         if value == 0 and value in self.terms:
#             self.terms.pop(value)
        else:
            self.terms[index] = value
            
            
            

    def __delitem__(self,index):
        if index in self.terms.values():
            del self.terms[index]
            

    def _add_term(self,c,p):
#         if c not in (int,float) and p != int and p<0:
#             raise TypeError('coefficient must be int or float type and power must be int that is greater than or equal to 0')
#         if p not in self.terms and c != 0:
#             self.terms[p] = c
        pass
       

    def __add__(self,right):
        if type(right) == Poly:
            pass
        elif type(right) in (int,float):
             pass
        else:
            raise TypeError('operand is not a Poly or int or float value')
        
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            pass
        elif type(right)  in (int,float):
            pass
        else:
            raise TypeError('operand not a Poly or int or float type')

    
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