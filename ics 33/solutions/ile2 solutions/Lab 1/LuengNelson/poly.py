class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coef, power in terms:
            assert type(coef) in (int, float), "Poly.__init__: illegal coefficient in: "+str(terms)
            assert type(power)==int and power>=0, "Poly.__init__: illegal power in: "+str(terms)
            assert power not in self.terms.keys() or coef==0, "Poly.__init__: duplicate power in: "+str(terms)
            if coef!=0:
                self.terms.update({power:coef})
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
        return "Poly("+",".join(str((coef, power)) for power, coef in self.terms.items())+")"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for power, coef in self.terms.items():
            result += coef*arg**power
        return result
    

    def __iter__(self):
        for power in sorted(self.terms.keys(), reverse=True):
            yield (self.terms[power],power)
            

    def __getitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                return self.terms[index]
            return 0
        raise TypeError("Invalid index for Poly object.")
            

    def __setitem__(self,index,value):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                self.terms[index] = value
            else:
                self.terms.update({index:value})
            if value==0:
                del self.terms[index]
            return
        raise TypeError("Invalid index for Poly object.")
            

    def __delitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                del self.terms[index]
            return
        raise TypeError("Invalid index for Poly object.")
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Poly._add_term: illegal coefficient in "+str(c))
        if type(p) != int or p<0:
            raise TypeError("Poly._add_term: illegal power in "+str(p))
        if p not in self.terms.keys():
            if c!=0:
                self.terms.update({p:c})
        else:
            self.terms[p] += c
            if self.terms[p]==0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) in (Poly, int, float):
            temp = Poly()
            for power, coef in self.terms.items():
                temp._add_term(coef, power)
            if type(right)==Poly:
                for power, coef in right.terms.items():
                    temp._add_term(coef, power)
            else:
                temp._add_term(right, 0)
            return temp
        raise TypeError("Invalid operand (+) for types: "+str(type(self))+" "+str(type(right)))

    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        if type(right) in (Poly, int, float):
            temp = Poly()
            if type(right)==Poly:
                for p1, c1 in self.terms.items():
                    for power, coef in right.terms.items():
                        temp._add_term(coef*c1, power+p1)
                return temp
            return self*Poly((right,0))
        raise TypeError("Invalid operand (*) for types: "+str(type(self))+" "+str(type(right)))
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) in (Poly, int, float):
            if type(right)==Poly:
                for power, coef in right.terms.items():
                    if power not in self.terms.keys() or coef!=self.terms[power]:
                        return False
                return True
            else:
                return self==Poly((right,0))
        raise TypeError("Uncomparable types: "+str(type(self))+" "+str(type(right)))

    
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