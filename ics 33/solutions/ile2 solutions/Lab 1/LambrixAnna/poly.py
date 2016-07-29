from collections import defaultdict
from copy import copy
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = defaultdict()
        for i in terms:
            assert isinstance(i[0], int) or isinstance(i[0], float),'Poly.__init__: Coefficient must be integer or float'
            assert isinstance(i[1], int) and i[1]>=0, 'Poly.__init__: Power must be integer larger or equal to zero'
            if i[0] !=0:
                assert i[1] not in self.terms.keys(), 'Poly.__init__:already in the dictionary'
                self.terms[i[1]] = i[0]
                
            
            
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
        return 'Poly{}'.format(tuple((v, k) for k, v in self.terms.items()))

    
    def __len__(self):
        l = list(k for k in self.terms.keys())
        if l != []:
            return max(l)
        else:
            return 0
    
    def __call__(self,arg):
        assert type(arg) is int or type(arg) is float, 'Poly.__call__: argument must be integer or float'
        answer = 0
        for k, v in self.terms.items():
            answer+= (arg**k)*v
        return answer
            
    

    def __iter__(self):
        l = sorted(list((v, k) for k, v in self.terms.items()), key= lambda x: x[1], reverse=True)
        it = iter(l)
        return it
        
        
            

    def __getitem__(self,index):
        if type(index) is int and index>=0:
            if index in self.terms.keys():
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError('Poly.__getitem__: index must be an integer and larger or equal to zero')
            

    def __setitem__(self,index,value):
        if type(index) is int and index>=0:
            if value !=0:
                self.terms[index] = value
            else:
                if index in self.terms.keys():
                    del self.terms[index]
                
        else:
            raise TypeError('Poly.__setitem__: index must be an integer and larger or equal to zero')
            
            

    def __delitem__(self,index):
        if type(index) is int and index>=0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            raise TypeError('Poly.__delitem__: index must be an integer and larger or equal to zero')
            

    def _add_term(self,c,p):
        if (type(c) is int or type(c) is float) and (type(p) is int and p>=0):
            if p not in self.terms.keys() and c!=0:
                self.terms[p] = c
            elif p not in self.terms.keys() and c==0:
                pass
            else:
                self.terms[p] = self.terms[p]+c
                if self.terms[p] == 0:
                    del self.terms[p]
                
        else:
            raise TypeError('Poly._add_term: index must be an integer and larger or equal to zero')
       

    def __add__(self,right):
        if type(right) is Poly or type(right) is int or type(right) is float:
            if type(right) is int or type(right) is float:
                right = Poly((right, 0))
            p = Poly()
            p.__dict__ = copy(self.__dict__)
            for k, v in right.terms.items():
                p._add_term(v, k)
            return p
        else:
            raise TypeError('Poly.__add__: right argument must be a Poly or an integer/float')

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) is Poly or type(right) is int or type(right) is float:
            pass #no time left
        else:
            raise TypeError('Poly.__mul__: right argument must be a Poly or an integer/float')
    

    def __rmul__(self,left):
        pass #no time left
    

    def __eq__(self,right):
        if type(right) is Poly or type(right) is int or type(right) is float:
             if type(right) is int or type(right) is float:
                 return right in [self.terms[k] for k in self.terms.keys()]
             else:
                 return self.terms == right.terms 
        else:
           raise TypeError('Poly.__eq__: right argument must be a Poly or an integer/float') 
         

    
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
    p1 = Poly((1,1),(2,0))
    p2 = Poly((3,2),(2,1),(1,0))
    p3 = Poly((3,5),(-2,2),(-4,0))
    print('sum: For some reason this is the same test as 91, but in bsc 91 does not pass while here it DOES:', p1+p3) #-->3x^5 - 2x^2 + x - 2
    print('sum of p3 and 2 again works here but not in bsc:', p3 +2)
    
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()