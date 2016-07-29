class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            self.terms[t[1]] = t[0]

        for c,p in self.terms.items():
            if type(p) not in (int,float):
                raise AssertionError ('Poly.__init__: Error Coefficient not an int or float')
            if type(c) is not int:
                raise AssertionError('Poly.__init__: Error power is not an int')
            if c < 0:
                raise AssertionError('Poly.__init__: Error power is not greater than 0')
           
                
            
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
        return 'Poly{}'.format(tuple(zip(self.terms.keys(),self.terms.values())))

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) not in(int,'float'):
            raise TypeError ('Poly.py, Poly: Error. Arguement is not in int or float')
        else:
            a=0
        for k,v in self.terms.items():
                a+= v*(arg**k)

        for k in self.terms.keys():
            for v in self.terms.values():

                return a
            
  
    

    def __iter__(self):
#         def __generator__(*terms):
#             for t in (terms):
#                 yield t
#         return _generator(self.terms.items())
# #             
        pass
    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('index is not an int')
        if index <0:
            raise TypeError('index should be >0 ')
        if index not in self.terms.keys():
            return 0 
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('index should be an int')
        if index<0:
            raise TypeError('index should be greater than 0')
#         if value == 0:
#             del self.terms[index]
#             self.terms[index]
#             
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('index should be an int')
        if index<0:
            raise TypeError('index should be greater than 0')
        pass
            

    def _add_term(self,c,p):
        if type(c)not in (int,'float'):
            raise TypeError
        if type(p) is not int:
            raise TypeError
        pass
       

    def __add__(self,right):
        if type(right) not in (int, 'float', Poly):
            raise TypeError
        

    
    def __radd__(self,left):
        if type(left) not in (int, 'float'):
            raise TypeError
        pass
    

    def __mul__(self,right):
        if type(right) not in (int, 'float',Poly):
            raise TypeError
        pass
    

    def __rmul__(self,left):
        if type(left) not in (int, 'float'):
            raise TypeError
        pass
    
    

    def __eq__(self,right):
        if type(right) not in (int, 'float'):
            raise TypeError
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
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()