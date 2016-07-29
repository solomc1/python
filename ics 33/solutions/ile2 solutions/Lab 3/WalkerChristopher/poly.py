class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            assert type(x[0]) is int or type(x[0]) is float, 'Poly.__init__: illegal coefficient in : {}'.format(str(x))
            assert type(x[1]) is int or type(x[1]) is float and term[1] >= 0, 'Poly.__init__: illegal power in : {}'.format(str(x))
            if x[0] != 0:
                self.terms.update({x[1]:x[0]})

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
        string = 'Poly('
        for x in self.terms:
            string += '({},{})'.format(self.terms[x], x)
        string += ')'
        return string

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms)
    
    def __call__(self,arg):
        value = 0
        for x in self.terms:
            value += self.terms[x]*(arg**x)
        return value
    

    def __iter__(self):
        itr_l = []
        for x in self.terms:
            itr_l.append((self.terms[x], x))
        itr_l.sort(key=lambda x : x[1], reverse=True)
        itr = iter(itr_l)
        return itr
            
    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: illegal power : {}'.format(str(index)))
        else:
            if index == 0:
                return 0
            else:
                return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: illegal power : {}'.format(str(index)))
        elif type(value) is not int:
            raise TypeError('Poly.__setitem__: illegal coefficient : {}'.format(str(index)))
        else:
            if value == 0:
                self.terms.pop(index)
            else:
                self.terms.update({index:value})

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: illegal power : {}'.format(str(index)))
        else:
            if index in self.terms.items():
                self.terms.pop(index)

    def _add_term(self,c,p):
        if type(p) is not int and type(p) is not float or p < 0:
            raise TypeError('Poly._add_term: illegal power : {}'.format(str(p)))
        elif type(c) is not int and type(c) is not float:
            raise TypeError('Poly._add_term: illegal coefficient : {}'.format(str(c)))
        else:
            if p not in self.terms.items():
                self.terms.update({p:c})
            elif c != 0:
                new_c = c + self.terms[p]
                if new_c == 0:
                    self.terms.pop(p)
                else:
                    self.terms.update({p:new_c})

    @staticmethod
    def convert(c):
        return Poly((c, 0))
    
    def __add__(self,right):
        if type(right) is not Poly and type(right) is not int and type(right) is not float:
            raise TypeError('Poly.__add__: unsupported type for + : Poly and {}'.format(type(right)))
        else:
            if type(right) is int or type(right) is float: 
                t = self.convert(right)
            else:
                t = right
            ret_poly = Poly()
            for x in t:
                ret_poly._add_term(x[0], x[1])
            for y in self:
                ret_poly._add_term(y[0], y[1])
            return ret_poly
    
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