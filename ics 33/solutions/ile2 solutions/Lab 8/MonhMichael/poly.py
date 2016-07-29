class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.termslist =()
        for pair in terms:
            assert type(pair[0]) in (int,float), 'Coefficient can only be an int or a float'
            assert type(pair[1]) is int and pair[1]>=0, 'Power must be an int >= 0'
            if pair[1] in self.terms.keys():
                raise AssertionError('You cannot have duplicate terms with the same power.')
            if pair[0] != 0:
                self.terms[pair[1]]=pair[0]
            self.termslist = self.termslist + (pair,)
            
        #print(self.terms)
        #print(self.termslist)
            
        
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
        return 'Poly'+str(self.termslist)+''

    
    def __len__(self):
        maxpower = 0
        for power in self.terms.keys():
            if power>maxpower:
                maxpower = power
        return maxpower
    
    def __call__(self,arg):
        answer = 0
        for power,coefficient in self.terms.items():
            answer+= coefficient*(arg)**power
        return answer
    

    def __iter__(self):
        for pair in self.termslist:
            yield pair
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError('index must be >=0')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError('Power must be an integer and >= 0')
        self.terms[index] = value
        if value == 0:
            del self.terms[index]
        
            

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Power must be an integer and >= 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Coefficient must be an int or float')
        if type(p) != int and p<0:
            raise TypeError('Power must be an integer >=0')
        if p in self.terms.keys():
            self.terms[p] += c
        elif p not in self.terms.keys():
            self.terms[p] = c
        if self.terms[p] == 0:
            del self.terms[p]
        
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('Operand must be a Poly, int, or float')
        if type(right) != Poly:
            right = Poly((right,0))
        for term in right.termslist:
            self._add_term(term[0],term[1])
        return self

    
    def __radd__(self,left):
        if type(left) not in (Poly,int,float):
            raise TypeError('Operand must be a Poly, int, or float')
        if type(left) != Poly:
            right = Poly((left,0))
        for term in right.termslist:
            self._add_term(term[0],term[1])
        return self
    

    def __mul__(self,right):
        c = Poly()
        if type(right) not in (Poly,int,float):
            raise TypeError('Operand must be a Poly, int, or float')
        for term in self.termslist:
            
            for term2 in right.termslist:
                c._add_term(term[1]*term2[1],term[0]+term2[0])
        return c   

    def __rmul__(self,left):
        c = Poly()
        if type(right) not in (Poly,int,float):
            raise TypeError('Operand must be a Poly, int, or float')
        for term in self.termslist:
            
            for term2 in right.termslist:
                c._add_term(term[1]*term2[1],term[0]+term2[0])
        return c
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('Operand must be a Poly, int, or float')
        if type(right) != Poly:
            right = Poly((right,0))
        return repr(self)==repr(right)

    
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
    #p = Poly((3,2),(-2,1))
    #print(p)
   # print(repr(p))
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()