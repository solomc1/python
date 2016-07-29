class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coefficient,power in terms:
            assert type(coefficient) in (int,float), 'coefficient, '+str(coefficient) +' , must be type int or float'
            assert type(power) == int and power >= 0, 'power, '+str(power)+' , must be an int greater than 0'
            assert power not in self.terms.keys(), 'power, '+str(power) +' , is already present in the Polynomial'
            if coefficient != 0:
                self.terms[power] = coefficient
                
            

            
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
        rep =''
        for power,coef in self.terms.items():
            rep += str((coef,power))+','
        return 'Poly('+rep[:-1] +')'

    
    def __len__(self):
        powers = self.terms.keys()
        if len(powers) == 0:
            return 0
        return sorted(powers)[-1]
    
    def __call__(self,arg):
        calc = 0
        for power,coef in self.terms.items():
            calc += (arg**power)*coef
        return calc
                
    

    def __iter__(self):
        sort_powers = sorted(self.terms.items(),reverse=True)
        for i in sort_powers:
            yield i[-1],i[0]
            

    def __getitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError('index, '+str(index)+' , must be int that is greater than or equal to 0')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index <0:
            raise TypeError('index, '+str(index)+' , must be int that is greater than or equal to 0')
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
            else:
                return
        else:
            self.terms[index] = value
        
            

    def __delitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError('index, '+str(index)+' , must be int that is greater than or equal to 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('coefficient, '+str(c) +' , must be type int or float')
        if type(p) is not int or p<0:
            raise TypeError('power, '+str(p)+' , must be int that is greater than or equal to 0')
        if p not in self.terms.keys() and c != 0:
            
            self.terms[p]=c
        elif p in self.terms.keys() and c != 0:
            self.terms[p]+= c
            if self.terms[p] == 0:
                del self.terms[p]
        else:
            None
            

    def __add__(self,right):
        new_poly = Poly()
        if type(right) not in (Poly,int,float):
            raise TypeError(str(right)+' must be type Poly, int, or float')
        if type(right) in (int,float):
            return self + Poly((right,0))
        for p,c in self.terms.items():
            if p in right.terms.keys():
                new_c = c+ right.terms[p]
                new_poly._add_term(new_c,p)
            elif p not in right.terms.keys():
                new_poly._add_term(c,p)
        for p,c in right.terms.items():
            if p not in self.terms.keys():
                new_poly._add_term(c,p)
        return new_poly

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        new_poly = Poly()
        if type(right) not in (Poly,int,float):
            raise TypeError(str(right)+' must be type Poly, int, or float')
        if type(right) in (int,float):
            return self*Poly((right,0))
        for p,c in self.terms.items():
            for rp,rc in right.terms.items():
                new_p = p + rp
                new_c = c * rc
                new_poly._add_term(new_c,new_p)
        return new_poly

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError(str(right)+' must be type Poly, int, or float')
        if type(right) in (int,float):
            if len([self.terms.items]) == 1 and 0 in self.terms.keys():
                return self.terms[0] == right
            else:
                return False
        
                
    
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