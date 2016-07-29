class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x,y in terms:
            if not (type(x) == int or type(x) == float):
                assert False, "illegal coefficient in : " + str((x,y))
            if not(type(y) == int and y >= 0):
                assert False, "illegal power in : " + str((x,y))
            if y in self.terms.keys():
                assert False, "power already used"
            if not x == 0:
                self.terms[y] = x
            
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
        tupLis = []
        for x,y in self.terms.items():
            tupLis.append((y,x))
        return "Poly{}".format(tuple(tupLis))
    
    def __len__(self):
        x = self.terms.keys()
        if len(x) == 0:
            return 0
        return max(x)
           
    def __call__(self,arg):
        sum = 0
        # k is power, v is coefficient
        for k,v in self.terms.items():
            sum +=v * (arg**k)
        return sum 

    def __iter__(self):
        def gen(self):
            for pow in list(self.terms)[::-1]:
                yield (self.terms[pow],pow)
        return gen(self)            

    def __getitem__(self,index):
        if type(index) == int and index >=0:
            if index in self.terms.keys():
                return self.terms[index]
            return 0
        raise TypeError("Index was not an int equal to or greater than 0")  
            
    def __setitem__(self,index,value):
        if type(index) == int and index>=0:
            if value == 0:
                if index in self.terms.keys():
                    del(self.terms[index])
                return
            self.terms[index] = value
            return
        raise TypeError("Index must be an int greater than or equal to 0")
            
    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                del(self.terms[index])
            return
        raise TypeError("Index must be an int greater than or equal to 0")
            

    def _add_term(self,c,p):
        if type(c) == int or type(c) == float:
            if type(p) == int and p >= 0:
                if p in self.terms.keys():
                    self.terms[p] += c
                    if self.terms[p] == 0:
                        del self.terms[p]
                    return
                else:
                    if not c == 0:
                        self.terms[p] = c
                    return
            raise TypeError("power must be an int greater than or equal to 0")
        raise TypeError("coefficient entered was not an int or float")
       

    def __add__(self,right):
        typR = type(right)
        if typR == int or typR == float:
            copi = eval(repr(self))
            copi._add_term(right,0)
            return copi
        if typR == Poly:
            copi = eval(repr(self))
            for k,v in right.terms.items():
                copi._add_term(v,k)
            return copi
        raise TypeError("Can not add Poly object and " + str(typR))
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        typR = type(right)
        if typR == int or typR == float:
            copi = eval(repr(self))
            for k,v in copi.terms.items():
                copi[k] *= right
            return copi
        if typR == Poly:
            pol = Poly()
            for k,v in self.terms.items():
                for k2,v2 in right.terms.items():
                    # v is a co, k is a power
                    pol._add_term(v*v2,k2 + k)
            return pol
        raise TypeError("Can not add Poly object and " + str(typR))
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == int or type(right) == float:
            return str(self) == str(eval("Poly({})".format((right,0))))
        if type(right) == Poly:
            return str(right) == str(self)
        raise TypeError("uncomparable types: Poly and " + type(right))
   
# just in case, Neeraj Shah - Lab 3 - 46134667
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