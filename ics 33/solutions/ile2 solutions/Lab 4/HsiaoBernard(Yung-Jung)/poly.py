

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if i[0] == 0:
                raise AssertionError
            if i[1] < 0 :
                raise AssertionError
            
      #      self.terms[i[0]].add[i[1]]
            
        self.terms = (3,2),(-2,1),(4,0)
        print(self.terms)
                  
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
        return 'Poly('+str(self.terms)+')'

    
    def __len__(self):
        y = 0
        for i in self.terms:
            y += 1 
        return y
    
    def __call__(self,arg):
        z = 0
        for i in self.terms:
            x = arg**i[1]
            y = x*i[0]
            z += y
        return z 
    

    def __iter__(self):
        for i in self.terms:
            yield i
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError
        if self.terms.items(index) == None:
            return 0
        else:
            return self.terms.items(index)
            

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError
            

    def _add_term(self,c,p):
        if p == 0 and c == 0:
            raise TypeError 
        self.term[c].add[p]
        return self
       

    def __add__(self,right):
        if type(right) != Poly:
            raise TypeError
        
        for i in range(max(len(self.terms),len(right.terms))):
            if self.terms[i][1] == right.terms[i][1]:
                self.terms[i][1] += right.terms[i][0]
        return self

    
    def __radd__(self,left):
        if type(left) != Poly:
            raise TypeError
        for i in range(max(len(self.terms),len(left.terms))):
            if self.terms[i][1] == self.terms[i][1]:
                self.terms[i][0] += left.terms[i][0]
        return self
    

    def __mul__(self,right):
        if type(right) != Poly:
            raise TypeError
        for i in range(max(len(self.terms),len(right.terms))):
            if self.terms[i][1] == self.terms[i][1]:
                self.terms[i][0] *= right.terms[i][0]
        return self
            
    

    def __rmul__(self,left):
        if type(left) != Poly:
            raise TypeError
        for i in range(max(len(self.terms),len(left.terms))):
            if self.terms[i][1] == self.terms[i][1]:
                self.terms[i][0] *= left.terms[i][0]
        return self
    

    def __eq__(self,right):
        if type(right) != Poly:
            raise TypeError
        if self.terms == self.right:
            return 
            

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    #print('  str(p):',p)
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