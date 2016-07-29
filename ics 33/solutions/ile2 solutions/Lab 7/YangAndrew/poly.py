class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for t in terms:
            if type(t[0]) != float and type(t[0]) != int:
                raise AssertionError('Poly.__init__: illegal coefficient in {}'.format(t))
            if type(t[1]) != int:
                raise AssertionError('Poly.__init__: illegal power in {}'.format(t))
            assert t[1] >= 0
            assert t[1] not in self.terms.keys()
            if t[0] != 0:
                self.terms[t[1]] = t[0]
       
        
            
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
        temp = list((k,v) for k, v in self.terms.items())
        return 'Poly({})'.format(str(temp)[1:-1])

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            max = 0
            for k in self.terms.keys():
                if k > max:
                    max = k
            return max
    
    def __call__(self,arg):
        sum = 0
        for k, v in self.terms.items():
            if k == 0:
                sum += v
            else:
                temp = pow(arg, k)
                temp *= v
                sum += temp
        return sum
    
    def __iter__(self):
        to_iter = iter([(v,k) for k,v in self.terms.items()])
        for i in sorted(to_iter, key = lambda x: x[1], reverse = True):
            yield i
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly:.__getitem__: illegal index')
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly:.__setitem__: illegal index')
        if value == 0:
            if 0 in self.terms.keys():
                del self.terms[0]
        self.terms[index] = value
            
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly:.__delitem__: illegal index')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Poly:._add_term: illegal coefficient')
        if type(p) != int or p < 0:
            raise TypeError('Poly:._add_term: illegal power')
        if p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        else:
            self.terms[p] = c
       

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly:.__eq__: illegal comparison')
        empty = Poly()
        if type(right) == Poly:
            for k,v in self.terms.items():
                if k in right.terms.keys(): 
                    empty._add_term(k, v)
            for k,v in right.terms.items():
                if k not in self.terms.keys():
                    empty._add_term(k,v)
            return empty
        else:
            for k,v in self.terms.items():
                empty._add_term(k, v+ right)
            return empty
                    
            
    
    def __radd__(self,left):
        self + left
    

    def __mul__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly:.__eq__: illegal comparison')
        if type(right) == Poly:
            pass
        else:
            pass
    

    def __rmul__(self,left):
        self * left
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly:.__eq__: illegal comparison')
        if type(right) == Poly:
            if self.terms == right.terms:
                return True
            else:
                return False
        elif type(right) == int or type(right) == float:
            if right in self.terms.values():
                if len(self.terms) == 1:
                    return True
                else:
                    return False
            return False
            

    
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
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()