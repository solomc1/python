# GiaLan Cao, Lab 5.

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coefficient, power in terms:
            assert type(coefficient) == int or type(coefficient) == float,\
                "Poly.__init__: Coefficient must be an int or float (given: {})".format(repr(coefficient))
            assert type(power) == int and power >= 0,\
                "Poly.__init__: Power must be an int whose value is greater than or equal to 0 (given: {})".format(repr(power))
            assert power not in self.terms,\
                "Poly.__init__: The power {} has already been specified".format(repr(power))
            if coefficient != 0:
                self.terms[power] = coefficient

            
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
        contentList = []
        for power, coefficient in self.terms.items():
            contentList.append("({},{})".format(coefficient, power))
        return "Poly({})".format(",".join(contentList))

    def __len__(self):
        return 0 if len(self.terms) == 0 else max(self.terms)
    
    def __call__(self,arg):
        return sum([coefficient * arg ** power for power, coefficient in self.terms.items()])
    
    
    def __iter__(self):
        for power, coefficient in sorted(self.terms.items(), key = lambda pair: pair[0], reverse = True):
            yield coefficient, power

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: Index (given: {}) must be an int greater than or equal to 0".format(repr(index)))
        return 0 if index not in self.terms else self.terms[index]
    

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__setitem__: Index/power (given: {}) must be an int greater than or equal to 0".format(repr(index)))
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__: Index/power (given: {}) must be an int greater than or equal to 0".format(repr(index)))
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError("Poly._add_term: Coefficient (given: {}) must be an int or a float".format(repr(c)))
        if type(p) != int or p < 0:
            raise TypeError("Poly._add_term: Power (given: {}) must be an int greater than or equal to 0".format(repr(p)))
        if c != 0:
            if p not in self.terms:
                self.terms[p] = c
            else:
                self.terms[p] += c
                if self.terms[p] == 0:
                    self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("Poly.__add__: Other operand must be Poly, int, or float (given: {})".format(repr(right)))
        result = Poly()
        if type(right) != Poly:
            right = Poly((right, 0))
        for polyObject in [self, right]:
            for power, coefficient in polyObject.terms.items():
                result._add_term(coefficient, power)
        return result

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("Poly.__mul__: Other operand must be Poly, int, or float (given: {})".format(repr(right)))
        result = Poly()
        if type(right) != Poly:
            right = Poly((right, 0))
        for powerOne, coefficientOne in self.terms.items():
            for powerTwo, coefficientTwo in right.terms.items():
                result._add_term(coefficientOne * coefficientTwo, powerOne + powerTwo)
        return result
        

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("Poly.__eq__: Other operand must be Poly, int, or float (given: {})".format(repr(right)))
        if type(right) != Poly:
            right = Poly((right, 0))
        return self.terms == right.terms

    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()