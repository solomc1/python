

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for v,k in terms:
            assert type(v) in (int, float), AssertionError('Poly.__init__: illegal coefficient in: ({},{})'.format(str(v),str(k)))
            assert k >= 0, AssertionError('Poly.__init__: illegal power in: ({},{})'.format(str(v),str(k)))
            if v == 0:
                pass
            elif k not in self.terms.keys():
                self.terms[k] = v
            else:
                raise AssertionError('A power cannot appear in a later term, if used in an earlier term')

            
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
        return 'Poly({})'.format(','.join(str((k,v)) for k,v in self.terms.items()))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(k for k in self.terms.keys())
    
    def __call__(self,arg):
        eval('{}'.format('+'.join(str(v*(arg^k)) for k,v in self.terms.items())))
    

    def __iter__(self):
        for k in sorted(self.terms.keys(), reverse = True):
            yield (self.terms[k], k)
            

    def __getitem__(self,index):
        if type(index) == int and index >= 0:
            try:
                return self.terms[index]
            except:
                return 0
        else:
            raise TypeError('The index:{} is not legal'.format(str(index)))
            

    def __setitem__(self,index,value):
        if type(index) == int and index >= 0:
            if value == 0:
                if index in self.terms.keys():
                    self.terms.remove(index)
            else:
                self.terms[index] = value
        else:
            raise TypeError('The index:{} is not legal'.format(str(index)))
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                self.terms.remove(index)
        else:
            raise TypeError('The index:{} is not legal'.format(str(index))) 
            

    def _add_term(self,c,p):
        if type(p) == int and p >= 0 and type(c) in (int, float):
            if p not in self.terms.keys():
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p] += c
                if c == 0:
                    self.terms.remove(p)
        else:
            raise TypeError('The coefficient or power are not legal')
       

    def __add__(self,right):
        result = Poly()
        if type(self) == Poly and type(right) == Poly:
            for k,v in self.terms.items():
                result._add_term(v,k)
            for k,v in right.terms.items():
                result._add_term(v,k)
        elif type(self) == Poly and type(right) in (int,float):
            for k,v in self.terms.items():
                result._add_term(v,k)
                result.terms[k] += right
        else:
            raise TypeError('The operands are of an illegal type')
        return result

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(self) == Poly and type(right) == Poly:
            return all(a == b for a,b in zip(self.terms, right.terms))

    
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