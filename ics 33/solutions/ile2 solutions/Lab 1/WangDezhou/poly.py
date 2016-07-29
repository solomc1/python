class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        polypower = []
        for term in terms:
            assert type(term[0]) in [int,float], "coefficent not numeric: '{}'".format(term[0])
            assert type(term[1]) in [int,float], "power not numeric: '{}'".format(term[1])
            assert type(term[1]) == int, "power not int: '{}'".format(term[1])
            assert term[1] >= 0, "power negative: '{}'".format(term[1])
            assert term[1] not in polypower, "power repeated"
            if term[0] != 0:
                polypower.append(term[1])
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
        return 'Poly('+','.join(' ({},{})'.format(c,p) for p,c in sorted(self.terms.items(),reverse=True))+')'

    
    def __len__(self):
        polylen = 0
        for p in self.terms.keys():
            if p > polylen:
                polylen = p
        return polylen
    
    def __call__(self,arg):
        polyanswer = 0
        for p,c in sorted(self.terms.items(),reverse = True):
            polyanswer += c*(arg**p)
        return polyanswer
    

    def __iter__(self):
        polylist = [(c,p) for p,c in sorted(self.terms.items(),reverse = True)]
        for item in polylist:
            yield item
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            return self.terms[index] if index in self.terms.keys() else 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            self.terms[index] = value
            if value == 0:
                self.terms.pop(index)
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            try:
                self.terms.pop(index)
            except:
                pass
            

    def _add_term(self,c,p):
        assert type(c) in [int,float], "coefficent not numeric: '{}'".format(c)
        assert type(p) in [int,float], "power not numeric: '{}'".format(p)
        assert type(p) == int, "power not int: '{}'".format(p)
        assert p >= 0, "power negative: '{}'".format(p)
        if c != 0:
            if p in self.terms.keys():
                self.terms[p] += c
                if self.terms[p] == 0:
                    self.terms.pop(p)
            else:
                self.terms[p] = c

       

    def __add__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError
        elif type(right) == Poly:
            newPoly = Poly()
            for power in range(max(len(self),len(right))+1):
                newPoly._add_term(self[power]+right[power],power)
            return newPoly
        else:
            self.terms[0] += right
            if self.terms[0] == 0:
                self.terms.pop(0)
            return self

    
    def __radd__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError
        elif type(left) == Poly:
            newPoly = Poly()
            for power in range(max(len(self),len(left))+1):
                newPoly._add_term(self[power]+left[power],power)
            return newPoly
        else:
            self.terms[0] += left
            if self.terms[0] == 0:
                self.terms.pop(0)
            return self

    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError
        elif type(right) == Poly:
            newPoly = Poly()
            for spower, scoef in sorted(self.terms.items(),reverse=True):
                for rpower, rcoef in sorted(right.terms.items(),reverse=True):
                    newPoly += Poly((scoef*rcoef,spower+rpower))
            return newPoly
        else:
            for power in sorted(self.terms.keys(),reverse=True):
                self.terms[power] *= right
            return self
    

    def __rmul__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError
        elif type(left) == Poly:
            newPoly = Poly()
            for spower, scoef in sorted(self.terms.items(),reverse=True):
                for lpower, lcoef in sorted(left.terms.items(),reverse=True):
                    newPoly += Poly((scoef*lcoef,spower+lpower))
            return newPoly
        else:
            for power in sorted(self.terms.keys(),reverse=True):
                self.terms[power] *= left
            return self

    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError("Unexpected type to compare Poly and: '{}'".format(type(right)))
        elif type(right) == Poly:
            for power in range(max(len(self),len(right))+1):
                if self[power] != right[power]:
                    return False
            return True
        else:
            try:
                if self[0] == right and len(self) == 0:
                    return True
                else:
                    return False
            except:
                return True if right == 0 else False

    
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