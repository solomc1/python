class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if item[0]==0:
                continue
            if type(item[1])!=int:
                raise AssertionError("Power must be an int greater than or equal to 0")
            if item[1]<0:
                raise AssertionError("Power must be an int greater than or equal to 0")
            if item[1] in self.terms.keys():
                raise AssertionError("Power can't appear in a later term")
            if type(item[0])!=int and type(item[0])!=float:
                raise AssertionError("Coefficient must be an int greater than or equal to 0")
            self.terms[item[1]] = item[0]
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
        return_str = 'Poly('
        for key in self.terms.keys():
            return_str=return_str + str((self.terms[key], key))+','
        if return_str[-1]==',':
            return_str = return_str[:-1] + ')'
            return return_str
        else:
            return return_str+')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for key in self.terms.keys():
            total=total+(self.terms[key]*(arg**key))
        return total
    

    def __iter__(self):
        for item in sorted(list(self.terms.items()), reverse = True):
            yield (item[1], item[0])
            

    def __getitem__(self,index):
        if type(index)!=int:
            raise TypeError('power value must be an int and greater than zero')
        if index<0:
            raise TypeError('power value must be an int and greater than zero')
        if index in self.terms:
                return self.terms[index]
        return 0
                         
            

    def __setitem__(self,index,value):
        if type(index)!=int and index<0:
            raise TypeError('power value must be an int and greater than zero')
        if value == 0:
            self.terms = self.terms.pop(0)
            return
        self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError('power value must be an int and greater than zero')
        if index<0:
            raise TypeError('power value must be an int and greater than zero')

        self.terms.pop(index)
            

    def _add_term(self,c,p):
        if p not in self.terms and c!=0:
            self.terms[p]=c
            return
        if p in self.terms:
            if self.terms[p]+c !=0:
                self.terms[p]= self.terms[p]+c
            else:
                self.terms.pop(p)
        
       

    def __add__(self,right):
#        exec_str = 'Poly('
#        for key in self.terms.keys():
#            if key in right.terms:
#                exec_str = exec_str + str((right.terms[key]+self.terms[key],key)+',')
#        exec_str=exec_str[:-1]+')'            
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

  

p = Poly( (3,2), (-2,1), (4,0) )
p[5] = -2
print(str(p))

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