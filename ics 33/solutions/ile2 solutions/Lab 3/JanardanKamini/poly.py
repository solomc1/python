class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict({})
        for a,b in terms:
            assert type(a) in [int,float], 'Wrong type'
            assert type(b)==int, 'Wrong type'
            assert b>=0, 'Power cannot be negative'
            if a!=0:
                self.terms[b]=(a)
            else:
                raise AssertionError('Poly.__init__:illegal power in: '+str(b))

        
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
        for k,v in self.terms.items():
            return 'Poly('
                               
    def __len__(self):
        for k in self.terms.keys():
            return k

    
    def __call__(self,arg):
        sum=0
        for k,v in self.terms.items():
            sum+= (v*(arg**k))
        return sum
        
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield v,k

    def __getitem__(self,index):
        if type(index)!=int:
            raise TypeError('Not an integer')
        if index<0:
            raise TypeError('Cannot be negative value')
        return self.terms[index]

            

    def __setitem__(self,index,value):
        if type(index)!=int:
            raise TypeError('Not an integer')
        if index<0:
            raise TypeError('Cannot be negative value')
        if index!=0:
            self.terms[index]=value
        if self.terms[index] ==0:
            del self.terms[index]

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError('Not an integer')
        if index<0:
            raise TypeError('Cannot be negative')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Coefficient not numeric')
        if type(p) !=int or p<0:
            raise TyperError('Power not an integer')
        if p !=0:
            self.terms[p]=c
        if p==0:
            self.terms[p]=c

    

    def __add__(self,right):
        assert type(right) in [int,float,Poly], 'Type of right not numeric'
        if type(right) in [int,float]:
            for k,v in self.terms.items():
                if k==0:
                    self.terms[k]=v+right
        if type(right) is Poly:
            for r, rv in right.terms.items():
                if r in self.terms.keys():
                    for k in self.terms.keys():
                        return k+r
        if right ==0:
            return 0
                

    def __radd__(self,left):
        if type(left) in [int,float]:
            for k,v in self.terms.items():
                if k==0:
                    self.terms[k]=left+v
        if left==0:
            return 0      
    

    def __mul__(self,right):
        assert type(right) in [int,float,Poly], 'Type of right not numeric'
        if type(right)==int or type(right)==float:
            if right == 0:
                return 0    
            for k,v in self.terms.items():
                self.terms[k]=(right*v)
                return self.terms
        if type(right)==Poly:
            for r,rv in right.terms.items():
                for k,v in self.terms.items():
                    self.terms[k+r]=[v+rv]
                    return self.terms
        if type(right)==Poly:
            if int not in right.terms.items():
                return 0



    def __rmul__(self,left):
        left*self
    

    def __eq__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('Type of right not numeric or Poly')
        if type(right) == Poly:
            return self.terms.keys()==right.terms.keys()
        if type(right)==int or type(right)==float:
            return self.terms[0]==right

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    #print('Start simple tests')
    #p = Poly((3,2),(-2,1), (4,0))
    #print('  For Polynomial: 3x^2 - 2x + 4')
    #print('  str(p):',p)
    #print('  repr(p):',repr(p))
    #print('  len(p):',len(p))
    #print('  p(2):',p(2))
    #print('  list collecting iterator results:',[t for t in p])
    #print('  p+p:',p+p)
    #print('  p+2:',p+2)
    #print('  p*p:',p*p)
    #print('  p*2:',p*2)
    #print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()