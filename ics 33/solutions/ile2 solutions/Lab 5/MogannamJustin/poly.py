class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for item in terms:
            self.terms[item[1]] = item[0]
        ### {power: coefficient}
        
        for item in self.terms:
            if type(self.terms[item]) != int and type(self.terms[item]) != float:
                raise AssertionError('Poly.__init__: illegal power in :')
            if type(item) != int or item < 0:
                raise AssertionError('Poly.__init__: illegal power in :', item)
#         if 0 in self.terms.keys():
#             self.terms.remove()
            
            
        
            
        
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
        reprstr = ''
        for item in self.terms:
            reprstr += '({},{})'.format(self.terms[item], item)
        return 'Poly({})'.format(reprstr)
            

    
    def __len__(self):
        return max(list(self.terms.keys()))
    
    def __call__(self,arg):
        callsum = 0
        for item in self.terms:
            callsum += self.terms[item] * arg ** item
        return callsum
    

    def __iter__(self):
        for c,p in self.terms:
            yield (p,c)
        
            

    def __getitem__(self,index):
        if index < 0 or type(index) != 0:
            raise TypeError()
        return self.items[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError()
        self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError()
        del self.terms[index]            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError()
        if p < 0 or type(p) != int:
            raise TypeError
        
        
       

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