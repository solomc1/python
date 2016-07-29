class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.dummy = []
        for a in terms:
            self.dummy.append(a)
        for i,j in self.dummy:
            assert type(i) in [int,float], "Poly.__init__: Coefficient must be int or float"
            assert type(j) in [int] and j >= 0, "Poly.__init__: Power must be int and >= 0"
            assert j not in self.terms, "Poly.__init__: Power appears in earlier term"
            if i != 0:
                self.terms[j]=i
            
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
        if self == "Poly()":
            return "Poly()"
        else:
            return "Poly("+str(self)+")"

    
    def __len__(self):
        if self.terms == {} or None:
            return 0
        return max(self.terms)
    
    def __call__(self,arg):
        answer=0
        for i,j in self.terms.items():
            answer += j*arg**i
        return answer 

    def __iter__(self):
        return self
            

    def __getitem__(self,index):
        if type(index) not in [int] or index <0:
            raise TypeError
            print( "Poly.__getitem__: Argument must be integer and greater than 0")
        if index not in self.terms:
            return 0
        return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) not in [int] or index <0:
            raise TypeError
            print("Poly.__setitem__: Argument must be integer and greater than 0")
        if index == 0:
            return 
        self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index) not in [int] or index <0:
            raise TypeError
            print("Poly.__setitem__: Argument must be integer and greater than 0")
        if index not in self.terms:
            return
        del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in [int,float] and type(p) not in [int] and p <0:
            raise TypeError
            print("Poly._add_term: Invalid coefficient and/or power")
        if p in self.terms:
            self.terms[p]+=c
            if self.terms[p] == 0:
                del self.terms[p]
        if p not in self.terms and c != 0:
            self.terms[p]=c
       

    def __add__(self,right):
        if type(self) and type(right) not in [Poly, int,float]:
            raise TypeError
            print("Poly.__add__: Invalid operand types")
        if type(self) is Poly and type(right) is Poly:
            for i in self.terms:
                if i in right.terms:
                    return "Poly("+str(self.terms[i])

    
    def __radd__(self,left):
        if type(self) and type(left) not in [Poly, int,float]:
            raise TypeError
            print("Poly.__add__: Invalid operand types")
    

    def __mul__(self,right):
        if type(self) and type(right) not in [Poly, int,float]:
            raise TypeError
            print("Poly.__add__: Invalid operand types")
    

    def __rmul__(self,left):
        if type(self) and type(left) not in [Poly, int,float]:
            raise TypeError
            print("Poly.__add__: Invalid operand types")
    

    def __eq__(self,right):
        if type(self) and type(right) not in [Poly, int,float]:
            raise TypeError
            print("Poly.__add__: Invalid operand types")
        return self == right

    
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
    #===========================================================================
    # print('  list collecting iterator results:',[t for t in p])
    #===========================================================================
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()