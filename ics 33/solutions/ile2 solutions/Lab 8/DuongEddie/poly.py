class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for item in terms:
            assert type(item[0]) in [int,float]
            assert type(item[1]) == int and item[1] >= 0
            assert type(item[1]) not in self.terms.keys()
            self.terms[item[1]] = [item[0]]
            
        self.args = terms
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
        return 'Poly({})'.format(self.args)

    
    def __len__(self):
        power = 0 
        for k, v in self.terms.items():
            if k > power:
                power = k
        return power 
    
    def __call__(self,arg):
        value = 0
        
        assert type(arg) in [int,float]
        for k,v in self.terms.items():
            value += v * arg**k
        return value
    

    def __iter__(self):
        for item in sorted(self.terms.keys(),reverse = True):
            yield (self.terms[item],item)
            

    def __getitem__(self,index):
        if  index < 0 or type(index) != int:
            raise TypeError('Poly.__getitem__: index has to be an integer and greater than 0')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if index < 0 or type(index) != int:
            raise TypeError('Poly.__setitem__: index has to be an integer and greater than 0')
        if value == 0 and index in self.terms.keys():
            del self.terms[index] 
        else:
            if value != 0:
                self.terms[index] = value
            
            
    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError('Poly.__delitem__: index has to be an integer and greater than 0')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and p > 0:
            raise TypeError('Poly.__add_term__: coefficient has to be an integer and power has to be less than than 0')
        if c != 0:
            if p not in self.terms.keys():
                self.terms[p] = c
            else:
                self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
    
       

    def __add__(self,right):
#         if type(right) not in [int,float,Poly]
#         raise TypeError
        pass

    
    def __radd__(self,left):
#         if type(left) not in [int,float,Poly]
#         raise TypeError
        pass
    

    def __mul__(self,right):
#         if type(right) not in [int,float,Poly]
#         raise TypeError
        pass
    

    def __rmul__(self,left):
#         if type(left) not in [int,float,Poly]
#         raise TypeError
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