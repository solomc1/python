class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for t in terms:
            if (type(t[0]) == int or type(t[0]) == float) and (type(t[1]) == int and t[1] >= 0):
                
                for k in self.terms.keys():
                    if t[1] == k and (t[1] != 0):
                            raise AssertionError
                if t[0] != 0:
                    self.terms[t[1]] = t[0]
                
            else:
                raise AssertionError
    
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
        answer = "Poly("
        switch = True
        for k, v in self.terms.items():
            if switch:
                answer += "({},{})".format(v, k)
                switch = False
            else:
                answer += ",({},{})".format(v, k)
        return answer + ")"

    
    def __len__(self):
        highest = 0
        if self.terms == None:
            return 0
        switch = True
        for k in self.terms.keys():
            if switch:
                highest = k
            elif k > highest:
                highest = k
        return highest
    
    def __call__(self,arg):
        assert type(arg) == int or type(arg) == float, "Type must be an int or a float"
        total = 0
        for k, v in self.terms.items():
            total += v*(arg**k)
        return total
    

    def __iter__(self):
        def gen(poly):
            for k, v in sorted(self.terms.items(), reverse = True):
                    yield (v, k)
        return gen(self.terms)       

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index in self.terms.keys():
            return self.terms[index]
        else:    
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if (type(c) != int or type(c) != float) and (type(p) != int and p <0):
            raise TypeError
        switch = True
        for k,v in self.terms.items():
            if p == k:
                switch = False
        if switch and c != 0:
            self.terms[p] = c
        elif not switch:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        
        if type(right) == int or type(right) == float:
            pass
        elif type(right) == Poly:
            pass
        else:
            raise TypeError
    
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