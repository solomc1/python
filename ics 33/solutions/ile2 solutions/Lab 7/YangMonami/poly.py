class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if term[1] in self.terms:
                assert term[0]==0, 'Two similar power must not be in the same tuple'
            #print(term)
            assert term[0]!=0, 'The object must be 0'
            assert type(term[0]) in (int, float) and type(term[1])==int, 'Coefficient must be an int or a float while the power must be an int'
            assert term[1] >= 0, 'The object must be greater than equal to 0'
            self.terms[term[1]]=term[0]
            #print(self.terms)
        
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
        return 'Poly({})'.format(', '.join(repr((v,k)) for k,v in self.terms.items()))
        

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
        else:
            #p=[k for k in self.terms.keys()]
            #print(max(p))
            return max([int(k) for k in self.terms.keys()])
    
    def __call__(self,arg):
        return sum([c*(arg**p)for p,c in self.terms.items()])
    

    def __iter__(self):
        for p,c in sorted(self.terms.items(), reverse=True):
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The object must be an greater than or equal to 0 integer')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('The object must be an greater than or equal to 0 integer')
        if value == 0 and index in self.terms:
            del self.terms[index]
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The object must be an greater than or equal to 0 integer')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        #print(c,p)
        #print(type(c))
        if type(c) not in (int,float):
            raise TypeError('The object '+str(c)+' must be an integer or a float')
        if type(p)!= int and p<0:
            raise TypeError('The object', str(p),' must be greater than equal to 0 integer')
        if p not in self.terms and c != 0:
            self[p] = c
        elif p in self.terms:
            #print('here')
            self[p] = self[p]+c
        
        
    def __add__(self,right):
        result=self
        print(result)
        if type(right) in (int, float):
            result._add_term(right, 0)
        elif type(right) is Poly:
            for c,p in right:
                result._add_term(c,p)
        else:
            raise TypeError('Expected the object to be (int, float, Poly), instead '+str(type(right)))
        print(result)
        return result
    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        result = Poly()
        if type(right) in (int, float):
            for c, p in self:
                result._add_term(c,p)
            result[0]=result[0]+right
        elif type(right) is Poly:
            for c, p in right:
                for cs, ps in self:
                    result._add_term(c*cs,p+ps)
        else:
            raise TypeError('Expected the object to be (int, float, Poly), instead '+str(type(right)))
        
        return result

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) in (int,float):
            if len(self) == 1:
                return 
        else:
            raise TypeError('Expected the object to be (int, float, Poly), instead '+str(type(right)))

    
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
    
    p=Poly( (1,5), (-2,4), (3,3), (-4,2), (5,1), (-6,0) )
    print(p)
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()