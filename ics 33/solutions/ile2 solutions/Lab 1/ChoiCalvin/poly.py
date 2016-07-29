

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coef, power in terms:
            if type(coef) != int and type(coef) != float:
                raise AssertionError("Coefficient {} is not of type int or float".format(coef))
            if type(power) != int:
                raise AssertionError("Power {} is not of type int.".format(power))
            if power < 0:
                raise AssertionError("Power {} is not greater than or equal to 0".format(power))
            if power in self.terms.keys():
                raise AssertionError("Power {} cannot appear as a later term.".format(power))
            if coef == 0:
                continue
            else:
                self.terms[power] = coef
            
        
            
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
        parameters = set()
        for power, coef in self.terms.items():
            parameters.add((coef, power))
        if parameters == set():
            return 'Poly()'
        return 'Poly({})'.format(parameters).replace('{', '').replace('}', '')

    
    def __len__(self):
        result = []
        for power in self.terms.keys():
            result.append(power)
        if result == []:
            return 0
        return max(result)
    
    def __call__(self,arg):
        result = 0
        for power, coef in self.terms.items():
            result += coef * (arg**power)
        return result

    def __iter__(self):
        list_powers = []
        for power in self.terms.keys():
            list_powers.append(power)
        list_powers.sort(reverse = True)
        for power in list_powers:
            yield (self.terms[power], power)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("{} is not an integer.".format(index))
        if index < 0:
            raise TypeError("{} is less than 0.".format(index))
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        ''' index = power, value = coefficient
        '''
        if type(index) != int:
            raise TypeError("Index {} is not an integer.".format(index))
        if index < 0:
            raise TypeError("Index is less than 0.")
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index] = value
        
            

    def __delitem__(self,index):
        ''' index = power
        '''
        if type(index) != int:
            raise TypeError("Index {} is not an integer".format(index))
        if index < 0:
            raise TypeError("Index {} is less than 0".format(index))
        
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise AssertionError("Coefficient {} is not of type int or float".format(c))
        if type(p) != int:
            raise AssertionError("Power {} is not of type int.".format(p))
        if p < 0:
            raise AssertionError("Power {} is not greater than or equal to 0".format(p))
        
        if p in self.terms.keys():
            current_coef = self.terms[p]
            self.terms[p] = current_coef + c
                
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
          
        for power in self.terms.keys():
            if self.terms[power] == 0:
                self.terms.pop(power)
                break
        
            
            
            
            
    
            
                
        
        
       

    def __add__(self,right):
        if type(self) == type(right):
            for power, coef in right.terms.items():
                self._add_term(coef, power)
            return self
        
        if type(right) == int or type(right) == float:
            self._add_term(0, right)
            return self
        
        else:
            raise TypeError("Cannot add Poly with a {}".format(type(right)))
        
        

    
    def __radd__(self,left):
        if type(left) == int or type(left) == float:
            self._add_term(left, 0)
            return self
        else:
            raise TypeError("Cannot add Poly with a {}".format(type(left)))       
    

    def __mul__(self,right):
        if type(self) == type(right):
            new_poly = dict()
            for rpower, rcoef in right.terms.items():
                for power, coef in self.terms.items():
                    if (rpower + power) in new_poly.keys():
                        current_coef = new_poly[rpower + power]
                        new_poly[rpower + power] = current_coef + (rcoef * coef)
                    else:
                        new_poly[rpower + power] = rcoef * coef
            self.terms = new_poly
            return self
        
        if type(right) == int or type(right) == float:
            for power in self.terms.keys():
                current_coef = self.terms[power]
                self.terms[power] = current_coef * right
            return self
    

    def __rmul__(self,left):
        if type(left) == int or type(left) == float:
            for power in self.terms.keys():
                current_coef = self.terms[power]
                self.terms[power] = current_coef * left
            return self
        
        
        
        
        #### RETURN TO MUL AND ADD
    

    def __eq__(self,right):
        result = True
        if type(self) == type(right):
            for power, coef in self.terms.items():
                for rpower, rcoef in right.terms.items():
                    if power == rpower:
                        if coef != rcoef:
                            result = False
                    else:
                        result = False
            return result
                            
        if type(right) == int or type(right) == float:
            if len(self.terms.items()) == 1:
                for key in self.terms.keys():
                    if key == 0:
                        return self.terms[key] == right
                else:
                    return False
            else:
                return False
            
        else:
            raise TypeError("Cannot compare Poly with a {}".format(type(right))) 

    
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