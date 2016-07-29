class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i in terms:
            assert type(i[0]) in (int, float), "Coefficient is not an int or float"
            assert type(i[1]) == int, "Power is not an int"
            assert i[1] >= 0, "Power is not >= 0"
            assert i[1] not in self.terms.keys(), "Power is already in keys"
            if i[0] != 0: self.terms[i[1]] = i[0]
            
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
        result = ''
        count = 0
        for k,v in self.terms.items():
            if count == len(self.terms)-1: result += '('+str(v)+', '+str(k)+')'
            else:
                result += '('+str(v)+', '+str(k)+'), '
                count += 1
        return "Poly("+result+")"

    
    def __len__(self):
        if len(self.terms.keys()) == 0: return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += (arg**k)*v
        return result
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), reverse = True):
            yield (v, k)
            

    def __getitem__(self,index):
        if type(index) != int: raise TypeError("Index is not an int")
        if index < 0: raise TypeError("Index is < 0")
        if index not in self.terms.keys(): return 0
        for k,v in self.terms.items():
            if index == k: return v
        

    def __setitem__(self,index,value):
        if type(index) != int: raise TypeError("Index is not an int")
        if index < 0: raise TypeError("Index is < 0")
        if value != 0: self.terms[index] = value
        elif index in self.terms.keys(): del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int: raise TypeError("Index is not an int")
        if index < 0: raise TypeError("Index is < 0")
        if index in self.terms.keys(): del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float): raise TypeError("Coefficient is not int or float")
        if type(p) != int: raise TypeError("Power is not an int")
        if p < 0: raise TypeError("Power is < 0")
        if c == 0: return
        if p not in self.terms.keys(): self.terms[p] = c
        else: 
            value = c+self.terms[p]
            if value != 0: self.terms[p] = value
            else: del self.terms[p]
        

    def __add__(self,right):
        if type(right) not in (int, float, Poly): raise TypeError('Right is an invalid type')
        result = Poly()
        for k,v in self.terms.items():
            result._add_term(v, k)
        if type(right) in (int, float): result.terms[0] = result.terms[0]+right
        else:
            for k,v in right.terms.items():
                if k in result.terms.keys(): result.terms[k] = result.terms[k]+v
                else: result.terms[k] = v
        return result
        

    
    def __radd__(self,left):
        if type(left) not in (int, float, Poly): raise TypeError('Right is an invalid type')
        result = Poly()
        for k,v in self.terms.items():
            result._add_term(v, k)
        if type(left) in (int, float): result.terms[0] = result.terms[0]+left
        else:
            for k,v in left.terms.items():
                if k in result.terms.keys(): result.terms[k] = result.terms[k]+v
                else: result.terms[k] = v
        return result
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly): raise TypeError('Right is an invalid type')
        result = Poly()
        answer = Poly()
        for k,v in self.terms.items():
            result._add_term(v, k)
        if type(right) in (int, float):
            for k,v in result.terms.items():
                answer.terms[k] = v*right
        else:
            for k,v in right.terms.items():
                for k2,v2 in result.terms.items():
                    answer._add_term(v*v2, k+k2)
        return answer
        
    

    def __rmul__(self,left):
        if type(left) not in (int, float, Poly): raise TypeError('Right is an invalid type')
        result = Poly()
        answer = Poly()
        for k,v in self.terms.items():
            result._add_term(v, k)
        if type(left) in (int, float):
            for k,v in result.terms.items():
                answer.terms[k] = v*left
        else:
            for k,v in left.terms.items():
                for k2,v2 in result.terms.items():
                    answer._add_term(v*v2, k+k2)
        return answer
    

    def __eq__(self,right):
        result = True
        if type(right) not in (int, float, Poly): raise TypeError('Right is an invalid type')
        if type(right) not in (int, float):
            for k,v in self.terms.items():
                for k2,v2 in right.terms.items():
                    if k != k2: result = False
                    if v != v2: result = False
        else:
            for k,v in self.terms.items():
                if v != right: result = False
        return result
                    

    
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