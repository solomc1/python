class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for a,b in terms:
            assert type(a) in (int,float), 'Poly.__init__: illegal type for coefficient: must be int or float'
            assert type(b) is int, 'Poly.__init__: illegal type for power: must be an int'
            assert b >= 0, 'Poly.__init__: power must be 0 or greater'
            assert b not in self.terms.keys(), 'Poly.__init__: a power with a nonzero int cannot be repeated'     
            if a != 0:
                self.terms[b] = a
        
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
        repr_str = 'Poly('
        for k,v in self.terms.items():
            repr_str += '('+ str(v) + ',' + str(k) + '),'
        repr_str = repr_str[:-1]
        repr_str += ')'
        return repr_str

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return max(self.terms.keys())
            
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += v * (arg**k)
        return result
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), reverse = True):
            yield (v,k)
            

    def __getitem__(self,index):
        if index is not int:
            raise TypeError('Poly.__getitem__: argument must be of type int')
        if index < 0:
            raise TypeError('Poly.__getitem__: argument must be an int with a value equal to or greater than 0')
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if index is not int:
            raise TypeError('Poly.__setitem__: argument must be of type int')
        if index < 0:
            raise TypeError('Poly.__setitem__: argument must be an int with a value equal to or greater than 0')
        if value == 0:
            for k,v in self.terms.items():
                if v == value:
                    del self.terms[k]
        self.terms[index] = value
            

    def __delitem__(self,index):
        if index is not int:
            raise TypeError('Poly.__setitem__: argument must be of type int')
        if index < 0:
            raise TypeError('Poly.__setitem__: argument must be an int with a value equal to or greater than 0')
        del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Poly._add_term: the argument "c" must be an int or float')
        if type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: the argument "b" must be an int with a non-negative value')
        if c != 0 and p not in self.terms.keys():
            self.terms[p] = c
        if p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__add__: operand must be of a Polynomial, int, or float type')
        
        temp = self.terms.copy()
        
        if type(right) is Poly:
            for p,c in right.terms.items():
                self._add_term(c,p)
        elif type(right) in (int,float):
            self._add_term(right, 0)
            
        tuples = []
        for k,v in self.terms.items():
            tuples.append((v,k))
            
        self.terms = temp #changes back the mutated dictionary
        
        temp_poly = 'Poly(' + str(tuples) + ')'
        temp_poly = temp_poly.replace(']','')
        temp_poly = temp_poly.replace('[','')
        return eval(temp_poly)

    
    def __radd__(self,left):
        if type(left) not in (int,float):
            raise TypeError('Poly.__radd__: operand must be of type int or float')
        temp = self.terms.copy()
        self._add_term(temp, left, 0)
        
        tuples = []
        for k,v in self.terms.items():
            tuples.append((v,k))
            
        self.terms = temp #changes back the mutated dictionary
        
        temp_poly = 'Poly(' + str(tuples) + ')'
        temp_poly = temp_poly.replace(']','')
        temp_poly = temp_poly.replace('[','')
        return eval(temp_poly)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__mul__: operand must be of a Polynomial, int, or float type')

    def __rmul__(self,left):
        if type(left) not in (int,float):
            raise TypeError('Poly.__rmul__: operand must be of type int or float')
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__eq__: operand must be of a Polynomial, int, or float type')
        if type(right) is Poly:
            return self.terms == right.terms
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