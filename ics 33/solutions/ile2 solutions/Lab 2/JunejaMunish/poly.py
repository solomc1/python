class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coef,power in terms:
            assert ((type(coef) == int or type(coef) == float) and (type(power) == int)), \
            "Coefficients must be ints or floats and powers must be ints"
            assert power >= 0, "Powers must be greater than or equal to 0"
            if not coef == 0:
                assert not power in self.terms.keys()
                self.terms[power] = coef

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
        return "Poly(" + ",".join(str((coef, power)) for power,coef in self.terms.items()) + ")"

    
    def __len__(self):
        max_len = 0
        for x in self.terms.keys():
            if x>max_len:
                max_len = x
        return max_len
    
    def __call__(self,arg):
        return sum([(arg**power)*coef for power, coef in self.terms.items()])
    

    def __iter__(self):
        for power, coef in sorted(self.terms.items(), reverse = True):
            yield (coef, power)
            

    def __getitem__(self,index):
        if not (type(index) == int and index >= 0):
            raise TypeError("Index must be an integer not less than 0")
        if not index in self.terms.keys():
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if not (type(index) == int and index >= 0):
            raise TypeError("Power must be an int not less than 0")
        if value == 0:
            self.__delitem__(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if not (type(index) == int and index >= 0):
            raise TypeError("Power must be an int not less than 0")
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not ((type(c) == int or type(c) == float) and type(p) == int and p >= 0):
            raise TypeError("Coefficients can be ints or floats, and Powers must be ints not less than 0")
        if not p in self.terms.keys():
            self.__setitem__(p, c)
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.__delitem__(p)

    def __add__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float):
            raise TypeError("Polys must be added with another Poly or numerical value")
        result = Poly()
        for x,y in self.terms.items():
            result.terms[x] = y
        if not type(right) == Poly:
            right_copy = Poly((right, 0))
        else:
            right_copy = Poly()
            for x,y in right.terms.items():
                right_copy.terms[x] = y
        for power, coef in right_copy.terms.items():
            result._add_term(coef, power)
        return result
            

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float):
            raise TypeError("Polys must be multiplied with another Poly or numerical value")
        result = Poly()

        if not type(right) == Poly:
            right_copy = Poly((right, 0))
        else:
            right_copy = Poly()
            for x,y in right.terms.items():
                right_copy.terms[x] = y
        for power, coef in self.terms.items():
            for r_power, r_coef in right_copy.terms.items():
                result._add_term(coef * r_coef, power + r_power)
        return result

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float):
            raise TypeError("Right side of equals with Poly must be another Poly or numeric")
        if not type(right) == Poly:
            right_copy = Poly((right, 0))
        else:
            right_copy = right
        
        if right_copy.__dict__ == self.__dict__:
            return True
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