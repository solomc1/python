class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for (a,b) in terms:
            if type(a) != int and type(a) != float:
                raise AssertionError('must be int or float!')
            if type(b) != int and b < 0:
                raise AssertionError('must be an int whose value is >= 0')
            if b in self.terms:
                raise AssertionError('power cannot appear as a later term')
            self.terms[b] = a
        for k,v in self.terms.items():
            if v == 0:
                self.terms.pop(k)   
                
        
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
        start = ''
        for k,v in self.terms.items():
            pass
    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            temp = []
            for k,v in self.terms.items():
                temp.append(k)
            return max(temp)
    
    def __call__(self,arg):
        temp = []
        for k,v in self.terms.items():
            temp.append(((v*arg)**k))
        ans = sum(temp)
        return ans
    

    def __iter__(self):
        for k in self.terms:
            ans = sorted(k, key = lambda x: x[0], reverse = True)
        return (ans,self.terms[ans])
            
            
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('has to be a positive int')
        else:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int and index < 0:
            raise TypeError('has to be a positive int')
        else:
            if value == 0:
                for k,v in self.terms.items():
                    if v == 0:
                        self.terms.pop(k)
            return self.terms
                        

    def __delitem__(self,index):
        if type(index) != int and index < 0:
            raise TypeError('has to be a positive int')
        else:
            for k,v in self.terms.items():
                if k == index:
                    self.terms.pop(k)
                    return self.terms
                else:
                    return self.terms
                    
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('c must be int or float')
        if type(p) != int and p < 0:
            raise TypeError('p must be int that is >= 0')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            if p in self.terms and c != 0:
                self.terms[p] += c
        return self.terms
                
       

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('must be Poly, int or float')
        else:
            if type(right) == Poly:
                for k,v in right.items():
                    if k in self.terms:
                        self.terms[k] + v
                    else:
                        self._add_term(v,k)
                return self.terms
            else:
                self.terms + right 
                
                
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('must be Poly, int or float')
        else:
            if type(right) == Poly:
                for k,v in self.terms.items():
                    for a,b in right.items():
                        return k==a and v==b 
            else:
                for k,v in self.terms.items():
                    pass

    
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
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()