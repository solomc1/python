class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for coef,power in terms:
            if type(power) != int:
                raise AssertionError('Power must be a positive integer.')
            if power < 0:
                raise AssertionError('Power must be a positive integer.')
            if type(coef) != int:
                if type(coef) != float:
                    raise AssertionError('Coefficient must be an integer or float value.')
            if power in self.terms.keys():
                raise AssertionError('The same power cannot be included twice.')
            if coef != 0:
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
        result = 'Poly('
        for key,val in self.terms.items():
            result += '({},{}),'.format(val,key)
        if self.terms != {}:
            result = result[0:-1]
        result += ')'
        return result

    
    def __len__(self):
        if self.terms != {}:
            return sorted(self.terms)[-1]
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for power,coef in self.terms.items():
            result += (arg**power)*coef
        return result
    

    def __iter__(self):
    #    class poly_iter:
    #        def __init__(self, iter_poly):
    #            pass
    #        def __next__(self):
    #            pass
    #    return poly_iter(self)
        pass

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Argument must be an integer >= 0')
        try:
            return self.terms[index]
        except:
            return 0

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index argument must be an integer >= 0')
        if type(value) != int:
            if type(value) != float:
                raise TypeError('Value argument must be an integer or float value')
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index argument must be an integer >= 0')
        if index in self.terms.keys():
            self.terms.pop(index)
        
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Index argument must be an integer >= 0')
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        else:
            coef_sum = self.terms[p]
            coef_sum += c
            if coef_sum == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = coef_sum

    def __add__(self,right):
        result = self
        if type(right) == int or type(right) == float:
            result._add_term(right,0)
        elif type(right) == Poly:
            for key,val in right.terms.items():
                result._add_term(val,key)
        else:
            raise TypeError('Poly object cannot be added with {} object'.format(type(right)))
        return result

    
    def __radd__(self,left):
        result = self
        if type(left) == int or type(left) == float:
            result._add_term(left,0)
        else:
            raise TypeError('Poly object cannot be added with {} object'.format(type(left)))
        return result
    

    def __mul__(self,right):
        result = Poly()
        if type(right) == Poly:
            for power_self,coef_self in self.terms.items():
                for power_right,coef_right in right.terms.items():
                    result._add_term(coef_self*coef_right, power_self+power_right)
        elif type(right) == int or type(right) == float:
            for power,coef in self.terms.items():
                result._add_term(coef*right,power)
        else:
            raise TypeError('Poly object cannot be multiplied with {} object'.format(type(right)))
        return result
    

    def __rmul__(self,left):
        result = Poly()
        if type(left) == int or type(left) == float:
            for power,coef in self.terms.items():
                result._add_term(coef*left,power)
        else:
            raise TypeError('Poly object cannot be multiplied with {} object'.format(type(left)))
        return result

    def __eq__(self,right):
        if type(right) == int or type(right) == float:
            if len(self.terms.keys()) == 1:
                if 0 in self.terms.keys():
                    if self.terms[0] == right:
                        return True
            return False
        elif type(right) == Poly:
            if self.terms == right.terms:
                return True
            return False
        else:
            raise TypeError('Poly object cannot be compared to {} object'.format(type(right)))


    
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
    #print('  list collecting iterator results:',[t for t in p])
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