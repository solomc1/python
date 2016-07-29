class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms: 
            if not (i[0]==0):
                if (type(i[0]) is int or type(i[0]) is float) and (type(i[1]) is int):
                    if (i[1]>=0):
                        mykeys=self.terms.keys()
                        if not i[1] in mykeys:
                            self.terms[i[1]]=i[0]
                        else:
                            raise AssertionError("power was specified earlier ")
                    else:
                        raise AssertionError("power cannot be negative")
                else:
                    raise AssertionError("Poly.__init__:illegal power in :", i)
       
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
        mystr="Poly("
        for i in self.terms:
            mystr+="("+str(self.terms[i])+","+str(i)+")"+','
        
        if mystr[-1] is ",":
            mystr=mystr[:-1]
        mystr+=")"
        return mystr
    
    def __len__(self):
        x=self.terms.keys()
        if (len(x)==0):
            return 0
        else:
            x=sorted(x,reverse = True)
            return x[0]
        
    
    def __call__(self,arg):
        sum=0
        if type(arg) is int or type(arg) is float:
            for i in self.terms:
                sum+=(self.terms[i]*(arg**i))
        return sum
    def __iter__(self):
        x=list(self.terms.keys())
        x=sorted(x,reverse =True)
        for i in x:
            yield((self.terms[i],i))
            

    def __getitem__(self,index):
        if (type(index)is int):
            if index>=0:
                if index in self.terms.keys():
                    return( self.terms[index])
                else:
                    return 0
            else:
                raise TypeError("power cannot be less than 0")
        else:
            raise TypeError("power cannot be non int") 

    def __setitem__(self,index,value):
        if (type(index) is int):
            if index > 0:
                    if value ==0:
                        if index in self.terms.keys():
                            self.terms.pop(index,self.terms[index])
                    else:
                        self.terms[index]= value
            
            else:
                raise TypeError("power cannot be less than 0")
        else:
            raise TypeError("is not valid index")
            

    def __delitem__(self,index):
        if type(index) is int:
            if index >=0:
                if index in self.terms.keys():
                    self.terms.pop(index)
            else:
                raise TypeError("index cannot be less than 0")
        else:
            raise TypeError("Inappropriate value/type")
            

    def _add_term(self,c,p):
        if (type(c) is int or type(c) is float):
            if (type(p) is int):
                if p>=0:
                    if (not (p in self.terms.keys())) and c is not 0:
                        self.terms[p]=c
                    elif (p in self.terms.keys()):
                        self.terms[p]+=c
                        if self.terms[p]==0:
                            self.terms.pop(p,0)
                else:
                    raise TypeError("Power cannot be less than 0")
            else:
                raise TypeError("Invalid Type")
        else:
            raise TypeError("Invalid Type")
    def __add__(self,right):
        z=Poly()
        if (type(z)==type(right)):
            for i in right.terms.keys():
                z._add_term(right.terms[i], i)            
            for key in self.terms.keys():
                z._add_term(self.terms[key], key)

            
        elif(type(right) is int or type(right) is float):
            for key in self.terms.keys():
                z._add_term(self.terms[key],key)
            z._add_term(right,0)
        else:
            raise TypeError("invalid operand type")
        return z

    def __radd__(self,left):
        z=Poly()
        if (type(z)==type(left)):
            for i in left.terms.keys():
                z._add_term(left.terms[i], i)            
            for key in self.terms.keys():
                z._add_term(self.terms[key], key)
        elif(type(left) is int or type(left) is float):
            for key in self.terms.keys():
                z._add_term(self.terms[key],key)
            z._add_term(left,0)
        else:
            raise TypeError("invalid operand type")
        return z
    

    def __mul__(self,right):
        Polym=Poly()
        if type(Polym) is type(right):
            for rightkey in right.terms.keys():
                for selfkey in self.terms.keys():
                    Polym._add_term(self.terms[selfkey]*right.terms[rightkey], selfkey+rightkey)
                    
        elif(type(right) is int) or type(right) is float:
            for i in self.terms.keys():
                Polym._add_term(self.terms[i]*right, i)
        else:
            raise TypeError("invalid type")
        return Polym

    def __rmul__(self,left):
        Polym=Poly()
        if type(Polym) is type(left):
            for leftkey in left.terms.keys():
                for selfkey in self.terms.keys():
                    Polym._add_term(self.terms[selfkey]*left.terms[leftkey], selfkey+leftkey)
                    
        elif(type(left) is int) or type(left) is float:
            for i in self.terms.keys():
                Polym._add_term(self.terms[i]*left, i)
        else:
            raise TypeError("invalid type")
        return Polym
    

    def __eq__(self,right):
        z=Poly()
        if (type(z) is type(right)):
            for i in right.terms.keys():
                if i in self.terms.keys():
                    if not(right.terms[i]==self.terms[i]):
                        return False
                else:
                    return False

            return True    
            
        elif (type(right) is int or type(right) is float):
            x=self.terms.keys()
            if len(x)==1 and (right== self.terms[0]):
                return True
            else:
                return False
        else:
            raise TypeError("invalid type")
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
    print('  p(2):',p(2))
    print('  list collecting iterator results:',[t for t in p])
    print(p)
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    p1 = Poly((1,1),(2,0))
    p2 = Poly((3,2),(2,1),(1,0))
    print(' p1+p2',p1+p2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()