class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for co, power in terms:
            if type(co) not in (int, float):
                raise AssertionError('Coefficient must be an int or float')
            elif (type(power) is not int) or (power < 0):
                raise AssertionError('Powers must be int and must be greater than or equal to 0')
            elif power in self.terms.keys(): 
                raise AssertionError('That term with the power of ' + str(power) + ' already exists')
            else:
                if co != 0:
                    self.terms[power] = co
        
            
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
        return 'Poly(' + ','.join([str((co,power)) for power, co in self.terms.items()]) + ')'

    
    def __len__(self):
        if self.terms == dict():
            return 0
        else:
            return max([k for k in self.terms.keys()])
    
    def __call__(self,arg):
        if type(arg) not in (int, float):
            raise AssertionError('Argument must be int or float')
        else:
            y = 0
            for power, co in self.terms.items():
                y += co * (arg**power)
            return y
    
    def __iter__(self):
        for co, power in sorted(self.terms.items(), key = lambda x : x[0], reverse = True):
            yield((power, co))
            

    def __getitem__(self,index):
        if index < 0 or type(index) not in [int]:
            raise TypeError('Index must be greater than 0 and of type int')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        # index = any power
        # value = its coefficient
        
#         print('\nindex(power) = ', index)
#         print('value(coeff) = ', value)
        if index < 0 or type(index) is not int:
            raise TypeError('Index must be greater than 0 and of type int')
        elif value == 0:
            if value in self.terms.values():
                del self.terms[index]
        else:
            self.terms[index] = value
        
        

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Index must be an int')
        elif index < 0:
            raise TypeError('Index must be greater than 0')
        if index in self.terms.keys():
            del self.terms[index]
        
            
    #helper methods
    def _add_term(self,c,p):
#         if c not in (int, float):
#             raise TypeError('Coefficient must be int or float')
#         elif p < 0 or type(p) is not int:
#             raise TypeError('Power must be greater than or equal to 0 and must be an int')
        #rules
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        
       

    def __add__(self,right):
        
        if type(right) in (int, float):
            if self.terms[0] in self.terms.keys():
                self.terms[0] += right
        else:
            pass
            

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Can only compare a numeric (int or float) or another Poly object')
        else:
            if type(right) in (int, float):
                if self.terms[0] in self.terms.values():
                    return True if self.terms[0] == right else False
            else:
                check = []
                if len(self.terms.items()) != len(right.items()):
                    return False
                else:
                    for term in self.term.items():
                        if term in right.items():
                            check.append(True)
                        else:
                            check.append(False)
                return all(check)
                        
                        

    
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