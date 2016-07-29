class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:        
            if type(term[0]) != int and type(term[0]) != float:
                raise AssertionError('Illegal coefficient: The coefficient '+str(term[0])+' must be an int or float value.')
            elif type(term[1]) != int or term[1] < 0:
                raise AssertionError('Illegal power: The power '+str(term[1])+' must be an int whose value is >= 0.')
            elif term[1] in self.terms:
                raise AssertionError('Illegal power: The power '+str(term[1])+' appeared as an earlier term.')
            elif term[0] != 0:
                self.terms[term[1]] = term[0]
        
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
        term = ''
        for p, c in self.terms.items():
            term += '({},{}),'.format(c,p)
        return ('Poly('+ term[:-1] +')')
    
    def __len__(self):
        high = 0
        for i in self.terms:
            if i > high:
                high = i
        return high
    
    def __call__(self,arg):
        result = 0
        for p, c in self.terms.items():
            result += c*(arg**p)
        return result

    def __iter__(self):
        for p in sorted(self.terms, reverse=True):
            yield (self.terms[p], p)

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Illegal index: must be an int and >= 0.')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            
    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Illegal power: must be an int and >= 0')
        if value == 0 and index in self.terms:
            del self.terms[index]
        elif value != 0:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Illegal power: must be an int and >= 0')
        elif index in self.terms:
            del self.terms[index]
            
    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Illegal power: must be an int and >= 0')
        elif type(c) != int and type(c) != float:
            raise TypeError('Illegal coefficient: must be int or float')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms and self.terms[p]+c != 0:
                self.terms[p] = self.terms[p]+c

    def __add__(self,right):
        poly = self
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Illegal type: must be a Polynomial, a integer, or a float')
        elif type(right) == Poly:
            for p,c in right.terms.items():
                if p in self.terms:
                    poly._add_term(c, p)
                else:
                    poly._add_term(c, p)
        elif type(right) == int or type(right) == float:
            poly._add_term(self.terms[0], 0)
        return poly
                    
    
    def __radd__(self,left):
        poly = self
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError('Illegal type: must be a Polynomial, a integer, or a float')
        elif type(left) == Poly:
            for p,c in left.terms.items():
                if p in self.terms:
                    poly._add_term(c, p)
                else:
                    poly._add_term(c, p)
        elif type(left) == int or type(left) == float:
            poly._add_term(self.terms[0], 0)
        return poly
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Illegal type: must be a Polynomial, a integer, or a float')
        elif type(right) == Poly:
            if self.terms.keys == right.terms.keys:
                flag = False
                for k in self.terms:
                    flag = True if self.terms[k] == right.terms[k] else False
                return flag
            else:
                return False
        elif type(right) == int or type(right) == float:
            if len(list(self.terms.keys())) == 1:
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