class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            assert type(term[0]) == int or type(term[0])== float, 'Poly.__init__: coefficient must be int or float'
            assert type(term[1]) == int and term[1] >= 0, 'Poly.__init__: power must be an int and >= 0'
            if term[0] == 0:
                continue
            if term[1] in self.terms.keys():
                raise AssertionError('Poly.__init__: power > 0 cannot appear more than once')
            else:
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
        return 'Poly('+','.join('('+str(v)+','+str(k)+')' for k,v in self.terms.items())+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        answer = 0
        for k,v in self.terms.items():
            if k > 0:
                exponent = 1
                for num in range(k):
                    exponent *= arg
                answer += v*exponent
            else:
                answer += v
        return answer
                
    

    def __iter__(self):
        if len(self.terms) == 0:
            return 0
        power_list = [v for v in self.terms.keys()]
        for tups in sorted(power_list, reverse=True):
            yield self.terms[tups], tups
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: index not an int or less than 0')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: index not an int or less than 0')
        elif value == 0 and value in self.terms.values():
            for k,v in self.terms.items():
                if v == value:
                    self.terms.pop(k)
        else:
            self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitems__: index must be an int and not less than 0')
        elif index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Poly._add_term: coefficient must be an int or a float')
        elif type(p) != int or p < 0:
            raise TypeError('Poly.add_term: power must be an int and >= 0')
        else:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                c += self.terms[p]
                if c == 0:
                    self.terms.pop(p)
                else:
                    self.terms[p] = c 

    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: type must be an int, float, or Poly')
        else:
            if type(right) in [int,float]:
                self._add_term(right, 0)
            else:
                for term in right:
                    self._add_term(term[0], term[1])
            return self
                
    
    def __radd__(self,left):
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: type must be an int, float, or Poly')
        else:
            if type(left) in [int,float]:
                self._add_term(left, 0)
            else:
                for term in left:
                    self._add_term(term[0], term[1])
            return self
    

    def __mul__(self,right):
#         new_poly = Poly()
#         for k,v in self.terms.items():
        pass
            

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__eq__: type must be an int, float, or Poly')
        elif type(right) in [int, float]:
            return self.terms[0] == right
        else:
            for k,v in self.terms.items():
                if right[k] != v:
                    return False
            return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()