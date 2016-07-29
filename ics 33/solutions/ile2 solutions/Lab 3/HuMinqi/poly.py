class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c,p in terms:
            assert type(c) in [int, float],'coefficient'+str(c)+'is not int or float'
            assert p >= 0,'power'+str(p)+'is not greater than 0'
            assert type(p) is int,'Poly.__init__:illegal power in:'+str(p)+'.'
            assert p not in self.terms and c != 0,'same power twice'+str(p)+'.'
            self.terms[p].add(c)
            
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
        return 'Poly('+','.join((c,p) for p,c in self.terms.items())+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) in [int,float],'AssertionError'+str(arg)+'should be numeric'
        value = 0
        for p,c in self.terms:
            value += c*(arg**p)
        return value
            
    def __iter__(self):
        it = iter(sorted(self.terms.items(),reverse = True))
        t = next(it)
        yield (self.terms[t],t)
            
    def __getitem__(self,index):
        if type(index) != int or index <= 0:
            raise TypeError('Index'+str(index)+'is not int or greater than 0')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]**index
        
    def __setitem__(self,index,value):
        if type(index) != int or index <= 0:
            raise TypeError('Index'+str(index)+'is not int or greater than 0')
        for index,value in self.terms:
            if value == 0:
                del self.terms[index]
            
    def __delitem__(self,index):
        if type(index) != int or index <= 0:
            raise TypeError('Index'+str(index)+'is not int or greater than 0')
        else:
            if index in self.terms.items():
                self.terms.pop(index)
                
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('coefficient'+str(c)+'should be int or float')
        elif type(p) != int:
            raise TypeError('power'+str(p)+'should be a int')
        elif p < 0:
            raise TypeError('Power'+str(p)+'should be positive')
        else:
            if p not in self.terms.items():
                self.terms.update(p,c)
            elif c == 0:
                self.terms.pop(c)
            else:
                self.terms[p] = c
       

    def __add__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('right'+str(right)+'should be a Polynomial or int or float')
        elif type(right) == Poly:
            newc = 0
            for right.c,right.p in right:
                if self.p == right.p:
                    newc = self.c + right.c
                    self.terms.pop(self.c)
            return self.terms.update(p,newc)
            
        elif type(right) in [int,float]:
            return self.terms.update(0,self.c + right)
                
    
    def __radd__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError('left'+str(left)+'should be a Polynomial or int or float')
        elif type(left) == Poly:
            newc = 0
            for left.c,left.p in left:
                if self.p == left.p:
                    newc = self.c + left.c
                    self.terms.pop(self.c)
            return self.terms.update(p,newc)
            
        elif type(left) in [int,float]:
            return self.terms.update(0,self.c + left)
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('right'+str(right)+'should be a Polynomial or int or float')
        elif type(right) == Poly:
            pass
        elif type(right) in [int,float]:
            for i in self.terms:
                self.terms.update(i,self.c*right)

    def __rmul__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError('left'+str(left)+'should be a Polynomial or int or float')
        elif type(left) == Poly:
            pass
        elif type(left) in [int,float]:
            for i in self.terms:
                self.terms.update(i,self.c*left)
    

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