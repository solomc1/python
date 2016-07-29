class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        for term in terms:
            assert type(term[0]) in [int, float], 'Illegal coefficient in {}'.format(term)
            assert type(term[1]) == int and term[1] >= 0, 'Power less than zero in {}'.format(term)
            assert term[1] not in self.terms.keys(), 'Power in {} already specified'.format(term)
            if term[0] != 0:
                self.terms[term[1]] = term[0]

        
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
        return'Poly('+','.join('({},{})'.format(self.terms[key], key) for key in self.terms)+')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        res_sum = 0
        for power in self.terms:
            res_sum += (self.terms[power] * (arg**power))
        return res_sum

    def __iter__(self):
        for i in sorted(list(self.terms.items()), key = lambda x : x[0], reverse = True):
            yield (i[1],i[0])
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The index was not an integer greater than or equal to zero')
        else:
            return self.terms[index] if index in self.terms else 0

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('The index was not an integer greater than or equal to zero')
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] =  value
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('The index was not an integer greater than or equal to zero')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        assert type(c) in [int, float], 'Coefficient not an integer or float'
        assert type(p) == int and p >= 0, 'Power not an integer greater than zero'
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            result = self.terms[p] + c
            if result != 0:
                self.terms[p] = result
            else:
                del self.terms[p]
       

    def __add__(self,right):
        copy = Poly()
        for power in self.terms:
            copy._add_term(self.terms[power], power)
        if type(right) == Poly:
            for power in right.terms:
                copy._add_term(right.terms[power], power)       
        elif type(right) in [int, float]:
            copy._add_term(right, 0)
        else:
            raise TypeError('Right operand not of type Polynomal, float, or integer')
        
        return copy

    
    def __radd__(self,left):
        if type(left) in (int,float):
            copy = Poly()
            for power in self.terms:
                copy._add_term(self.terms[power], power)
            copy._add_term(left, 0)
            return copy
        else:
            raise TypeError('Operand not of type integer or float')
    

    def __mul__(self,right):
        copy = Poly()
            
        if type(right) == Poly:
            for power in self.terms:
                for power2 in right.terms:
                    copy._add_term(self.terms[power]*right.terms[power2], power+power2)
        elif type(right) in [float,int]:
            for power in self.terms:
                copy._add_term(self.terms[power] * right,power)
        else:
            raise TypeError('Operand was not of type integer or float or Poly')
        
        return copy
    

    def __rmul__(self,left):
        copy = Poly()
        
        if type(left) in [int,float]:
            for power in self.terms:
                copy._add_term(self.terms[power] * left,power)
            return copy
        else: 
            raise TypeError('Operand was not of type integer or float')
    

    def __eq__(self,right):
        if type(right) == Poly:
            if len(self.terms) != len(right.terms):
                return False
            
            boolean = True
            for power in self.terms:
                if power not in right.terms or self.terms[power] != right.terms[power]:
                    boolean = False
            return boolean
        
        elif type(right) in (float,int):
            return self == Poly((right, 0))
        
        else:
            
            raise TypeError('Right hand operand was not of type Poly, float, or int')

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.


    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True

    
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