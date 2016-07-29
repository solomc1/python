class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for item in terms:
            assert(item[1] >= 0), "Poly.__init__: illegal power in: (" + str(item[0]) + "," + str(item[1]) + ")"
            if item[0] != 0:
                #if item[1] not in self.terms.keys():
                self.terms[item[1]] = item[0]
            else:
                raise AssertionError ("Poly.__init__: illegal coefficient in: (" + str(item[0]) + "," + str(item[1]) + ")")
        print(self.terms)
        
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
        return str(self)
    
    def __len__(self):
        if len(self.terms) > 0:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for item in self.terms:
            result += (self.terms[item]*(arg**item))
        return result
    
    def __iter__(self):
        pass      

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError ("Poly.__getitem__: illegal type: " + str(type(index)) + ")")
        elif index < 0:
            raise TypeError ("Poly.__getitem__: illegal value: " + str(index) + ")")
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError ("Poly.__setitem__: illegal type: " + str(type(index)) + ")")
        elif index < 0:
            raise TypeError ("Poly.__setitem__: illegal value: " + str(index) + ")")
        elif value == 0:
            self.terms.pop(value)
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError ("Poly.__delitem__: illegal type: " + str(type(index)) + ")")
        elif index < 0:
            raise TypeError ("Poly.__delitem__: illegal value: " + str(index) + ")")
        else:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int or type(c) != float:
            raise TypeError ("Poly._add_term: illegal type: " + str(type(c)) + ")")
        elif p < 0:
            raise TypeError ("Poly._add_term: illegal value: " + str(p) + ")")
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] = int(self.terms[p]) + int(c)
            if self.terms[p] == 0:
                self.terms.pop(p)
                
    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

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
    #print('  list collecting iterator results:',[t for t in p])
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