class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.trueterms= terms
        for i in terms:
            coef,power = i[0],i[1]
            assert type(coef) in (int,float), 'coefficient: '+ str(coef)+ ' should be an int or float'
            assert type(power) == int and power >=0, 'power: '+ str(power)+ ' should be >= 0'
            if coef != 0:
                self.terms[power] = coef
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
        return('Poly{}'.format(self.trueterms))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            highest = 0
            for i in self.terms.keys():
                if i > highest: highest = i
            return highest
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result+=(arg**k)*v
        return result
    

    def __iter__(self):
        sortedpowers = []
        for i in self.terms.keys():
            sortedpowers.append(i)
        yield (sortedpowers.pop(max(sortedpowers)))
        
            

    def __getitem__(self,index):
        if type(index) == int and index >=0:
            if index in self.terms.keys():
                return self.terms[index]
            else: return 0
        else:
            raise TypeError('Index:'+ str(index)+ ' must be an int >=0')
            

    def __setitem__(self,index,value):
        if type(index)== int and index >=0:
            if value == 0:
                del self.terms[index]
            else:
                self.terms[index] = value
        else:
            raise TypeError('Index:'+ str(index)+ ' must be an int >=0')
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            try: del self.terms[index]
            except KeyError: pass
        else:
            raise TypeError('Index:'+ str(index)+ ' must be an int >=0')

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p) == int:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            if p in self.terms.keys():
                if c+self.terms[p] !=0:
                    self.terms[p] = c+self.terms[p]
                else:
                    del self.terms[p]
                
        elif type(c) not in (int,float):
            raise TypeError('coefficient : ' +str(c)+ ' must be an int or float')
        else:
            raise TypeError('power : ' +str(p)+ ' must be an int')
            
       

    def __add__(self,right):
        #if type(right) in (int,float,Poly):
        #    pass
        #else: 
    #    raise TypeError
        pass
        
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) in (int,float,Poly):
            return self == right
        else: 
            raise TypeError
        
    
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