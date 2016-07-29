class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[0]) not in (int, float):
                raise(AssertionError('coefficient must be an int or float'))
            if type(i[1]) != int or i[1] < 0:
                raise(AssertionError('power must be an int greater than or equal to 0'))
            if i[0] != 0:
                if i[1] not in self.terms.keys():
                    self.terms[i[1]] = i[0]
                else:
                    raise(AssertionError('powers cannot be repeated'))

        
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
        terms = [(v, k) for k, v in self.terms.items()]
#         print('repr: Poly('+ str(terms).strip('[').strip(']') + ')')
        return 'Poly('+ str(terms).strip('[').strip(']') + ')'


    
    def __len__(self):
        highest = 0
        for k in self.terms.keys():
            if k > highest:
                highest = k
        return highest
    
    def __call__(self,arg):
        total = 0
        for k, v in self.terms.items():
            total += v * arg ** k
        return total
    

    def __iter__(self):
        keys = []
        for k in self.terms.keys():
            keys.append(k)
        keys.sort(key = None, reverse = True)
        for k in keys:
            yield((self.terms[k], k))

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise(TypeError('can only index with an integer greater than or equal to 0'))
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise(TypeError('powers must be integers greater than or equal to 0'))
        if type(value) not in (int, float):
            raise(TypeError('coefficient must be an int or float'))
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise(TypeError('powers must be integers greater than or equal to 0'))
        if index in self.terms.keys():
            del self.terms[index]
        else:
            None
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise(TypeError('powers must be integers greater than or equal to 0'))
        if type(c) not in (int, float):
            raise(TypeError('coefficient must be an int or float'))
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        else:
            if self.terms[p] + c != 0:
                self.terms[p] = self.terms[p] + c
            else:
                del self.terms[p]    
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise(TypeError('can only add a Poly, int, or float'))
        if type(right) in (int, float):
            p = Poly()
            for k, v in self.terms.items():
                p._add_term(v, k)
            p._add_term(right, 0)
            return p
        elif type(right) == Poly:
            p = Poly()
            for k, v in self.terms.items():
                p._add_term(v, k)
            for k, v in right.terms.items():
                p._add_term(v, k)
            return p

    
    def __radd__(self,left):
        if type(left) not in (Poly, int, float):
            raise(TypeError('can only add a Poly, int, or float'))
        if type(left) in (int, float):
            p = Poly()
            for k, v in self.terms.items():
                p._add_term(v, k)
            p._add_term(left, 0)
            return p
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise(TypeError('can only add a Poly, int, or float'))
        if type(right) in (int, float):
            p = Poly()
            for k, v in self.terms.items():
                p._add_term(v * right, k)
            return p
        if type(right) == Poly:
            p = Poly()
            for k, v in self.terms.items():
                for i, j in right.terms.items():
                    p._add_term(v * j, k + i)
            return p
    

    def __rmul__(self,left):
        if type(left) not in (Poly, int, float):
            raise(TypeError('can only add a Poly, int, or float'))
        if type(left) in (int, float):
            p = Poly()
            for k, v in self.terms.items():
                p._add_term(v * left, k)
            return p
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise(TypeError('can only compare a Poly to a Poly, int, or float'))
        if type(right) in (int, float):
            if len(self.terms.keys()) <= 1:
                for v in self.terms.values():
                    return v == right
            else:
                return False
        elif type(right) == Poly:
            if self.terms.items() == right.terms.items():
                return True
            else:
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