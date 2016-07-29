class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for v, k in terms:
            assert type(k) is int and k >= 0, 'Poly.__init__: illegal power in :' + '('+str(v)+','+str(k)+')'
            assert type(v) in (int, float), 'Poly.__init__: illegal coefficient in :' + '('+str(v)+','+str(k)+')'
            if k not in self.terms:
                if v != 0:
                    self.terms[k] = v
            else:
                raise AssertionError('Poly.__init__: illegal power in :' + '('+str(v)+','+str(k)+')')
        
            
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
        return 'Poly({})'.format(','.join(str(tuple((v,k))) for k,v in self.terms.items()))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += v*(arg**k)
        return total
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), reverse= True):
            yield (v,k)
            

    def __getitem__(self,index):
        if type(index) is int:
            if index >= 0:
                if index in self.terms:
                    return self.terms[index]
                else: return 0
            else: raise TypeError('Poly.__getitem__: index error,' + str(index) +'< 0')
        else: raise TypeError('Poly.__getitem__: index error: index must be int not '+str(type(index)))        
            

    def __setitem__(self,index,value):
        if type(index) is int:
            if index >= 0:
                if value != 0:
                    self.terms[index] = value
                else:
                    if index in self.terms:
                        del self.terms[index]
            else: raise TypeError('Poly.__setitem__: index error,' + str(index) +'< 0')
        else: raise TypeError('Poly.__setitem__: index error: index must be int not '+str(type(index)))

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: index must be int and greater than or equal to 0')
        else:
            if index in self.terms:
                del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (float, int) or type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: coeffiecent must be float, int, power must be int and less than 0')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                self.terms[p] += c
                if self.terms[p] == 0:
                    del self.terms[p]

                
       

    def __add__(self,right):
        empty_poly = Poly()
        for k, v in self.terms.items():
            empty_poly._add_term(v, k)
        if type(right) in (int, float):
            empty_poly._add_term(right, 0)
            return empty_poly
        elif type(right) is Poly:
            for k,v in right.terms.items():
                empty_poly._add_term(v, k)
            return empty_poly
        else:
            raise TypeError('Poly.__add__: right operand must be int, float, or class Poly')
            

    
    def __radd__(self,left):
        empty_poly = Poly()
        for k, v in self.terms.items():
            empty_poly._add_term(v, k)
        if type(left) in (int, float):
            empty_poly._add_term(left, 0)
            return empty_poly
        elif type(left) is Poly:
            for k,v in left.terms.items():
                empty_poly._add_term(v, k)
            return empty_poly
        else:
            raise TypeError('Poly.__radd__: left operand must be int, float, or class Poly')
    

    def __mul__(self,right):
        empty_poly = Poly()
        if type(right) in (int, float):
            for k, v in self.terms.items():
                empty_poly._add_term(v*right, k)
            return empty_poly
        elif type(right) is Poly:
            for k, v in self.terms.items():
                for p, c in right.terms.items():
                    empty_poly._add_term(v*c, k+p)
            return empty_poly
        else:
            raise TypeError('Poly.__mul__: right operand must be int, float or clas Poly')

    def __rmul__(self,left):
        empty_poly = Poly()
        if type(left) in (int, float):
            for k, v in self.terms.items():
                empty_poly._add_term(v*left, k)
            return empty_poly
        elif type(left) is Poly:
            for k, v in self.terms.items():
                for p, c in left.terms.items():
                    empty_poly._add_term(v*c, k+p)
            return empty_poly
        else:
            raise TypeError('Poly.__rmul__: left operand must be int, float or clas Poly')
    

    def __eq__(self,right):
        if type(right) is Poly:
            for k,v in self.terms.items():
                for p,c in right.terms.items():
                    if k != p or v != c:
                        return False
                    else:
                        return True
        elif type(right) in (int, float):
            if len(self.terms) == 1 and 0 in self.terms:
                return right == self.terms[0]
            else:
                return False
        else:
            raise TypeError('Poly.__eq__: argument on the right must be class Poly or int and float')    



    
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
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()