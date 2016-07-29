# Katherine Fitzpatrick Lab 6
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms\
        for term in terms:
            if type(term[0]) not in (int,float):
                
                raise AssertionError('Poly.__init__: illegal power in', term)
            elif type(term[1]) not in (int,float):
                raise AssertionError('Poly.__init__: illegal power in', term)
            elif term[1] < 0:
                raise AssertionError('Poly.__init__: illegal power in', term)
            else:
                if term[1] not in self.terms.keys() and term[0] != 0:
                    self.terms[term[1]] = term[0]
                else:
                    raise AssertionError('Poly.__init__: illegal power in', term)
                
                
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
        s = ''
        for power in self.terms.keys():
            s += "({},{}),".format(self.terms[power], power)
        return 'Poly({})'.format(s.strip(','))

    
    def __len__(self):
        highest = 0
        for power in self.terms.keys():
            if int(power) > highest:
                highest = int(power)
        return highest
    
    def __call__(self,arg):
        result = 0
        for power in self.terms.keys():
            result += ((arg**power)*self.terms[power])
        return result
    

    def __iter__(self):
        keys = sorted(self.terms.keys(), reverse=True)
        for power in keys:
            yield (self.terms[power], power)#'({},{})'.format(self.terms[power],power)
            

    def __getitem__(self,index):
        if type(index)!= int:
            raise TypeError('Poly.__getitem__: illegal index: '+ index)
        elif index<0:
            raise TypeError('Poly.__getitem__: illegal index: '+ index)
        else:
            if index in self.terms.keys():
                return self.terms[index]
            else: return 0

    def __setitem__(self,index,value):
        if type(index) and type(value) != int:
            raise TypeError('Poly.__setitem__: illegal index: '+ index)
        elif index and value < 0:
            raise TypeError('Poly.__setitem__: illegal index: '+ index)
        elif value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__delitem__: illegal index: '+ index)
        elif index <0:
            raise TypeError('Poly.__delitem__: illegal index: '+ index)
        else:
            if index in self.terms.keys():
                del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Poly._add_term: illegal coefficient: '+ c)
        elif type(p) != int:
            raise TypeError('Poly._add_term: illegal power: '+ p)
        elif p < 0:
            raise TypeError('Poly._add_term: illegal power: '+ p)
        else:
            if p not in self.terms.keys():
                if c != 0:
                    self.terms[p] = c
            elif p in self.terms.keys():
                if c != 0:
                    self.terms[p] = self.terms[p]+c
                    if self.terms[p] == 0:
                        del self.terms[p]
                elif c == 0:
                    del self.terms[p]

       

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('Poly.__add__: illegal argument: '+ right) 
        else:
            self_double = self
            if type(right) in (int,float):
                right = Poly((right,0))
            for pow in right.terms.keys():
                self_double._add_term(right.terms[pow], pow)
            return self_double
                    

    
    def __radd__(self,left):
        if type(left) not in (int,float,Poly):
            raise TypeError('Poly.__add__: illegal argument: '+ left) 
        else:
            self_double = left
            if type(self) in (int,float):
                self = Poly((self,0))
            for pow in self.terms.keys():
                self_double._add_term(self.terms[pow], pow)
            return self_double
    

    def __mul__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('Poly.__add__: illegal argument: '+ right)
        else:
            self_double = self
            #out of time!
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass
#         if type(right) not in (int,float,Poly):
#             raise TypeError('Poly.__add__: illegal argument: '+ right)
#         else:
#             return self == right

    
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