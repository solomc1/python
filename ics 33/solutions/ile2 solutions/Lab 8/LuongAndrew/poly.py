class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for co,power in terms:
            assert type(co) in (int,float), ('Poly.__init__: illegal coefficient in :', (co,power))
            assert type(power) == int and power >=0, ('Poly.__init__: illegal power in :', (co,power))
            if co != 0:
                assert power not in self.terms.keys(), ('Poly.__init__: power cannot appear twice :' ,(co,power))
                self.terms[power] = co
            
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
        return 'Poly('+ str([(v,k) for k,v in self.terms.items()]).strip('[]') +')'

    
    def __len__(self):
        max = 0
        for power in self.terms.keys():
            if power > max:
                max = power
        return max
    
    def __call__(self,arg):
        answer = 0
        for p,c in self.terms.items():
            answer += (c * arg**p)
        return answer
            
    

    def __iter__(self):
        iter = []
        for k,v in self.terms.items():
            iter.append((v,k))
        iter.sort(key = lambda x: x[1], reverse = True)
        for i in iter:
            yield i 
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError()
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError()
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
        
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError()
        if index in self.terms.keys():
            del self.terms[index]

    def _add_term(self,c,p):
        if (type(p) != int or p <0) or (type(c) not in (int,float)):
            raise TypeError
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
                                        
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) == Poly:
            for k,v in right.terms.items():
                self._add_term(v,k)
            return self
        if type(right) in (int,float):
            self.terms[0] += right
            return self

    
    def __radd__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError
        

    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) == Poly:
            pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) is Poly:
            if self.terms == right.terms:
                return True
            else:
                return False
        if type(right) in (int,float):
            if right in self.terms.values() :
                return True
            return False
            

    
if __name__ == '__main__':
#     # Some simple tests; you can comment them out and/or add your own before
#     # the driver is called.
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
    Poly( (3,2), (-2,1), (4,0) )(-2)
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()