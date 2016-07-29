class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for v,k in terms:
            assert(type(v) in [int, float]), "Poly.__init__: illegal value in: ({},{})".format(v, k)
            assert(type(k) == int and k >= 0), "Poly.__init__: illegal power in: ({},{})".format(v, k)
            if v != 0:
                if k not in self.terms:
                    self.terms[k] = v
                else:
                    raise AssertionError("Poly.__init__: power {} already in use".format(k))
        #print(self.terms)
            
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
        temp = []
        for key in self.terms:
            temp.append(str((self.terms[key], key)))
        parameters = ",".join(temp)
        return "Poly({})".format(parameters)

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    
    def __call__(self,arg):
        assert(type(arg) in [int, float])
        value = 0
        for key in self.terms:
            value += (self.terms[key] * (arg ** key))
        return value
    

    def __iter__(self):
        copy = sorted(self.terms, reverse = True)
        for term in copy:
            yield (self.terms[term], term) 
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__getitem__: Power {} not an int".format(index))
        elif index < 0:
            raise TypeError("Poly.__getitem__: Power {} must be greater than 0".format(index))
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Poly.__setitem__: Power {} not an int".format(index))
        elif index < 0:
            raise TypeError("Poly.__setitem__: Power {} must be greater than 0".format(index))
        elif value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__delitem__: Power {} not an int".format(index))
        elif index < 0:
            raise TypeError("Poly.__delitem__: Power {} must be greater than 0".format(index))
        elif index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError("Poly._add_term: Power {} not an int".format(p))
        elif p < 0:
            raise TypeError("Poly._add_term: Power {} must be greater than 0".format(p))
        elif type(c) not in [int, float]:
            raise TypeError("Poly._add_term: Coefficient {} must be an int or float".format(c))
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            previous_c = self.terms[p]
            new_c = previous_c + c
            if new_c == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = new_c

    def __add__(self,right):
        if type(self) != Poly:
            raise TypeError("Poly.__add__: Left {} operand must be a Polynomial".format(self))
        if type(right) not in [Poly, int, float]:
            raise TypeError("Poly.__add__: Right {} operand must be a Polynomial, int, or float".format(right))
        
        
        if type(right) == Poly:
            for power in right.terms:
                self._add_term(right.terms[power], power)
            
            parameters = []
            for key in self.terms:
                parameters.append("({},{})".format(self.terms[key], key))
            temp = ",".join(parameters)
            r_value = "Poly({})".format(temp)
            return eval(r_value)
        
        if type(right) in [int, float]:
            self._add_term(right, 0)
            
            parameters = []
            for key in self.terms:
                parameters.append("({},{})".format(self.terms[key], key))
            temp = ",".join(parameters)
            r_value = "Poly({})".format(temp)
            return eval(r_value)
            
            
            
            
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError("Poly.__add__: Right {} operand must be a Polynomial, int, or float".format(left))
        self._add_term(left, 0)
            
        parameters = []
        for key in self.terms:
            parameters.append("({},{})".format(self.terms[key], key))
        temp = ",".join(parameters)
        r_value = "Poly({})".format(temp)
        return eval(r_value)

    def __mul__(self,right):
        if type(self) != Poly:
            raise TypeError("Poly.__mul__: Left {} operand must be a Polynomial".format(self))
        if type(right) not in [Poly, int, float]:
            raise TypeError("Poly.__mul__: Right {} operand must be a Polynomial, int, or float".format(right))
        
        return

    def __rmul__(self,left):
        pass
    

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