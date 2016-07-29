class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
            
        self.terms = {}
        for i in terms:
            assert type(i[0]) in (int, float), 'coefficient must be an int or float value'
            assert type(i[1]) == int and i[1] >= 0, 'power must be an integer whose value is >= 0'
            assert i[1] not in self.terms, 'power cannot appear as a later term if it appears'
            if i[0] != 0:
                self.terms[i[1]] = i[0]
        
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
        return 'Poly('+','.join('('+str(v)+','+str(k)+')' for k,v in self.terms.items())+')'

    
    def __len__(self):
        if self.terms != {}:
            return max(k for k in self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += v*(arg**k)
        return result
    

    def __iter__(self):
        for i in sorted([k for k in self.terms], reverse = True):
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError('index must be an integer whose value is >= 0')      
            

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0 and index in self.terms:
                self.terms.pop(index)
            elif value != 0:
                self.terms[index] = value
        else:
            raise TypeError('index must be an integer whose value is >= 0')   

            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            raise TypeError('index must be an integer whose value is >= 0')   
            

    def _add_term(self,c,p):
        if type(p) == int and p >= 0 and type(c) in (int, float):
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                if self.terms[p]+c != 0:
                    self.terms[p] +=c
                else:
                    self.terms.pop(p)     
        else:
            raise TypeError
       

    def __add__(self,right):
        if type(right) == Poly:
            new_poly = Poly()
            for k, v in self.terms.items():
                new_poly._add_term(v,k)
            for k, v in right.terms.items():
                new_poly._add_term(v, k)
            return new_poly
        elif type(right) in (int, float):
            new_poly = Poly()
            for k, v in self.terms.items():
                if k != 0:
                    new_poly._add_term(v, k)
                else:
                    new_poly._add_term(v+right, k)
            return new_poly
        else:
            raise TypeError('unsupported operand type(s) for +: Poly and {}'.format(str(type(right))[8:-2]))


    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) == Poly:
            new_poly = Poly()
            for k1, v1 in self.terms.items():
                for k2, v2 in right.terms.items():
                    new_poly._add_term(v1*v2, k1+k2)
            return new_poly
        elif type(right) in (int, float):
            new_poly = Poly()
            for k, v in self.terms.items():
                new_poly._add_term(v*right, k)
            return new_poly
        else:
            raise TypeError('unsupported operand type(s) for *: Poly and {}'.format(str(type(right))[8:-2]))
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) in (int, float):
            return list(self.terms.items()) == [(0, right)]
        else:
            raise TypeError('unsupported operand type(s) for ==: Poly and {}'.format(str(type(right))[8:-2]))

    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()