class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for eachterm in terms:
            if not type(eachterm[0]) in (int,float) or type(eachterm[1]) != int or eachterm[1] < 0:
                raise AssertionError('The term is either not an int or float whose value is >= 0')
            
            if eachterm[0] == 0:
                pass
            elif eachterm[1] in self.terms.keys():
                raise AssertionError('The term has repeating powers which is not allowed')
            else:
                self.terms.update({eachterm[1]: eachterm[0]})
            
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
        s = 'Poly('
        for eachterm in self.terms.keys():
            s += '(' + str(self.terms[eachterm]) + ',' + str(eachterm) + '),'
        return s[:-1] + ')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        y = [x for x in self.terms.keys()]
        return max(y)
    
    def __call__(self,arg):
        val = 0
        if type(arg) in (float,int):
            for eachterm in self.terms:
                val += self.terms[eachterm] * (arg**eachterm)
            return val

    def __iter__(self):
        for eachterm in sorted(self.terms, reverse = True):
            yield (self.terms[eachterm], eachterm)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The index must be > 0 and an int')
        
        for eachterm in self.terms:
            if index == eachterm:
                return self.terms[eachterm]
        return 0

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('The index must be > 0 and an int')
        elif value != 0:
            self.terms.update({index: value})
        elif value == 0 and index in self.terms:
            self.terms.pop(index)
        
        
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The index must be > 0 and an int')
        elif index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if not type(c) in (int,float) or type(p) != int:
            raise TypeError('The coefficient must be numeric and the power must be an integer.')
        if c != 0 and not p in self.terms:
            self.terms.update({p: c})
        elif p in self.terms:
            num = self.terms[p] + c
            self.terms.pop(p)
            self.terms.update({p : num})
        
        newterm = {}
        for eachterm in self.terms:
            if self.terms[eachterm] != 0:
                newterm.update({eachterm : self.terms[eachterm]})
        
        self.terms = newterm
        
        
    def __add__(self,right):
        if not type(right) in (Poly, int, float):
            raise TypeError('Adding requires a Poly, int, or a float')
        if type(right) in (int, float):
            l = eval(self.__repr__())
            l._add_term(right,0)
            return l
        if type(right) == Poly:
            l = eval(self.__repr__())
            for eachterm in right.terms:
                l._add_term(right.terms[eachterm],eachterm)
            return l
        
    def __radd__(self,left):
        if not type(left) in (int, float):
            raise TypeError('Adding a polynomial on the right side requires a int or a float')
        l = eval(self.__repr__())
        l._add_term(left,0)
        return l


    def __mul__(self,right):
        l = Poly()
        if not type(right) in (Poly, int, float):
            raise TypeError('Multiplication requires a Poly, int, or a float')
        if type(right) in (int,float):
            for eachterm in self.terms:
                l._add_term(self.terms[eachterm] * right, eachterm)
            return l
        if type(right) == Poly:
            for eachterm in self.terms:
                for eachterm2 in right.terms:
                    l._add_term(self.terms[eachterm] * right.terms[eachterm2], eachterm + eachterm2)
            return l
        
    def __rmul__(self,left):
        if not type(left) in (int, float):
            raise TypeError('Multiplication on the right side requires a int or a float')
        l = Poly()
        for eachterm in self.terms:
            l._add_term(self.terms[eachterm] * left, eachterm)
        return l

    def __eq__(self,right):
        if not type(right) in (Poly, int, float):
            raise TypeError('Comparing with equals requires a Poly, int, or a float')
        if type(right) in (int,float):
            if right == self.__call__(right):
                return True
            return False
        if type(right) == Poly:
            if self.terms == right.terms:
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