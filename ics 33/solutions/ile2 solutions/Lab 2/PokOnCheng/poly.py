class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for t in terms:
            assert type(t[0]) in [int,float],'Each coefficient must be an int or float value.'
            assert type(t[1]) is int and t[1]>=0,'Each power must be an int whose value is >=0'
            assert t[1] not in self.terms,'Power is repeated'
            if t[0] != 0:
                    self.terms[t[1]] = t[0]
        

            
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
        return 'Poly('+','.join(['('+str(v)+','+str(k)+')' for k,v in self.terms.items()])+')'

    
    def __len__(self):
        highest=0
        for key in self.terms.keys():
            if key>=highest:
                highest=key
        return highest
    
    def __call__(self,arg):
        answer = 0
        if type(arg) in [int,float]:
            for k,v in self.terms.items():
                answer = answer + (arg**k)*v
        return answer
    

    def __iter__(self):
        temp = sorted(self.terms,reverse=True)
        for key in temp:
            yield (self.terms[key],key)
            

    def __getitem__(self,index):
        if type(index) is int and index >= 0:
            return self.terms[index] if index in self.terms else 0
        else:
            raise TypeError('The argument should be an integer or >= 0')
            

    def __setitem__(self,index,value):
        if type(index) is int and index >=0:
            if value == 0:
                if index in self.terms:
                    del self.terms[index]
            else:
                self.terms[index]=value
        else:
            raise TypeError('The argument should be an integer or >= 0')
            

    def __delitem__(self,index):
        if type(index) is int and index >=0:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError('The argument should be an integer or >= 0')
            

    def _add_term(self,c,p):
        if type(c) in [int,float] and type(p) is int and p >= 0:
            if p not in self.terms and c != 0:
                self.terms[p]=c
            elif p in self.terms:
                self.terms[p]+=c
                if self.terms[p]==0:
                    del self.terms[p]
        else:
            raise TypeError('Coefficient must be int or float; power must be int and >= 0')
       

    def __add__(self,right):
        if type(right) in [Poly,int,float]:
            if type(right) is Poly:
                for rk,rv in right.terms.items():
                    if rk in self.terms:
                        self.terms[rk]+=rv
                    else:
                        self.terms[rk]=rv
            else:
                if self.terms[0]:
                    self.terms[0]+=right
                else:
                    self.terms[0]=right
            return self.__str__()
        else:
            raise TypeError('the compared item must be Poly, int, or float')

    
    def __radd__(self,left):
        if type(left) in [int,float]:
            if 0 in self.terms:
                self.terms[0]+=left
            else:
                self.terms[0]=left
            return self.__str__()
        else:
            raise TypeError('The compared item must be an int, float, or Poly')
    

    def __mul__(self,right):
        answer=dict()
        if type(right) in [Poly, int, float]:
            if type(right) is Poly:
                for k1,v1 in self.terms.items():
                    for k2,v2 in right.terms.items():
                        tempk=k1+k2
                        tempv=v1*v2
                        if tempk in answer:
                            answer[tempk]+=tempv
                        else:
                            answer[tempk]=tempv
                self.terms=answer
            else:
                for k in self.terms.keys():
                    self.terms[k]*=right
            return self.__str__()
        else:
            raise TypeError()
    

    def __rmul__(self,left):
        if type(left) in [int,float]:
            for k in self.terms.keys():
                self.terms[k]*=left
            return self.__str__()
        else:
            raise TypeError()
    

    def __eq__(self,right):
        if type(right) in [Poly,int,float] or len(self.terms)==len(right.terms):
            for k1,v1 in self.terms:
                if k1 in right.terms:
                    if v1 != right.terms[v1]:
                        return False
            return True
        else:
            raise TypeError()
        

    
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