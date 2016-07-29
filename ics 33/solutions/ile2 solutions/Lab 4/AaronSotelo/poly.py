class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for power in terms:
            assert isinstance(power[0],int) or isinstance(power[0],float),"Poly.__init__: illegal type in {}".format(power)
            assert isinstance(power[-1],int),  "Poly.__init__: illegal type in {}".format(power)
           # assert isinstance(power[0],float) and isinstance(power[-1],float), "Poly.__init__: illegaltype in {}".format(power)
            assert power[-1] >= 0, "Poly.__init__: illegal power in {}".format(power)
            if power[-1] not in self.terms:
                if power[0] == 0:
                    continue
                self.terms[power[-1]] = power[0]
            else:
                raise AssertionError("Poly.__init__: illegal repetition of a power in {}") 
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

        result = 'Poly('
        for key in self.terms:
            result += "(" + str(self.terms[key]) + ',' + str(key)+"),"
        return result.rstrip(",") + ")"
            
        if self.terms is {}:
            return "Poly()"
    
    def __len__(self):
        if self.terms is {}:
            return 0
        result = 0
        for power in self.terms:
            if power > result:
                result = power
        return result
    
    def __call__(self,arg):
        result = 0
        for element in self.terms:
            result+= self.terms[element]*arg**element
        return result

    def __iter__(self):
        pass

    def __getitem__(self,index):
        if type(index) is int:
            if index >= 0:
                try:
                    return self.terms[index]
                except:
                    return 0
            else:
                raise TypeError("__getitem__ error, the index is less than 0")
        else:
            raise TypeError("__getitem__ error, the index is not of type int")
        
    def __setitem__(self,index,value):
        if type(index) is int:
            if index >= 0:
                if value != 0:
                    self.terms[index] = value
                else:
                    del self.terms[index]
            else:
                raise TypeError("__setitem__ error, the index is less than 0")
        else:
            TypeError("__setitem__ error, the index is not of type int")
    def __delitem__(self,index):
        if type(index) is int:
            if index  >= 0:
                if index in self.terms:
                    del self.terms[index]
            else:
                raise TypeError("__delitem__ error, the index is less than 0")
        else:
            raise TypeError("__delitem__ error, the index is not of type int")

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p) is int:
            if p >= 0:
                if p not in self.terms:
                    if c != 0:
                        self.terms[p] = c
                else:
                    self.terms[p] = self.terms[p] + c  
                    if self.terms[p] == 0:
                        del self.terms[p]
            else:
                raise TypeError("_add_term error, the power is less than 0")
        else:
            raise TypeError("_add_term error, the coefficient or power are illegal types\n {}   {}".format(type(c), type(p)))        


    def __add__(self,right):
        result = Poly()
        if type(right) in (Poly,int,float):
            if right is Poly:
                for element in self.terms:
                    result._add_term(self.terms[element],element)
                for element in right.terms:
                    result._add_term(right.terms[element],element)    
            else:
                result._add_term(right,0)
            return result    
        else:
            raise TypeError("__add__ the argument is not a legal type")

    
    def __radd__(self,left):
        result = Poly()
        if type(left) in (Poly,int,float):
            if left is Poly:
                for element in self.terms:
                    result._add_term(self.terms[element],element)
                for element in left.terms:
                    result._add_term(left.terms[element],element)    
            else:
                result._add_term(left,0)
            return result    
        else:
            raise TypeError("__add__ the argument is not a legal type")
    

    def __mul__(self,right):
        result = Poly()
        if type(right) in (Poly,int,float):
            if right is Poly:
                pass
        else:
            raise TypeError("__mul__ the argument is not a legal type")
            
    

    def __rmul__(self,left):
        result = Poly()
        if type(left) in (Poly,int,float):
            if left is Poly:
                pass
        else:
            raise TypeError("__mul__ the argument is not a legal type")
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
   # print(eval(repr(p)).terms)
    #print(p.terms)
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
    #print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()