class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:
            if type(x[1]) not in [int]:
                raise AssertionError; 'Not an int or a float'
            if type(x[0]) not in [int, float]:
                raise AssertionError; 'Not an int or a float'
            if x[1] < 0:
                raise AssertionError; 'The power cannot be less than 0'
            if x[1] in self.terms:
                raise AssertionError; 'The power cannot be repeated'
            if x[0] != 0:
                self.terms[x[1]] = x[0]
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
        string = ''
        for x in self.terms:
            string += '(' + str(self.terms[x]) + ',' + str(x) + '),'
        string = string[:-1]
        return 'Poly(' + string + ')'

    
    def __len__(self):
        max = 0
        if len(self.terms) == 0:
            return 0
        for x in self.terms:
            if x > max:
                max = x
        return max
        
    
    def __call__(self, arg):
        value = 0
        for x in self.terms:
            value += ((arg ** x) * self.terms[x])
        return value
    

    def __iter__(self):
        listterms1 = []
        for x in self.terms:
            listterms1.append((self.terms[x], x))
        listsorted = sorted(listterms1, key = (lambda x: x[1]), reverse = True)
        for y in listsorted:
            yield y
    
    
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError; 'The provided index cannot be used'
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError; 'The provided index cannot be used'
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError; 'The provided index cannot be used'
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError; 'This coefficient cannot be used'
        if type(p) != int or p < 0:
            raise TypeError; 'The power cannot be used'
        if p in self.terms:
            self.terms[p] += c 
        else:    
            if c != 0:
                self.terms[p] = c
        if p in self.terms and self.terms[p] == 0:
            del self.terms[p]
            

    def __add__(self,right):
        p = Poly()
        if type(right) in [int, float]:
            for x in self.terms:
                p._add_term((self.terms[x]), x)
            p._add_term(right, 0)
            return p  
        elif type(right) == Poly:
            for x in self.terms:
                if x not in right.terms:
                    p._add_term(self.terms[x], x)
                else:
                    p._add_term((self.terms[x] + right.terms[x]), x)
            for x in right.terms:
                if x not in self.terms:
                    p._add_term(right.terms[x], x)
            return p
        else:
            raise TypeError; 'The polynomial cannot be added with the provided value'

    
    def __radd__(self,left):
        p = Poly()
        if type(left) in [int, float]:
            for x in self.terms:
                p._add_term((self.terms[x]), x)
            p._add_term(left, 0)
            return p  
        elif type(left) == Poly:
            for x in self.terms:
                if x not in left.terms:
                    p._add_term(self.terms[x], x)
                else:
                    p._add_term((self.terms[x] + left.terms[x]), x)
            for x in left.terms:
                if x not in self.terms:
                    p._add_term(left.terms[x], x)
            return p
        else:
            raise TypeError; 'The polynomial cannot be added with the provided value'
    

    def __mul__(self,right):
        p = Poly()
        if type(right) in [int, float]:
            for x in self.terms:
                p._add_term(((self.terms[x]) * right), x)
            return p  
        elif type(right) == Poly:
            pass
        else:
            raise TypeError; 'The polynomial cannot be added with the provided value'
    

    def __rmul__(self,left):
        p = Poly()
        if type(left) in [int, float]:
            for x in self.terms:
                p._add_term(((self.terms[x]) * left), x)
            return p
        elif type(left) == Poly:
            pass
        else:
            raise TypeError; 'The polynomial cannot be added with the provided value'
    

    def __eq__(self,right):
        if type(right) in [int, float]:
            if len(self.terms) == 1:
                if self.terms[0] == right:
                    return True
                else:
                    return False
            else:
                return False
        elif type(right) == Poly:
            for x in self.terms:
                if x in right.terms:
                    if self.terms[x] == right.terms[x]:
                        return True
                    else:
                        return False
                else:
                    return False      
        else:
            raise TypeError; 'The polynomial cannot be added with the provided value'

    
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