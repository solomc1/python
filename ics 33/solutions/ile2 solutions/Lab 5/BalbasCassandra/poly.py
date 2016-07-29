class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        # ------------------------------------------------------------------------
        # Fill in the rest of this method, using *terms to intialize self.terms
 
        # tup[1] = power
        # tup[0] = coefficient
        # format of tuple: (power, coefficient)
 
        self.terms = dict()
        for tup in terms:
            self.terms[tup[1]] = tup[0]
            
        for key, value in self.terms.items():
            if type(value) not in (int, float):
                raise AssertionError('poly.py, Poly, Error. Coefficient type must be int or float')
            elif type(key) != int and key < 0:
                raise AssertionError('poly.py, Poly, Error. Coefficient type must be int and greater than 0')
        
        values = []
        for value in self.terms.values():
            if value not in values:
                values.append(value)
            else:
                raise AssertionError('poly.py, Poly, Error. Power already stated in expression')
                
        
            
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
        temp = []
        for item in self.terms.items():
            temp.append(item)
        return 'Poly{}'.format(tuple(temp))
        
    
    def __len__(self):
        if Poly == None:
            return 0
        else:
            return max(self.terms.keys()) 
    
    def __call__(self,arg):
        # __call__ makes our class methods act like functions
        
        if type(arg) not in (int, float):
            raise TypeError('poly.py, Poly, Error. Argument is not an int or float')
        else:
            # x will be replaced with *arg
            # return self.terms.power
            pass  
        
    
    def __iter__(self):
        def _gen(iterable):
            for o in (iterable):
                yield o
                
        return _gen(self.terms.items())

    def __getitem__(self,index):
        # index is any power
        if type(index) != int or index < 0:
            raise TypeError('poly.py, Poly, Error. Index is either not an int or is less than 0')
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        # index = power
        # value = coefficient
        
        if index != int or index < 0:
            raise TypeError('poly.py, Poly, Error. Index is either not an int or is less than 0')
        else:
            if value == 0:
                del value
            
    def __delitem__(self,index):
        if index != int or index < 0:
            raise TypeError('poly.py, Poly, Error. Index is either not an int or is less than 0')
        else:
            if index in self.terms.keys():
                del index

    def _add_term(self,c,p):
        if type(c) not in (int,float) or type(p) != int:
            raise TypeError
        if p < 0:
            raise TypeError()
        else:
            if p not in self.terms.keys() and c != 0:
                return '{}x{}'.format(c,p)
            elif p in self.terms.keys():
                return '{}x'.format(c)
            elif c == None:
                pass
       
    def __add__(self,right):
        if type(right) not in (int, float):
            raise TypeError('poly.py, Poly, Error. Other operand is not an int or float.')
        else:
            pass
    
    def __radd__(self,left):
        if type(left) not in (int, float):
            raise TypeError('poly.py, Poly, Error. Other operand is not an int or float.')
        else:
            pass
    

    def __mul__(self,right):
        if type(right) not in (int, float):
            raise TypeError('poly.py, Poly, Error. Other operand is not an int or float.')
        else:
            pass
    

    def __rmul__(self,left):
        if type(left) not in (int, float):
            raise TypeError('poly.py, Poly, Error. Other operand is not an int or float.')
        else:
            pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('poly.py, Poly, Error. Other operand is not an int, float, or Poly.')

    
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
    # print('  list collecting iterator results:',[t for t in p])
    # print('  p+p:',p+p)
    # print('  p+2:',p+2)
    # print('  p*p:',p*p)
    # print('  p*2:',p*2)
    # print('End simple tests\n')
    
    import driver
    # driver.default_show_exception=True
    # driver.default_show_exception_message=True
    # driver.default_show_traceback=True
    driver.driver()