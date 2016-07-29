class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.tup = terms
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for each_num in self.tup:
 
            if each_num[1] < 0:
                raise AssertionError()                
            for nums in each_num:
                if type(nums) not in [int, float]:
                    raise AssertionError('Poly.__init__'+str(*terms)+'must be float or int')
                
        # assert *terms >= 0, AssertionError()
        # need one mor assert statement
        
            
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
        if self.tup == ():
            return 'Poly()'
        return '(Poly'+str(self.tup)+')'

    def __len__(self):
        pl = []
        for power in self.tup:
            pl.append(power[1])
        pl.sort
        return pl[0]
               
    def __call__(self,arg):
        if type(arg) in [int,float]:
            sums = []
            for each_num in self.tup:
                sums.append((each_num[0])*arg**each_num[1])
            s = sum(sums)    
        else:
            raise AssertionError() ###
        return s
     

    def __iter__(self):
        def _gen(iterator):
            for each in iterator:
                yield each
        return _gen(self.tup)

    def __getitem__(self,index):
        if type(index) not in [int]:
            raise TypeError('Poly.__getitem__:'+str(index)+'must be an int')
        if index < 0:
            raise TypeError('Poly.__getitem__:'+str(index)+'must be greater than 0')
        else:
            return self.tup[index]
            

    def __setitem__(self,index,value):
        if type(index) not in [int]:
            raise TypeError('Poly.__getitem__:'+str(index)+'must be an int')
        if index < 0:
            raise TypeError('Poly.__getitem__:'+str(index)+'must be greater than 0')
        else:
            self.__dict__[index] = value
        return self.__dict__[index]
    
    def __delitem__(self,index):
        if type(index) not in [int]:
            raise TypeError('Poly.__delitem__:'+str(index)+'must be an int')
        if index < 0:
            raise TypeError('Poly.__delitem__:'+str(index)+'must be greater than 0')
        else:
            print(self.tup[index])
            for k,v in self.__dict__.items():
                if k == 'tup':
                    k.rem(v[index])
            
    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError
        if type(p) not in [int]:
            raise TypeError()
        if p < 0:
            raise TypeError()
       

    def __add__(self,right):
        if right is Poly:
            return (self.x + right.y, self.y + right.y)
        if right is [int,float]:
            return (self.x + right, self.y + right)
#         if right not in [int,float,Poly]:
#             raise TypeError()

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