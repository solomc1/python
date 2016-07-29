class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.d = {}
        L = []
        for i in terms:
            if type(i[0]) != int and type(i[0]) != float:
                raise AssertionError( 'All coefficients must be ints or floats')
            if type(i[1]) != int or i[1] < 0:
                raise AssertionError( 'All powers must be ints and greater than or equal to 0')
            if i[1] in L:
                if i[0] != 0:
                    raise AssertionError( 'Cannot repeat powers')
            if i[1] not in L:
                if i[0] != 0:
                    L.append(i[1])
            if i[0] != 0:
                self.terms[i[1]] = i[0]
            if i[1] not in self.d.keys():
                self.d[i[1]] = []
            self.d[i[1]].append(i[0])   
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
        s = []
        for i in self.d.keys():
            for j in self.d[i]:
                s.append('(' + str(j) + ',' + str(i) + ')')
        return 'Poly(' + ','.join(p for p in s) + ')'

    
    def __len__(self):
        if self.d == {}:
            return 0
        else:
            L = []
            for i in self.d.keys():
                L.append(i)
            return max(L)
            
    def __call__(self,arg):
        total = 0
        for i in self.terms.keys():
            total += (self.terms[i] * (arg ** i))
        return total
    

    def __iter__(self):
        L = []
        for i in self.terms.keys():
            L.append(i)
        Lsort = sorted(L, reverse = True)
        for x in Lsort:
            yield (self.terms[x], x)
                
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than 0')
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than 0')
        self.terms[index] = value
        for i in self.terms.keys():
            if self.terms[i] == 0:
                del self.terms[i]   

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Power must be an int greater than 0')
        if type(c) != int and type(c) != float:
            raise TypeError('Coefficient must be int or float')
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        else:
            if self.terms[p] + c == 0:
                del self.terms[p]
            else:
                self.terms[p] = c + self.terms[p]
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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