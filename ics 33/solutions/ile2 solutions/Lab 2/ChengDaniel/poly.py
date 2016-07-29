class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coefficient, power in terms:
            if type(coefficient) in (int, float) and type(power) == int and power >= 0 and power not in self.terms:
                if coefficient == 0:
                    continue
                self.terms[power] = coefficient
            else:
                raise AssertionError
            
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
        if len(self) > 0:
            result = "Poly("
            for (power, coefficient) in self.terms.items():
                result += "(" + str(coefficient) + "," + str(power) + "),"
            return result[:-1] + ")" 
        return "Poly()"
        

    
    def __len__(self):
        if self.terms.keys():
            return max(self.terms.keys())
        return 0
    
    def __call__(self,arg):
        result = 0
        for power, coefficient in self.terms.items():
            result += coefficient * arg ** power
        return result
    

    def __iter__(self):
        sorted_powers_list = sorted(self.terms.items(), key=lambda t: t[0])
        while sorted_powers_list:
            result = sorted_powers_list.pop()
            yield (result[1], result[0])

    def __getitem__(self,index):
        if index < 0:
            raise TypeError("Index must be non-negative")
        if index in self.terms:
            return self.terms[index]
        return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Index must be non-negative integer")
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if index < 0:
            raise TypeError("Index must be non-negative")
        if index in self.terms:
            self.terms.pop(index)

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Coefficient must be of type int or float")
        if type(p) != int:
            raise TypeError("Power must be of type int")
        if p < 0:
            raise TypeError("Power must be non-negative")
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            total = c + self.terms[p]
            if total == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = total
       

    def __add__(self,right):
        result_poly = Poly()
        if type(right) == int:
            right = Poly((right, 0))
        if type(right) == Poly:
            for power, coefficient in self.terms.items():
                result_poly._add_term(coefficient, power)
            for power, coefficient in right.terms.items():
                result_poly._add_term(coefficient, power)
            return result_poly
        raise TypeError("Right operand must be of type int or Poly")
        

    
    def __radd__(self,left):
        result_poly = Poly()
        if type(left) == int:
            left = Poly((left, 0))
        if type(left) == Poly:
            for power, coefficient in self.terms.items():
                result_poly._add_term(coefficient, power)
            for power, coefficient in left.terms.items():
                result_poly._add_term(coefficient, power)
            return result_poly
        raise TypeError("Right operand must be of type int or Poly")
        

    def __mul__(self,right):
        result_poly = Poly()
        if type(right) == int:
            right = Poly((right, 0))
        if type(right) == Poly:
            for power_s, coefficient_s in self.terms.items():
                for power_r, coefficient_r in right.terms.items():
                    result_poly._add_term(coefficient_s * coefficient_r, power_s + power_r)
            return result_poly
        raise TypeError("Right operand must be of type int or Poly")
            

    def __rmul__(self,left):
        result_poly = Poly()
        if type(left) == int:
            left = Poly((left, 0))
        if type(left) == Poly:
            for power_s, coefficient_s in self.terms.items():
                for power_l, coefficient_l in left.terms.items():
                    result_poly._add_term(coefficient_s * coefficient_l, power_s + power_l)
            return result_poly
        raise TypeError("Right operand must be of type int or Poly")
    

    def __eq__(self,right):
        if type(right) == int:
            right = Poly((right, 0))
        if type(right) == Poly:
            for power in self.terms:
                if power not in right.terms or self.terms[power] != right.terms[power]:
                    return False
            return True
        raise TypeError("Right operand must of type int or Poly")

    
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