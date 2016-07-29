class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            assert type(term[0]) in (int,float), 'coefficient must be int or float'
            assert type(term[1]) is int and term[1] >= 0, 'powers must be int >= 0'
            assert term[1] not in self.terms.keys()
            if term[0] != 0:
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
        return 'Poly('+str([(term[1],term[0]) for term in sorted(self.terms.items())]).strip('[]')+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for term in self.terms:
            result += self.terms[term] * arg ** term
        return result
    

    def __iter__(self):
        for term in sorted([(term[1],term[0]) for term in self.terms.items()], key = lambda x: x[1], reverse = True):
            yield term
            
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index must be int >= 0')
        if index not in self.terms.keys():
            return 0
        for k in self.terms:
            if k == index:
                return self.terms[k]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('index must be int >= 0')
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index must be int >= 0')
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('coefficient must be int or float')
        if type(p) is not int or p < 0:
            raise TypeError('power must be int >= 0')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
            
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('invalid operand for +: '+type(right))
        if type(right) in (int,float):
            right = Poly((right,0))
        new_poly = self
        for term in right:
            new_poly._add_term(term[0],term[1])
        return new_poly

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('invalid operand for *: '+type(right))
        new_poly = self
        if type(right) in (int,float):
            for term in new_poly.terms:
                new_poly.terms[term] *= right
        return new_poly
            
        

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('invalid operand for ==: '+type(right))
        if type(right) is Poly:
            for i in self.terms:
                if self.terms[i] != right.terms[i]:
                    return False
            return True
        else:
            for i in self.terms.items():
                if i != (0, right):
                    return False
            return True
    
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