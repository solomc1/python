class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            coefficient = term[0]
            power = term[1]
            assert type(coefficient) is int or type(coefficient) is float, "Poly.__init__:it should be an int or float type object"
            assert type(power) is int , "Poly.__init__:it should be an int or float type object"
            assert power >= 0, "Poly.__init__:it should be larger or equal to 0"
            if coefficient!= 0:
                if power in self.terms.keys():
                    assert coefficient == self.terms[power],"Poly.__init__: an addition value appears"
                    self.terms.update({coefficient:power})
                else:
                    self.terms.update({coefficient:power})
            
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
        empty_string = ""
        item_number = 0
        for coefficient, power in self.terms.items():
            item_number += 1
            item_string = "("+str(coefficient)+","+str(power)+")"
            if item_number != len(self.terms.items()):
                empty_string += item_string+","
            else:
                empty_string += item_string
        return "Poly({})".format(empty_string)

    
    def __len__(self):
        return sorted(self.terms.values(), key = lambda x:x, reverse = True)[0]
    
    def __call__(self,arg):
        assert type(arg) is int or type(arg) is float, "Poly:__call__: it must be int or float"
        calculate_number = 0
        for coefficient, power in self.terms.items():
            calculate_number += coefficient*(arg**power)
        return calculate_number
    

    def __iter__(self):
        for item_tuple in sorted(self.terms.items(),key = lambda x:x[1],reverse = True):
            yield(item_tuple)
            

    def __getitem__(self,index):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__getitem__: it should be int type and larger than 0")
        else:
            for coefficient, power in self.terms.items():
                if power == index:
                    return coefficient
    def __setitem__(self,index,value):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__setitem__: it should be int type and larger than 0")
        else:
            self.terms.update({value:index})

    def __delitem__(self,index):
        if (type(index) is not int) or (index < 0):
            raise TypeError("Poly.__delitem__: it should be int type and larger than 0")
        else:
            for coefficient, power in self.terms.items():
                if power == index:
                    del self.terms[coefficient]

    def _add_term(self,c,p):
        if (type(c) is not int or not float) or (type(p) is not int or p<0):
            raise TypeError("Poly._add_term: Type Error")
        else:
            if p in self.terms.values():
                for coefficient, power in self.terms.items():
                    if power == p:
                        self.terms.update({coefficient+c:p})
            else:
                self.terms.update({c:p})
    def __add__(self,right):
        if type(right) is not Poly or not int or not float:
            raise TypeError("Poly.__add__: it should be int float or Poly")
        elif type(right) is Poly:
            for rcoeff, rpower in right.terms.items():
                if rpower in self.terms.values():
                    for coeff,power in self.terms.items():
                        if power == rpower:
                            self.terms.update({rcoeff+coeff,power})
                else:
                    self.terms.update({rcoeff,power})
        else:
            for coefficient, power in self.terms.items():
                if power == 0:
                    self.terms.update({coeff+right,power})
        
    def __radd__(self,left):
        if type(left) is not Poly or not int or not float:
            raise TypeError("Poly.__radd__:it should be int float or Poly")
        elif type(left) is Poly:
            for lcoeff, lpower in left.terms.items():
                if lpower in self.terms.values():
                    for coeff,power in self.terms.items():
                        if power == lpower:
                            self.terms.update({lcoeff+coeff,power})
                else:
                    self.terms.update({lcoeff,power})
        else:
            for coefficient, power in self.terms.items():
                if power == 0:
                    self.terms.update({coeff+left,power})

    def __mul__(self,right):
        if type(right) is not Poly or not int or not float:
            raise TypeError("Poly.__mul__: it should be int float or Poly")
        elif type(right) is Poly:
            for rcoeff, rpower in right.terms.items(): 
                for coeff,power in self.terms.items():
                    self.terms.update({rcoeff*coeff,rpower+power})    

    def __rmul__(self,left):
        if type(left) is not Poly or not int or not float:
            raise TypeError("Poly.__rmul__: it should be int float or Poly")
        elif type(left) is Poly:
            for lcoeff, lpower in left.terms.items(): 
                for coeff,power in self.terms.items():
                    self.terms.update({lcoeff*coeff,lpower+power})  

    def __eq__(self,right):
        if type(right) is not Poly or not int:
            raise TypeError("Poly.__eq__: wrong type")
        elif type(right) is Poly:
            return self.terms == right.terms
        else:
            for coefficient, power in self.terms.items():
                if power == 0:
                    return coefficient == right
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-1,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print(" p[2]:", p[2])
#     p[5] = -2
#     print(repr(p))
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print("p=p",p==p)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    #driver.driver()