class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert(type(term[0])==int or type(term[0])==float),'Poly.__init__:The coefficient must be type int or float'
            if term[0]!=0 and term[1] in self.terms.keys():
                raise AssertionError('Poly.__init__:There already exists a Polynomial with this power')
            assert(type(term[1])==int and term[1]>=0),'Poly.__init__:The power must be an int that is greater or equal to 0'
            #assert(term[0] not in self.terms.keys()),'Poly.__init__:There already exists a Polynomial with this power'
            if term[0]!=0 and term[1] in self.terms.values():
                raise AssertionError('Poly.__init__:There already exists a Polynomial with this power')
            if term[0]!=0: 
                self.terms[term[1]]=term[0]
            
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
        s=''
                    
        for item in self.terms.items():
            s+='('+repr(item[0])+','+repr(item[1])+')'+','
        return 'Poly('+s[:-1]+')'

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
    
        else:

            term=self.terms.keys()
            return max(term)
                
            
    def __call__(self,arg):
        count=0
        for item in self.terms.items():
            count+=item[1]*arg**item[0]
        return count
        


    def __iter__(self):
        val=sorted(self.terms.keys(),reverse=True)
        it=iter(val)
        
        for item in self.terms.items():
           
            if item[0]==next(it):
                
                return item[1],item[0]
        #print(self.terms.get(next(it)))
        #return item[1],item[0]
            

    def __getitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError('Poly.__getitem__: '+str(index)+' is not a proper type int or is greater than 0')
        for item in self.terms.items():
            if index==item[0]:
                return item[1]
            if index not in self.terms.keys():
                return 0
            

    def __setitem__(self,index,value):
        if type(index)!=int or index<0:
            raise TypeError('Poly.__setitem__: '+str(index)+' is not a proper type int or is greater than 0')
        if value!=0:
            self.terms[index]=value
            
    def __delitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError('Poly.__delitem__: '+str(index)+' is not a proper type int or is greater than 0')
        for item in self.terms.items():
            if item[0]==index:
                self.terms.pop(item[0])

    def _add_term(self,c,p):
        #if type(c)!=int or type(c)!=float:
            #raise TypeError()
        pass
       

    def __add__(self,right):
        if type(right)!=int or type(right)!=float or type(right)!=Poly:
            raise TypeError('Poly.__add__: '+str(type(right))+' is not a proper type')

    
    def __radd__(self,left):
        if type(left)!=int or type(left)!=float or type(left)!=Poly:
            raise TypeError('Poly.__radd__: '+str(type(left))+' is not a proper type')
    

    def __mul__(self,right):
        if type(right)!=int or type(right)!=float or type(right)!=Poly:
            raise TypeError('Poly.__mul__: '+str(type(right))+' is not a proper type')
    

    def __rmul__(self,left):
        if type(left)!=int or type(left)!=float or type(left)!=Poly:
            raise TypeError('Poly.__rmul__: '+str(type(left))+' is not a proper type')
    

    def __eq__(self,right):
        if type(right)!=int or type(right)!=float or type(right)!=Poly:
            raise TypeError('Poly.__eq__: '+str(type(right))+' is not a proper type')

    
if __name__ == '__main__':
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
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