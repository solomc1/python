class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            assert type(x[0]) is float or type(x[0]) is int, ("Poly.__init__: illegal coefficient in" + str(x) + ".")
            assert type(x[1]) is int and x[1] >= 0, ("Poly.__init__: illegal power in: " + str(x) + ".") 
            assert x[1] not in self.terms, "Poly.__init__: power {} is repeated.".format(x[1])
            if x[0] != 0:
                self.terms[x[1]] = x[0]
            
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
        return "Poly(" + ",".join([str((x[1], x[0])) for x in self.terms.items()]) + ")"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max([x for x in self.terms])
            
    
    def __call__(self,arg):
        assert type(arg) is int or type(arg) is float, ("Poly.__init__: illegal arg:", arg)
        result = 0
        for k in self.terms:
            result += arg ** k * self.terms[k]
        return result
    

    def __iter__(self):
        for k in sorted(self.terms, reverse=True):
            yield (self.terms[k], k)
            

    def __getitem__(self,index):
        self._checkIndexLegality(index, "__getitem__")
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        self._checkIndexLegality(index, "__setitem__")
        if value == 0 and index in self.terms:
            del self.terms[index]
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        self._checkIndexLegality(index, "__delitem__")
        if index in self.terms:
            del self.terms[index]
    
    def _checkIndexLegality(self, index, functionName):
        if index < 0 or type(index) is not int:
            raise TypeError("Poly." + functionName+": illegal index " + str(index))
                

    def _add_term(self,c,p):
        if type(c) is not int and type(c) is not float:
            raise TypeError("Poly._add_term: illegal coefficient", c)
        if type(p) is not int or p < 0:
            raise TypeError("Poly._add_term: illegal power", p)
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
        if p in self.terms and self.terms[p] == 0:
            del self.terms[p]
       

    def __add__(self,right):
        self._checkArithmeticCompatibility(right, "__add__")
        return self._add_into_self(right)

    
    def __radd__(self,left):
        self._checkArithmeticCompatibility(left, "__radd__")
        return self._add_into_self(left)
    

    def __mul__(self,right):
        self._checkArithmeticCompatibility(right, "__mul__")
        return self._mul_into_self(right)

    def __rmul__(self,left):
        self._checkArithmeticCompatibility(left, "__rmul__")
        return self._mul_into_self(left)
    
    def _mul_into_self(self, term):
        result =  Poly()
        if type(term) is Poly:
            for x in self.terms.items():
                for y in term.terms.items():
                    result._add_term(x[1] * y[1], x[0] + y[0])
        else:
            for x in self.terms.items():
                result._add_term(term * x[1], x[0])
        return result
                    
    
    def _add_into_self(self, term):
        result = Poly(*[(x[1], x[0]) for x in self.terms.items()])
        if type(term) is Poly:
            for x in term:
                result._add_term(x[0], x[1])
        else:
            result._add_term(term, 0)
        return result
    
    def _checkArithmeticCompatibility(self, operand, functionName):
        if type(operand) is not int and type(operand) is not float and type(operand) is not Poly:
            raise TypeError("Poly." + functionName + ": illegl operand: " + str(operand))

    def __eq__(self,right):
        self._checkArithmeticCompatibility(right, "__eq__")
        if type(right) is Poly:
            for x in right:
                if x[1] not in self.terms or self.terms[x[1]] != x[0]:
                    return False
            return True
        return self.terms[0] == right

    
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