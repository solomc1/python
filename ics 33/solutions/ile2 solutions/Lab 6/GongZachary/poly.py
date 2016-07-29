class Poly:
    #coefficient, power
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        prev = None
        for key, value in terms:
            if type(key) != (int or float):
                raise AssertionError('coefficient is not an int or float')
            if value < 0:
                raise AssertionError('value has to be greater than 0')
            if type(value) != int:
                raise AssertionError('power has to be an int')
            if prev != None and key != 0 and value > prev:
                raise AssertionError('Cannot write a polynomial this way')
            if key != 0:
                self.terms[value] = key
            prev = value
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
        contents = ''
        for key, value in self.terms.items():
            contents += '({},{}),'.format(value, key)
        return 'Poly({})'.format(contents[:-1])

    
    def __len__(self):
        value = None
        for key in self.terms.keys():
            if value == None:
                value = key
            if key > value:
                value = key
        return value
    
    def __call__(self,arg):
        result = 0
        for key, value in self.terms.items():
            result += (arg**key)*value
        return result
    

    def __iter__(self):
        pieces = []
        for key, value in self.terms.items():
            pieces.append((value, key))
        pieces.reverse()
        for item in pieces:
            yield item
            

    def __getitem__(self,index):
        if type(index) !=  int or index < 0:
            raise TypeError('power is not an int or is less than 0')
        for key, value in self.terms.items():
            if index == key:
                return value
            if key not in self.terms.keys():
                return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('power is not an int or is less than 0')
        if value != 0:
            self.terms[index] = value
        if value == 0 and index in self.terms.keys():
            del self.terms[index]


    def __delitem__(self,index):
        if type(index) != (int or float) or index < 0:
            raise TypeError('coefficient is not an int or float or is not greater than 0')
        if index in self.terms.keys():
            del self.terms[index]


    def _add_term(self,c,p):
        if type(c) != (int or float) or type(p) != int or p < 0:
            raise TypeError('coefficient is not an int or float or the power is not an int or is not greater than 0')
        if c not in self.terms.keys():
            self.terms[p] = c
        for key, value in self.terms.items():
            if p == value:
                self.terms[key + p] = value
        

    def __add__(self,right):
#         if type(right) != (int or float or Poly):
#             raise TypeError('adding item is not an int or float')
#         if type(right) == (int or float):
#             for key, value in self.terms.items():
#                 if value == 0:
#                     self.terms[key + right] = value
#         for key, value in self.terms.items():
#             if key in self.terms.keys():
#                 if value == right[1]:
#                     self.terms[right[0] + key] = value
#             self.terms[right[0]] = right[1]
        pass
        
            
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != (int or float or Poly):
            raise TypeError('Cannot do operation')
        return right == self.terms.items()

    
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