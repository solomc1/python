class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            coeff = i[0]
            pwr = i[1]
            assert (type(coeff)==int or type(coeff)==float), ''
            assert (type(pwr) == int and pwr>=0), ''
            if coeff != 0:
                if (pwr in self.terms.keys()):
                    if ((self.terms[pwr] >0 and coeff <0) or (self.terms[pwr])<0 and coeff>0):
                        self.terms[pwr] = coeff
                    else:
                        raise AssertionError('')
                elif pwr not in self.terms.keys():
                    self.terms[pwr] = coeff
        
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
        result = 'Poly('
        for k in self.terms:
            result += '({},{})'.format(self.terms[k],k)
        result += ')'
        return result

    
    def __len__(self):
        pwrs = list(self.terms.keys())
        if pwrs == []:
            return 0
        else:
            return max(pwrs)
    
    def __call__(self,arg):
        assert isinstance(arg, int) or isinstance(arg, float), ''
        sum = 0
        for k,v in self.terms.items():
            sum += v*(arg**k)
        return sum
    

    def __iter__(self):
        t = self.terms.items()
        for i in sorted(t, reverse = True):
            yield i[1],i[0]
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError('')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if index <0 or type(index)!=int:
            raise TypeError('')
        self.terms[index] = value
        if value == 0:
            self.terms.pop(index)

            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('')
        elif index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            result = self.terms[p] + c
            if result != 0:
                self.terms[p] = result
            else:
                self.terms.pop(p)
        
        
       

    def __add__(self,right):
        result = 'Poly('
        if type(right) == Poly:
            new = Poly()
            for k in self.terms:
                new._add_term(self.terms[k],k)
            for k, v in right.terms.items():
                new._add_term(v,k)
            return new
        elif type(right) == int or type(right) == float:
            return Poly((right,0)) + self
        else:
            raise TypeError('')

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) == int or type(right) == float:
            return Poly((right,0))*self
        elif type(right) == Poly:
            new = Poly()
            values = dict(self.terms.items())
            add_to_v = {}
            for k,v in right.terms.items():
                for key, val in values.items():
                    c = v*val
                    p = k+key
                    if p in add_to_v.keys():
                        add_to_v[p] += c
                    else:
                        add_to_v[p] = c
            for k,v in add_to_v.items():
                new._add_term(v,k)
            return new
        else:
            raise TypeError('')
        pass

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            for k in self.terms:
                if k not in right.terms:
                    return False
                elif self.terms[k] != right.terms[k]:
                    return False
            for k in right.terms:
                if k not in self.terms:
                    return False
                elif self.terms[k] != right.terms[k]:
                    return False
            return True
            
        elif type(right) == int or type(right) == float:
            k = list(self.terms.keys())
            if len(k) ==1 and k[0] == 0:
                if self.terms[k[0]] == right:
                    return True
            else:
                return False
        else:
            raise TypeError('')

    
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