class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c,p in terms:
            if (type(c) == int or type(c) == float) and (type(p) == int and p >= 0):
                if p not in self.terms.keys():
                    self.terms[p] = c  
                else: raise AssertionError('Poly.__init__: illegal power in :({},{})'.format(c,p))
            else:
                raise AssertionError('Poly.__init__: illegal power in :({},{})'.format(c,p))  
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
        return ('Poly{}'.format(tuple((k,v) for k,v in self.terms.items())))
        

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return (max(self.terms.keys()))
    
    def __call__(self,arg):
        fin = 0
        for p,v in self.terms.items():
            fin += v*arg^p
        return fin
    

    def __iter__(self):
        l=[]
        for p,v in (self.terms.items()):
            l.append((p,v))
        l.sort(reverse = True)
        for p,v in l:
            yield (v,p)
            
            

    def __getitem__(self,index):
        if type(index) == int and index > 0:
            if self.terms[index] != None:
                return self.terms[index]
            else:
                raise TypeError('Index not in dict')
        else:
            return 0
            
            

    def __setitem__(self,index,value):
        if type(index) == int and index > 0:
            self.terms[index] = value
        elif value == 0:
            if self.terms[index] != None:
                self.terms.delitem(index)
        else:
            raise TypeError('Invalid index')

    def __delitem__(self,index):
        if type(index) == int and index >0:
            if self.terms[index] != None:
                self.terms.delitem(index)
        else:
            raise TypeError('Invalid index')
            

    def _add_term(self,c,p):
        if (type(c) == int or type(c) == float) and type(p) == int and p >= 0:
            if c != 0 and p not in self.terms.keys():
                self.terms[p] = c
            elif c != 0 and p in self.terms.keys():
                if self.terms[p] + c == 0:
                    self.terms.delitem(p)
                else:
                    self.terms[p] += c
                
       

    def __add__(self,right):
        #unfinished
        l = []
        if type(right) == Poly:
            for a,b in right.terms.items():
                for c,d in self.terms.items():
                    if a == c:
                        l.append((a,b+d))
                    elif a != c:
                        l.append((a,b))
                        l.append((c,d))
        else:
            pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right)==Poly:
            if right.terms.keys() == self.terms.keys():
                return True
            else:
                return False
        elif type(right) == int or type(right)==float:
            if len(self.terms.keys()) == 1 and self.terms.keys()[0] == right:
                return True
            else:
                return False
        else:
            raise TypeError('Invalid operand type')

    
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