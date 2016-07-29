class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for arg in terms:
            assert type(arg[0])in [int, float]
            assert type(arg[1]) is int and arg[1] >= 0
            assert arg[1] not in self.terms
            if arg[0] != 0:
                self.terms[arg[1]] = arg[0]
        
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
        result = []
        for k,v in self.terms.items():
            result.append((v,k))
        if len(result) == 0:
            return 'Poly()'   
        final = 'Poly(' 
        for item in result:
            if item != result[-1]:
                final += str(item) + "," 
            else:
                final += str(item) + ')'  
        return final
        pass

    
    def __len__(self):
        result = 0
        for k in self.terms:
            if k > result:
                result = k
        return result
            
        pass
    
    def __call__(self,arg):
        answer = 0
        for k,v in self.terms.items():
            answer += v * (arg**k)
        return answer
        pass
    

    def __iter__(self):
        result = []
        for k,v in self.terms.items():
            result.append((k,v))
        for item in sorted(result, reverse=True):
            yield (item[1], item[0])
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms:
            return 0
        else:
            return self.terms.get(index)          

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
        pass
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index in self.terms:
            del self.terms[index]
        pass
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError
        if type(p) != int or p < 0:
            raise TypeError
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if c + self.terms.get(p) == 0:
                del self.terms[p]
            else:
                self.terms[p] = self.terms.get(p) + c
        elif p == 0:
            self.terms[p] = c
            
        pass
       

    def __add__(self,right):
        if type(right) == Poly:
            for k,v in right.terms.items():
                self._add_term(v, k)
            return self
        if type(right) == int or type(right) == float:
            self.terms[0] = self.terms.get(0) + right
            return self
        else:
            raise TypeError
                
        
        pass

    def __radd__(self,left):
        if type(left) == Poly:
            for k,v in left.terms.items():
                self._add_term(v, k)
            return self
        if type(left) == int or type(left) == float:
            self.terms[0] = left + self.terms.get(0)
            return self
        else:
            raise TypeError
        pass
    

    def __mul__(self,right):
        if type(right) == Poly:
            if right == Poly():
                return 0
            
            check = []
            result = Poly()
            for k,v in self.terms.items():
                for p,c in right.terms.items():
                    powers = p + k
                    coef = v * c
                    check.append((coef, powers))
            for item in check:
                result._add_term(item[0], item[1])
            return result
        if type(right) == int:
            result = Poly()
            for k,v in self.terms.items():
                result.terms[k] = self.terms.get(k) * right
            return result
        
        pass
    

    def __rmul__(self,left):
        if type(left) == Poly:
            if left == Poly():
                return 0
            
            check = []
            result = Poly()
            for k,v in self.terms.items():
                for p,c in left.terms.items():
                    powers = p + k
                    coef = v * c
                    check.append((coef, powers))
            for item in check:
                result._add_term(item[0], item[1])
            return result
        
        if type(left) == int:
            result = Poly()
            for k,v in self.terms.items():
                result.terms[k] = self.terms.get(k) * left
            return result
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            for k in self.terms:
                if k in right:
                    if self.terms.get(k) == right.terms.get(k):
                        continue
                else:
                    return False
            return True
        if type(right) == int:
            for k,v in self.terms.items():
                if right == v:
                    return True
            return False
        
        else:
            raise TypeError

    
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