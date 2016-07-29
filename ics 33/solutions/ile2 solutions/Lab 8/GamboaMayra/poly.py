from goody import type_as_str
import math

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for c, p in self.terms:
            if type(c) not in [int, float]:
                raise AssertionError('Poly.__init__: ({}) must be int/float type'.format(type_as_str(c)))
            assert isinstance(p, int)
            if p < 0:
                raise AssertionError()        #
        #clist = [t[0] for t in terms] 
        plist = [p for c,p in self.terms]
        if len(plist) != len(set(plist)):
            raise AssertionError()
                      
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
        return 'Poly(' + ','.join(['('+str(c)+',' + str(p) +')' for c, p in self.terms ]) + ')'

    
    def __len__(self):
        powerlist = [t[1] for t in self.terms]
        powerlist.sort()
        return powerlist[-1]
                     
    
    def __call__(self,arg):
        assert isinstance(arg, int)
        assert isinstance(arg, float)
        for c, p in self.terms:
            return (c*arg) ** p + (c*arg)**p + (c*arg) **p
    

    def __iter__(self):
        for t in sorted(self.terms, key = lambda x: x[1], reverse = True):
            yield (t[0], t[1])
                    

    def __getitem__(self,index):
        return self.terms[index]
        if type(index) != int or index <0:
            raise TypeError()
                    

    def __setitem__(self,index,value):
        for index, value in self.terms:
            if type(index) != int or index < 0:
                raise TypeError()
            if value == 0:
                del index
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0 :
            raise TypeError()
        for index in self.terms.keys():
            if index in self.terms.keys():
                del index
                
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError()
        if type(p) != int or p < 0:
            raise TypeError()
        if p not in self.terms and p !=0:
            return c, p
        
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError()
        if type(right) in [int, float]:
            return self._add_term(self, right.c, right.p)
        if type(right) in Poly:
            return self._add_term(self, right.c, right.p)

    
    def __radd__(self,left):
        return left + self
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError()
    

    def __rmul__(self,left):
        return left * self
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError()
        else:
            
            return self.terms == right.terms

    
if __name__ == '__main__':
    pass
    # Some simple tests; you can comment them out and/or add your own before
#