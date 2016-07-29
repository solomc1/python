class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        
#         # Fill in the rest of this method, using *terms to intialize self.terms
        for i in terms:
            if not type(i[0]) in [int,float]:
                raise AssertionError("Ply.__init__: Error. {} Not type into of float".format(i[0]))
            if not type(i[1]) in [int] or not i[1] >= 0:
                raise AssertionError("Error. {} Not int or greater than 0".format(i[1]))
            if i[0] == 0:
                del(i[0])
            self.coef = i[0]
            self.power = i[1]
            self.terms[i[1]]=i[0]

            

        
            
            
        

            
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
#         return "Poly("+str(sorted(self.terms.items()))+")"
        return "Poly("+str(tuple(i for i in self.terms.values()))+str(tuple(i for i in self.terms.keys()))+")"


    
    def __len__(self):
        if len(self.terms.keys()) <= 0:
            raise ValueError("max() arg is an empty sequence")
        return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) in [int, float], "Error. Type of arg was MUST be int or float"
        for i in self.terms.values():
            return arg**i
    

    def __iter__(self):
        pass
       # print(sorted(self.terms.items()))
            

    def __getitem__(self,index):
        if not type(index) in [int] or index < 0:
            raise TypeError("Type Error. {} not a valid input".format(index))
        if not index in self.terms:
            return 0 
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if not type(index) in [int] or index < 0:
            raise TypeError("Index arg is not of type int OR is less than 0")
        if value == 0:
            if value in self.terms:
                del(value)
        self.terms[index] = value
            

    def __delitem__(self,index):
        del(self.terms[index])
            

    def _add_term(self,c,p):
        pass
#         if not type(c) in [int, float]:
#             raise TypeError("Type of c arg is not int or float")
#         if not type(p) in [int] or p >= 0:
#             raise TypeError("Type of p arg is not int OR it is not greater than 0")
#         if p not in self.terms.items() and p != 0:
#             self.terms[p] = c 
#         if p in self.terms.items():
#             self.terms[p] += c 
#         
            
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("Argument not valid type")
        if type(right) is Poly:
            return Poly(self.coef+right.coef, self.power)
        if type(right) in [int, float]:
            return Poly(self.coef+right. self.power)

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("Argument not valid type")
        if type(right) is Poly:
            return Poly(self.coef*right.coef, self.power)
        if type(right) in [int, float]:
            return Poly(self.coef*right. self.power)
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) is Poly:
            pass
        if type(right) in [int, float]:
            pass


    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    #the driver is called.
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
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()