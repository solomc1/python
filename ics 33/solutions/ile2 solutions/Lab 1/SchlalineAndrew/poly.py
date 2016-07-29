class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in (float,int), 'Poly.__init__:illegal power in: '+str(term)
            assert type(term[1]) == int and term[1]>=0, 'Poly.__init__: illegal type or power specified: '+str(term)
            power = term[1]
            coefficient=term[0]
            assert power not in self.terms.keys(), "Poly.__init__: Term " +str(term)+ " already added"
            if coefficient!=0:
                if power in self.terms.keys():
                    self.terms[power]+=coefficient
                self.terms[power]=coefficient
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
        result='Poly('
        for v,k in self.terms.items():
            result+="({},{}),".format(k,v)
        else:
            result+=')'
        result=result[:-1]+')'
        return result

    
    def __len__(self):
        result=0
        for k in self.terms.keys():
            if k>result:
                result=k
        return result
    
    def __call__(self,arg):
        if type(arg) not in (float, int):
            raise TypeError( str(arg) + ' is not an int or float')
        result = 0
        for power,coefficient in self.terms.items():
            result+=coefficient*arg**power
        return result
            

    def __iter__(self):
        for power in sorted(self.terms.keys(),reverse=True):
            yield (self.terms[power],power)
            

    def __getitem__(self,index):
        result=0
        if type(index) != int or index<0:
            raise TypeError( str(index)+ ' is not an int')
        try:
            result=self.terms[index]
        except KeyError:
            return 0
        return result
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError( str(index)+ ' is not an int')
        if type(value) not in (int,float):
            raise TypeError( str(value)+ ' is not of type int or float')
        if value==0:
            try:
                del self.terms[index]
            except KeyError:
                pass
        self.terms[index]=value

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError( str(index)+ ' is not an int')
        try:
            del self.terms[index]
        except KeyError:
            pass
            

    def _add_term(self,c,p):
        if type(p) != int or p<0:
            raise TypeError( str(p)+ ' is not an int')
        if type(c) not in (int,float):
            raise TypeError( str(c)+ ' is not of type int or float')
        if p not in self.terms.keys():
            if c!=0:
                self.terms[p]=c
        else: #p is in terms.keys()
            self.terms[p]+=c
            if self.terms[p]==0:
                del self.terms[p]
                
       

    def __add__(self,right):
        result=Poly()
        rightpoly=None
        if type(right) in (int, float):
            rightpoly=Poly((right, 0))
        elif type(right) == Poly:
            rightpoly=right
        else:
            raise TypeError("Invalid type specified")
        
        for term in rightpoly:
            result._add_term(term[0],term[1])
        for term in self:
            result._add_term(term[0],term[1])
        return result

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        result=Poly()
        rightpoly=None
        if type(right) in (int, float):
            rightpoly=Poly((right,0))
        elif type(right) == Poly:
            rightpoly=right
        else:
            raise TypeError("Invalid type specified")
        
        for pterm in rightpoly:
            for sterm in self:
                result._add_term(pterm[0]*sterm[0],pterm[1]+sterm[1])
        
        return result
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        rightpoly=None
        if type(right)==int:
            rightpoly=Poly((right,0))
        elif type(right)==Poly:
            rightpoly=right
        for pterm in rightpoly:
            if pterm not in self:
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
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()