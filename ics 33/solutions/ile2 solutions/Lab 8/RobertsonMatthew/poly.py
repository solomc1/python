class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            if type(term[0]) not in (int, float): raise AssertionError('A coefficient must be an int or a float.')
            elif type(term[1]) != int or term[1] < 0: raise AssertionError('A power must be greater than or equal to 0.')
            elif term[1] in self.terms: raise AssertionError('There cannot be more than one of the same power.')
            elif term[0] != 0: self.terms[term[1]] = term[0]

            
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
        return 'Poly('+','.join(['('+str(self.terms[term])
                                 +','+str(term)+')' for term in self.terms])+')'

    
    def __len__(self):
        if len(self.terms) == 0: return 0
        else: return max(self.terms.keys())
    
    
    def __call__(self,arg):
        result = 0
        for power in self.terms: result += (arg**power)*self.terms[power]
        return result
    

    def __iter__(self):
        result = []
        for power in self.terms: result.append((self.terms[power], power))
        result.sort(key=(lambda x: x[1]),reverse=True)
        for item in result: yield item
            

    def __getitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('The index must be an int greater than or equal to zero.')
        elif index not in self.terms: return 0
        else: return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0: raise TypeError('The index must be an int greater than or equal to zero.')
        elif value == 0 and index in self.terms: del self.terms[index]
        elif value == 0: pass
        else: self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('The index must be an int greater than or equal to zero.')
        if index in self.terms: del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float): raise TypeError('The coefficient must be an int or float.')
        elif type(p) != int or p < 0: raise TypeError('The power must be an int greater than or equal to 0.')
        if c == 0: pass
        elif p not in self.terms: self.terms[p] = c
        elif self.terms[p]+c == 0: del self.terms[p]
        else: self.terms[p] += c
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly): raise TypeError('Invalid operands for +.')
        result = eval(self.__repr__())
        if type(right) in (float, int):
            result._add_term(right,0)
            return result
        else: 
            for item in right: result._add_term(item[0], item[1])
            return result 

    
    def __radd__(self,left):
        if type(left) not in (int, float): raise TypeError('Invalid operands for +.')
        result = eval(self.__repr__())
        result._add_term(left,0)
        return result

    def __mul__(self,right):
        if type(right) not in (int, float, Poly): raise TypeError('Invalid operands for *.')
        result = eval(self.__repr__())
        if type(right) in (float, int):
            for num in range(right-1):
                for term in result.terms: result._add_term(result.terms[term], term)
            return result
        else:
            result = Poly()
            for s_term in self.terms:
                for r_term in right.terms:
                    result._add_term((self.terms[s_term]*right.terms[r_term]), (s_term+r_term))
            return result

    def __rmul__(self,left):
        if type(left) not in (int, float): raise TypeError('Invalid operands for *.')
        result = eval(self.__repr__())
        for num in range(left-1):
            for term in result.terms: result._add_term(result.terms[term], term)
        return result
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly): raise TypeError('Invalid operands for ==.')
        if type(right) in (int, float):
            if len(self.terms) == 1 and self.terms[0] == right: return True
            else: return False
        else:
            temp = zip(self, right)
            for item in temp:
                if item[0] != item[1]: return False
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