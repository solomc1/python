class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms={}
        for coef, power in self.terms.items():
            coef= self.terms.keys()
            power = self.terms.values() 
            self.coef = coef
            self.power = power   
        if type(self.coef) != int or type(self.power) != float:
            raise AssertionError("Poly.__init__: Coefficient must be an int or float: " +str(self.coef))
        if type(self.power) != int and self.power<0:
            raise AssertionError("Poly.__init__: Power must be an int and value must be greater than 0"+ str(self.power))
        if self.power in self.terms.items():
            raise AssertionError("Poly.__init__: illegal power in:: "+ self.terms)
         
            
        
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
        return ('Poly'+self.key+self.value)

    
    def __len__(self):
        if len(self.power)== 0:
            return 0
        for i in len(self.power):
            return max(i)
    
    def __call__(self,arg):
        for a in arg:
            return Poly(self.coef,self.power)

    def __iter__(self):
        result = ()
        for i in self.power:
            yield result(i)
        return result
            
            

    def __getitem__(self,index):
        if (type(index) != int) or index <0:
            raise TypeError("Poly.__getitem__ must be a positive number"+ index)
        if index not in self.power():
            return 0
        return self.coef[index]
            

    def __setitem__(self,index,value):
        if self.power <0:
            raise(TypeError("Poly.__setitem__ must be positive: "+ self.power))
        if self.coef == 0:
            self.terms.pop(value)
        
            

    def __delitem__(self,index):
        if index!= int or index<0:
            raise TypeError("Poly.__delitem__ is not an integer or is negative")
        return self.terms.pop(self.power[index])
            

    def _add_term(self,c,p):
        if (type(self.coef) != int or type(self.coef != float)) and self.power>=0:
            raise TypeError('self._add_term must be int or float and greater than 0')
        
       

    def __add__(self,right):
        if type(self.terms)!= type(Poly):  
            raise TypeError("self.__add__ must be class:"+self.terms) 
        if type(self.terms)!= (int or float):
            raise TypeError("self.__add__ must be an int or float"+self.terms)
        return self.terms+right.terms

    
    def __radd__(self,left):
        if type(self.terms)!= type(Poly):  
            raise TypeError("self.__add__ must be class:"+self.terms) 
        if type(self.terms)!= (int or float):
            raise TypeError("self.__add__ must be an int or float"+self.terms)
        return left.terms+self.terms
    

    def __mul__(self,right):
        if type(self.terms)!= type(Poly):  
            raise TypeError("self.__add__ must be class:"+self.terms) 
        if type(self.terms)!= (int or float):
            raise TypeError("self.__add__ must be an int or float"+self.terms)
        return self.terms*right.terms
    

    def __rmul__(self,left):
        if type(self.terms)!= type(Poly):  
            raise TypeError("self.__add__ must be class:"+self.terms) 
        if type(self.terms)!= (int or float):
            raise TypeError("self.__add__ must be an int or float"+self.terms)
        return self.terms*left.terms
    

    def __eq__(self,right):
        if type(self.terms)!= type(Poly):  
            raise TypeError("self.__add__ must be class:"+self.terms) 
        if type(self.terms)!= (int or float):
            raise TypeError("self.__add__ must be an int or float"+self.terms)
        return self.terms == right.terms

    
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