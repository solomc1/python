class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for i in terms:
            assert type(i[0]) in [int,float], 'Illegal coefficient in'+str(i)
            assert type(i[1])==int, 'Illegal power in'+str(i)
            assert i[1] not in self.terms, 'The power cannot be overwritten.'
            assert i[0]!=0, 'Coefficient cannot be 0'
            self.terms[i[1]]=i[0]
            
            
        
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
        for i in self.terms.items():
            a = a+str(i)+','
        return 'Poly('+a[:-1]+')'
            

    
    def __len__(self):
        if len(self.terms.keys())==0:
            return 0
        else:
            result =0
            for i in self.terms:
                if result<i:
                    result = i
            return result
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += (arg**k)*v
        return result
    

    def __iter__(self):
        for i in sorted(self.terms.keys(),reverse=True):
            yield (self.terms[i],i)
            

    def __getitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError ('The index must be an integer and greater than 0')
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!=int or index<0:
            raise TypeError ('The index must be an integer and greater than 0')
        else:
            if value == 0:
                if index in self.terms:
                    del self.terms[index]
            else:
                self.terms[index]=value

    def __delitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError ('The index must be an integer and greater than 0')
        else:
            if index in self.terms:
                del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float) or type(p)!=int or p<0:
            raise TypeError ('Please enter valid coefficient and power')
        else:
            if p not in self.terms and c!=0:
                self.terms[p]=c
            elif p in self.terms and c+self.terms[p]!=0:
                self.terms[p]+=c
            elif p in self.terms and c+self.terms[p]==0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) in (float,int):
            if 0 in self.terms:
                self.terms[0]=right+self.terms[0]
            return self
        elif type(right) == Poly:
            for i in right.terms:
                self._add_term(right.terms[i],i)
            return self
        else:
            raise TypeError('Only an integer, a float or a Polynomial can be computed.')

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) in (float,int):
            for i in self.terms:
                self.terms[i]=self.terms[i]*right
            return self
        elif type(right)==Poly:
            for i in right.terms:
                for k,v in self.terms.items():
                    if i>0:
                        k+=1
                    v*=right.terms[i]
            return self
        else:
            raise TypeError('Only an integer, a float or a Polynomial can be computed.')
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) in (int,float):
            if len(self.terms.keys())==1 and 0 in self.terms.keys():
                return right==self.terms[0]
            else:
                return False
        elif type(right)==Poly:
            if sorted(self.terms.keys())==sorted(right.terms.keys()):
                for i in self.terms:
                    if self.terms[i] != right.terms[i]:
                        return False
                return True
            else:
                return False
        else:
            raise TypeError('Only an integer, a float or a Polynomial can be compared.')
            

    
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