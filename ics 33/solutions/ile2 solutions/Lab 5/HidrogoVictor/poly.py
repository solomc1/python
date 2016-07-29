class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        for c,p in terms:
            assert type(c) in (int,float), 'Poly.__init__: illegal coefficient in : ('+str(c)+','+str(p)+').'
            assert type(p) is int and p >= 0, 'Poly.__init__: illegal power in : ('+str(c)+','+str(p)+').'
            
        self.terms = {p:c for c,p in terms if c != 0}
        
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
        return 'Poly'+str(tuple((c,p) for p,c in self.terms.items()))

    
    def __len__(self):
        if self.terms != {}:
            for p,c in self.terms.items():
                highest = 0
                highest = p if p > highest else highest
            return highest
        else:
            return 0
    
    def __call__(self,arg):
        return eval(str(p).replace('x^','*'+str(arg)+'**').replace('x','*'+str(arg)))
    

    def __iter__(self):
        tuples = [(c,p) for p,c in self.terms.items()]
        for i in sorted(tuples,key=lambda x: x[1],reverse=True):
            yield i
            

    def __getitem__(self,index):
        if not type(index) in (int,float) or index < 0:
            raise TypeError('Poly.__getitem__: '+str(index)+'must be integer > 0')
        elif index == 0:
            del(self.terms[0])
        elif not index in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if not type(index) in (int,float) or index < 0:
            raise TypeError('Poly.__settitem__: '+str(index)+'must be integer > 0')
        elif index == 0:
            del(self.terms[0])
        elif not index in self.terms:
            return 0
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if not type(index) in (int,float) or index < 0:
            raise TypeError('Poly.__deltitem__: '+str(index)+'must be integer > 0')
        elif index == 0:
            del(self.terms[0])
        elif not index in self.terms:
            return 0
        else:
            del(self.terms[0])
            

    def _add_term(self,c,p):
        if not type(c) in (int,float):
            raise TypeError('Poly._add_term: '+str(c)+' must be a numeric integer')
        elif type(p) != int or p < 0:
            raise TypeError('Poly._add_term: '+str(p)+' must be a numeric integer and > 0')
        elif not p in self.terms and p != 0:
            self.terms[p] = c
        else:
            self.terms[p] += c
       

    def __add__(self,right):
        if not type(right) in (int,float,Poly):
            raise TypeError('Poly.__add__: invalid operand '+str(right))
        else:
            return self

    
    def __radd__(self,left):
        if not type(left) in (int,float,Poly):
            raise TypeError('Poly.__add__: invalid operand '+str(left))
    

    def __mul__(self,right):
        if not type(right) in (int,float,Poly):
            raise TypeError('Poly.__add__: invalid operand '+str(right))
    

    def __rmul__(self,left):
        if not type(left) in (int,float,Poly):
            raise TypeError('Poly.__add__: invalid operand '+str(left))
    

    def __eq__(self,right):
        if not type(right) in (int,float,Poly):
            raise TypeError('Poly.__add__: invalid operand '+str(right))
        else:
            return self == right

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-1,1), (4,0))
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