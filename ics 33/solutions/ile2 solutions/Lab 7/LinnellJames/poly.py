class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to initialize self.terms
        
        # Add the powers and coefficients based on the rules
        for coeff, power in terms:
            self._ensure_power_type(AssertionError, power)
            self._ensure_coeff_type(AssertionError, coeff)
            if power in self.terms and self.terms[power] != coeff:
                raise AssertionError("Poly: mismatching coefficients (got {} and {}) for power {}".format(coeff, self.terms[power], power))
            
            # __setitem__ will handle values of 0
            self[power] = coeff
            
            
    # Helper methods for the cumbersome type/value checks
    @staticmethod
    def _ensure_power_type(exc_type, power):
        # Checks for type == int and value >= 0
        if type(power) is not int:
            raise exc_type("Poly: expected power of type int, got {}".format(type(power)))
        if power < 0:
            raise exc_type("Poly: expected positive power, got {}".format(power))
        
    @staticmethod
    def _ensure_coeff_type(exc_type, coeff):
        # Checks just for type = (int|float)
        if type(coeff) not in (int, float):
            raise exc_type("Poly: expected coefficient of type (int, float), got {}".format(type(coeff)))
        
            
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
        return "Poly({})".format(", ".join([repr((coeff, power)) for power, coeff in self.terms.items()]))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max([power for power in self.terms])
    
    
    def __call__(self,arg):
        return sum([coeff * (arg ** power) for power, coeff in self.terms.items()])
    

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), reverse=True):
            yield coeff, power
            

    def __getitem__(self,index):
        self._ensure_power_type(TypeError, index)
        
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        self._ensure_power_type(TypeError, index)
        self._ensure_coeff_type(TypeError, value)
        
        if value == 0 and index in self.terms:
            del self[index]
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        self._ensure_power_type(TypeError, index)
        
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,coeff,power):
        self._ensure_power_type(TypeError, power)
        self._ensure_coeff_type(TypeError, coeff)
        
        if coeff != 0:
            self[power] = self[power] + coeff
       

    def __add__(self,right):
        result = Poly() # Construct the result beforehand and mutate while we add
        for coeff, power in self:
                result._add_term(coeff, power)
                
        if type(right) in (int, float):
            result._add_term(right, 0)
            
        elif type(right) is Poly:
            for coeff, power in right:
                result._add_term(coeff, power)
                
        else:
            raise TypeError("Poly: expected operand of type (Poly, int, float), got {}".format(type(right)))
        
        return result

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        # Create an empty result and add the multiplied values
        # in the process of multiplication
        result = Poly()
                
        if type(right) in (int, float):
            for coeff, power in self:
                # Multiply each coeff by the right operand
                result._add_term(coeff * right, power)
                
        elif type(right) is Poly:
            # Multiply everything by everything, looping through self which is static
            for coeff_right, power_right in right:
                for coeff_self, power_self in self:
                    result._add_term(coeff_right * coeff_self, power_right + power_self)
                    
        else:
            raise TypeError("Poly: expected operand of type (Poly, int, float), got {}".format(type(right)))
        
        return result
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) in (int, float):
            if len(self) == 0 and 0 in self.terms:  # If the maximum power is 0
                # We also check if the 0 power is in our terms as well,
                # because if len() returns 0 it means either one term of 0 power or no terms
                return self[0] == right
            else:
                return False
            
        elif type(right) is Poly:
            for self_poly, right_poly in zip(self, right):
                if self_poly[0] != right_poly [0] or self_poly[1] != right_poly[1]:
                    return False
            return True
        
        else:
            raise TypeError("Poly: expected operand of type (Poly, int, float), got {}".format(type(right)))

    
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
    print('  getindex:', p[5], p[2], p[1], p[0])
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  2+p:',2+p)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('  2*p:',2*p)
    print('End simple tests\n')
    
    print()
    print(Poly((3,2), (2,1), (1,0)) * Poly((1,1), (2,0)))
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()