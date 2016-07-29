import math
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            assert type(c) in [int,float]
            assert type(p) in [int]
            assert p >= 0
            assert p not in self.terms.keys()
            if c == 0:
                pass
            else:
                self.terms[p] = c       
        
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
        coe = []
        pow = []
        for c,p in self.terms.items():
            coe.append(c)
            pow.append(p)
        return 'Poly(('+str(pow[0])+','+str(coe[0])+'),('+str(pow[1])+','+str(coe[1])+'),('+str(pow[2])+','+str(coe[2])+'))'

    
    def __len__(self):
        pow = []
        for p,c in self.terms.items():
            pow.append(p)
        if len(pow) == 0:
            return 0
        else:
            return max(pow)
             
    
    def __call__(self,arg):
        holder = []
        for p,c in self.terms.items():
            if p != 0:
                a = (math.pow(arg,p))
                b = c*a
                holder.append(b)
            else:
                holder.append(c)
        return int(sum(holder))
        

    def __iter__(self):
        woot = []
        for p,c in self.terms.items():
            woot.append(p)
            woot.append(c)
            
            
            

    def __getitem__(self,index):
        pass
            

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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