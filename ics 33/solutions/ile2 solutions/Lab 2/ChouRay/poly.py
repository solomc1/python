#from collection import defaultdict
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        for i in terms:
            assert type(i[0])== float or type(i[0])==int
            assert type(i[1])==int and i[1]>=0
            assert i[1] not in self.terms
            if i[0]!=0:
            #self.terms[terms[i][1]]=terms[i][0]
                self.terms.update({i[1]:i[0]})
          
    
        
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
        a=""
        for i in self.terms:
            a+="("+str(self.terms[i])+","+str(i)+")"
        result="Poly({x})".format(x=a)
        return result

    
    def __len__(self):
        if self.terms !={}:
            result=[]
            for i in self.terms:
                result.append(i)
            result.sort()
            return result[-1]
        else:
            return 0
    
    def __call__(self,arg):
        result=0
        for i in self.terms:
           
            result+=(self.terms[i]*(arg**i))
         
        return result
    

    def __iter__(self):
        result=[]
        for i in self.terms:
            yield ( (self.terms[i],i))
            #result.append( (self.terms[i],i))
        
       
            

    def __getitem__(self,index):
        if type(index)!= int: raise TypeError("must be integer")
        if index <0: raise TypeError("must be bigger than 0")
        if index not in self.terms:
            return int(0)
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!= int: raise TypeError("must be integer")
        if index <0: raise TypeError("must be bigger than 0")
        if value !=0:
            self.terms[index]=value
        elif value ==0 and index in self.terms:
            self.terms.pop(index) 
        
        
            

    def __delitem__(self,index):
        if type(index)!= int: raise TypeError("must be integer")
        if index <0: raise TypeError("must be bigger than 0")
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        assert type(c)==int or type(c)==float
        if type(p)!= int: raise TypeError("must be integer")
        if p<0:  raise TypeError("must be bigger equal than 0")
        
        if p in self.terms:
            self.terms[p]+=c
            if self.terms[p]==0:
                self.terms.pop(p)
        elif  c!=0:
            self.terms.update({p:c})
                
       

    def __add__(self,right):
        if type(right)!=Poly:raise TypeError
        for i in right.terms:
            if i in self.terms:
                self.terms[i]+=right.terms[i]
            else:
                self.terms.update({i:right.terms[i]})
        return self.terms
            

    
    def __radd__(self,left):
        return self.__add__(left)
    

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