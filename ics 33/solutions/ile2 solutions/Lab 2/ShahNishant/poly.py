class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for i,j in terms:
            assert type(i) in [int, float]
            assert type(j) == int and j >= 0
            if i == 0:
                continue
            elif j in self.terms.keys():
                raise AssertionError
            else:
                self.terms.update({j:i})
        
        
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
        final = 'Poly('
        
        if self.terms != {}:
            for i,j in list(self.terms.items())[:-1]:
                final += '({},{}),'.format(j,i)
            final += '({},{}))'.format(self.terms[list(self.terms.keys())[-1]], list(self.terms.keys())[-1])
        else:
            final += ")"
        
        return final

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            high = 0
            
            for i in self.terms.keys():
                if i > high:
                    high = i
            return high
    
    def __call__(self,arg):
        assert type(arg) in [int, float]
        answer = 0
        for i,j in self.terms.items():
            answer += (arg ** i) * j
        return answer
    

    def __iter__(self):
        for i,j in sorted(self.terms.items(), reverse=True):
            yield (j,i)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__: index ({}) not an int'.format(index))
        elif index < 0:
            raise TypeError('Poly.__getitem__: index ({}) less than 0'.format(index))
        else:
            try:
                return self.terms[index]
            except:
                return 0
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Poly.__setitem__: index ({}) not an int'.format(index))
        elif index < 0:
            raise TypeError('Poly.__setitem__: index ({}) less than 0'.format(index))
        elif value == 0:
            try:
                del self.terms[index]
            except:
                pass
        else:
            if index in self.terms.keys():
                self.terms[index] = value
            else:
                self.terms.update({index:value})
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__setitem__: index ({}) not an int'.format(index))
        elif index < 0:
            raise TypeError('Poly.__setitem__: index ({}) less than 0'.format(index))
        elif index not in self.terms.keys():
            pass
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError('Poly.__setitem__: p ({}) not an int'.format(p))
        elif p < 0:
            raise TypeError('Poly.__setitem__: p ({}) less than 0'.format(p))
        elif type(c) not in [int, float]:
            raise TypeError('Poly._add_term: coefficient ({}) not a numeric value'.format(c))
        elif p not in self.terms.keys() and c != 0:
            self.terms.update({p:c})
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
            else:
                pass
            

    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: unsupported operand + for type {} and {}'.format(type(self), type(right)))
        elif type(right) in [int, float]:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            new._add_term(right, 0)
        else:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            for i,j in right.terms.items():
                new._add_term(j,i)
        return new

    
    def __radd__(self,left):
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: unsupported operand + for type {} and {}'.format(type(self), type(left)))
        elif type(left) in [int, float]:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            new._add_term(left, 0)
        else:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            for i,j in left.terms.items():
                new._add_term(j,i)
        return new
    

    def __mul__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: unsupported operand + for type {} and {}'.format(type(self), type(right)))
        elif type(right) in [int, float]:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            for i,j in new.terms.items():
                del new.terms[i]
                new.terms.update({i: j*right})
        else:
            new = Poly()
            for i,j in self.terms.items():
                for l,r in right.terms.items():
                    new._add_term(j*r, i+l)
        return new
    

    def __rmul__(self,left):
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__add__: unsupported operand + for type {} and {}'.format(type(self), type(left)))
        elif type(left) in [int, float]:
            new = Poly()
            for i,j in self.terms.items():
                new._add_term(j,i)
            for i,j in new.terms.items():
                del new.terms[i]
                new.terms.update({i: j*left})
        else:
            new = Poly()
            for i,j in self.terms.items():
                for l,r in left.terms.items():
                    new._add_term(j*r, i+l)
        return new
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__eq__: right ({}) not an int'.format(right))
        elif type(right) in [int, float]:
            return len(self.terms.items()) == 1 and list(self.terms.keys()) == [0] and list(self.terms.values()) == [right]
        elif type(right) == Poly:
            return right.terms == self.terms
        
        

    
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