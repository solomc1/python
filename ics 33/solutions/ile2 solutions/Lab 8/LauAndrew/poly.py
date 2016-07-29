class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coe,power in terms:
            assert type(coe) == int or type(coe) == float, 'Invalid coefficient'
            assert type(power) == int and power >=0, 'Power must be an int and greater than 0'
            assert power not in self.terms.keys(), 'Power is defined more than once'
            if coe != 0:
                self.terms[power] = coe
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
        args = []
        for power, coe in self.terms.items():
            args.append((coe,power))
        return 'Poly{}'.format(tuple(args))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for power,coe in self.terms.items():
            total += coe*(arg**power)
        return total
    

    def __iter__(self):
        results = []
        for power,coe in self.terms.items():
            results.append((coe,power))
        return iter(sorted(results,key= lambda x: x[1], reverse = True))
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index provided must be and int and >= 0')
        return (self.terms[index] if index in self.terms.keys() else 0)


    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index provided must be and int and >= 0')
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
        

            

    def __delitem__(self,index):
        self[index] = 0
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Coefficient must be an int or float')
        if type(p) != int or p < 0:
            raise TypeError('Power must be an int and greater than 0')
        if p not in self.terms.keys() and c != 0:
            self[p] = c
        elif p in self.terms.keys():
            self[p] = c+self[p]
            if self[p] == 0:
                del self[p]
                
        
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError(right+ ' is not a Polynomial, int or float')
        newpoly = Poly()
        if type(right) in (int,float):
            right = Poly((right,0))
        for c,p in self:
            newpoly._add_term(c,p)
        for c,p in right:
            newpoly._add_term(c,p)
        return newpoly
        

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError(right+ ' is not a Polynomial, int or float')
        newpoly = Poly()
        if type(right) in (int,float):
            right = Poly((right,0))
        for c,p in self:
            for c2,p2 in right:
                newpoly._add_term(c*c2,p+p2)
        return newpoly
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError(right+ ' is not a Polynomial, int or float')
        elif type(right) == Poly:
            return self.terms == right.terms
        else:
            return self[0]== right 
    
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