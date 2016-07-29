class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for v, k in terms:
            assert type(v) in (int,float)
            assert type(k) is int
            assert k >= 0
            assert k not in self.terms
            if v != 0:
                self.terms[k] = v
            
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
        return "Poly(" + ",".join((str((v, k)) for k, v in self.terms.items())) + ")"

    
    def __len__(self):
        return (max(self.terms) if len(self.terms) > 0 else 0)
    
    def __call__(self,arg):
        return sum(v*arg**k for k, v in self.terms.items())
    

    def __iter__(self):
        return ((v, k) for k, v in sorted(self.terms.items(), reverse = True))
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError("Indexes can only be integers")
        if index < 0:
            raise TypeError("Indexes must be greater than 0")
        return (self.terms[index] if index in self.terms else 0)
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError("Indexes can only be integers")
        if index < 0:
            raise TypeError("Indexes must be greater than 0")
        self.terms[index] = value
        if value == 0:
            self.terms.pop(index)
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError("Indexes can only be integers")
        if index < 0:
            raise TypeError("Indexes must be greater than 0")
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Coeffiecients can only be integers or flaots")
        if type(p) != int:
            raise TypeError("Powers can only be integers")
        if p < 0:
            raise TypeError("Powers must be greater than 0")
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.terms.pop(p)
            

    def __add__(self,right):
        if right is not Poly:
            return ("Poly(" + ", ".join(str((v, k)) for k, v in self.terms.items() if k != 0) + "," + str((self.terms[0]+right, right)) + ")")
        else:
            p = "Poly("
            for k, v in self.terms.items():
                for n,k2, v2 in enumerate(right.terms.items()):
                    p += str(v + v2, k + k2)
                    if n != len(right.terms.items()):
                        p += ","
            
            return eval(p)
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int, Poly):
            raise TypeError("Must be an integer or Poly")
        if type(right) is Poly:
            for i, v in self.terms.items():
                for i2, v2 in right.terms.items():
                    return  (i, v) == (i2, v2)
        else:
            if len(self.terms.items()) > 1:
                return False
            else:
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