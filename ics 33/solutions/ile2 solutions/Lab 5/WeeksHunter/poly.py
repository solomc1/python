class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert type(t)==tuple,"Poly.__init__:argument not tuple: {}".format(t)
            assert  ((type(t[0])==float) or (type(t[0])==int)), "Poly.__init__: illegal coefficient in {}".format(t)
            assert type(t[1])==int,"Poly.__init__:illegal power in: {}".format(t)
            assert t[1]>=0,"Poly.__init__: negative power inL {}".format(t)
            assert t[1] not in self.terms.keys(), "Poly__init__:power already in polynomial: {}".format(t)
            if t[0] != 0:
                self.terms[t[1]]=t[0]
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
        result=set()
        for p,c in self.terms.items():
            result.add("({},{})".format(c,p))
        return "Poly({})".format(','.join(result))

    
    def __len__(self):
        if len(self.terms.keys()) ==0:
            return 0
        result=(sorted(self.terms.keys(),reverse=True))[0]
        return result
            
    
    def __call__(self,arg):
        assert (type(arg)==float) or (type(arg)==int),"Poly.__call__: illegal arg:{}, must be int or float".format(arg)
        result=0
        for p,c in self.terms.items():
            result+=arg**p*c
        return result
    

    def __iter__(self):
        for p,c in sorted(self.terms.items(),reverse=True):
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__getitem__:illegal index:{}".format(index)) 
        if index < 0:
            raise TypeError("Poly.__getitem__:index less than 0:{}".format(index))
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Poly.__setitem__:illegal index:{}".format(index)) 
        if type(value) != int:
            raise TypeError("Poly.__setitem__:illegal value:{}".format(index)) 
        if index < 0:
            raise TypeError("Poly.__setitem__:index less than 0:{}".format(index))  
        if value==0:
            if index in self.terms.keys():
                self.terms.pop(index)
            else:
                return None
        else:
            self.terms[index]=value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__delitem__:illegal index:{}".format(index)) 
        if index < 0:
            raise TypeError("Poly.__delitem__:index less than 0:{}".format(index))
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError("Poly._add_term:illegal power:{}".format(p)) 
        if p < 0:
            raise TypeError("Poly._add_term:power less than 0:{}".format(p))
        if (type(c)!=int) and (type(c)!=float):
            raise TypeError("Poly._add_term:illegal coefficient:{}".format(c))
        if (p not in self.terms.keys()) and c != 0:
            self.terms[p]=c
        elif p in self.terms.keys():
            if self.terms[p]+c == 0:
                self.__delitem__(p)
            else:
                self.terms[p]+=c
        
       

    def __add__(self,right):
        if (type(right)==int) or (type(right)==float):
            return self+Poly((right,0))
        elif type(right)==Poly:
            result=Poly()
            for p in range(0,max(len(self),len(right))+1):
                if self[p] + right[p]!=0:
                    result._add_term(self[p] + right[p], p)
            return result
        else:
            raise TypeError("Poly.__add__: cannot add {}:{} to Poly".format(type(right),right))

    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        if (type(right)==int) or (type(right)==float):
            return self*Poly((right,0))
        elif type(right)==Poly:
            result=Poly()
            for c1,p1 in self:
                for c2,p2 in right:
                    result+=Poly((c1*c2,p1+p2))
            return result
        else:
            raise TypeError("Poly.__mul__: cannot multiply {}:{} to Poly".format(type(right),right))
    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if (type(right)==int) or (type(right)==float):
            return self==Poly((right,0))
        elif type(right)==Poly:
            result=True
            for p in range(0,max(len(self),len(right))+1):
                if self[p]!=right[p]:
                    result=False

            return result
        else:
            raise TypeError("Poly.__eq__: inorderable types: {}, Poly".format(type(right)))
    
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