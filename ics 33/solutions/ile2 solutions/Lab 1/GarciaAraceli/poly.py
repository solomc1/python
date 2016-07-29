class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for tup in terms:
            if type(tup[0]) not in [int, float]:
                raise AssertionError("Poly.__init__: must be int or float.")
            if type(tup[1]) != int:
                raise AssertionError("Poly.__init__: must be int")
            if tup[1] == 0:
                pass
            if tup[1] < 0:
                raise AssertionError("Poly.__init__: power must be positive.")
            if tup[0] in self.terms.values():
                raise AssertionError("Poly.__init__: power already exists.")
            self.terms[tup[1]] = tup[0]
                                        
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
        return "Poly({})".format(','.join(str((value, key)) for key, value in self.terms.items()))
   
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.values())
    
    def __call__(self,arg):
        p = self.__str__()
        p = p.replace('x', str(arg))
        p = p.replace('^', '**')
        return eval(p)
    

    def __iter__(self):
        L = []
        for key, val in self.terms.items():
            L.append((val,key))
        L.sort(key=(lambda tup : tup[1]),reverse=True)
        for i in L:
            yield i
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__getitem__: argument must be an integer.")
        if index == 0:
            raise TypeError("Poly.__getitem__: argument cannot be zero.")   
        if index not in self.terms.keys():
            raise TypeError("Poly.__getitem__: power does not exist.")  
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Poly.__setitem__: power must be an int.")
        if index < 0:
            raise TypeError("Poly.__setitem__: power cannot be zero.")
        for key, val in self.terms.items():
            if val == 0:
                del self.terms[key]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__setitem__: argument must be an int.")
        if index < 0:
            raise TypeError("Poly.__setitem__: argument must be greater than zero.")
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError("Poly._add_term: args must be int or float.")
        if type(p) != int:
            raise TypeError("Poly._add_term:power must be an int.")
        if p < 0:
            raise TypeError("Poly._add_term: power must be greater than zero.")
        if p in self.terms.keys():
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
        elif p not in self.terms.keys() and p != 0:
            self.terms[p] = c
            

    def __add__(self,right):
        if type(right) == int:
            pass
        if type(right) == float:
            pass
        if type(right) == Poly:
            p = Poly()
            for key, val in self.terms.items():
                p.terms[key] = val
            for k, v in right.terms.items():
                p._add_term(v,k)
            return p
                
            

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == int:
            return self.terms[0] == right
        if type(right) == float:
            return self.terms[0] == right
        if type(right) == Poly:
            return self.terms == right.terms
        else:
            raise TypeError("Poly.__eq__: operan must be int, float, or Poly.")

    
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