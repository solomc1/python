# Alyssa Tan, Lab 2
# ICS-33: In-Lab Programming Exam #2
# 5/22/2014

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for term in terms:
            coeff,pow = term[0],term[1]
            
            assert type(coeff) in (int, float), \
            'Poly.__init__: illegal coefficient in: ' + str(term)
            
            assert type(pow) is int, \
            'Poly.__init__: illegal power in : ' + str(term)
            
            assert pow >= 0, \
            'Poly.__init__: illegal power in : ' + str(term)
            
            assert pow not in self.terms.keys(), \
            'Poly.__init__: illegal power in : ' + str(term)
            
            if coeff != 0:
                self.terms[pow] = coeff
        
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
        terms = []
        for pow in self.terms.keys():
            terms.append('({}, {})'.format(self.terms[pow], pow))
        return 'Poly({})'.format(', '.join(terms))
    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for pow in self.terms.keys():
            result += self.terms[pow] * (arg**pow)
        return result
    

    def __iter__(self):
        items = sorted(self.terms.items(), reverse=True)
        for item in items:
            yield (item[1], item[0])
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__getitem__: illegal index : ' + str(index))
        
        if index < 0:
            raise TypeError('Poly.__getitem__: illegal index : ' + str(index))
        
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Poly.__setitem__: illegal power : ' + str(index))
        
        if index < 0:
            raise TypeError('Poly.__setitem__: illegal power : ' + str(index))
        
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__delitem__: illegal index : ' + str(index))
        
        if index < 0:
            raise TypeError('Poly.__delitem__: illegal index : ' + str(index))
        
        if index in self.terms.keys():
            del self.terms[index]
        else:
            pass
            

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError('Poly._add_term: illegal power : ' + str(p))
        
        if p < 0:
            raise TypeError('Poly._add_term: illegal power : ' + str(p))  
        
        if type(c) not in (int, float):
            raise TypeError('Poly._add_term: illegal coefficient : ' + str(c))
        
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__add__: illegal operand : ' + str(right))
        else:
            p = Poly()
            for pow in self.terms.keys():
                p._add_term(self.terms[pow], pow)
            
            if type(right) is Poly:
                for pow in right.terms.keys():
                    p._add_term(right.terms[pow], pow)
                    
            else:
                p._add_term(right, 0)
            
        return p

    
    def __radd__(self,left):
        if type(left) in (int, float):
            p = Poly()
            for pow in self.terms.keys():
                p._add_term(self.terms[pow], pow)
                
            p._add_term(left, 0)
            return p
        
        else:
            raise TypeError('Poly.__radd__: illegal operand : ' + str(left))
    

    def __mul__(self,right):
        p = Poly()
        
        if type(right) is Poly:
            for pow in self.terms.keys():
                for pow_2 in right.terms.keys():
                    p._add_term(self.terms[pow] * right.terms[pow_2], pow + pow_2)
                    
            return p
        
        elif type(right) in (int, float):
            for pow in self.terms.keys():
                p._add_term(self.terms[pow] * right, pow)
                
            return p
        
        else:
            raise TypeError('Poly.__mul__: illegal operand : ' + str(right))
    

    def __rmul__(self,left):
        p = Poly()
        
        if type(left) in (int, float):
            for pow in self.terms.keys():
                p._add_term(self.terms[pow] * left, pow)
                
            return p
        
        else:
            raise TypeError('Poly.__rmul__: illegal operand : ' + str(left))
    

    def __eq__(self,right):
        if type(right) is Poly:
            for pow in self.terms.keys():
                if pow not in right.terms.keys():
                    return False
                if self.terms[pow] != right.terms[pow]:
                    return False
                
            for pow in right.terms.keys():
                if pow not in self.terms.keys():
                    return False
                if self.terms[pow] != right.terms[pow]:
                    return False
                    
            return True
        
        elif type(right) in (int, float):
            return len(self.terms) == 1 and self.terms[0] == right
        
        else:
            raise TypeError('Poly.__eq__: illegal operand : ' + str(right))

    
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