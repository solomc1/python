class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for p in terms:
            if p[1] in self.terms.keys():
                raise AssertionError("Power is already defined earlier in" + str(p))
            
            if type(p[0]) not in {int,float}:
                raise AssertionError("Coefficient is not an int in " + str(p))
            elif type(p[1]) is not int:
                raise AssertionError("Power is not an int in " + str(p))
            elif p[1] < 0:
                raise AssertionError("Power " + str(p) + " cannot be negative")
            elif p[0] == 0:
                continue
            
            self.terms[p[1]] = p[0]
            
            
        
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
        if len(self.terms) == 0:
            return "Poly()"
        retr = "Poly("
        for k,v in self.terms.items():
            retr = retr + "(" + str(v) + "," + str(k) + "),"
        retr = retr[:-1] + ")"
        return retr
        pass

    
    def __len__(self):
        if len(self.terms.keys()) < 1:
            return 0
        return sorted(self.terms.keys(),reverse = True)[0]
        pass
    
    def __call__(self,arg):
        if type(arg) not in {int, float}:
            raise TypeError("Value " + str(arg) + "is not an int or float.")
        sum = 0
        for k,v in self.terms.items():
            sum += v*(arg**k)
        return sum
        pass
    

    def __iter__(self):
        x = iter(sorted(
            self.terms.items(),
            key = lambda v: v[0],
            reverse = True
        ))
        while True:
            try:
                hold = next(x)
                yield (hold[1],hold[0])
            except StopIteration:
                break
        pass
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError(str(index) + " is not an integer.")
        elif index < 0:
            raise TypeError(str(index) + " is less than 0.")
        elif index not in self.terms:
            return 0
        return self.terms[index]
        pass
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError(str(index) + " is not an integer.")
        elif index < 0:
            raise TypeError(str(index) + " is less than 0.")
        elif type(value) not in {int,float}:
            raise TypeError(str(value) + " is not an integer or float.")
        elif value == 0:
            if index in self.terms:
                self.terms.pop(index)
            else: pass
        else:
            self.terms[index] = value
        pass
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError(str(index) + " is not an integer.")
        elif index < 0:
            raise TypeError(str(index) + " is less than 0.")
        elif index in self.terms.keys():
            self.terms.pop(index)
        pass
            

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError("Power " + str(p) + " is not an integer.")
        elif p < 0:
            raise TypeError("Power " + str(p) + " is less than 0.")
        elif type(c) not in {int,float}:
            raise TypeError("Coefficient " + str(c) + " is not an integer or float.")
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.terms.pop(p)
        pass
       

    def __add__(self,right):
        x = Poly()
        x.terms = dict(self.terms)
        if type(right) == Poly:
            for k,v in right.terms.items():
                x._add_term(v,k)
        else:
            x._add_term(right,0)
        return x
        pass

    
    def __radd__(self,left):
        return self.__add__(left)
        pass
    

    def __mul__(self,right):
        x = Poly()
        x.terms = {}
        if type(right) in {int, float}:
            for k,v in self.terms.items():
                x[k] = v*right
        else:
            for k,v in self.terms.items():
                for k2,v2 in right.terms.items():
                    k3, v3 = k+k2, v*v2
                    x._add_term(v3, k3)
        return x
        pass
    

    def __rmul__(self,left):
        return self.__mul__(left)
        pass
    

    def __eq__(self,right):
        if type(right) not in {Poly, int, float}:
            raise TypeError(str(right) + " is not a Poly, int, or float.")
        elif type(right) is Poly:
            if self.terms.keys() != right.terms.keys():
                return False
            for k in self.terms.keys():
                if self.terms[k] != right.terms[k]:
                    return False
            return True
        return self[0] == right
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