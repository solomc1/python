# Michael Tran, Lab 2

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
    
        for coeff, power in terms:
            assert type(coeff) in (int, float), 'Coefficient not int or float'
            assert type(power) == int and power >= 0, 'Bad power'
            
            if coeff != 0:
                assert power not in self.terms, 'Power already in'
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
        return 'Poly(' + ','.join('('+str(coeff)+','+str(power)+')' for power,coeff in self.terms.items()) + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        answer = 0
        for power, coeff in self.terms.items():
            answer += coeff * (arg**power)
        return answer
    

    def __iter__(self):
        for power, coeff in sorted(self.terms.items(), reverse=True):
            yield coeff,power
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('bad index')
        return 0 if index not in self.terms.keys() else self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('bad index')
        if value == 0 and index in self.terms.keys():
            del self.terms[index]
        elif value != 0:
            self.terms[index] = value
        
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('bad index')   
        if index in self.terms.keys():
            del self.terms[index]     
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('coefficient must be int or float')
        if type(p) != int or p < 0:
            raise TypeError('power must be int and >= 0')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if c + self.terms[p] == 0:
                del self.terms[p]
            else: 
                self.terms[p] += c
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('bad operand for +')
        new_poly = Poly()
        for p,c in self.terms.items():
            new_poly._add_term(c,p)
        if type(right) in (int,float):
            new_poly._add_term(right,0)
        else:
            for p,c in right.terms.items():
                new_poly._add_term(c,p)
        return new_poly

    
    def __radd__(self,left):
        return Poly.__add__(self,left)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('bad operand for *')
        
        new_poly = Poly()
        
        if type(right) in (int,float):
            right = Poly((right,0))

        for p1,c1 in right.terms.items():
            for p2,c2 in self.terms.items():
                new_poly._add_term(c1*c2,p1+p2)
                
        return new_poly
        
        
    def __rmul__(self,left):
        return Poly.__mul__(self,left)
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('bad operand for ==')
        if type(right) == Poly:
            return all(self.terms[p] == right.terms[p] for p in self.terms.keys())
        else:
            return all(self.terms[p] == right for p in self.terms.keys())
    
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