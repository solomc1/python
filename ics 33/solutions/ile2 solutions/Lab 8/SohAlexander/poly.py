class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c, p in terms:
            if type(c) not in (int,float):
                raise AssertionError
            if type(p) != int:
                raise AssertionError
            if p < 0:
                raise AssertionError
            if p in self.terms and self.terms[p] != 0:
                raise AssertionError
            else:
                if c != 0:
                    self.terms[p] = c

                
        
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
        if len(self.terms) == 0:
            return 'Poly()'
        string = 'Poly('
        for p,c in self.terms.items():
            string += '(' + str(p) +',' + str(c) +')' +','
        string = string[:-1]
        string += ')'
        return string
    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        max = 0
        for p in self.terms.keys():
            if p > max:
                max = p
        return p
    
    def __call__(self,arg):
        return sum(self.terms[p] * arg ** p for p in self.terms)
    

    def __iter__(self):
        for p,c in sorted(list(self.terms.items()), key = lambda x: self.terms.items()):
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError
        elif index in self.terms:
            if value == 0:
                del self.terms[index]
            if self.terms[index] == 0:
                del self.terms[index]
            self.terms[index] = value
        else:
            if value != 0:
                self.terms[index] = value
            
        
        


    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError
        elif index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if p in self.terms:
            sum = c + self.terms[p]
            if sum == 0:
                del self.terms[p]
            self.terms[p] = sum
        elif p not in self.terms and c != 0:
            self.terms[p] = c
            

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError
        if type(right) is Poly:
            Poly._add_term(self,right,0)
        else:
            pass
            

    
    def __radd__(self,left):
        Poly._add_term(self,left,0)
        return self
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if right not in (int,float,Poly):
            raise TypeError
        if type(right) is Poly:
            x = self.terms.items()
            y = right.terms.items()
        elif type(right) in (int,float):
            if right in self.terms.values():
                return True
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