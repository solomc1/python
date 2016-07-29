class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        #(coefficient, power)
        #d[power] = coefficient
        for term in terms:
            if type(term[0]) not in [float, int]:
                raise AssertionError
            if type(term[1]) not in [int]:
                raise AssertionError
            if term[1] < 0:
                raise AssertionError
            
        if len(terms) == 0:
            pass
        else:
            for term in terms:
                if term[0] == 0:
                    pass
                else:
                    if term[1] in self.terms.keys():
                        raise AssertionError
                    else:
                        self.terms[term[1]]= term[0]
        
            
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
        if len(self.terms.keys()) == 0:
            return "Poly()"
        string = 'Poly('
        i = ''
        for p, c in self.terms.items():
            i ='(' + str(c) + ','+ str(p) + '),'
            string += i
        return string[:-1] + ')'
    
    
    def __len__(self):
        max = 0
        for p, c in self.terms.items():
            if p > max:
                max = p
        return max
    
    def __call__(self,arg):
        result = 0
        if type(arg) not in [int, float]:
            raise AssertionError
        for p, c in self.terms.items():
            result += c * arg**p
        return result
    

    def __iter__(self):
        lst = sorted(self.terms.items(), key = lambda x: x[0], reverse = True)
        lst2 = []
        for i in lst:
            lst2.append((i[1], i[0]))
        return iter(lst2)
            

    def __getitem__(self,index):
        if type(index) not in [int]:
            raise TypeError
        if index < 0:
            raise TypeError 
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) not in [int]:
            raise TypeError
        if index < 0:
            raise TypeError 
        if type(value) not in [int, float]:
            raise TypeError
        if value == 0:
            pass
        self.terms[index] = value
#         for k, v in self.terms.items():
#             if v == 0:
#                 del self.terms[k]
        

    def __delitem__(self,index):
        if type(index) not in [int]:
            raise TypeError
        if index < 0:
            raise TypeError 
        if index not in self.terms.keys():
            return
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError
        if type(p) not in [int]:
            raise TypeError
        if p < 0:
            raise TypeError
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
            return
        if p in self.terms.keys():
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
                
                
    def __add__(self,right):
        if type(right) not in [int, Poly, float]:
            raise TypeError
        p = Poly()
        lst = []
        #power, coefficient
        for one, two in zip(sorted(self.terms.items()), sorted(self.terms.items())):
            lst.append((one[1]))
            ###############################
            
        return p

    
    def __radd__(self,left):
        if type(left) not in [int, Poly, float]:
            raise TypeError
    

    def __mul__(self,right):
        if type(right) not in [int, Poly, float]:
            raise TypeError
    

    def __rmul__(self,left):
        if type(left) not in [int, Poly, float]:
            raise TypeError
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError
        if type(right) in [int, float]:
            if len(self.terms.keys()) == 1:
                return 1 in self.terms.keys() and right in self.terms.values()
            else:
                return False
        if type(right) is Poly:
            for one, two in zip(sorted(self.terms), sorted(right.terms)):
                if one != two:
                    return False
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