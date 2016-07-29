class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for key, value in terms:
            self.terms[value] = key
        for power in self.terms.keys():
            assert type(power) == int and power >= 0, "Poly.__init__: illegal coefficient in" + str(coefficient, power)
        for coefficient in self.terms.values():    
            assert type(coefficient) == (int or float), "Poly.__init__: illegal coefficient in" + str(coefficient)
        print (self.terms)
                  
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
        str = 'Poly('
        for key, value in self.terms.items():
            str += '({},{})'.format(value, key)
        str += ')'
        return str

    def __len__(self):
        big_value = []
        for value in sorted(self.terms.values()):
            big_value.append(value)
        return big_value[-1]
    
    def __call__(self,arg):
        final_result = []
        assert type(arg) == (int or float), "Poly.__call__: arg must be int or float"
        for key, value in self.terms.items():
            final_result.append((value * (arg ** key)))
        return final_result[-1]
    
    def __iter__(self):
        for key, value in self.terms.items():
            yield ((value, key))

    def __getitem__(self,index):
        assert type(index) is int and int > 0, 'TypeError, __getitem__ index is not an int, or > than 0'
        with index as value:
            for key, value in self.terms.items():
                if value:
                    yield key
            
    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        self.right = {}
        self.final = {}
        for key, value in right:
            self.right[value] = key
        for key, value in self.terms.items():
            for keys, values, in self.right.items():
                if value == values:
                    self.final[value] = (key + keys)
        return(self.final)

    
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