class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert isinstance(t[0], (int, float)), 'illegal coefficient'
            assert isinstance(t[1], (int)), 'illegal power'
            assert t[1] >= 0, 'illegal power'
#             if not isinstance(t[0], (int, float)):
#                 raise AssertionError('illegal coefficient')
#             if not isinstance(t[1], (int)):
#                 raise AssertionError('illegal power')
            if t[1] in self.terms.keys():
                raise AssertionError('power already exists')  
            if t[0] != 0:
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
        result = 'Poly('
        for k, v in self.terms.items():
            result += '(' + str(v) + ',' + str(k) + '),'
        if len(result) > 5:
            result = result[:-1]
        result += ')'    
        return result

    
    def __len__(self):
        if len(self.terms) > 0:
            return max(self.terms.keys())
        else: 
            return 0
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += v*(arg**k)
        return total
    
    
    def __iter__(self):
        powers = list(self.terms.keys())
        powers.sort(reverse=True)
        for p in powers:
            yield self.terms[p], p
            

    def __getitem__(self,index):
        if not isinstance(index, (int)):
            raise TypeError('Power must be an int')
        if index < 0:
            raise TypeError('Power must be > 0')
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0

    def __setitem__(self,index,value):
        if not isinstance(index, (int)):
            raise TypeError('Power must be an int')
        if index < 0:
            raise TypeError('Power must be > 0')
        if value == 0:
            if index in self.terms.keys():
                del(self.terms[index])
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if not isinstance(index, (int)):
            raise TypeError('Power must be an int')
        if index < 0:
            raise TypeError('Power must be > 0')
        if index in self.terms.keys():
            del(self.terms[index])
            

    def _add_term(self,c,p):
        if not isinstance(c, (int, float)):
            raise TypeError('Coefficient must be int or float')
        if not isinstance(p, (int)):
            raise TypeError('Power must be int')
        if p < 0:
            raise TypeError('Power must be >= 0')
        if p in self.terms.keys():
            self[p] = c + self.terms[p]
        else:
            self[p] = c
       

    def __add__(self,right):
        result = Poly()
        if not isinstance(right, (int, float, Poly)):
            raise TypeError('right parameter must be int or Poly type')
        if isinstance(right, (int)):
            for k,v in self.terms.items():
                result._add_term(v, k)
            result._add_term(right, 0)
        if isinstance(right, (Poly)):
            for k,v in right.terms.items():
            
                result._add_term(v, k)
            for k,v in self.terms.items():
                result._add_term(v, k)
        return result

    
    def __radd__(self,left):
        result = Poly()
        if not isinstance(left, (int, Poly)):
            raise TypeError('right parameter must be int or Poly type')
        if isinstance(left, (int)):
            for k,v in self.terms.items():
                result._add_term(v, k)
            result._add_term(left, 0)
        if isinstance(left, (Poly)):
            for k,v in left.terms.items():
                result._add_term(v, k)
            for k,v in self.terms.items():
                result._add_term(v, k)
        return result
    

    def __mul__(self,right):
        result = Poly()
        if not isinstance(right, (int, Poly)):
            raise TypeError('right parameter must be int or Poly type')
        if isinstance(right, (int)):
            for k,v in self.terms.items():
                result._add_term(right*v, k)
            result._add_term(right, 0)
        if isinstance(right, Poly):
            for k,v in self.terms.items():
                for p,c in right.terms.items():
                    result._add_term(v*c, k+p)
        return result
    

    def __rmul__(self,left):
        result = Poly()
        if not isinstance(left, (int, Poly)):
            raise TypeError('right parameter must be int or Poly type')
        if isinstance(left, (int)):
            for k,v in self.terms.items():
                result._add_term(left*v, k)
            result._add_term(left, 0)
        if isinstance(left, Poly):
            for k,v in self.terms.items():
                for p,c in left.terms.items():
                    result._add_term(v*c, k+p)
        return result
    

    def __eq__(self,right):
        if not isinstance(right, (int, float, Poly)):
            raise TypeError('Must be type int, float, or Poly')
        
        if isinstance(right, Poly):
            sk = list(self.terms.keys())
            sv = list(self.terms.values())
            
            rk = list(right.terms.keys())
            rv = list(right.terms.values())
            
            sk.sort()
            sv.sort()
            rk.sort()
            rv.sort()
            
            if sk == rk and rk == rv:
                return True
            else:
                return False
            
if __name__ == '__main__':
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
    
    
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