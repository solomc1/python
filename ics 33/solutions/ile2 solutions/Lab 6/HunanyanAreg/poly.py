class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if type(term[0]) not in [int, float]:
                raise AssertionError('Poly.__init__: illegal coefficient in', term)
            
            if type(term[1])!=int or term[1]<0:
                raise AssertionError('Poly.__init__: illegal power in', term)
            
            if term[1] in self.terms.keys():
                raise AssertionError('Poly.__init__: can not have multiple coefficients with the same power power in', term)
            
            if term[0]!=0:
                self.terms[term[1]]=term[0]
                
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
        pol=''
        for k,v in self.terms.items():
            pol+='({},{}),'.format(v,k)
        return 'Poly({})'.format(pol[:-1])

    
    def __len__(self):
        len=0
        for k in self.terms.keys():
            if k > len:
                len=k
        return len
    
    def __call__(self,arg):
        ret=0
        for k,v in self.terms.items():
            ret+=(arg**(k))*v
        return ret

    def __iter__(self):
        li=[]
        for k,v  in self.terms.items():
            li.append((v,k))
        li.reverse()
        
        for i in li:
            yield i
             

    def __getitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError('Index must be a non negative integer')
        
        else:
            for key, value in self.terms.items():
                if key==index:
                    return value
                
                elif index not in self.terms.keys():
                    return 0
            

    def __setitem__(self,index,value):
        if type(index)!=int or index<0:
            raise TypeError('Setting index must be a non negative integer')
        
        if value == 0:
            for k,v in self.terms.items():
                if v == value:
                    del self.terms[k]   
                    
        else:
            self.terms[index]=value

    def __delitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError('Delete index must be a non negative integer')
        
        else:
            if index in self.terms.keys():
                del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Coefficient must be an int or float')
        
        if type(p) not in [int] or p<0:
            raise TypeError('Power must be a non negative int')
        
        if p not in self.terms.keys() and c>0:
            self.terms+=[p]=c
        
        else:
            for k,v in self.terms.items():
                if k == p:
                    s=c+v
                    if s == 0:
                        del self.terms[k]
                    else:    
                        self.terms[p]=s
            

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    #Some simple tests; you can comment them out and/or add your own before
    #the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
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