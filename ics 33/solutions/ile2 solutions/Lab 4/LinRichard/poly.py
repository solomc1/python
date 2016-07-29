class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        r = []
        for c,p in terms:
            r.append((p,c))
        p1, c1 = r[0]
            
        if len(terms) > 0:
            for x,y in sorted(r):
                assert type(y) in (int, float), 'Poly.__init: coefficient must be an integer or float'
                assert type(x) == int and x >= 0, 'Poly.__init__: power must be an integer greater than or equal to 1'
                assert x <= p1, 'Poly.__init__: power cannot appear as a later term if it appearts as an earlier term'
                if y != 0:
                    self.terms.update({x:y})
            
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
        result = ''
        r = [(x,y) for x,y in self.terms.items()]
        for x,y in sorted(r, reverse = True):
            result += '('+str(y)+','+str(x)+'),'
        return 'Poly({})'.format(result.strip(','))

    
    def __len__(self):
        return max(p for p in self.terms.keys())
            
            
    
    def __call__(self,arg):
        result = 0
        for p,c in self.terms.items():
            result += (c*(arg**p))
        return result
    

    def __iter__(self):
        result = [(p,c) for p,c in self.terms.items()]
        for p,c in sorted(result,reverse =True):    
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__: index must be an integer')
        if index < 0:
            raise TypeError('Poly.__getitem__: index must be greater than 0')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Poly.__setitem__: index must be an integer')
        if index < 0:
            raise TypeError('Poly.__setitem__: index must be greater than 0')
        if type(value) == int and value == 0:
            del self.terms[index]
        self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__delitem__: index must be an integer')
        if index < 0:
            raise TypeError('Poly.__delitem__: index must be greater than 0')
            
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Poly._add_term: illegal coefficient')
        if type(p) != int and p<=0:
            raise TypeError('Poly._add_term: illegal power')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
#         if p in self.terms.keys():
#             x = self.terms[p]
#             self.terms[p] = x+c
#         if self.terms[p] == 0:
#             del self.terms[p]

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__add__: illegal input')
        if type(right) in (int, float):
            if 0 in self.terms.keys():
                self.terms[0] = self.terms[0] + right
            else:
                self.terms[0] = right
        else:
            for p,c in right.terms:
                if p in self.terms[p]:
                    self.terms[p] = self.terms[p] + c
                else:
                    self.terms[p] = c
        return str(self)
        
            

    
    def __radd__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Poly.__left__: illegal input')
        if 0 in self.terms.keys():
            return str(self) + ' + ' +str(self.terms[0]+left)
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__mul__: illegal input')
    

    def __rmul__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Poly.__rmul__: illegal input')
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__: illegal input')
        return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()