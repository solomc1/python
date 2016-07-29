class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert type(t[0]) in (int, float),'coefficient attribute is not a numeric value'
            assert type(t[1]) is int,'power attribute is not a int value'
            assert t[1] >= 0
            if t[0] != 0:
                assert t[1] not in self.terms,'power '+t[1]+' is already in the terms'
                self.terms[t[1]] = t[0]
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
        return 'Poly('+','.join('(' + str(c)+','+str(p)+')' for p,c in self.terms.items())+')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) in (int, float),'argument is not numeric value'
        sum = 0
        for p,c in self.terms.items():
            sum += c*(arg**p)
        return sum
    

    def __iter__(self):
        terms = sorted(self.terms.items(),key=(lambda x:x[0]),reverse=True)
        for i in terms:
            yield (i[1],i[0])

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Power is not int value')
        if index < 0:
            raise TypeError('Power is lower than 0')
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Power is not int value')
        if index < 0:
            raise TypeError('Power is lower than 0')
        if type(value) not in (int,float):
            raise TypeError('Coefficient is not numeric value')
        if value == 0:
            del self[index]
        else:
            self.terms[index] = value
        

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Power is not int value')
        if index < 0:
            raise TypeError('Power is lower than 0')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('coefficient attribute is not a numeric value')
        if type(p) != int:
            raise TypeError('power attribute is not a int value')
        if p <0:
            raise TypeError('Power is lower than 0')
        if c != 0:
            if p in self.terms:
                self.__setitem__(p,c+self.terms[p])
            else:
                self.terms[p] = c
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('right is not a legal opperand')
        new = Poly()
        for p,c in self.terms.items():
            new._add_term(c, p)
        if type(right) == Poly:
            for p,c in right.terms.items():
                new._add_term(c,p)
        else:
            new._add_term(right,0)
        return new

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('right is not a legal opperand')
        new = Poly()
        if type(right) == int:
            for p,c in self.terms.items():
                    new._add_term(c, p)
            for i in new.terms:
                new.__setitem__(i, new.terms[i]*right)
        else:
            pass
#              t =[]
#              for p1,c1 in right.terms.items():
#                  _temp = Poly()
#                  for p2,c2 in self.terms.items():
#                      _temp._add_term(c2, p2)
#                  for p in _temp.terms:
#                      _temp[p*p1] = _temp.terms.pop(p) * c2
#                  t.append(_temp)
#              for i in t:
#                  new += i
        return new
    

    def __rmul__(self,left):
        self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('right is not a legal opperand')
        if type(right) == int:
            if len(self) == 0 and self[0] == right:
                return True
            else:
                return False
        else:
            answer = True
            for p,c in right.terms.items():
                if self[p] != c:
                    return False
            return answer

    
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