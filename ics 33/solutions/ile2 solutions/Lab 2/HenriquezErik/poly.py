class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for t in terms:
            assert type(t[0]) in (int,float), "Poly.__init__: Coefficient must be an int or float"
            assert type(t[1]) is int and t[1] >= 0, "Poly.__init__: Power must be an in greater or equal to 0"
            if t[0] == 0 : #If the coefficient is zero
                continue    #Ignore it
            assert t[1] not in self.terms.keys(), "Poly.__init__: Power already has coefficient set"
            self.terms[t[1]] = t[0]
                
            
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
        #pairs = self.terms.items()
        terms = []#could use a set
        for k,v in self.terms.items():
            #print (p)
            terms.append(str((v,k)))
        parameters = ",".join(terms)
        return "Poly({})".format(parameters)
    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        s = 0
        for power,coef in self.terms.items():
            s += coef * (arg**power)
        return s

    def __iter__(self):
        powers = set(self.terms.keys())
        while len(powers) != 0:
            highest =  max(powers)
            powers.remove(highest)
            yield (self.terms[highest],highest)
        
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: parameter must be an integer greater or equal to 0")
        elif index not in self.terms.keys():
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__setitem__: parameter must be an integer greater or equal to 0")
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
        
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__: parameter must be an integer greater or equal to 0")
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("Poly._add_term: Coefficient parameter must be an integer or float")
        elif type(p) != int or p < 0:
            raise TypeError("Poly._add_term: Power parameter must be an integer greater than or equal to 0")
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p]=c
        elif (c + self.terms[p]) == 0:
            del self.terms[p]
        else:
            self.terms[p] += c
        
    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("Poly.__add__: " + str(right) +" is an invalid operand! Must be a Poly, integer, or float")
        new_Poly = Poly()
        if type(right) is Poly:
            for coef,power in right: #Poly objects are iterable
                #new_coef = coef + right[power]
                new_Poly._add_term(coef+right[power], power)
        else:
            new_Poly._add_term(right,0)
        
        return new_Poly
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("Poly.__mul__: " + str(right) +" is an invalid operand! Must be a Poly, integer, or float")
        new_Poly = Poly()
        
        return new_Poly

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
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