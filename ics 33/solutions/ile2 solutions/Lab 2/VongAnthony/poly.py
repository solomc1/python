class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c, p in terms:
            if type(c) not in (int, float): raise AssertionError()
            if type(p) != int or p < 0: raise AssertionError()
            if p in self.terms: raise AssertionError()
            if c != 0: 
                self.terms[p] = c
            
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
        for p, c in self.terms.items():
            repr_str += '({},{}),'.format(c, p)
        repr_str = repr_str.strip(',') + ')'
        return repr_str
        
    def __len__(self):
        return 0 if self.terms == {} else max(self.terms.keys())
    
    def __call__(self,arg):
        value = []
        for p, c in self.terms.items():
            value.append(c * (arg ** p))
        return sum(value)
    

    def __iter__(self):
        def power(x):
            return x[0]
        for c, p in sorted(self.terms.items(), key = power, reverse = True):
            yield (p, c)
            

    def __getitem__(self,index):
        if not isinstance(index, int): raise TypeError(str(type(index)) + ' is not an integer')
        if index < 0: raise TypeError(str(index) + ' may not a negative integer')
        if index in self.terms:
            return self.terms.get(index)
        else: return 0
            

    def __setitem__(self,index,value):
        if not isinstance(index, int): raise TypeError(str(type(index)) + ' is not an integer')
        if not isinstance(value, int): raise TypeError(str(type(value)) + ' is not an integer')
        if index < 0: raise TypeError(str(index) + ' must be a positive integer')
        if value == 0:
            if 0 in self.terms:
                del self.terms[0]
        else:
            pass
            
        
    def __delitem__(self,index):
        if not isinstance(index, int): raise TypeError(str(type(index)) + ' is not an integer')
        if index < 0: raise TypeError(str(index) + ' must be a positive integer')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float): raise TypeError()
        if type(p) != int or p < 0: raise TypeError()
        if p not in self.terms and c != 0:
            self.terms[p] = c
        if p in self.terms:
            self.terms[p] = self.terms.get(p)
            
       

    def __add__(self,right):
        add_str = 'Poly('
        if isinstance(right, Poly):
            for c, p in right.terms.items():
                if c not in self.terms:
                    self.terms[c] = p
                else:
                    self.terms[c] = self.terms.get(c) + p
            for c, p in self.terms.items():
                add_str += '({}, {}),'.format(p, c)
            add_str = add_str.strip(',') + ')'
            return eval(add_str)
            
        if type(right) in (int, float):
            for c, p in self.terms.items():
                self.terms[c] = self.terms.get(c) + right
            for c, p in self.terms.items():
                add_str += '({}, {}),'.format(p, c)
            add_str = add_str.strip(',') + ')'
            return eval(add_str)
        else: raise AssertionError()

    
    def __radd__(self,left):
        add_str = 'Poly('
        if isinstance(left, Poly):
            for c, p in self.terms.items():
                if c not in self.terms:
                    left.terms[c] = p
                else:
                    left.terms[c] = self.terms.get(c) + p
            for c, p in left.terms.items():
                add_str += '({}, {}),'.format(p, c)
            add_str = add_str.strip(',') + ')'
            return eval(add_str)
            
        if type(left) in (int, float):
            for c, p in self.terms.items():
                self.terms[c] = self.terms.get(c) + left
            for c, p in self.terms.items():
                add_str += '({}, {}),'.format(p, c)
            add_str = add_str.strip(',') + ')'
            return eval(add_str)
        else: raise AssertionError()
    

    def __mul__(self,right):
        if isinstance(right, Poly):
            pass
        if type(right) in (int, float):
            pass
        #else: raise AssertionError()
    

    def __rmul__(self,left):
        if isinstance(left, Poly):
            pass
        if type(left) in (int, float):
            pass
        #else: raise AssertionError()
    
    

    def __eq__(self,right):
        if isinstance(right, Poly):
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