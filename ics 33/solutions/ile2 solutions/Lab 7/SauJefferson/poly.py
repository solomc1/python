class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}

        for i in terms:
            if type(i[0]) not in (float,int) or type(i[1]) != int:
                raise AssertionError('Poly.__init__: terms must be either float or int, pwoer must be int' )
            elif i[1] < 0:
                raise AssertionError('Poly.__init__: power must be greater than or eqaul to 0')
            elif i[0] == 0:
                pass
            elif i[1] not in self.terms: 
                self.terms[i[1]]=i[0]
            elif i[1] in self.terms:
                if i[0] == 0:
                    self.terms[i[1]]=i[0]
                else:
                    raise AssertionError('Poly.__init__: cannot have two of the same powers')
#             
#        Fill in the rest of this method, using *terms to intialize self.terms

            
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
        pass
    
    def __len__(self):
        if self.terms =={}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        sumof = 0
        for k,v in self.terms.items():
            sumof +=(v)*(arg**k)
        return sumof
    

    def __iter__(self):
        for k,v in sorted((self.terms.items()),reverse=True):
            yield (v,k)

                
            
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('must be int that is greater than 0')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError('must be int that is greater than 0')
        elif value == 0:
            if index in self.terms:
                del self.terms[index]
            else:
                pass
        else:
            self.terms[index]= value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('must be int that is greater than 0')
        if index in self.terms:
            del self.terms[index]
        else:
            pass
            

    def _add_term(self,c,p):
        if type(c) not in (float,int) or type(p) != int:
            raise AssertionError('Poly.add :_term terms must be either float or int, power must be int' )
        elif p <0:
            raise AssertionError('power must be greater than eqaul to 0')
        elif p not in self.terms:
            self.terms[p] = c
        elif p in self.terms:
            x= c+ self.terms[p]
            self.terms[p]= x
       

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
#     
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()