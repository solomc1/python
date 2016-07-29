class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c, p in terms:
            assert type(c) is int or type(c) is float, "Poly.__init__: illegal coefficient({}).".format(c)
            assert type(p) is int and p >= 0, "Poly.__init__: illegal power({}).".format(p)
            if c != 0:
                assert p not in self.terms, "Poly.__init__: power({}) already exists.".format(p)
                self.terms[p] = c
            
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
        result=''
        for p, c in self.terms.items():
            if not result == '':
                result += ','
            result += '({},{})'.format(c,p)
        return "Poly({})".format(result)
    
    def __len__(self):
        return 0 if len(self.terms.keys())==0 else max(list(self.terms.keys()))
#         maximum=0
#         for power in self.terms:
#             maximum=power
#         for power in self.terms:
#             if power>maximum:
#                 maximum=power
#         return maximum
#     '''########FIXFIXFIXFIXFIX###############'''
    
    def __call__(self,arg):
        result=0
        for p, c in self.terms.items():
            result+=c*arg**p
        return result
    

    def __iter__(self):
        for p in sorted(self.terms,reverse=True):
            yield self.terms[p], p
            

    def __getitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError('Poly.__getitem__: illegal index({})'.format(index))
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: illegal power({})'.format(index))
        elif value != 0:
            self.terms[index] = value
        elif index in self.terms:
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError('Poly.__delitem__: illegal power({})'.format(index))
        elif index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if p not in self.terms and c!=0:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c == 0:
                del self.terms[p]
            else:
                self.terms[p] = self.terms[p] + c
       

    def __add__(self,right):
        if type(right) is not int and type(right) is not float and type(right) is not Poly:
            raise TypeError('Poly.__add__: illegal object')
        
        result = Poly()
        for p, c in self.terms.items():
            result._add_term(c, p)
            
        if type(right) is int or type(right) is float:
            result._add_term(right, 0)
        else:
            for pr, cr in right.terms.items():
                result._add_term(cr, pr)
        return result

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) is not int and type(right) is not float and type(right) is not Poly:
            raise TypeError('Poly.__mul__: illegal object')
        
        result=Poly()
        if type(right) is int or type(right) is float:
            for p, c in self.terms.items():
                result._add_term(c*right,p)
        else:
            for p, c in self.terms.items():
                for pr, cr in right.terms.items():
                    result._add_term(c*cr, p+pr)
        return result

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) is not int and type(right) is not float and type(right) is not Poly:
            raise TypeError('Poly.__eq__: illegal type({})'.format(type(right)))
        elif type(right) is int or type(right) is float:
            if list(self.terms.keys()) == [0]:
                return self.terms[0] == right
            else:
                return False
        else:
            return self.terms.items() == right.terms.items()

    
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
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()