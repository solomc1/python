class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if type(item[0])!=int and type(item[0])!=float:
                raise AssertionError('Coefficient must be a float or and int.')
            
            if type(item[1])!=int or item[1]<0:
                raise AssertionError('The power must be an integer whose value is greater than or equal to 0.')
            
            if item[1] in self.terms.keys():
                raise AssertionError('Cannot have the same power appear twice in the polynomial, must be entered as one.')
            
            if item[0]!=0:
                self.terms[item[1]]=item[0]
        
        
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
        answer=''
        count=0
        for key,value in self.terms.items():
            if count==0:
                count+=1
                answer+='(%s,%s)' % (value,key)
            else:
                answer+=',(%s,%s)' % (value,key)
        return 'Poly(%s)' % answer


    def __len__(self):
        answer=0
        for key in self.terms.keys():
            if key>answer:
                answer=key
        return answer
     
    def __call__(self,arg):
        sum=0
        for key,value in self.terms.items():
            sum+=value*(arg**key)
        return sum
 
 
    def __iter__(self):
        order=sorted(self.terms.keys(),reverse=True)
        order=iter(order)
        while True:
            try:
                a=next(order)
                yield (self.terms[a],a)
            except StopIteration:
                break
 
    def __getitem__(self,index):
        if type(index)!=int or index<0:
             raise TypeError('Index used must be a positive integer or 0')
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
 
    def __setitem__(self,index,value):
        if type(index)!=int or index<0:
            raise TypeError('Index used must be a positive integer or 0')
        if type(value)!=int and type(value)!=float:
            raise TypeError('Value used must be an integer or a float.')   
        if index in self.terms.keys():
            if value==0:
                del self.terms[index]
            else:
                self.terms[index]=value
        else:
            if value!=0:
                self.terms[index]=value
        
             
 
    def __delitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError('Index used must be a positive integer or 0')
        if index in self.terms.keys():
            del self.terms[index]        
             
 
    def _add_term(self,c,p):
        if type(p)!=int or p<0:
            raise TypeError('Index used must be a positive integer or 0')
        
        if type(c)!=int and type(c)!=float:
            raise TypeError('Value used must be an integer or a float.')  
         
        if p not in self.terms.keys():
            if c!=0:
                self.terms[p]=c
        else:
            sum=self.terms[p]+c
            if sum!=0:
                self.terms[p]=sum
            else:
                del self.terms[p]
        return self
        
    def __add__(self,right):
        if type(right)!=int and type(right)!=float and type(right)!=Poly:
            raise TypeError('Unsupported operands.')
        
        if type(right)==Poly:
            for key,value in right.terms.items():
                self._add_term(value,key)
    
        else:
            if 0 in self.terms.keys():
                self.terms[0]=self.terms[0]+right
            else:
                self.terms[0]=right
                
        return self
     
    def __radd__(self,left):
        return self.__add__(left)
     
 
    def __mul__(self,right):
        pass
     
 
    def __rmul__(self,left):
        pass
     
 
    def __eq__(self,right):
        if type(right)!=int and type(right)!=float and type(right)!=Poly:
            raise TypeError('Unsupported operands.')
        if type(right==Poly):
            order1=sorted(self.terms.keys())
            order2=sorted(self.terms.keyS())
            check=True
 
     
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
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
    print('End simple tests\n')
     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()