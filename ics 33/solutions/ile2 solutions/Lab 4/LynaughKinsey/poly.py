class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) == int or type(term[0]) == float
            assert type(term[1]) == int
            assert term[1] >= 0
            #assert term[0] != 0
            assert term[1] not in self.terms.keys()
            if term[0] != 0:
                self.terms[term[1]] = term[0]
        
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
        tms = ""
        for key in self.terms.keys():
            tms += "(" + str(self.terms[key]) + "," + str(key) + "),"
        return "Poly(" + tms[:-1] + ")"

    
    def __len__(self):
        if [key for key in self.terms.keys()] != []:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        total = 0
        for power in self.terms.keys():
            total += self.terms[power] * (arg**power)
        return total
    

    def __iter__(self):
        powers= sorted([key for key in self.terms.keys()], reverse = True)
       # print(powers)
        for power in powers:
           # print((self.terms[power],power))
            yield (self.terms[power],power)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Invalid index type, must  be int.")
        if index < 0:
            raise TypeError("Invalid index, must be > 0.")
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Invalid index type, must  be int.")
        if index < 0:
            raise TypeError("Invalid index, must be > 0.")
        if value == 0:
            del self.terms[index]
        else:   
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Invalid index type, must  be int.")
        if index < 0:
            raise TypeError("Invalid index, must be > 0.")
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not(type(c) == int or type(c) == float):
            raise TypeError("Invalid type for c, must be int or float.")
        if type(p) != int:
            raise TypeError("Invalid power type, must  be int.")
        if p < 0:
            raise TypeError("Invalid power, must be > 0.")
        if p not in self.terms.keys() and c != 0:
            self[p] = c
        elif p in self.terms.keys():
            if c + self[p] == 0:
                del self.terms[p]
            else:
                self[p] = c + self[p]
   
    def __add__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError("Unsupported type for +: must be int, float, or Poly")
        if type(right) in [int,float]:
            self._add_term(right,0)
        else:
            for power in right.terms.keys():
                self._add_term(right[power],power)
                #print(self)
        return self

    
    def __radd__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError("Unsupported type for +: must be int, float, or Poly")
        if type(left) in [int,float]:
            self._add_term(left,0)
        else:
            for power in left.terms.keys():
                self._add_term(left[power],power)
                #print(self)
        return self
    

    def __mul__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError("Unsupported type for +: must be int, float, or Poly")
        if type(right) in [int,float]:
            for power in self.terms.keys():
                self[power] = self[power]*right
            return self
        else:
            result = Poly()
            for power1 in self.terms.keys():
                for power2 in right.terms.keys():
                    result._add_term(self[power1]*right[power2],power1+power2)
            return result
                    
                 

    def __rmul__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError("Unsupported type for +: must be int, float, or Poly")
        if type(left) in [int,float]:
            for power in self.terms.keys():
                self[power] = self[power]*left
            return self
        else:
            result = Poly()
            for power1 in self.terms.keys():
                for power2 in left.terms.keys():
                    result._add_term(self[power1]*left[power2],power1+power2)
            return result
    

    def __eq__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError("Unsupported type for ==: must be int, float, or Poly")
        if type(right) in [int,float]:
            return len([key for key in self.terms.keys()]) == 1 and 0 in self.terms.keys() and self[0] == right
        else:
            equality = True
            for power in self.terms.keys():
                try:
                    equality = right[power] == self[power]
                except:
                    return False
                if not equality:
                    return equality
            return equality
            
            
            
            

    
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