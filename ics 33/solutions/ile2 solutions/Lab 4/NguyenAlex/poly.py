class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for each in terms:
            if type(each[0]) not in (int, float) or type(each[1]) != int or each[1] < 0:
                raise AssertionError('Poly.__init__: illegal power in : {}'.format(each))
            if each[1] in self.terms.values():
                raise AssertionError('Poly.__init__: power occurs more than once as an argument')
            self.terms[each[1]] = each[0]
    
        
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
        return 'Poly(' + ''.join('{}'.format((x[1], x[0]) for x in self.terms.items())) + ')'

    
    def __len__(self):
        return max(self.terms.keys()) if len(self.terms) != 0 else 0


    
    def __call__(self,arg):
        if arg not in (int,float):
            raise AssertionError('Poly.__call__: argument {} must be an int or float'.format(arg))
        else:
            total = 0
            for each in self.terms.keys():
                total += self.terms[each] * (arg**each)
        return total
    

    def __iter__(self):
        i = iter(sorted(self.terms.items(), key = self.terms.keys(), reverse = True))
        while True:
            try:
                x = next(i)
                yield (x[1], x[0])
            except StopIteration:
                break
        
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: {} must be an int greater than or equal to 0'.format(index))
        else:
            return self.terms[index] if index in self.terms.keys() else 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: {} has to be an int greater than or equal to 0'.format(index))
        elif value == 0:
            for each in self.terms.keys():
                if self.terms[each] == value:
                    self.terms.popitem(each, value)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError('Poly.__delitem__: {} has to be an int greater than or equal to 0'.format(index))
        if index in self.terms.keys():
            self.terms.popitem(index, self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int or p < 0:
            raise TypeError('Poly._add_term: illegal entry in {} or {}'.format(c,p))
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        else:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                self.terms.popitem(p, self.terms[p])
                        
       

    def __add__(self,right):
        if type(right) is Poly:
            new_P = Poly((x[1], x[0]) for x in self.terms.items())
            for each in right.terms.items():
                new_P._add_term(each[0], each[1])
            return new_P
        elif type(right) in (int, float):
            new_P = Poly((x[1], x[0]) for x in self.terms.items())
            new_P._add_term(right, 0)
            return new_P
        else:
            raise TypeError('Poly.__add__: type({}) is not an int, float, or Poly'.format(right))
            

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return sorted(self.terms) == sorted(right.terms)
        elif type(right) in (int, float):
            if len(self.terms) == 1 and 0 in self.terms.keys():
                return self.terms[0] == right
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