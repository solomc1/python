class Poly:
    
    def __init__(self,*terms):
#         print(terms)
        self.x = terms
        self.terms = {}
        for values in terms:
            assert type(values[0]) in (int, float), 'Poly__init__:Illegal coefficient in: '+ str(values)
            assert type(values[1]) == int and values[1] >=0 , 'Poly__init__:Illegal power in: '+ str(values)
            if values[0] != 0:
                if values[1] in self.terms:
                    raise AssertionError
                else:
                    self.terms[values[1]] = values[0]
#         print(self.terms)
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
#         self.terms = {}
        
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
        return 'Poly('+ ','.join((str(c) for c in self.x))+')'

    
    def __len__(self):
        return  max(list(self.terms.keys()))
    
    def __call__(self,arg):
#         pass
#         string = str(self)
#         c = string.format('x', str(arg))
        pass
            
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('__getitem__, invalid index specified')
        if index in list(self.terms.keys()):
            return self.terms[index]
        else:
            return 0

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError('__setitem__, invalid index specified')
        if value == 0:
            if value in self.terms.values():
                for values in self.terms.keys():
                    if self.terms[values] == value:
                        del self.terms[values]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (self, int, float):
            raise TypeError('__eq__ incorrect object specified')
        if type(right) == self:
            for values in list(self.terms.items()):
                for values2 in list(right.terms.items()):
                    if values == values2:
                        return True
                    else:
                        return False
                    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
#     print(p)
#     print(p.__repr__())
#     print(len(p))
#     print(p[1])
#     p(2)
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