class Poly:
    
    def __init__(self, *terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        if len(terms) != 0:
            for t in terms:
                if type(t[1]) != type(int()) or t[1] < 0:
                    raise AssertionError("Poly.__init__: illegal power in: " + str(t))
                if type(t[0]) != type(int()) and type(t[0]) != type(float()):
                    raise AssertionError("Poly.__init__: illegal coefficient in: " + str(t))
                
                if t[1] in self.terms:
                    raise AssertionError("Poly.__init__: a power cannot appear twice in a set of terms")
                elif t[0] != 0:
                    self.terms.setdefault(t[1], t[0])
            
            
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
        return_str = "Poly("
        
        for k, v in self.terms.items():
            return_str += "(" + str(v) + "," + str(k) + "),"
        
        return return_str.rstrip(',') + ")"

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        
        return max(self.terms.keys())

    
    def __call__(self, arg):
        total = 0
        
        for k, v in self.terms.items():
            total += v * arg ** k
        
        return total
    

    def __iter__(self):
        for k, v in sorted(self.terms.items(), reverse = True):
            yield (v, k)
            

    def __getitem__(self, index):
        if type(index) != type(int()):
            raise TypeError("Poly.__getitem__: illegal index type: " + str(type(index)))
        elif index < 0:
            raise TypeError("Poly.__getitem__: illegal index: " + str(index))
        
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self, index, value):
        if type(index) != type(int()) or index < 0:
            raise TypeError("Poly.__setitem__: illegal power: " + str(index))
        
        if index in self.terms:
            if value == 0:
                del self.terms[index]
            else:
                self.terms[index] = value
        elif value != 0:
            self.terms.setdefault(index, value)
            

    def __delitem__(self, index):
        if type(index) != type(int()) or index < 0:
            raise TypeError("Poly.__delitem__: illegal power: " + str(index))
        
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self, c, p):
        if type(p) != type(int()) or p < 0:
            raise TypeError("Poly._add_term: illegal power: " + str(p))
        if type(c) != type(int()) and type(c) != type(float()):
            raise TypeError("Poly._add_term: illegal coefficient: " + str(c))
        
        if p in self.terms:
            if c + self.terms[p] != 0:
                self.terms[p] += c
            else:
                del self.terms[p]
        elif c != 0:
            self.terms.setdefault(p, c)
            

    def __add__(self, right):
        eval_str = ""
        if type(right) == type(int()) or type(right) == type(int()):
            return self + Poly((right, 0))
        elif type(right) == type(self):
            for k, v in self.terms.items():
                if k in right.terms:
                    if v + right[k] != 0:
                        eval_str += "(" + str(v + right.terms[k]) + "," + str(k) + "),"
                else:
                    eval_str += "(" + str(v) + "," + str(k) + "),"
            
            for k, v in right.terms.items():
                if k not in self.terms:
                    eval_str += "(" + str(v) + "," + str(k) + "),"
        else:
            raise TypeError("Poly.__add__: illegal type for + " + str(type(right)))
        
        return eval("Poly(" + eval_str.rstrip(",") + ")")

    
    def __radd__(self, left):
        if type(left) == type(int()) or type(left) == type(int()):
            return Poly((left, 0)) + self 
        else:
            raise TypeError("Poly.__radd__: illegal type for + " + str(type(left)))
    

    def __mul__(self,right):
        eval_str = ""
        if type(right) == type(int()) or type(right) == type(int()):
            return self * Poly((right, 0))
        elif type(right) == type(self):
            for k1, v1 in self.terms.items():
                for k2, v2 in right.terms.items():
                    #eval_str += "(" + str(v1 * v2) + "," + str(k1 + k2) + "),"
                    pass            
        else:
            raise TypeError("Poly.__mul__: illegal type for + " + str(type(right)))
        return eval("Poly(" + eval_str.rstrip(",") + ")")

    

    def __rmul__(self,left):
        if type(left) == type(int()) or type(left) == type(int()):
            return Poly((left, 0)) * self 
        else:
            raise TypeError("Poly.__rmul__: illegal type for + " + str(type(left)))
    

    def __eq__(self,right):
        if type(right) == type(int()) or type(right) == type(int()):
            return self * Poly((right, 0))
        elif type(right) == type(self):
            for k1, v1 in sorted(self.terms.items()):
                for k2, v2 in sorted(right.terms.items()):
                        if k1 != k2 or v1 != v2:
                            return False
        else:
            raise TypeError("Poly.__eq__: illegal type for == " + str(type(right)))
        return True

    
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