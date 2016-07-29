# Zixun Ai 63572173 Lab 8 
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for coefficient, power in terms:
            assert type(coefficient) == int or type(coefficient) == float, 'coefficient must be an int or float'
            assert type(power) == int and power >= 0, 'power must be an int whose value is >= 0'
            if power != 0: assert power not in self.terms, 'a power cannot appear as a later term if it is not 0'
            if coefficient != 0: 
                if power == 0 and power in self.terms: self.term[power] = self.term[power] + coefficient
                else: self.terms[power] = coefficient
        
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
        for term in self.terms:
            result = '{}({}, {}),'.format(result, self.terms[term], term)
        if result[-1] == ',': result = result[:-1]
        return result + ')' 

    def __len__(self):
        result = 0
        for term in self.terms:
            if term > result: result = term
        return result 
    
    def __call__(self,arg):
        result = 0
        for term in self.terms:
            result = result + self.terms[term] * (arg ** term)
        return result
    
    def __iter__(self):
        result = list()
        for term in self.terms:
            result.append((self.terms[term], term))
        result.sort(key=(lambda x: x[1]) , reverse=True)
        for term in result:
            yield term

    def __getitem__(self,index):
        result = 0
        if type(index) != int: raise TypeError('index should be int') 
        if index < 0 : raise TypeError('index should >= 0')
        if index in self.terms:
            result = self.terms[index]
        return result
         
    def __setitem__(self,index,value):
        if type(index) != int: raise TypeError('index should be int') 
        if index < 0 : raise TypeError('index should >= 0')
        if value == 0:
            if index in self.terms: del self.terms[index]
        else: self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int: raise TypeError('index should be int') 
        if index < 0 : raise TypeError('index should >= 0')
        if index in self.terms: del self.terms[index]
            
    def _add_term(self,c,p):
        if not ( type(c) == int or type(c) == float ): raise TypeError('coefficient must be an int or float')
        if not ( type(p) == int and p >= 0 ): raise TypeError('power must be an int whose value is >= 0')
        if (not p in self.terms) and (c != 0): self.terms[p] = c
        elif p in self.terms:  
            self.terms[p] = c + self.terms[p]
            if self.terms[p] == 0: del self.terms[p]

    def __add__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float): raise TypeError('Argument should be int or float or poly')
        if type(right) != Poly: right = Poly((right, 0)) 
        result = Poly()
        for item in [self, right]:
            for term in item.terms:
                result._add_term(item.terms[term], term)
        return result
    
    def __radd__(self,left):
        return self.__add__(left)
    
    def __mul__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float): raise TypeError('Argument should be int or float or poly')
        if type(right) != Poly: right = Poly((right, 0)) 
        result = Poly()
        for self_item in self.terms:
            for right_item in right.terms:
                result._add_term(self.terms[self_item] * right.terms[right_item] , self_item + right_item)
        return result
    
    def __rmul__(self,left):
        return self.__mul__(left)
    
    def __eq__(self,right):
        if not (type(right) == Poly or type(right) == int or type(right) == float): raise TypeError('Argument should be int or float or poly')
        if type(right) != Poly: 
            if 0 in self.terms and right == self.terms[0]: return True
            return False
        else: 
            for term in right.terms:
                if term not in self.terms: return False
            for term in self.terms:
                if term not in right.terms: return False
                if self.terms[term] != right.terms[term]: return False
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