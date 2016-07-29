class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            if term[0] != 0:
                if type(term[0]) == int or type(term[0]) == float:
                    if type(term[1]) == int:
                        if term[1]>=0:
                            if term[1] in self.terms.keys():
                                raise AssertionError('A duplicate power was defined in the parameters.')
                            else:
                                self.terms.update({term[1]:term[0]})
                        else:
                            raise AssertionError('Poly.__init: illegal power in', (term[0], term[1]))
                    else:
                        raise AssertionError('Poly.__init__: illegal power in,'(term[0], term[1]))
                else:
                    raise AssertionError('Poly.__init__: illegal coefficient in', (term[0],term[1]))
                    
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
        for key, value in self.terms.items():
            result += '('+str(value)+', '+str(key)+'), '
        return result[:-2]+')' if self.terms != {} else 'Poly()'

    def __len__(self):
        return max(self.terms.keys()) if self.terms != {} else 0
        
    def __call__(self,arg):
        result = 0
        for key, value in self.terms.items():
            result+= value*pow(arg,key)
        return result
    
    def __iter__(self):
        for key, value in list(self.terms.items()):
            yield (value, key) 
        
    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Index is not an integer or is less than 0.')
        else:
            return self.terms[index] if index in self.terms else 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError('Index is not an integer or is less than 0.')
        else:
            if value == 0:
                if index in self.terms:
                    self.terms.pop(index)
            else:
                self.terms[index] = value
                
    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Index is not an integer or is less than 0.')
        elif index not in self.terms:
            pass
        else:
            self.terms.pop(index)
                 
    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Coefficient is not an integer or a float.')
        elif type(p) != int and p<0:
            raise TypeError('Power is not an integer or is less than 0.')
        else:
            if p in self.terms:
                newcoef = self.terms[p]+c
                if newcoef != 0:
                    self.terms.update({p:newcoef})
                else:
                    self.terms.pop(p)
            else:
                if c != 0:
                    self.terms[p] = c
                
    def __add__(self,right):
        result = Poly()
        for key, value in self.terms.items():
            result._add_term(value, key)
        if type(right)==Poly:
            for key, value in right.terms.items():
                result._add_term(value, key)
            return result
        elif type(right) == int or type(right)== float:
            result._add_term(right, 0)
            return result
        else:
            raise TypeError('Incorrect type '+type(right)+'for operand "+".')
        
    def __radd__(self,left):
        return self.__add__(left)

    def __mul__(self,right):
        result = Poly()
        for key, value in self.terms.items():
            result._add_term(value,key)
        if type(right)== Poly:
            for key,value in right.terms.items():
                pass
    
    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            for key, value in self.terms.items():
                if key in right.terms and right[key] == value:
                    pass
                else:
                    return False
            return True
        
        elif type(right) == int or type(right) == float:
            return self == Poly((right, 0))
        
        else:
            raise TypeError('Incorrect type '+type(right)+' for operand "=".')

    
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