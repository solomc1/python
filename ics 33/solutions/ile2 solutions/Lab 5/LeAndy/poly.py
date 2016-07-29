class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in (int, float)
            assert term[1] >= 0
            assert type(term[1]) == int
            assert term[1] not in list(self.terms.keys())
            if term[0] != 0:
                self.terms[term[1]] = term[0]
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
        polystr = 'Poly('
        if len(self.terms) == 0:
            return polystr + ')'
        
        for key in list(self.terms.keys()):
            polystr += '(' + str(self.terms[key]) +',' + str(key) + '),'
        return polystr[:-1] + ')'
    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            pmax = 0
            for key in list(self.terms.keys()):
                if key > pmax:
                    pmax = key
            return pmax
    
    def __call__(self,arg):
        total = 0
        for key in list(self.terms.keys()):
            total += arg**(key) * self.terms[key]
        return total
    

    def __iter__(self):
        for key in sorted(list(self.terms.keys()), reverse=True):
            yield (self.terms[key], key)
            

    def __getitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError('index must be an int greater than 0')
        if index not in self.terms:
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if index < 0 or type(index) != int:
            raise TypeError('power must be an int greater than 0')
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError('index must be an int greater than 0')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('coefficient must be numeric (int or float)') 
        if type(p) != int and p < 0:
            raise TypeError('power must be int and >= 0')
        if p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]       
        if p not in self.terms and c != 0:
            self.terms[p] = c
        

    def __add__(self,right):
        if right not in (Poly, int, float):
            return TypeError('right operand must be Poly, int or float')
        polystr = 'Poly('
        if type(right) == Poly:
            for key in list(self.terms.keys()):
                for key2 in list(right.terms.keys()):
                    if key == key2:
                        polystr += '(' + str(self.terms[key] + right.terms[key2]) + ',' + str(key) +'),'
            polystr = polystr[:-1] + ')'
        if type(right) in (int, float):
            polystr += '(' + str(self.terms[0] + right) + ',' + '0' + '))'
        return eval(polystr)

    
    def __radd__(self,left):
        if left not in (int, float):
            return TypeError('left operand must be int or float')
    

    def __mul__(self,right):
        if right not in (Poly, int, float):
            return TypeError('right operand must be Poly, int or float')
    

    def __rmul__(self,left):
        if left not in (int, float):
            return TypeError('left operand must be int or float')
    

    def __eq__(self,right):
        if type(self) != Poly or type(right) not in (Poly, int, float):
            return TypeError('right operand must be Poly, int or float')
        

    
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
    p.__setitem__(6,2)
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