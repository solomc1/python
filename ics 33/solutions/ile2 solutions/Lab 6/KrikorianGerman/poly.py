class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        #term = (coefficient, power)
        #self.terms: power = key, coeff = value
        self.input = terms
        self.terms = {}
        for term in terms:
            if type(term[0]) is not float and type(term[0]) is not int:
                raise AssertionError('coefficient must be int or float')
            if type(term[1]) is not int or term[1] < 0:
                raise AssertionError('power must be int and >= 0')
            if term[0] != 0:
                if term[1] in self.terms:
                    raise AssertionError('same power for multiple coefficients is not allowed')
                else:
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
        return 'Poly'+str(self.input)

    
    def __len__(self):
        largest = 0
        if self.terms == {}:
            return 0
        else:
            for power in self.terms.keys():
                if power > largest:
                    largest = power
            return largest
    
    def __call__(self,arg):
        result = 0
        for item in self.terms.items():
            result += item[1] * (arg**item[0])
        return result
    

    def __iter__(self):
        tuplelist = []
        for key in sorted(self.terms.keys(), reverse = True):
            tuplelist.append((self.terms[key], key))
        for item in tuplelist:
            yield(item)
                

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('argument must be an int >= 0')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('argument must be an int >= 0')
        if value == 0:
            for key in self.terms.keys():
                if self.terms[key] == value:
                    del self.terms[key]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('argument must be an int >= 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('coefficient must be int or float')
        if type(p) != int or p < 0:
            raise TypeError('power must be an int >= 0')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if c == 0:
                del self.terms[p]
            else:
                self.terms[p] = c
       

    def __add__(self,right):
        if type(right) == int or type(right) == float:
            pass
        elif type(right) == Poly:
            for power in self.terms.keys():
                if power in right.terms.keys():
                    self._add_term(self[power]+right[power],power)
                else:
                    self._add_term(self[power],power)
            for power2 in right.terms.keys():
                if power2 not in right.terms.keys():
                    self._add_term(self[power2],power)
            return self.terms
        else:
            raise TypeError('argument must be an int, float, or polynomial')

    
    def __radd__(self,left):
        if type(left) == int or type(left) == float:
            pass
        elif type(left) == Poly:
            for power in self.terms.keys():
                if power in left.terms.keys():
                    self._add_term(self[power]+left[power],power)
                else:
                    self._add_term(self[power],power)
            for power2 in left.terms.keys():
                if power2 not in left.terms.keys():
                    self._add_term(self[power2],power)
            return self.terms
        else:
            raise TypeError('argument must be an int, float, or polynomial')
    

    def __mul__(self,right):
        if type(right) == int or type(right) == float:
            tuplelist = []
            for key in self.terms.keys():
                tuplelist.append((right * self.terms[key], key))
        elif type(right) == Poly:
            pass
        else:
            raise TypeError('argument must be an int, float, or polynomial')
    

    def __rmul__(self,left):
        if type(left) == int or type(left) == float:
            tuplelist = []
            for key in self.terms.keys():
                tuplelist.append((left * self.terms[key], key))
        elif type(left) == Poly:
            pass
        else:
            raise TypeError('argument must be an int, float, or polynomial')
    

    def __eq__(self,right):
        if type(right) == Poly:
            return sorted(self.terms) == sorted(right.terms)
        elif type(right) == int or type(right) == float:
            return (len(self.terms) == 1 and right in self.terms.values())
        else:
            raise TypeError('argument must be an int, float, or polynomial')

    
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