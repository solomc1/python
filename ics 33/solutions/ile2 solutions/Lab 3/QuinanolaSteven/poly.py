class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for k,v in terms:
            assert v not in self.terms.keys(), 'Multiples of powers not accepted'
            assert type(k) in [int, float], 'Coefficients must be of types int or float'
            assert type(v) == int and v >= 0, 'Powers must be int values greater than or equal to zero'
            if k != 0:
                self.terms[v] = k
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
        strs = ''
        for k in self.terms.keys():
            strs = strs +'({},{}),'.format(self.terms[k],k)
        fin = strs[:-1]
        return 'Poly('+fin+')'

    
    def __len__(self):
        x = 0
        try:
            for v in self.terms.keys():
                if v > x:
                    x = v
        except:
            pass
        finally:
            return x
            
    
    def __call__(self,arg):
        total = 0
        for k in self.terms:
            fluff = self.terms[k]*(arg**k)
            total += fluff
        return total
    

    def __iter__(self):
        ran = [x for x in self.terms.keys()]
        ran.sort(reverse = True)
        for item in ran:
            yield (self.terms[item],item)   
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Powers must be int and >= 0')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Powers must be int and >= 0')
        elif value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)    
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Powers must be int and >= 0')
        elif index not in self.terms.keys():
            pass
        else:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in [int, float] or type(p) != int or p < 0:
            raise TypeError('Invalid coefficient or power')
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            new = self.terms[p] + c
            if new == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = new
       

    def __add__(self,right):
        new = Poly()
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly can only add with Poly, int, or float')
        elif type(right) == Poly:
            for powa in self.terms.keys():
                new._add_term(self.terms[powa], powa)
                if powa in right.terms.keys():
                    new._add_term(right.terms[powa],powa)
            for powa in right.terms.keys():
                if powa not in new.terms.keys():
                    new._add_term(right.terms[powa],powa)
        else:
            for powa in self.terms.keys():
                new._add_term(self.terms[powa],powa)
            new._add_term(right,0)
        return new

    
    def __radd__(self,left):
        new = Poly()
        if type(left) not in [Poly, int, float]:
            raise TypeError('Poly can only add with Poly, int, or float')
        elif type(left) == Poly:
            for powa in self.terms.keys():
                new._add_term(self.terms[powa], powa)
                if powa in left.terms.keys():
                    new._add_term(left.terms[powa],powa)
            for powa in left.terms.keys():
                if powa not in new.terms.keys():
                    new._add_term(left.terms[powa],powa)
        else:
            for powa in self.terms.keys():
                new._add_term(self.terms[powa],powa)
            new._add_term(left,0)
        return new
    

    def __mul__(self,right):
        new = Poly()
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly can only add with Poly, int, or float')
        elif type(right) == Poly:
            for powa1 in self.terms.keys():
                for powa2 in right.terms.keys():
                    new._add_term(right.terms[powa2]*self.terms[powa1],powa2+powa1)
        else:
            for powa in self.terms.keys():
                new._add_term(self.terms[powa]*right, powa)
        return new
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        x = True
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly can only add with Poly, int, or float')
        elif type(right) == Poly:
            for powa in right.terms.keys():
                if powa not in self.terms.keys():
                    return False
                else:
                    if right.terms[powa] != self.terms[powa]:
                        x = False
                    else:
                        pass
        else:
            if self.__len__() > 0:
                x = False
            else:
                if self.terms[0] == right:
                    pass
        return x

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    P = Poly( (3,2), (-2,1), (4,0) )
    print(P.__repr__())
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