class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x,y in terms:
            if type(x) not in (int,float):
                raise AssertionError('Coefficient must be either int or float')
            elif type(y) != int:
                raise AssertionError('Power must be of type int')
            else:
                if x  == 0:
                    pass
                elif y in self.terms:
                    raise AssertionError("Can't have the same power twice")
                elif y == 0:
                    self.terms[0] = x
                elif y <0:
                    raise AssertionError('Power must be greater than or equal to zero')
                else:
                    self.terms[y] = x     
                            
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
        reprstr = ''
        items = self.terms.items()
        for x in items:
            reprstr += str(x)
        return 'Poly({})'.format(reprstr)

    
    def __len__(self):
        highest = 0
        if self.terms == {}:
            return highest
        else:
            for x in self.terms:
                if x > highest:
                    highest = x
            return highest
                
    
    def __call__(self,arg):
        final = 0
        for power in self.terms:
            if power == 0:
                final += self.terms[power]
            else:
                final += (arg**power)*self.terms[power]
        return final
    

    def __iter__(self):
        y = []
        items = self.terms.items()
        for x in items:
            y.append(x)
        return iter(self.terms)
            
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Index must be int')
        elif index < 0:
            raise TypeError('Index must be zero or greater')
        else:
            if index in self.terms:
                return self.terms[index]
            else:
                return 0
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Power must be int')
        elif index < 0:
            raise TypeError('Power must be zero or greater')
        elif value == 0:
            if index in self.terms:
                self.terms.pop(index)
            else:
                pass
        else:
            self.terms[index] = value     

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Power must be int')
        elif index < 0:
            raise TypeError('Power must be zero or greater')
        else:
            if index in self.terms:
                self.terms.pop(index)
            else:
                pass
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('coefficient must be either int or float')
        elif type(p) != int:
            raise TypeError('power must be int')
        elif p < 0:
            raise TypeError('Power must be zero or greater')
        else:
            if p not in self.terms and p != 0:
                self.terms[p] = c
            elif p in self.terms:
                new = c + self.terms[p]
                if new == 0:
                    self.terms.pop(p)
                else:
                    self.terms[p] = new
       

    def __add__(self,right):
        if type(right) == Poly:
            final = ''
            if len(self) > len(right):
                higher = self
            else:
                higher = right
            for x in higher.terms:
                final += str((self.terms[x] +right.terms[x],x))
            return final
        elif type(right) == int:
            pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms.items() == right.terms.items()
        elif type(right) not in (int,float):
            raise TypeError('cant compare to {} object'.format(type(right)))

    
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