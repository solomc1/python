class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coeff, power in terms:
            if type(coeff) not in [int, float]:
                raise AssertionError
            if type(power) is not int:
                raise AssertionError
            if power < 0:
                raise AssertionError
            if power in self.terms:
                if self.terms[power] < 0:
                    self.terms[power] = coeff
                    break
                else:
                    raise AssertionError
            if coeff != 0:
                self.terms[power] = coeff
        
            
            
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
        if len(self.terms) == 0:
            return 'Poly()'
        s = 'Poly('
        for k,v in self.terms.items():
            s+= '(' + str(v) + ',' + str(k) +'),'
        s = s[:-1] + ')'
        return s
            
            

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        max = 0
        for k in self.terms.keys():
            if k > max:
                max = k
        return max
    def __call__(self,arg):
        sum = 0
        for k,v in self.terms.items():
            sum += v * (arg ** k)
        return sum
    

    def __iter__(self):
        k = sorted(list(self.terms.items()))
        k = list(reversed(k))
        pairs = []
        for pair in k:
            pairs.append((pair[1], pair[0]))
        return iter(pairs)
            

    def __getitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError
        try:
            return self.terms[index]
        except:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index <0:
            raise TypeError
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError
        if type(p) is not int or p < 0:
            raise TypeError
        if p in self.terms.keys():
            sum = c + self.terms[p]
            if sum == 0:
                del self.terms[p]
                return
            else:
                self.terms[p] = sum
                return
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
            return

    def __add__(self,right):
        if type(right) is Poly:
            for k,v in right.terms.items():
                Poly._add_term(self, v, k)
                
        else:
            Poly._add_term(self, right, 0) 
        return eval(repr(self))
            

    
    def __radd__(self,left):
        Poly._add_term(self, left, 0)
        return eval(repr(self))
    

    def __mul__(self,right):
        if type(right) == Poly:
            if len(right.terms) == 0:
                return 0
            results = {}
            for k,v in self.terms.items():
                for k1,v1 in right.terms.items():
                    if k1 != 0 and k == k1:
                        results[k] = v + v1
                    if k1 == 0 and k == k1:
                        results[k] = v* v1
                    if k1 != 0 and k != k1:
                        newk = k + k1
                        newv = v * v1
                        results[newk] = newv
                    if k1 == 0 and k != k1:
                        results[k] = v * v1
            s = 'Poly('
            for k,v in results.items():
                s+= '(' + str(v) + ',' + str(k) +'),'
            s = s[:-1] + ')'

            return eval(s)
        else:
            for k,v in self.terms.items():
                self.terms[k] = v* right
            return eval(repr(self))
            
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError
        if type(right) is Poly:
            selfd = sorted(list(self.term.items()))
            rightd = sorted(list(right.terms.items()))
            for i in range(len(selfd)):
                if selfd[i] != rightd[i]:
                    return False
            return True
        else:
            if 0 in self.terms.keys():
                if self.terms[0] == right:
                    return True
        
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