class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.tuples=terms
        self.terms = {}
        
        for i in terms:
            assert type(i[0]) in  (int,float), 'Poly.__init__: Coefficent type '+str(type(i[0]))+'not valid'
            assert i[1]>=0,'Poly.__init__: Power value '+str(i[1])+'not greater than 0' 
            
            self.terms[i[1]]=i[0]
        
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
        return 'Poly('+','.join([str(i) for i in self.tuples])

    
    def __len__(self):
        a=[]
        for i in self.tuples:
            a.append(i[1])

        return max(a)

    
    def __call__(self,arg):
        return arg 
    

    def __iter__(self):
        a=set()
        for i in self.tuples:
            if i not in a:
                yield(i)
            

    def __getitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError('type'+ str(type(index))+'not valid')
        else:
            for i in self.terms:
                if i[0]==index:
                    return i[1]
            return 0
            
            

    def __setitem__(self,index,value):
        for i in self.terms:
            for k,v in i.items():
                if k==index:
                    i[k]=value
                    
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        if type(right) is Poly:
            a=[]
            for i in self.tuples:
                if i[0]==right[0]:
                   a.append((i[0],i[1]+right[1]))
                else:
                    a.append(i) 
            return Poly(a)


    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        return self*left
    

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