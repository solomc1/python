class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.given = terms
            
        if len(self.given) == 0:
            self.terms = {}
        else:
            for n in self.given:
                new = {n[1]:n[0] for n in self.given}
            self.terms = new
        
        for power,coeff in self.terms.items():
            if type(coeff) not in (int,float):
                raise AssertionError('coefficient must be an int or float value')
            if type(power) not in (int,float):
                raise AssertionError('power must be an int or float value')
            if power < 0:
                raise AssertionError('power must be greater than or equal to 0')
            if coeff == 0:
                pass
#         print(self.terms, 'poo')
            

        
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
        return 'Poly{}'.format(self.given)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
            
    
    def __call__(self,arg):
        eq = str(self)
        new = eq.replace('x',('*'+str(arg)))
        new2 = new.replace('^', '**')
        return eval(str(new2))
    

    def __iter__(self):
        #return something iterable
        for power,coeff in self.terms.items():
            reversed = {coeff:power for power,coeff in self.terms.items()}
            return sorted(reversed)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError(index, 'is not an integer')
        if index < 0:
            raise TypeError(index, 'is less than zero')
        if index not in self.terms.keys():
            return 0
        else:
            for power,coeff in self.terms.items():
                if index == power:
                    return coeff
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError(index, 'is not an integer')
        if index < 0:
            raise TypeError(index, 'is less than zero')
        if value == 0:
            del self.terms[value]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError(index, 'is not an integer')
        if index < 0:
            raise TypeError(index, 'is less than zero')
        else:
            for power,coeff in self.terms.items():
                if index == power:
                    del self.terms[coeff]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError(c,'is not an int or float')
        if type(p) != int:
            raise TypeError(p, 'is not an integer')
        if p < 0:
            raise TypeError(p, 'is less than zero')
        else:
            if p not in self.terms.keys() and p != 0:
                self.terms[p] = c
            for power,coeff in self.terms.items():
                if p == power:
                    item = self.terms[p]
                    self.terms[p] = c+coeff
#             if p in self.terms.keys():
#                 item = self.terms[p]
#                 self.terms[p] = c+
            
        
       

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('type',type(right),'is not supported')
        empty = self.terms.copy()
        if type(right) == Poly:
            pass
        if type(right) in (int,float):
            for power,coeff in empty.items():
                if power == 1:
                    empty[power] = coeff + right
                    

            
        

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('type',type(right),'is not supported')
        empty = self.terms.copy()
        if type(right) == Poly:
            pass
        if type(right) in (int,float):
            for power,coeff in empty.items():
                if power == 1:
                    empty[power] = coeff * right
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('operand type not supported')
        if type(right) == Poly:
            for power,coeff in self.terms.items():
                for p,c in right.items():
                    if power == p:
                        if coeff == c:
                            return True
                        else:
                            return False
        if type(right) in (int,float):
            if self.terms == right:
                return True
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
#     print('  list collecting iterator results:',[t for t in p])
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