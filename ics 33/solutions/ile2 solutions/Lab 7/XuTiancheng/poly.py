class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            power=t[1]
            coef=t[0]
            if type(coef) not in [int,float]:
                raise AssertionError('The coefficient must be int or float.')
            if type(power)!=int:
                raise AssertionError('The power must be int.')
            if type(power)==int and power<0:
                raise AssertionError('The power must be greater than or equal to 0.')
            if power in self.terms:
                raise AssertionError('The power has already existed.')
            if coef!=0:
                self.terms[power]=coef

        
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
        args=[]
        for p,c in self.terms.items():
            args.append((c,p))
        args=tuple(args)
        return ('Poly'+str(args))

    
    def __len__(self):
        if len(self.terms.keys())==0:
            return 0
        else:
            length=max(self.terms.keys())
            return length
        
    
    def __call__(self,arg):
        result=0
        for p,c in self.terms.items():
            result+=c*(arg**p)
        return result
    

    def __iter__(self):
        def gen(dic):
            for p,c in reversed(sorted(dic.items())):
                yield (c,p)
        
        return gen(self.terms)
            

    def __getitem__(self,index):
        if type(index)!=int:
            raise TypeError('The index must be int.')
        if type(index)==int and index<0:
            raise TypeError('The index must be greater than or equal to 0.')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!=int:
            raise TypeError('The index must be int.')
        if type(index)==int and index<0:
            raise TypeError('The index must be greater than or equal to 0.')
        if value==0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError('The index must be int.')
        if type(index)==int and index<0:
            raise TypeError('The index must be greater than or equal to 0.')
        if index in self.terms:
            del self.terms[index]
        
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('The coefficient must be int or float.')
        if type(p)!=int:
            raise TypeError('The power must be int.')
        if type(p)==int and p<0:
            raise TypeError('The power must be greater than or equal to 0.')
        if p not in self.terms:
            self[p]=c
        else:
            old_c=self.terms[p]
            new_c=c
            sum_c=old_c+new_c
            self[p]=sum_c
                
       

    def __add__(self,right):
        copy=eval(self.__repr__())
        if type(right) not in [Poly,int,float]:
            raise TypeError('The operand must be Poly, int or float.')
        if type(right)==Poly:
            for p,c in right.terms.items():
                copy._add_term(c,p)
        if type(right) in [int,float]:
            copy._add_term(right,0)
        return copy
                 

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('The operand must be Poly, int or float.')
        if type(right) in [int,float]:
            copy=eval(self.__repr__())
            for p,c in self.terms.items():
                copy.terms[p]=right*c
            return copy
            
        if type(right)==Poly:
            result=Poly()
            for p1,c1 in self.terms.items():
                for p2,c2 in right.terms.items():
                    new_p=p1+p2
                    new_c=c1*c2        
                    result._add_term(new_c,new_p)
            return result


    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('The operand must be Poly, int or float.')
        if type(right)==Poly:
            return self.terms==right.terms
        if type(right) in [int,float]:
            return self.terms=={0:right}

    
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
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()