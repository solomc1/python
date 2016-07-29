class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coeff, power in terms:
            if type(coeff) != int and type(coeff) != float:
                raise AssertionError('Poly.__init__: each coefficient must be and int or float value.')
            if type(power) != int or power < 0:
                raise AssertionError('Poly.__init__: each power must be an int whose value is >= 0.')
            if power in self.terms and self.terms[power] != 0:
                raise AssertionError('Poly.__init__: a power cannot appear as a later term if it appears as an earlier term.')
                
            if coeff != 0: 
                self.terms[power] = coeff
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
        pairs = ''
        for k_power, v_coeff in self.terms.items():
            pairs += str((v_coeff,k_power)) + ','
            
        pairs = pairs[0:-1]
        to_return = 'Poly(' + pairs + ')' 
        return to_return

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(self.terms)
        
    
    def __call__(self,arg):
        result = 0
        for k_power, v_coeff in self.terms.items():
            result += v_coeff * (arg**k_power)
        
        return result
    

    def __iter__(self):
        list_of_pairs = []
        for k_power, v_coeff in self.terms.items():
            list_of_pairs.append((v_coeff, k_power))
        
        rev_list = list_of_pairs[::-1]
        for pair in rev_list:
            yield pair

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError ('Poly.__getitem__: power must be an integer greater than or equal to 0.')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value): #power, coeff
        if type(index) != int or index < 0:
            raise TypeError ('Poly.__setitem__: power must be an integer greater than or equal to 0.')
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value
          
            
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError ('Poly.__deliitem__: power must be an integer greater than or equal to 0.')
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
                raise TypeError('Poly._add_term: coefficient must be numeric')
        if type(p) != int or p < 0:
            raise TypeError('Poly._add_term: each power must be an int whose value is >= 0.')
       
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                self.terms.pop(p)

    def __add__(self,right):
        to_return = Poly()
        
        for coeff, power in self:
            to_return._add_term(coeff, power)
            
        if type(right) == Poly:
            for coeff, power in right:
                to_return._add_term(coeff, power)
        elif type(right) == int or type(right) == float:
            to_return._add_term(right, 0)
        else:
            raise TypeError('Poly.__add__: right argument must be of type Poly, int, or float')
        
        return to_return
#        
    def __radd__(self,left):
        to_return = Poly()
        
        for coeff, power in self:
            to_return._add_term(coeff, power)
            
        if type(left) == Poly:
            for coeff, power in left:
                to_return._add_term(coeff, power)
        elif type(left) == int or type(left) == float:
            to_return._add_term(left, 0)
        else:
            raise TypeError('Poly.__radd__: left argument must be of type Poly, int, or float')
        
        return to_return    

    def __mul__(self,right):
        to_return = Poly()
        
        if type(right) == Poly:
            for c1, p1 in self:
                for c2, p2 in right:
                    to_return._add_term(c1*c2, p1+p2)
        elif type(right) == int or type(right) == float:
            for c1, p1 in self:
                to_return._add_term(c1*right, p1)
        else:
            raise TypeError('Poly.__mul__: left argument must be of type Poly, int, or float')
        
        return to_return
    

    def __rmul__(self,left):
        to_return = Poly()
        
        if type(left) == Poly:
            for c1, p1 in self:
                for c2, p2 in left:
                    to_return._add_term(c1*c2, p1+p2)
        elif type(left) == int or type(left) == float:
            for c1, p1 in self:
                to_return._add_term(c1*left, p1)
        else:
            raise TypeError('Poly.__rmul__: left argument must be of type Poly, int, or float')
        
        return to_return    

    def __eq__(self,right):
        if (type(self) == int or type(self) == float or type(self) == Poly) and (type(right) == int or type(right) == float or type(right) == Poly):
            if type(self) != type(right):
                if self.terms[0] == right and len(self.terms) == 1:
                    return True
                else:
                    return False
            else:
                for c1, p1 in self:
                    for c2, p2 in right:
                        if c1 != c2 or p1 != p2:
                            return False
            return True
        else:
            raise TypeError('Poly.__eq__: illegal type in arguments')


    
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