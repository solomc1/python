class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        for c,p in terms:
            assert type(c) in {int,float}
            assert type(p) is int and p >= 0
        
        self.terms = {}
        
        for coefficient,pow in terms:
            assert pow not in self.terms
            if coefficient != 0:
                self.terms[pow] = coefficient
        
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
        return "Poly({})".format(",".join("("+str(v)+","+str(k)+")" for k,v in self.terms.items()))

    
    def __len__(self):
        if not self.terms:
            return 0
        else:
            return sorted(self.terms, reverse=True)[0]
    
    def __call__(self,arg):
        total = 0
        for p,c in self.terms.items():
            total += c*(arg**p)
        return total
    

    def __iter__(self):
        a = [(v,k) for k,v in sorted(self.terms.items())]
        a.sort(key=lambda x:x[1], reverse = True)
        return iter(a)
#         return iter({(v,k) for k,v in sorted(self.terms.items())}) #TODO
            
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError(index, "is not an integer or less than 0.")
        
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0: raise TypeError(index, "is not an integer or less than 0.")
        if value == 0 and index in self.terms:
            del self.terms[index]
        else:
            if value != 0:
                self.terms[index] = value
            
    def __delitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError(index, "is not an integer or less than 0.")
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in {int, float} or type(p) is not int or p < 0:
            raise TypeError("Coefficients can only be ints/floats and integers can only be integers >= 0")
        try:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            else:
                self.terms[p] += c
                if self.terms[p] == 0:
                    self.__delitem__(p)
        except KeyError:
            pass     

    def __add__(self,right):
        if type(right) not in {Poly, int, float}: 
            raise TypeError("Operand can only only be Poly, int, or float")

        if type(right) is Poly:
            for p,c in right.terms.items():
                self._add_term(c,p)
            return self
        else:
            self._add_term(right,0)
            return self
    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        if type(right) not in {Poly, int, float}: 
            raise TypeError("Operand can only only be Poly, int, or float")
        a = Poly()
        if type(right) is Poly:
            terms = []
            for p,c in self.terms.items():
                for p_r,c_r in right.terms.items():
                    terms.append((p+p_r,self.terms[p]*right.terms[p_r]))
            for i in terms:
                if i[0] in terms:
                    a.terms[i[0]] *= i[1]
                else:
                    a._add_term(i[1],i[0])
            return a
        else:
            a = Poly()
            for k,v in self.terms.items():
                a.terms[k] = v
            for k,v in a.terms.items():
                a.terms[k] *= right
            return a
                
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) not in {Poly, int, float}: 
            raise TypeError("Operand can only only be Poly, int, or float")
        if type(right) is Poly:
            for p,c in self.terms.items():
                if right.terms[p] != c:
                    return False
            return True
        else:
            return len(self) == 0 and self.terms[0] == right

    
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
#     #driver.default_show_exception=True
#     #driver.default_show_exception_message=True
#     #driver.default_show_traceback=True
    driver.driver()