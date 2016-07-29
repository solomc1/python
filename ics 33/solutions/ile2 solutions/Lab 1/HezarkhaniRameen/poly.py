class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for t in terms:
            assert type(t[0]) == int or type(t[0]) == float
            assert type(t[1]) == int and t[1] >= 0
            assert t[1] not in self.terms.keys()
            if t[0] != 0:
                self.terms[t[1]] = t[0] 
            
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
        return 'Poly(' + ','.join([str((self.terms[k],k)) for k in self.terms.keys()]) + ')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        return sum([self.terms[k] * (arg ** k) for k in self.terms.keys()])

    def __iter__(self):
        return iter([(self.terms[k],k) for k in sorted(self.terms.keys(), reverse = True)])
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError ('Index out of bounds')
        try:
            return self.terms[index]
        except:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError ('Index out of bounds')
        if value == 0 and index not in self.terms.keys():
            pass
        elif value == 0 and index in self.terms.keys():
            self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError ('Index out of bounds')
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and c != float:
            raise TypeError ('Invalid coefficient')
        if type(p) != int or p < 0:
            raise TypeError ('Index out of bounds')
        if p not in self.terms.keys():
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] = self.terms[p] + c
        if self.terms[p] == 0:
            self.terms.pop(p)
       

    def __add__(self,right):
        result = Poly()
        for k in self.terms.keys():
            result._add_term(self.terms[k],k)
        if type(right) == Poly:
            for k in right.terms.keys():
                result._add_term(right.terms[k],k)
        elif type(right) == int or type(right) == float:
            result._add_term(right,0)
        else:
            raise TypeError ('Must be adding an int or a float')
        return result
        

    
    def __radd__(self,left):
        result = Poly()
        for k in self.terms.keys():
            result._add_term(self.terms[k],k)
        if type(left) == int or type(left) == float:
            result._add_term(left,0)
        else:
            raise TypeError ('Must be adding an int or a float')
        return result
    

    def __mul__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError ('Invalid data type')
        result = Poly()
        temp_result = Poly()
        for k in self.terms.keys():
            result._add_term(self.terms[k],k)
        if type(right) == Poly:
            for k in right.terms.keys():
                for g in result.terms.keys():
                    temp_result._add_term(result.terms[g] * right.terms[k], k + g)
            return temp_result
        elif type(right) == int or type(right) == float:
            for k in result.terms.keys():
                result._add_term(result.terms[k] * right, k)
            return result
        else:
            raise TypeError ('Must be adding an int or a float')
        
    

    def __rmul__(self,left):
        if type(left) != int and type(left) != float:
            raise TypeError ('Invalid data type')
        result = Poly()
        for k in self.terms.keys():
            result._add_term(self.terms[k] * left, k)
        return result
    

    def __eq__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError ('Invalid data type')
        if type(right) == Poly:
            if sorted(self.terms.keys()) != sorted(right.terms.keys()):
                return False
            for k in self.terms.keys():
                if self.terms[k] != right.terms[k]:
                    return False
            return True
        else:
            if len(self.terms.keys()) == 1: 
                for k in self.terms:
                    if self.terms[k] == 1 and self.terms[self.terms[k]] == right:
                        return True
            else:
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