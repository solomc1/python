class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert type(t[1]) == int, "illegal power in " + str(t)
            assert t[1] >= 0, "power must be equal to or greater than 0"
            assert t[1] not in self.terms, "illegal power provided; already stored in dictionary"
            assert type(t[0]) in (float, int), 'illegal coefficient provided'
            if t[0] != 0:
                self.terms[t[1]] = t[0]
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
        poly_str = ''
        count = 0
        for t in self.terms:
            if count != len(self.terms) - 1:
                poly_str +=  '(' + str(self.terms[t]) + ',' + str(t) + ')' + ','
                count += 1
            else:
                poly_str +=  '(' + str(self.terms[t]) + ',' + str(t) + ')'
        return 'Poly(' + poly_str + ')'
    # self.terms[t] refers to coefficient
    # t refers to the power
    
    def __len__(self):
        # Placeholder for returning 0
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        poly_sum = 0
        for t in self.terms:
            if t == 0:
                poly_sum += self.terms[t]
            else:
                poly_sum += self.terms[t] * (arg ** t)
        return poly_sum
    

    def __iter__(self):
        iter_list = []
        for t in self.terms:
            iter_list.append((self.terms[t], t))
        for i in sorted(iter_list, key = lambda x: x[1], reverse = True):
            yield i
        
    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('can only index with int')
        if index < 0:
            raise TypeError('cannot have negative index')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('index must be int and greater than 0')
        if index in self.terms and value == 0:
            del self.terms[index]
        else:
            if value != 0:
                self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError('cannot use negative indexes')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int or p < 0:
            raise TypeError('illegal power or coefficient provided')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c == 0:
                del self.terms[p]
            else:
                self.terms[p] = self.terms[p] + c
       

    def __add__(self,right):
        x = Poly()
        for t in self.terms:
            x._add_term(self.terms[t],t)
        if type(right) == int:
            right = Poly((right, 0))
        for rt in right.terms:
            x._add_term(right.terms[rt], rt)
        return x
                

    
    def __radd__(self,left):
        x = Poly()
        if type(left) == int:
            left = Poly((left, 0))
        for t in self.terms:
            x._add_term(self.terms[t],t)
        for rt in left.terms:
            x._add_term(left.terms[rt], rt)
        return x

    def __mul__(self,right):
        x = Poly()
        for t in self.terms:
            x._add_term(self.terms[t], t)
        return x
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != Poly:
            raise TypeError('cannot compare other types except for Poly')


    
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