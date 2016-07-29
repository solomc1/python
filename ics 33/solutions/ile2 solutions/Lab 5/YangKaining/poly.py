class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) in [int,float]; "Each coefficient should be an int or float."
            assert type(i[1]) == int and i[1] >=0; "Power should be int and >= 0."
            if i[1] not in self.terms:
                if i[0] != 0:
                    self.terms[i[1]] = i[0]
            elif i[0] != self.terms[i[1]]:
                raise AssertionError('cannot specify an items for twice')
        
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
        return "Poly(" + (','.join([str((k,v)) for k, v in self.terms.items()])) + ')'

    
    def __len__(self):
        if self.terms != {}:
            return max(self.terms)
        else:
            return 0
    
    def __call__(self,arg):
        sum = 0
        for i in self.terms:
            sum += (arg ** i) * self.terms[i]
        return sum
    

    def __iter__(self):
        for i in sorted(self.terms, reverse = True):
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Wrong Index!')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Wrong Index!')
        elif value == 0 and index in self.terms:
            del self.terms[index]
        elif value != 0:
            self.terms[index] = value 
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Wrong Index!')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Wrong Index!')
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms and c != 0:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        
    def __add__(self,right):
        result = Poly()
        for i in self.terms:
            result._add_term(self.terms[i],i)
        if type(right) == Poly:
            for i in right.terms:
                result._add_term(right.terms[i], i)
            return str(result)
        elif type(right) in [int, float]:
            result._add_term(right,0)
            return str(result)
        else:
            raise TypeError('Wrong Type!')
        
    def __radd__(self,left):
        return self. __add__(left)
    

    def __mul__(self,right):
        result = Poly()
        i = iter(self)
        if type(right) == Poly:
            x = iter(right)
            while True:
                try: 
                    a = next(i)
                    while True:
                        try:
                            b = next(x)
                            result._add_term(a[0]*b[0], a[1]+b[1])
                        except:
                            break
                except:
                    break
            return str(result)
        elif type(right) in [int, float]:
            while True:
                try:
                    a = next(i)
                    result._add_term(a[0] * right, a[1])
                except:
                    break
            return str(result)
        else:
            raise TypeError('Wrong Type!')
                    
                    
    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            return {t for t in iter(self)} == {t for t in iter(right)}
        elif type(right) in [int, float]:
            if len(self.terms) == 1 and 0 in self.terms:
                return right == self.terms[0]
            return False
        else:
            raise TypeError('Wrong Type!')
                

    
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