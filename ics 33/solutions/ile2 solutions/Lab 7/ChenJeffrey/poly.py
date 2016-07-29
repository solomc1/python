class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for k in terms:
            if type(k[0]) not in (int,float):
                raise AssertionError('Coefficent is not int or float')
            elif k[0] == 0:
                pass
            elif type(k[1]) is not int:
                raise AssertionError('Power must be an int')
            elif k[1]<0:
                raise AssertionError('Power must be greater or equal to 0')
            elif k[1] in self.terms :
                raise AssertionError('Power already exists in dict')
            else:
                self.terms[k[1]]=k[0]
            
            
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
        l=[]
        for k,v in self.terms.items():
            l.append((v,k))
        return 'Poly('+','.join(str(k) for k in l)+')'

    
    def __len__(self):
        leng=0
        if self.terms == {}:
            return leng
        else:
            for k in self.terms.keys():
                if k>leng:
                    leng=k
                else:
                    pass
            return leng
                
    
    def __call__(self,arg):
        if type(arg) in [int,float]:
            value = 0
            for k,v in self.terms.items():
                value+=(arg**k)*v
            return value
        else:
            raise AssertionError("arg is not int or float")
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(),reverse=True):
            yield (v,k)
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Index must be int')
        elif index<0:
            raise TypeError('Index must be greater or equal to 0')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Power must be int')
        elif index<0:
            raise TypeError('Power must be greater or equal to 0')
        elif value==0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Index must be int')
        elif index<0:
            raise TypeError('Index must be greater or equal to 0')
        elif index not in self.terms:
            pass
        else:
            del self.terms[index]
        
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Coefficient is not int or float')
        elif type(p) is not int:
            raise TypeError('Power is not int')
        elif p<0:
            raise TypeError('Power must be greater or equal to 0')
        elif p not in self.terms and c!=0:
            self.terms.__setitem__(p,c)
        elif p not in self.terms and c==0:
            pass
        else:
            self.terms[p]=self.terms[p]+c
            if self.terms[p]==0:
                del self.terms[p]
            
        
       

    def __add__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('Operand is not of type int, float or Poly')
        elif type(right) in [int,float]:
            k=Poly()
            r=Poly((right,0))
            for x in r:
                k._add_term(x[0],x[1])
            for x in self:
                k._add_term(x[0],x[1])
            return k
        else:
            k=Poly()
            
            for x in right:
                k._add_term(x[0],x[1])
            for x in self:
                k._add_term(x[0],x[1])
            return k
        

    
    def __radd__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError('Operand is not of type int, float or Poly')
        elif type(left) in [int,float]:
            k=Poly()
            r=Poly((left,0))
            for x in r:
                k._add_term(x[0],x[1])
            for x in self:
                k._add_term(x[0],x[1])
            return k
        else:
            k=Poly()
            
            for x in left:
                k._add_term(x[0],x[1])
            for x in self:
                k._add_term(x[0],x[1])
            return k
    

    def __mul__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('Operand is not of type int, float or Poly')
        elif type(right) in [int,float]:
            k=Poly()
            for key,v in self.terms.items():
                k[key]=v*right
            return k
        else:
            r=Poly()
            for k,v in self.terms.items():
                for k1,v1 in right.terms.items():
                    tp=k1+k
                    tc=v1*v
                    r._add_term(tc,tp)
            return r
            
    

    def __rmul__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError('Operand is not of type int, float or Poly')
        elif type(left) in [int,float]:
            k=Poly()
            for key,v in self.terms.items():
                k[key]=v*left
            return k
        else:
            r=Poly()
            for k,v in self.terms.items():
                for k1,v1 in left.terms.items():
                    tp=k1+k
                    tc=v1*v
                    r._add_term(tc,tp)
            return r
            
    

    def __eq__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('Operand is not of type int, float or Poly')
        elif type(right) in [int,float]:
            if len(self)==0:
                return self.terms[0]==right
            else:
                return False
        else:
            l=[]
            a=[]
            for k,v in sorted(self.terms.items(),reverse=True):
                l.append((k,v))
            for k,v in sorted(right.terms.items(),reverse=True):
                a.append((k,v))
            return a==l
                
            

    
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