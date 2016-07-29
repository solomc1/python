class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for item in terms:
            assert type(item[0]) in (int, float), 'value: {}, coeffiecients must be of type int or type float'.format(item[0])
            assert type(item[1]) is int and item[1] >= 0, 'value: {}, powers must be of type int and must be >= 0'.format(item[1])
            assert item[1] not in self.terms, 'value: {}, cannot set a certain power more than once'.format(item[1])
            
            if item[0] != 0:
                self.terms[item[1]] = item[0]
            
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
        
        return 'Poly({})'.format(','.join(['({},{})'.format(coeff,power) for power,coeff in self.terms.items()]))

    
    def __len__(self):
        
        return ((max(self.terms.keys())) if len(self.terms) > 0 else 0)
    
    def __call__(self,arg):
        
        assert type(arg) in (int, float), 'value: {}, arg must be of type int or type float'
        
        result = 0
        for power, coeff in self.terms.items():
            result += coeff * (arg ** power)
            
        return result
    

    def __iter__(self):
        
        ordered_list = sorted([(coeff,power) for power,coeff in self.terms.items()],
                              key=lambda x: x[1],
                              reverse=True)
        
        for item in ordered_list:
            yield item
            

    def __getitem__(self,index):
        
        if type(index) is not int or index < 0:
            raise TypeError('value: {}, index must be of type int and >= 0')
        
        return (self.terms[index] if index in self.terms else 0)
            

    def __setitem__(self,index,value):
        
        if type(index) is not int or index < 0:
            raise TypeError('value: {}, index must be of type int and >= 0')
        
        if index in self.terms and value == 0:
            self.terms.pop(index)
            
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        
        if type(index) is not int or index < 0:
            raise TypeError('value: {}, index must be of type int and >= 0')
        
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        
        if type(p) is not int or p < 0:
            raise TypeError('value: {}, p must be of type int and >= 0')
        
        if type(c) not in (int, float):
            raise TypeError('value: {}, c must be of type int or type float')
        
        if p not in self.terms and c != 0:
            self.terms[p] = c
            
        elif p in self.terms:
            self.terms[p] += c
            
            if self.terms[p] == 0:
                self.terms.pop(p)
       

    def __add__(self,right):
        
        if type(right) not in (Poly, int, float):
            raise TypeError('Polys can only be added to other Polys, ints, or floats')

        new_poly = eval(self.__repr__())
        
        if type(right) is Poly:
            for coeff, power in right:
                new_poly._add_term(coeff, power)
        
        else:
            new_poly._add_term(right, 0)
            
        return new_poly            

    
    def __radd__(self,left):
        
        if type(left) not in (Poly, int, float):
            raise TypeError('Polys can only be added to other Polys, ints, or floats')

        new_poly = eval(self.__repr__())
        
        if type(left) is Poly:
            for coeff, power in left:
                new_poly._add_term(coeff, power)
        
        else:
            new_poly._add_term(left, 0)
            
        return new_poly
    

    def __mul__(self,right):
        
        if type(right) not in (Poly, int, float):
            raise TypeError('Polys can only be multiplied with other Polys, ints, or floats')
        
        new_poly = Poly()
        
        if type(right) is Poly:
            
            for coeff1, power1 in self:
                for coeff2, power2 in right:
                    new_poly._add_term(coeff1 * coeff2, power1 + power2)
        
        else:
            for coeff, power in self:
                new_poly._add_term(coeff * right, power)
                
        return new_poly
    

    def __rmul__(self,left):
        
        if type(left) not in (Poly, int, float):
            raise TypeError('Polys can only be multiplied with other Polys, ints, or floats')
        
        new_poly = Poly()
        
        if type(left) is Poly:
            
            for coeff1, power1 in self:
                for coeff2, power2 in left:
                    new_poly._add_term(coeff1 * coeff2, power1 + power2)
        
        else:
            for coeff, power in self:
                new_poly._add_term(coeff * left, power)
                
        return new_poly
    

    def __eq__(self,right):
        
        if type(right) not in (Poly, int, float):
            raise TypeError('Polys can only be compared to other Polys, ints, or floats')
        
        if type(right) == Poly:
        
            if len(self) != len(right):
                return False
            
            else:
                for i in range(max(len(self),len(right))):
                    
                    if i in self.terms and i in right.terms:
                        if self[i] != right[i]:
                            return False
                    
                    elif i in self.terms or i in right.terms:
                        return False
                    
                return True
        
        else:
            if 0 in self.terms and len(self) == 0:
                return self[0] == right
            
            else:
                return False

    
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