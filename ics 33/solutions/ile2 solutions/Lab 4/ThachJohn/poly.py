class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            assert type(c) in [int,float]
            assert type(p) == int and p >= 0
            if p in self.terms:
                assert c == self.terms[p]
            else:
                if c == 0:
                    continue
                self.terms[p]=c
            
        
            
            
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
                
        
        return 'Poly('+','.join('('+(str(v)+','+str(k)+')') for k,v in self.terms.items())+')'

    
    def __len__(self):
        max=0
        for k,v in self.terms.items():
            if k > max:
                max = k
        return max
    
    def __call__(self,arg):
        value=0
        for k,v in self.terms.items():
            value += v * (arg ** k)
        return value
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(),reverse=True):
            yield v,k
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            if index in self.terms:
                return self.terms[index]
            else:
                return 0
                    
            

    def __setitem__(self,index,value):
        if type(index)!=int or index < 0:
            raise TypeError
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError
        if index < 0:
            raise TypeError
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]: 
            raise TypeError
        if (type(p) != int and p < 0):
            raise TypeError
        if p not in self.terms and c != 0:
            self.terms[p]=c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p]==0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in [Poly,int]:
            raise TypeError
        if type(right)==int:
            right = Poly((right,0))
        for p,q in right.terms.items():
            for k,v in self.terms.items():
                if k == p:
                    self._add_term(q,k)
        return self
        


    
    def __radd__(self,left):
        if type(left) not in [Poly,int]:
            raise TypeError
        if type(left)==int:
            left = Poly((left,0))
        for p,q in left.terms.items():
            for k,v in self.terms.items():
                if k == p:
                    self._add_term(q,k)
        return self
        
    

    def __mul__(self,right):
        if type(right) not in [Poly,int]:
            raise TypeError
        if type(right) == int:
            right = Poly((right,0))
        for k,v in self.terms.items():
            for p,q in right.terms.items():
                k = k+p
                v = v*q
                self._add_term(v,k)
        return self
             
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError
        if type(right)==Poly:
            for k,v in self.terms.items():
                if k not in right.terms:
                    return False
                else:
                    return v == right.terms[k]
        else:
            if len(self.terms) == 1:
                if 0 in self.terms:
                    return right == self.terms[0]
            else:
                return False
        

    
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