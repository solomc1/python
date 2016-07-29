class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        

        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            assert (type(x[0]) in [int, float]), "Coefficient must be int or float"
            assert (type(x[1]) == int and x[1] >= 0), "Power must be an int greater than or equal to 0"
        check_list = []
        for v, k in terms:
            assert k not in check_list, "Duplicate powers"
            if v!= 0:
                check_list.append(k)
                self.terms[k] = v


            
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
        return 'Poly({})'.format(','.join("("+str(c)+','+str(p)+")" for p, c in self.terms.items()))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max([p for p in self.terms.keys()])
    
    def __call__(self,arg):
        result = 0
        for p, c in self.terms.items():
            result += c*(arg**p)
        return result
    

    def __iter__(self):
        iter_list = sorted([(c, p) for p, c in self.terms.items()], key = (lambda x: x[1]), reverse = True)
        for item in iter_list:
            yield item
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("index needs to be a positive integer.")
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("index needs to be a positive integer.")
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("index needs to be a positive integer.")
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int:
            raise TypeError("c needs to be a positive integer.")
        if type(p) != int or p < 0:
            raise TypeError("p needs to be a positive integer.")
        
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) == Poly:
            new_poly = self
            for p, c in right.terms.items():
                if p in new_poly.terms.keys():
                    new_poly.terms[p] += right.terms[p]
                    if new_poly.terms[p] == 0:
                        del new_poly.terms[p]
                new_poly._add_term(c, p)
            
                    
        elif type(right) in [int, float]:
            new_poly = self
            new_poly.terms[0] += right

        else:
            raise TypeError("Poly can only add with poly, int, or float.")
        
        return new_poly

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) == Poly:
            new_poly = self
        elif type(right) in [int, float]:
            new_poly = self
            for p, c in new_poly.terms.items():
                new_poly.terms[p]  = new_poly.terms[p]*right
        else:
            raise TypeError("Poly can only multiply with poly, int, or float.")
        return new_poly

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            return sorted(self.terms.items()) == sorted(right.terms.items())
                
        elif type(right) in [int, float]:
            return self.terms.items() == Poly((right,0)).terms.items()
        else:
            raise TypeError("Poly can only compare with poly, int, or float.")

    
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