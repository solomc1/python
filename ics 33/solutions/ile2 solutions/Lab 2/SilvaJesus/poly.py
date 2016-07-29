class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
#         self.terms = {k: v for v,k in terms if k !=0}
        self.terms = {}
        for coef,power in terms:
            assert type(coef) in (int,float)
            assert type(power) == int and power >= 0
            if power not in self.terms:
                if coef != 0:
                    self[power] = coef
            else:
                raise AssertionError('Power already in dictionary')
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
        arg_str = [str((v,k)) for k,v in self.terms.items()]
        return "Poly({})".format(','.join(arg_str))

    
    def __len__(self):
        if [i for i in self.terms] == []:
            return 0
        return max([i for i in self.terms])
    
    def __call__(self,arg):
        return sum([v*arg**k for k,v in self.terms.items()])

    

    def __iter__(self):
        for k,v in self.terms.items():
            yield (v,k)
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError('Negative numbers not supported')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Invalid type or negeative')
        if value == 0:
            self.terms.pop(index)
        else:
            self.terms.update({index:value})

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Invalid type or negeative')
        elif index in self.terms:
            self.terms.pop(index)
        
            

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int or p < 0:
            raise TypeError('Invalid type or negeative')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                if c == 0:
                    self.terms.pop(p)
                else:
                    coef = self.terms[p] + c
                    self[p] = coef
    def __add__(self,right):
        new_poly = Poly()
        for k,v in self.terms.items():
            new_poly._add_term(v,k)
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid type')
        if type(right) == Poly:
            for i in right.terms:
                new_poly._add_term(right.terms[i], i)
            return new_poly
        else:
            new_poly._add_term(right, 0)
            return new_poly
                

    
    def __radd__(self,left):
        new_poly = Poly()
        for k,v in self.terms.items():
            new_poly._add_term(v,k)
        if type(left) not in (int, float):
            raise TypeError('Invalid type')
        new_poly._add_term(left, 0)
        return new_poly
                
    

    def __mul__(self,right):
        new_poly = Poly()
        for k,v in self.terms.items():
            new_poly._add_term(v,k)
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid type')
        if type(right) == Poly:
            second_poly = Poly()
#             for k1, v1 in new_poly.terms.items():
#                 for k2, v2 in right.terms.items():
#                     second_poly._add_term(k1+k2, v1+v2)
                    
            return second_poly
        else:
            for k,v in new_poly.terms.items():
                new_poly.terms[k] = v*right
            return new_poly

    def __rmul__(self,left):
        new_poly = Poly()
        for k,v in self.terms.items():
            new_poly._add_term(v,k)
        if type(left) not in (int, float, Poly):
            raise TypeError
        else:
            for k,v in new_poly.terms.items():
                new_poly.terms[k] = v*left
            return new_poly
    

    def __eq__(self,right):
        final_bool_s = True
        if type(right) not in (int, float, Poly):
            raise TypeError
        if type(right) == Poly:
            for k in self.terms.items():
                for k1 in right.items():
                    if self.terms[k] != right.terms[k1] and k != k1:
                        final_bool_s = False
        else:
            return right == self.terms[0]

    
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