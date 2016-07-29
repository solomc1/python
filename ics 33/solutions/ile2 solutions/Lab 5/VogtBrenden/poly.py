class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.rawterms = terms
        self.terms = {}
        for item in terms:
            assert type(item[0])in [int,float], ('not correct type: '+str(item[0]))
            assert type(item[1])in [int], ('illegal power in: '+str(item))
            assert item[1]>=0, ('exponent not greater than 0')
            if item[0] !=0 and item[-1] in self.terms:
                raise AssertionError ('not valid input for same exponents')
            if item[0] != 0:
                self.terms[item[-1]]=item[0]
        
        
        
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
        return self.__class__.__name__+str(self.rawterms)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        assert type(arg) in [int,float]
        result = 0
        for expo,coef in self.terms.items():
            result += (arg**expo)*coef
        return result
    

    def __iter__(self):
        for item in sorted(self.rawterms,key = lambda x: x[-1],reverse = True):
            yield item
            

    def __getitem__(self,index):
        if type(index) =='int' or index<0:
            raise TypeError(str(index)+' not of correct type or is less than zero')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) not in [int] or index<0:
            raise TypeError(str(index)+' not of correct type or is less than zero')
        if index in self.terms and value == 0:
            del self.terms[index]
        elif index not in self.terms and value == 0:
            pass
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index) not in [int] or index<0:
            raise TypeError(str(index)+' not of correct type or is less than zero')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        assert type(c) in [int,float]
        if type(p) not in [int] or p<0:
            raise TypeError(str(index)+' not of correct type "int" or is less than zero')
        if c == 0:
            return
        if p in self.terms.keys():
            self.terms[p]+=c
            if self.terms[p]==0:
                del self.terms[p]
        else:
            self.terms[p]=c

    def __add__(self,right):
        assert type(right)in [int,float,Poly]
        if type(right)==int:
            if 0 in self.terms.keys():
                self.terms[0]+=right
                if self.terms[0]==0:
                    del self.terms[0]
            else:
                self.terms[0]=right
        else:
            for power,coef in right.terms.items():
                if power in self.terms:
                    self.terms[power] += coef
                    if self.terms[power] == 0:
                        del self.terms[power]
                elif coef != 0:
                    self._add_term(coef, power)
        return self
                

    
    def __radd__(self,left):
        print(left)
        assert type(left)in [int,float,Poly]
        if type(left)==int:
            if 0 in self.terms.keys():
                self.terms[0]+=left
                if self.terms[0]==0:
                    del self.terms[0]
            else:
                self.terms[0]=left
        else:
            for power,coef in left.terms.items():
                if power in self.terms:
                    coef+=self.terms[power]
                    if self.terms[power] == 0:
                        del self.terms[power]
                elif coef != 0:
                    self._add_term(coef, power)
        return self
    

    def __mul__(self,right):
        if type(right)==int:
            for power,coef in self.terms.items():
                self.terms[power] = self.terms[power]*right
            return self
            if self.terms[power]==0:
                del self.terms[0]
        else:
            for power,coef in self.terms.items():
                for power1,coef1 in right.terms.items():
                    self.terms[power] = self.terms[power]*right.terms[power]
                if self.terms[power]==0:
                    del self.terms[0]
            return self
#             self.terms[0]=right 
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right)not in [Poly,int,float]:
            raise TypeError
#         state = True
#         for i in self.terms.keys():
#             if right not in 
        return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly()#(3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
    print('  list collecting iterator results:',[t for t in p])
#     p[0] = 0
    print(p)
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()