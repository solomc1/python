class Poly:
    #first value is coefficient, second is power
    #3,2 = 3x^2
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x,y in terms:
            assert type(x) in [float, int]
            assert type(y) == int and y >= 0
            #assert y in self.terms
            if x != 0: 
                self.terms[y] = x
           
            
        
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
        temp = ""
        for x,y in self.terms.items():
            temp += "({},{}),".format(y,x)
        return "Poly(" + temp[:-1]+")"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        temp = []
        for x in self.terms.keys():
            temp.append(x)
        return max(temp)
    
    def __call__(self,arg):
        result = 0
        for x,y in self.terms.items():
            result += y*(arg**x)
        return result
    

    def __iter__(self):
        x = sorted(self.terms.items(), reverse = True)
        temp = []
        for x,y in x:
            temp.append((y,x))
        return iter(temp)
        
#         
#         temp = {}
#         x = sorted(self.terms.items(), reverse = True)
#         for y,z in x:
#             temp[z] = y
#         print(temp)                   
#         return iter(temp)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Not an int or is <0")
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        #power, coefficient
        if type(index) != int or index < 0:
            raise TypeError("Not an int or is <0")
        if value != 0: #and index in self.terms:
            self.terms[index] = value
        elif index in self.terms:
            del self.terms[index]
        else:
            pass
        
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Not an int or is <0")
        if index in self.terms:
            del self.terms[index]    

    def _add_term(self,c,p):
        if type(c) not in [int, float] or (type(p) != int and not(p >= 0)):
            raise TypeError('Coefficient or power are invalid.')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p]+= c
            if self.terms[p] == 0:
                del self.terms[p]           
       

    def __add__(self,right):
        if type(right) == Poly or type(right) in [int, float]:
            temp = Poly()
            if type(right) == Poly:
                for a,b in self.terms.items():
                    if a in right.terms:
                        temp._add_term(b+right.terms[a], a)
                    else:
                        temp._add_term(a, b)
            else:
                for x,y in self.terms.items():
                    if x == 0:
                        temp._add_term(y+right, x)
                    else:
                        temp._add_term(y, x)
        else:
            raise TypeError('Invalid type for + operand')
#                 for x,y in right.terms.items():
#                     if a==x:
#                         temp._add_term(y+b, x)
        return temp              
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if (type(right) == Poly) or (type(right)  in [int, float]):
            if type(right) in [int, float]:
                right = Poly(right, 0)
            if self.__dict__ == right.__dict__:
                return True
        else:
            raise TypeError('Invalid type for = operand')
        return False

    
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