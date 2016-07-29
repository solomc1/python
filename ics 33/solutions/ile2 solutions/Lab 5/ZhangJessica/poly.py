
class Poly:
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.t = terms
        self.terms = {}
        for i in terms:
            self.coef = i[0]
            self.power = i[1]
            if type(self.coef) not in (float, int) or type(self.power) != int or self.power < 0 :
                raise AssertionError
            elif self.coef == 0:
                self.terms.update({})
            else: self.terms.update({self.power:self.coef})
     
            
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
        return 'Poly{}'.format(self.t)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else: return max(self.terms.keys())
    
    def __call__(self,arg):
        if self.terms == {}:
            return 0        
        
    def __iter__(self):
        return iter(self.t)
            
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms:
            return 0
        else:return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0 :
            raise TypeError
        elif value == 0:
            self.terms[index]=value
            del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms:
            self.terms = self.terms
        else: del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (float,int) or type(p) != int or p < 0:
            raise TypeError
        elif c == 0:
            self.terms = self.terms
        return self.terms.update({p:c})
            
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (float,int,Poly):
            raise TypeError
        elif type(right) == int:
            return self.coef == right
        else: return self.power == right.power and self.coef == right.coef            
    
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    #print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
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
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()