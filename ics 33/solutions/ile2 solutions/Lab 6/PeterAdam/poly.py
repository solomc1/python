class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            if type(term[0]) not in (int, float) or type(term[1]) != int or term[1] < 0:
                raise AssertionError('__init__: Coefficients must be an int or float and power must be a positive or zero int.')
            if term[1] in self.terms.keys():
                raise AssertionError('__init__: A power is defined twice.')
            elif term[0] != 0:
                self.terms[term[1]] = term[0]
            
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
        if self.terms == {}:
            return 'Poly()'
        else:
            reprstr = 'Poly('
            for term in self.terms:
                reprstr += '({},{}), '.format(self.terms[term], term)
            reprstr = reprstr[:-2] + ')'
            return reprstr

    
    def __len__(self):
        if self.terms == {}: return 0
        else: return sorted(list(self.terms.keys()))[-1]
    
    def __call__(self,arg):
        sum = 0
        for term in self.terms:
            sum += self.terms[term]*(arg**term)
        return sum
    

    def __iter__(self):
        for term in sorted(list(self.terms.keys()), reverse = True):
            yield (self.terms[term], term)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('__getitem__: Index must be a positive or zero integer.')
        if index not in self.terms.keys(): return 0
        else: return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0: raise TypeError('__setitem__: Index must be a positive or zero integer.')
        elif type(value) not in (int, float): raise TypeError('__setitem__: Value must be an int or a float.')
        elif value == 0 and index in self.terms.keys(): del self.terms[index]
        elif value != 0: self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('__delitem__: Index must be a positive or zero integer.')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0: raise TypeError('_add_term: p must be a positive or zero integer.')
        elif type(c) not in (int, float): raise TypeError('_add_term: c must be an int or a float.')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        else:
            if p not in self.terms.keys() and c == 0: return
            elif self.terms[p] + c == 0:
                del self.terms[p]
            else: self.terms[p] = self.terms[p] + c
            
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('__add__: right should be an int, float, or Polynomial.')
        newpoly = eval(self.__repr__())
        if type(right) in (int, float):
            newpoly._add_term(right, 0)
        else:
            for term in right.terms:
                newpoly._add_term(right.terms[term], term)
        return newpoly

    
    def __radd__(self,left):
        if type(left) not in (int, float):
            raise TypeError('__radd__: left should be an int or a float.')
        newpoly = eval(self.__repr__())
        newpoly._add_term(left, 0)
        return newpoly
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('__mul__: right should be an int, float, or Polynomial.')
        newpoly = Poly()
        if type(right) in (int, float):
            newpoly = eval(self.__repr__())
            for term in newpoly.terms:
                newpoly.terms[term] = right*newpoly.terms[term]
        else:
            for term in self.terms:
                for rterm in right.terms:
                    newpoly._add_term(self.terms[term]*right.terms[rterm], term + rterm)
        return newpoly
    

    def __rmul__(self,left):
        if type(left) not in (int, float):
            raise TypeError('__rmul__: left should be an int or a float.')
        newpoly = eval(self.__repr__())
        for term in newpoly.terms:
            newpoly.terms[term] = left*newpoly.terms[term]
        return newpoly
    
    def __eq__(self,right):
        if type(right) not in (Poly, int, float) or type(self) not in (Poly, int, float): 
            raise TypeError('__eq__: right and left arguments must be a Poly, int, or float.')
        if type(right) in (int, float):
            return list(self.terms.keys()) == [0] and self.terms[list(self.terms.keys())[0]] == right
        else:
            try:
                for term in sorted(list(self.terms.keys())):
                    if self.terms[term] != right.terms[term]\
                     or sorted(list(right.terms.keys()))[sorted(list(self.terms.keys())).index(term)] != term:
                        return False
                return True
            except:
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
#      
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()