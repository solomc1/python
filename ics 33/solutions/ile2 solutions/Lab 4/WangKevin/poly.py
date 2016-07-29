class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            if t[0] == 0:
                continue
            if type(t[0]) not in [int,float]:
                raise AssertionError("the coefficient, "+str(t[0])+", is not an int or float")
            if type(t[1]) == int:
                if t[1]>=0:
                    if t[1] not in self.terms.keys():
                        self.terms[t[1]] = t[0]
                    else:
                        raise AssertionError("the power, "+str(t[1])+", is already in the polynomial.")
                else:
                    raise AssertionError("the power, "+str(t[1])+", is not an interger above 0")
            else:
                raise AssertionError("the power, "+str(t[1])+", is not an interger")
            
        
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
        result = "Poly("
        count = 0
        for k in self.terms:
            if count== len(self.terms)-1:
                result+="("+str(self.terms[k])+","+str(k)+")"
            else:
                result+="("+str(self.terms[k])+","+str(k)+"),"
            count+=1
        return result+")"

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
        else:
            highest = 0
            for k in self.terms:
                if k>highest:
                    highest = k
            return highest
    
    def __call__(self,arg):
        result = 0
        for k in self.terms:
            result= result + ((arg**k)*self.terms[k])
        return result
    
    def __iter__(self):
        for p,c in sorted(self.terms.items(), key = lambda item: item[0], reverse = True):
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) is int:
            if index>=0:
                if index not in self.terms.keys():
                    return 0
                else:
                    return self.terms[index]
            else:
                raise TypeError("index, "+str(index)+", is not equal to or greater than 0")
        else:
            raise TypeError("index type: "+str(type(index))+" is not an int")
            

    def __setitem__(self,index,value):
        if type(index) is int:
            if index>=0:
                if value !=0:
                    self.terms[index]=value
                else:
                    if index in self.terms.keys():
                        del self.terms[index]
            else:
                raise TypeError("the power, "+str(index)+", is not greater than or equal to 0")
        else:
            raise TypeError("the power, "+str(index)+", is not an interger")
            

    def __delitem__(self,index):
        if type(index) is int:
            if index>=0:
                if index in self.terms.keys():
                    del self.terms[index]
            else:
                raise TypeError("the power, "+str(index)+", is not greater than or equal to 0")
        else:
            raise TypeError("the power, "+str(index)+", is not an interger")
                
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise AssertionError("the coefficient, "+str(c)+", is not an int or float")
        if type(p) == int:
            if p>=0:
                if p not in self.terms.keys() and c !=0:
                    self.terms[p] = c
                elif p in self.terms.keys():
                    if c+self.terms[p] != 0:
                        self.terms[p] = c + self.terms[p]
                    else:
                        del self.terms[p]
            else:
                raise AssertionError("the power, "+str(t[1])+", is not an interger above 0")
        else:
            raise AssertionError("the power, "+str(t[1])+", is not an interger")
       

    def __add__(self,right):
        if type(right) is Poly:
            result = Poly()
            for p1 in self.terms.keys():
                result._add_term(self.terms[p1],p1)
            for p2 in right.terms.keys():
                result._add_term(right.terms[p2],p2)
            return result
        elif type(right) in [int,float]:
            result = Poly()
            for p in self.terms.keys():
                result._add_term(self.terms[p],p)
            result._add_term(right,0)
            return result
        else:
            raise AssertionError("unaddable types: Poly() + "+str(type(right))+"()")
            

    
    def __radd__(self,left):
        if type(left) in [int,float]:
            result = Poly()
            for p in self.terms.keys():
                result._add_term(self.terms[p],p)
            result._add_term(left,0)
            return result
        else:
            raise AssertionError("unaddable types: "+str(type(left))+"() + Poly()")
    

    def __mul__(self,right):
        if type(right) is Poly:
            result = Poly()
            for p1 in self.terms.keys():
                for p2 in right.terms.keys():
                    result._add_term(self.terms[p1]*right.terms[p1],p1+p2)
            return result
                    
        elif type(right) in [int,float]:
            pass

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) is Poly:
            for p1,p2 in zip(self.terms.keys(),right.terms.keys()):
                if self.terms[p1]!=right.terms[p2]:
                    return False
                else:
                    return True
        elif type(right) in [int,float]:
            if self.terms[0] !=  right:
                return False
            else:
                return True
        else:
            raise TypeError("cannot compare types: Poly() == "+str(type(right))+"()")
            

    
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