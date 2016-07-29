class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c, p in terms:
            assert type(c)==int or type(c)==float, 'Coefficient must be int or float'
            assert type(p)==int and p>=0, 'Power must be int >= 0'
            if p not in self.terms.keys():
                self.terms[p]=c
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
        string = ''
        for c,p in self.terms.items():
            string += '('+str(c)+','+str(p)+')'
        return 'Poly('+string+')'

    
    def __len__(self):
        keys = []
        if self.terms=={}:
            return 0
        else:
            for key in self.terms.keys():
                keys.append(key)
            return max(keys)
            
    
    def __call__(self,arg):
        sum = 0
        list1 = []
        for p,c in self.terms.items():
            list1.append(str(c)+'*'+str(arg)+'**'+str(p))
        for item in list1:
           sum+=eval(item)
        return sum

    def __iter__(self):
        for c,p in self.terms.items():
            yield (c,p)

    def __getitem__(self,index):
        if type(index)!=int:
            raise TypeError('Index must be int')
        if index<0:
            raise TypeError('Index must be > 0')
        if index in self.terms.keys():
            return self.terms[index]
        if index not in self.terms.keys():
            return 0
            

    def __setitem__(self,index,value):
        if type(index)!=int:
            raise TypeError('Index must be int')
        if index<0:
            raise TypeError('Index must be > 0')
        if value!= 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError('Index must be int')
        if index<0:
            raise TypeError('Index must be > 0')
        if index in self.terms.keys():
            del self.terms [index]
            

    def _add_term(self,c,p):
#         if type(c)!=int or type(c)!=float:
#             raise TypeError('Coefficient must be numeric')
        if type(p)!=int:
            raise TypeError('Power must be int')
        if p<0:
            raise TypeError('Power must be >= 0')
        if p not in self.terms.keys() and p>0:
            self.terms[p]=c
            return self.__call__+int(c^p)
        if p in self.terms.keys() and p>0:
            self.terms[p]+=c
            
            
       

    def __add__(self,right):
#         if type(right)!= Poly or type(right)!=int or type(right)!=float:
#             raise TypeError('Operand must be Polynomial or numeric value')
#         if type(right)== int or type(right==float):
#             return sum(int(self.__call__(right)),right)
        pass
      
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right)!= Poly or type(right)!=int or type(right)!=float:
            raise TypeError('Operand must be Polynomial or numeric value')
        if type(right)==Poly:
            if self.terms.items==right.terms.items():
                return True
            else:
                return False

    
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