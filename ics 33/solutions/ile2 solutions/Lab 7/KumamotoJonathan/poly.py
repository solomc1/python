class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        self.terms = {}
        for polys in terms:
            assert type(polys[0]) == int or type(polys[0])==float
            assert type(polys[1]) == int
            assert polys[1] >= 0
            if polys[0] != 0:
                if polys[1] in self.terms:
                    raise AssertionError
                self.terms[polys[1]] = polys[0]

        
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
        stringy = 'Poly('
        for i,j in self.terms.items():
            if stringy[-1] == '(':
                stringy+='('+str(j)+','+str(i)+')'
            else:
                stringy+=',('+str(j)+','+str(i)+')'
        stringy += ')'
        return stringy

    
    def __len__(self):
        highest = 0
        for V,T in self.terms.items():
            if V > highest:
                highest = V
        return highest
    
    def __call__(self,arg):
        if self.terms == {}:
            return 0
        equation = 0
        for POWER,COEF in self.terms.items():
            equation += COEF*arg**POWER
        return equation
    

    def __iter__(self):
        for POWER, COEF in sorted(self.terms.items(), reverse = True):
            yield (COEF, POWER)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError
        if index < 0:
            raise TypeError
        if self.terms.get(index) == None:
            return 0
        else:
            return self.terms.get(index)
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError
        if index <0:
            raise TypeError
        new_dict = {}
        if self[index] == 0:
            #doesnt exist
            self.terms[index] = value
        for j,i in self.terms.items():
            if i != self.terms.get(index):
                new_dict[j]=i
            else:
                if value != 0:
                    new_dict[j]=value
        self.terms = {}
        self.terms = new_dict
    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError
        if index <0:
            raise TypeError
        new_dict = {}
        for j,i in self.terms.items():
            if i != self.terms.get(index):
                new_dict[j]=i
        self.terms = {}
        self.terms = new_dict
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('sorry')
        if type(p) != int:
            raise TypeError('sorry not an int')
        if p < 0:
            raise TypeError
        
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != tuple:
            raise TypeError
        return self == right

    
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