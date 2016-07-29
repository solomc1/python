class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert type(t[0]) in (float,int)
            assert type(t[1]) == int and t[1] >= 0
            assert t[1] not in self.terms
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
        s = 'Poly('
        a = []
        for k,v in self.terms.items():
            a.append('('+str(v)+','+str(k)+')')
        s += ','.join(a)
        s += ')'
        return s

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        sum = 0
        for k,v in self.terms.items():
            sum += (arg**k * v)
        return sum
    

    def __iter__(self):
        s = sorted(self.terms,reverse=True)
        for x in s:
            yield (self.terms[x],x)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        if value == 0 and index in self.terms:
            self.terms.pop(index)
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (float,int) or type(p) != int or p < 0:
            raise TypeError
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.terms.pop(p)
                
       

    def __add__(self,right):
        if type(right) == Poly:
            new = eval(repr(self))
            for p,c in right.terms.items():
                new._add_term(c,p)
            return new
        elif type(right) in (float,int):
            new = eval(repr(self))
            new._add_term(right,0)
            return new
        else:
            raise TypeError

    
    def __radd__(self,left):
        if type(left) in (float,int):
            new = eval(repr(self))
            new._add_term(left,0)
            return new
        else:
            raise TypeError
        
        
    def __mul__(self,right):
        if type(right) == Poly:
            new = Poly()
            for p1,c1 in self.terms.items():
                for p2,c2 in right.terms.items():
                    new._add_term(c1*c2,p1+p2)
            return new
        elif type(right) in (int,float):
            new = Poly()
            for p,c in self.terms.items():
                new._add_term(c*right,p)
            return new
        else:
            raise TypeError
    

    def __rmul__(self,left):
        if type(left) in (int,float):
            new = Poly()
            for p,c in self.terms.items():
                new._add_term(c*left,p)
            return new
        else:
            raise TypeError


    def __eq__(self,right):
        if type(right) == Poly:
            if sorted(self.terms.items()) != sorted(right.terms.items()):
                return False
            return True
        elif type(right) in (int,float):
            if len(self.terms) == 1 and 0 in self.terms and self.terms[0] == right:
                return True
            else:
                return False
        else:
            raise TypeError

    
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