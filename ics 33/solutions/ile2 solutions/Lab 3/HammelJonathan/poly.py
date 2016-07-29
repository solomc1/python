class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for c in terms:
            if (type(c[0]) == float or type(c[0])==int): 
                if (type(c[1])==int) and c[1]>=0:
                    if c[1] not in self.terms:
                        if c[0]!=0:
                            self.terms[c[1]]=c[0]
                    else:
                        raise AssertionError('Poly._init__: power defined twice')
                else:
                    raise AssertionError('Poly._init__: illegal power in :' + str(c))
            else:
                raise AssertionError('Poly._init__: illegal coefficient in :' + str(c))
        
        
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
        ans = 'Poly('
        for c,v in self.terms.items():
            ans+='('+str(c)+','+str(v)+'),'
        if ans[-1]==',':
            ans = ans[:-1]
        ans+=')'
        return ans
    
    def __len__(self):
        high = 0
        for c in self.terms:
            if c>high:
                high = c
        return high
    
    def __call__(self,arg):
        total = 0
        for c,v in self.terms.items():
            total += v*(arg**c)
        return total
    

    def __iter__(self):
        lst = []
        for c,v in self.terms.items():
            lst.append((v,c))
        lst.sort(key= (lambda x: x[1]), reverse = True)
        for i in lst:
            yield i
            
    def __getitem__(self,index):
        if type(index)!= int or index<0:
            return TypeError('self.__getitem__: index must be nonnegative integer')
        if index in self.terms:
            return self.terms[index]
        return 0

    def __setitem__(self,index,value):
        if index < 0 and type(index)!=int:
            return TypeError('self.__setitem__: index must be nonnegative integer')
        if type(value) != int and type(value) != float:
            return TypeError('self.__getitem__: coefficient must be a float or int')
        if value == 0:
            if index in self.terms:
                del(self.terms[index])
        else:
            self.terms[index]=value
        

    def __delitem__(self,index):
        if type(index)!= int:
            return TypeError('self.__delitem__: index must be nonnegative integer')
        if index<0:
            return TypeError('self.__delitem__: index must be nonnegative integer')
        if index in self.terms:
            del(self.terms[index])
            

    def _add_term(self,c,p):
        if (type(c)!= int or type(c)!=float) and type(p)!=int and p>=0:
            raise TypeError('invalid inputs')
        if p not in self.terms and c!=0:
            self.terms[p]=c
        elif p in self.terms:
            if self.terms[p]+c !=0:
                self.terms[p]+=c
            else:
                del(self.terms[p])
        
    def __add__(self,right):
        pol = Poly()
        for i in self:
            pol._add_term(i[0],i[1])
        if type(right)== int:
            temp = Poly((right,0))
        elif type(right)==Poly:
            temp = right
        else:
            raise TypeError
        for b in temp:
            pol._add_term(b[0],b[1])
        return pol
                
        pass
    def __radd__(self,left):
        pol = Poly()
        for i in self:
            pol._add_term(i[0],i[1])
        if type(left)== int:
            temp = Poly((left,0))
        else:
            raise TypeError
        for b in temp:
            pol._add_term(b[0],b[1])
        return pol
    

    def __mul__(self,right):
        pol = Poly()
        if type(right)== int:
            temp = Poly((right,0))
        elif type(right)==Poly:
            temp = right
        else:
            raise TypeError
        for i in self:
            for b in temp:
                pol._add_term(i[0]*b[0],i[1]+b[1])
        return pol

    def __rmul__(self,left):
        pol = Poly()
        if type(left)== int:
            temp = Poly((left,0))
        else:
            raise TypeError
        for i in self:
            for b in temp:
                pol._add_term(i[0]*b[0],i[1]+b[1])
        return pol
    

    def __eq__(self,right):
        if type(right)== int:
            temp = Poly((right,0))
        elif type(right)==Poly:
            temp = right
        else:
            raise TypeError
        for a in self:
            for b in temp:
                if a!=b:
                    return False
        return True

    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()