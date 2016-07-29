class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for coef,power in terms:
            assert type(coef) in [int,float]
            assert type(power)==int
            assert power >= 0 
            
            assert power not in self.terms.keys()
            
            if coef != 0:
                self.terms[power]=coef
            
            
            
        
        
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
        l = [str((coef,pwer)) for pwer, coef in self.terms.items()]
        mystr= ','.join(l)
        return('Poly({})'.format(mystr))

    
    def __len__(self):
        try:
            return max(list(self.terms.keys()))
        except:
            return 0
    
    def __call__(self,arg):
        mynum = 0
        for power,coef in self.terms.items():
            mynum+= (arg**power)*coef
        return mynum
    

    def __iter__(self):
        mytuplist =  list(self.terms.items())
        mytuplist= mytuplist.sort()
        def mygen(l):
            for p,c in l:
                yield (c,p)
        return(mygen(self.terms))

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError
        elif index not in self.terms.keys():
            return 0
        else:
            return(self.terms[index])
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError 
        elif index not in self.terms.keys() and value != 0:
            self.terms[index]=value
        elif index in self.terms.keys() and value != 0:
            self.terms[index]=value
        else:
            self.terms.pop(index)
            
            

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError 
        if index in self.terms.keys():
            self.terms.pop(index)
    
            

    def _add_term(self,c,p):
        if type(c) not in [int,float] or type(p)!= int or p<0:
            raise TypeError
        else:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p not in self.terms.keys() and c != 0:
                x = self.terms[p]+c
                if x !=0:
                    self.terms[p]=x
                else:
                    self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError
        else:
            if type(right)==Poly:
                for p,c in right.terms.items():
                    self._add_term(c,p)
                    return self
            else:
                self._add_term(right,0)
                return self
                         

    
    def __radd__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError
        self._add_term(left,0)
        return self
    

    def __mul__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError
        else:
            if type(right)==Poly:
                for p,c in right.terms.items():
                    c*p
                    return self
            else:
                self.terms[p]= c*right
                return self
    

    def __rmul__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError
        for p,c in self.terms.items():
            self.terms[p]= c*left
        return self 
            
    

    def __eq__(self,right):
        if type(right) not in[Poly,int,float]:
            raise TypeError
        for i in range[len(self)]:
            try:
                return(self.terms[i]==right.terms[i])
            except:
                return False
                
        
        

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
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
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()