class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for v,k in terms:
            assert type(v) in [int, float],"Poly.__init__: Coefficient must be an int or float" + str(v)
            assert type(k) is int and k>=0, "Poly.__init__: Power must be int whose value is >= 0" + str(k)
            assert k not in self.terms.keys(), "Poly.__init__: Power cannot be used more than once."
            
            self.coefficient = v
#             print("Coefficient = ",self.coefficient)
            self.power = k
#             print("Power = ",self.power)
            self.terms.update({self.power:self.coefficient})
            
            for v in self.terms.values():
                if v == 0:
                    self.terms.popitem()
#         print("Terms dictionary = ", self.terms)

            
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
        return "Poly("+"".join(str(k) for k in self.terms.items()) + ")"
        # Not placing keys/values in correct spots...


    
    def __len__(self):
        power_list = []
#         print(self.terms.keys())
        for k in self.terms.keys():
            power_list.append(k)
#             print(power_list)
            power_list = sorted(power_list, reverse = True)
#             print(power_list)
        return power_list[0]
    
    def __call__(self,arg):
        if type(arg) not in [int, float]:
            raise TypeError("Poly.__call__: arg must be int or float. arg = ", type(arg))
        poly_str = self.__str__()
#         print(poly_str)
        # Not finished...
        
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        pass
            

    def __setitem__(self,index,value):
        pass
            

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
    print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()