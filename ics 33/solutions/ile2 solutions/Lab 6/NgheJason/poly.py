class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.x = terms
        self.terms = {}
        for i,v in terms:
            assert type(i) in [int,float], 'Poly.__init__: terms('+str(i)+') not an int or float.'
            assert type(v) in [int], 'Poly.__init__: illegal power in : ('+ str(i)+ ','+str(v)+')'
            assert v >= 0, 'Poly.__init__: illegal power in : ('+ str(i)+ ','+str(v)+')'
            assert v not in self.terms.keys(), 'Poly.__init__: terms('+str(v)+') cannot appear as a later term if it appears as an earlier term.'
            if i != 0:
                self.terms[v] = i
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
        return 'Poly'+str(self.x)

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            list = []
            for x in self.terms.keys():
                list.append(x)
            return max(list)
    
    def __call__(self,arg):
        answer = 0
        if type(arg) in [int,float]:
            for x in self.terms.keys():
                answer += (self.terms[x]*arg**x)
        return answer
                
                        
    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) is int:
            if index >= 0:
                if index in self.terms.keys():
                    return self.terms[index]
                else:
                    return 0
            else:
                raise TypeError
        else:
            raise TypeError
            
            

    def __setitem__(self,index,value):
        '''if type(index) is int:
            if index >= 0:
                if index in self.terms.keys():
                    if value == 0:
                        self.terms.pop(index)
                    else: 
                        self.terms[index] = value
                else:
                    if value == 0:
                        self.terms.pop(index)
                    else:
                        self.terms[index] = value
            else:
                raise TypeError
        else:
            raise TypeError '''           

    def __delitem__(self,index):
        if type(index) is int and index >= 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            raise TypeError

    def _add_term(self,c,p):
        if type(c) in [int,float] and type(p) is int and p >= 0:
            if p in self.terms.keys():
                self.terms[p] += c
            else:
                self.terms[p] = c
            if self.terms[p] == 0:
                self.terms.pop(p)
            return self
        else:
            raise TypeError
       

    def __add__(self,right):
        if type(right) in [Poly]:
            for i in right.terms.keys():
                if i in self.terms.keys():
                    self.terms[i] += right.terms[i]
                else:
                    self.terms[i] = right.terms[i]
            return self
        if type(right) in [int,float]:
            return self._add_term(right,0)
        else:
            raise TypeError

    
    def __radd__(self,left):
        return self._add_term(left,0)
    

    def __mul__(self,right):
        pass
        

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        ans = False
        if type(right) is Poly:
            return self.terms == right.terms                   
        if type(right) in [int,float]:
            for i in self.terms.keys():
                if self.terms[i] == right:
                    ans = True
                return ans
        else:
            raise TypeError
        

    
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
   #print('  list collecting iterator results:',[t for t in p])
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