class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}

        for c, p in terms:
            #print(c,'terms') ##############################################
            if type(c) not in (int,float,tuple):
                raise AssertionError('coef msut be int or float')
            if type(p) is not int or p<0:
                if type(p) is tuple:
                    self.terms[p[0]]=p[1]
                else:
                    raise AssertionError('power must be an int whose value is >= 0')
            if c == 0:
                continue
            else:
                if p in self.terms.values():
                    raise AssertionError('power is already in terms')
                if type(c) is tuple:
                    self.terms[c[0]]=c[1]
                else:
                    self.terms[c]=p
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
        #print(self.terms)
        return 'Poly('+','.join('('+str(c)+','+str(p)+')' for c,p in self.terms.items())+')'

    
    def __len__(self):
        return max(self.terms.values())
    
    def __call__(self,arg):
        result=0
        for c,p in self.terms.items():
            result+=(arg**p)*c
        return result
    

    def __iter__(self):
       lsttuples=[]
       for c,v in self.terms.items():
           lsttuples.append((c,v))
       b=sorted(lsttuples,key= lambda x: x[1],reverse=True)
       for i in b:
           yield i
            

    def __getitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError('index is not an integer or it is negative')
        newdict={}
        for c,p in self.terms.items():
            newdict[p]=c
        if index in newdict.keys():
            return newdict[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(value) is not int or value < 0:
            raise TypeError('power is not integer or it is under 0')
        self.terms[index]=value
        if index==0:
            del self.terms[index]
    

    def __delitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError('power is not integer or it is under 0')
        for c,v in self.terms.items():
            if self.terms[c] == index:
                del self.terms[c]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('coefficient is not numeric')
        if type(p) is not int  or p <0:
            raise TypeError('power is not that integer or less than 0')
        if p not in self.terms.values() and p != 0:
            self.terms[c]=p
        else:
            newdict={}
            for c,p in self.terms.items(): #makign reverse keys,values
                newdict[p]=c
            if p in newdict.keys(): #if p is in dictionary, then add coefficient
                newdict[p]+=c
            for p,c in newdict.items():
                self.terms[c]=p
            for c,p in self.terms.items():
                if c==0:
                    del self.terms[c]
       

    def __add__(self,right):
        if type(right) not in (int,float, Poly):
            raise TypeError('add not int or float or Poly')
        if type(right) in (int, float):
            newitems={}
            newitems1={}
            for c,p in self.terms.items():
                newitems[c+right]=p
            for c,p in newitems.items():
                if c != 0:
                    newitems1[c]= p
            
            #print(list((c,p) for c,p in newitems1.items()),'f')
            #print(Poly((c,p) for c,p in newitems1.items()))
            for c,p in newitems1.items():
                print(c,p)
            return Poly((p,c) for c,p in newitems1.items())
        else:
            newitems={}
            for c1,p1 in self.terms.items():
                for c2,p2 in right.terms.items():
                    if p1==p2:
                        newitems[c1+c2]=p1
            newitems2={}
            for c,p in newitems.items():
                if c!=0:
                    newitems2[c]=p
                else: pass
            #for c,p in newitems2.items(): print(c,p)
            #print((c,v) for c,v in list(newitems2.items()))
            return Poly((c,p) for (c,p) in newitems2.items())
        

    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        if type(right) not in (int,float, Poly):
            raise TypeError('add not int or float or Poly')
        if type(right) in (int,float):
            newitems={}
            for c,v in self.terms.items():
                newitems[c*right]=v
            return Poly((c,p) for c,p in newitems.items())
        else:
            newitems={}
            for c,p in self.terms.items():
                for v,o in right.terms.items():
                    newitems[c*v]=p+o
            return Poly((c,p) for c,p in newitems.items())
    

    def __rmul__(self,left):
        return self * left    

    def __eq__(self,right):
        if type(right) not in (int,float, Poly):
            raise TypeError('wrong type of right')
        if type(right) is Poly:
            for i,v in self.terms.items():
                try:
                    if self.terms[i]!=right.terms[i]:
                        return False
                    
                except:
                    return False
            for i,v in self.rights.items():
                try:
                    if self.terms[i]!=right.terms[i]:
                        return False
                    
                except:
                    return False
            return True 
        else:
            if len(self.terms) != 1:
                return False
            if right in self.terms.values():
                return True
            else: return False
                
            
            

    
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