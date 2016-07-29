class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for pair in terms:
            assert( (type(pair[0])  in [int,float])),"Poly.__init__: coefficients must be of type int or float"
            assert(type(pair[1])==int),              "Poly.__init__: powers must be of type int"
            assert(pair[1]>=0),                      "Poly.__init__: powers must be >=0"
            assert(pair[1] not in self.terms),       "Poly.__init__: terms of the same order must be one entry"
            if pair[0]!=0:
                self.terms[pair[1]]=pair[0]
                
        
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
        return"Poly({})".format(",".join(["({coef},{pow})".format(coef = value, pow = key) for key, value in self.terms.items()]))

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
        else:
            maximum = -1    #power of -1 is smaller that the smallest legal power,
                            #something is very wrong if len returns -1 
            for key in self.terms:
                maximum = max(maximum, key)
            return maximum
    
    def __call__(self,arg):
        total = 0
        for pow, coef in self.terms.items():
            total+=coef*(arg**pow)
        return total
    

    def __iter__(self):
        for key in sorted(self.terms.keys(),reverse = True):
            yield((self.terms[key],key))
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("index must be of type int")
        if index<0:
            raise TypeError("index must be>=0")
        if index not in self.terms.keys():
            return int(0)
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        #print("index: ", type(index) ,index, "value: ",type(value), value)
        if type(index) not in  [int]:
            raise TypeError("power/index must be an integer")
        if type(value) not in [int, float]:
            raise TypeError("coefficient/value must be in int or float value")
        if index<0:
            raise TypeError("power/index must be>=0")
        if value==0:
            if  index in self.terms.keys():
                del self.terms[index]
            else:
                pass
        else:
            self.terms[index]= value

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError("index must be an int value")
        if index<0:
            raise TypeError("index must be>=0")
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p)!=int or p<0:
            raise TypeError("power must be >=0")
        if type(c) not in  [int,float]:
            raise TypeError("coefficient must be int or float")
        if c!=0:
            if p in self.terms:
                self.terms[p]+=c
            else:
                self.terms[p] = c
            if self.terms[p] == 0:
                self.__delitem__(p)  
       

    def __add__(self,right):
        if type(right)not in [int,float, type(self)]:
            raise TypeError("operand must be of type int, float or {}".format(type(self)))
        
        retPoly = Poly()
        for p,c in self.terms.items():
            retPoly._add_term(c, p)
 
        if type(right) in [int,float]:
            
            retPoly._add_term(right,0)
            return retPoly
        else:
            for p, c in right.terms.items():
                retPoly._add_term(c,p)
            return retPoly
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right)not in[int,float,type(self)]:
            raise TypeError("operand must be int,float or"+type(self))
        retPoly = Poly()
        if type(right) in [int,float]:
            for p, c in self.terms.items():
                retPoly._add_term(c*right, p)
        else:
            for s_p,s_c in self.terms.items():
                for r_p, r_c in right.terms.items():
                    retPoly._add_term(r_c*s_c, r_p+s_p)
        return retPoly

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right)not in[int,float,type(self)]:
            raise TypeError("operand must be int,float or"+type(self))
        return None
        for p,c in sorted(self.terms.items()):
            for rp,rc in sorted(right.terms.items()):
                pass

    
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