class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) in (int, float) and type(i[1]) is int and i[1]>=0 and i[1] not in self.terms, 'Wrong input, please try again'
            if i[0] == 0:
                continue
            self.terms[i[1]]= i[0]
        
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
        a = ','.join('(' + str(v) +','+ str(k)+')' for k,v in self.terms.items())
        return 'Poly('+ a +')'

    
    def __len__(self):
        if max(self.terms)>0:
            return max(self.terms)
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += v*arg**k
        return result
    

    def __iter__(self):
        class p_iter():
            def __init__(self, terms ):
                self.terms = terms
                self.n = (max(self.terms),self.terms[max(self.terms)])
            def __next__(self):
                if self.terms == {}:
                    raise StopIteration
                self.n = (self.terms[max(self.terms)], max(self.terms))
                del self.terms[max(self.terms)]
                return self.n
                
        return p_iter(self.terms)
                
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Index should be an int')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Index should be an int')
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Index should be an int')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) is not int or p < 0:
            raise TypeError('Please enter the correct input')
        if p not in self.terms and p != 0:
            self.terms[p] = c
        if p in self.terms:
            self.terms[p] = self.terms[p]+c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float ):
            raise TypeError('Poly object can only add Poly or int/float object')
        if type(right) is int:
            right = Poly((right,0))
        for i in self.terms:
            if i in right.terms:
                right.terms[i] += self.terms[i]
            else:
                right.terms[i] = self.terms[i]
        return right
        
        
        
            

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float ):
            raise TypeError('Poly object can only multiply Poly or int/float object')
        if type(right) is int:
            right = Poly((right,0))
        temp = Poly((0,0))
        for a,b in right.terms.items():
            for c,d in self.terms.items():
                temp.__add__(Poly((b+d,a*c)))
        return right

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float ):
            raise TypeError('Poly object can only compare with Poly or int object')
        if type(right) is int:
            right = Poly((right,0))
        return self.terms == right.terms
    

    
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
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()