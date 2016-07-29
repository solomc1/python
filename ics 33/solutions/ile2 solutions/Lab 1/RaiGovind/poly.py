from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for value, key in terms:
            if (type(value) == int or type(value) == float) and type(key) == int and key >= 0:
                if key in self.terms:
                    raise AssertionError('Powers cannot be repeated you fool!:'.format(key, value))
                if value == 0:
                    pass
                elif type(value) == float or type(value) == int:
                    self.terms[key] = value
            else:
                raise AssertionError('Poly.__init__: Illegal power or coefficient in: ({}, {})'.format(key, value))
            
#             if type(value) != int and type(value) != float:
#                 raise AssertionError('Poly.__init__: Illegeal power or coefficient value ({}, {})'.format(type_as_str(key), type_as_str(value)))
#             if key >= 0 and type(key) == int:
#                 if value == 0:
#                     pass
#                 elif type(value) == float or type(value) == int:
#                     self.terms[key] = value
#             else:
#                 raise AssertionError('Poly.__init__: Illegeal power or coefficient value ({}, {})'.format(type_as_str(key), type_as_str(value)))
#         print(self.terms)
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
        poly_str = 'Poly('
        if len(self.terms.items()) == 0:
            return 'Poly()'
        else: 
            for key, value in self.terms.items():
                poly_str += '({},{}),'.format(value, key)
            return poly_str[:-1] + ')'

    
    def __len__(self):
        if len(self.terms.items()) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for key, value in self.terms.items():
            result += value*(arg**key)
        return result
    

    def __iter__(self):
        
        for key,value in sorted(self.terms.items(), reverse=True):
            yield value,key
            

    def __getitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError("Poly.__getitem__: You can only index by integers greater than or equal to 0")
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if index < 0 or type(index) != int:
            raise TypeError("Poly.__setitem__: You can only index by integers greater than or equal to 0")
        elif value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
            else:
                pass
        else:
            self.terms[index] = value
            
            
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError("Poly.__delitem__: You can only index by integers greater than or equal to 0")
        if index in self.terms.keys():
            self.terms.pop(index)
        else:
            pass
            

    def _add_term(self,c,p):
        if type(c) == int or type(c) == float and type(p) == int and int >= 0:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                if self.terms[p] + c == 0:
                    self.terms.pop(p)
                else:
                    self.terms[p] = self.terms[p] + c
        else:
            raise TypeError('Poly.__init__: Illegal power or coefficient in: ({}, {})'.format(p,c))
       

    def __add__(self,right):
        if type(right) == int or type(right) == float or type(right):
            for key,value in self.terms.items():
                self.terms[key] = self.terms[key] + right
            return self
        elif type(right) == Poly:
            for key, value in self.terms.items():
                self.terms[key] = self.terms[key] + right.terms[key]
            return self
        else:
            raise TypeError("Poly.__add__: appropriate message here")

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     
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