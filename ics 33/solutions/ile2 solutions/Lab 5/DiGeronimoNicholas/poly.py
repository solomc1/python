class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for coeff, power in terms:
            if type(coeff) == int or type(coeff) == float:
                pass
            else:
                raise AssertionError('The coeffecient must be a float or int')
            if type(power) != int or power < 0:
                raise AssertionError('Must be int >= 0')
            if power in self.terms:
                if coeff != 0:
                    raise AssertionError('A power value appears more than once.')
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
        mesh = '('
        for key, value in self.terms.items():
            mesh += str(((value,key))) + ','
        mesh = mesh[:-1]
        mesh += ')'
        return 'Poly' + mesh
    
    def __len__(self):
        if self.terms == {}:
            return 0
        return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        total = 0
        if type(arg) == int or type(arg) == float:
            for power, coeff in self.terms.items():
                total += coeff*(arg**power)
        return total

    def __iter__(self):
        lst = []
        for power, coeff in self.terms.items():
            lst.append((coeff,power))
        return iter(sorted(lst, reverse = True))
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('power must be an int >= 0')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('power must be an int >= 0')
        if value == 0:
            for power, coeff in self.terms.items():
                if coeff == 0:
                    del self.terms[power]
                

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('power must be an int >= 0')
        if index in self.terms:
            del self.terms[index]
                
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    
    print('------nick tests-----')
    

    
    print('-----nick tests----')
    
    
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