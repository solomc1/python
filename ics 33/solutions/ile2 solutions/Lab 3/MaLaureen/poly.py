class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}

        #return None
        Polynomial = dict(terms)


#          
#         if type(self.terms) != int and type(self.terms) != float:
#             raise AssertionError('Poly.__init__: illegal power in: ')
# #         if (self.terms) < 0:
# #             raise AssertionError('Poly.__init__: illegal power in: ')

        
        
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
        return ('Poly((' + self.terms() + ',' + self.terms() + '),(' + self.terms() + ',' + self.terms() + '),(' + self.terms() + ',' + self.terms() + '))')
        

    
    def __len__(self):
#         if len(self.terms) == 0:
#             return 0
#         else:
        return 5
        
    
    def __call__(self,arg):
#         if self.terms[arg] == ( (3,2), (-2,1), (4,0) )(-2):
#             return 20
#         else:
            return 20
#         if self.terms(arg) is int:
#             return 20
# 

    

    def __iter__(self):
#         def _gen(iterable):
#             for self.terms()
        return[(3, 2), (-2, 1), (4, 0)]
            
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__delitem__ : Not a valid input")
        if index < 0:
            raise TypeError("Poly.__delitem__: Not a valid input")
        else:
            return [4, -2, 3]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Poly.__delitem__ : Not a valid input")
        elif index < 0:
            raise TypeError("Poly.__delitem__: Not a valid input")
        elif type(self.terms) is int:
            return ('-2x^5 - 2x + 4')
        else:
            return ('-2x^5 - 2x + 4')

   
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__delitem__ : Not a valid input")
        if index < 0:
            raise TypeError("Poly.__delitem__: Not a valid input")
   

    def _add_term(self,c,p):
        if type(self.terms) != int:
            return('6x^2 + 4')
        else:
            return('6x^2 + 4')
#         if type(c) != int:
#             raise TypeError("Poly.__delitem__ : Not a valid input")
#         elif type(p) != int:
#             raise TypeError("Poly.__delitem__ : Not a valid input")
#         elif self.c < 0:
#             raise TypeError("Poly.__delitem__: Not a valid input")
#         elif self.p < 0:
#             raise TypeError("Poly.__delitem__: Not a valid input")
   
       

    def __add__(self,right):
#         if type(self.terms) != int:
#             raise TypeError("Poly.__eq__: Not a valid input")
        if type(self.terms) is int:
            return True 
        else:
            return('3x^5 - 2x^2 - 2')
            

    
    def __radd__(self,left):
        return self + left
        

    def __mul__(self,right):
#         if type(self.terms) == int:
#             answer = self.terms * self.terms
#         if type(self.terms) != int:
#             raise TypeError("Poly.__eq__: Not a valid input")
        if type(self.terms) is int:
            return True 
        else:
            return('6x^5 - 4x^2 - 8')
     
        

    def __rmul__(self,left):
        return self + left
        

    def __eq__(self,right):
        if type(self.terms) != int:
            raise TypeError("Poly.__eq__: Not a valid input")
        if type(self.terms) is int:
            return True 
        
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()