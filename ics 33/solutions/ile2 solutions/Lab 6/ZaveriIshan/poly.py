class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        test = []
        for item in terms:
            if type(item[0]) in [int,float]: 
                if type(item[1]) == int and item[1] >= 0:
                    if item[1] not in test:
                        if item[0] != 0:
                            self.terms[item[1]] = item[0]
                            test.append(item[1])
                    else: 
                        raise AssertionError('Power aleady used')
                else: 
                    raise AssertionError('Poly.__init__: illegal power')
            else: 
                raise AssertionError('Poly.__init__:illegal coefficient')
        
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
        tups = ''
        for power in self.terms.keys():
                tups += '('+ str(self.terms[power]) + ','+ str(power) +')'
                tups += ','
        tups = tups[0:-1]
        return 'Poly'+'('+tups+')'

    
    def __len__(self):
        powers = []
        if self.terms == {}: 
            return 0 
        else: 
            for k in self.terms.keys(): 
                powers.append(k)
            return max(powers)
    
    def __call__(self,arg):
        power_total = []
        if type(arg) in [int,float]: 
            for k in self.terms.keys(): 
                power_total.append((arg**k)*self.terms[k]) 
            return sum(power_total)
    

    def __iter__(self):
        x = []
        for k in self.terms.keys():
            x.append(k)
        x.sort(reverse = True) 
        for item in x: 
            yield (self.terms[item], item)
            

    def __getitem__(self,index):
        if type(index)!=int: 
            raise TypeError('Index is not an int')
        else: 
            if index < 0: 
                raise TypeError('Index is less than 0')
            elif index not in self.terms.keys(): 
                return 0 
            else: 
                return self.terms[index] 
            

    def __setitem__(self,index,value):
        if type(index) != int or type(value)!= int: 
            raise TypeError('Index or value is not an int')
        else:
            if index < 0: 
                raise TypeError('Power cannot be less than 0')
            elif value == 0: 
                if index in self.terms: 
                    del self.terms[index]
            else: 
                self.terms[index] = value
                
            

    def __delitem__(self,index):
        if type(index) != int: 
            raise TypeError('Power is not an int')
        else: 
            if index < 0: 
                raise TypeError('Index cannot be less than 0')
            elif index in self.terms: 
                del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) in [int,float]: 
            if type(p) == int and p >= 0:
                if p not in self.terms: 
                    if c != 0:
                        self.terms[p] = c 
                else: 
                    if c != 0 and c + self.terms[p] != 0 : 
                        self.terms[p] = c + self.terms[p] 
                    else: 
                        del self.terms[p]
       

    def __add__(self,right):
        p = Poly()
        l = []
        if type(right) == Poly: 
            for i in self.terms.keys(): 
                l.append(i)
            for item in right.terms.keys(): 
                if item in l: 
                    p._add_term(right.terms[item]+self.terms[item],item)  
                else: 
                    p._add_term(right.terms[item],item)
        elif type(right) in [int,float]:
            for i in self.terms.keys(): 
                p._add_term(self.terms[i],i)
            p._add_term(self.terms[0] + right,0)  
        else: 
            raise TypeError('Right is not Poly, int, or float')
        
        return p       

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        key1 = []
        key2 = []
        if type(right) == Poly: 
            for k in self.terms.keys(): 
                key1.append(k)
            for i in right.keys():
                key2.append(i)
            if key1 == key2: 
                for item in key1: 
                    for value in key2: 
                        if self.terms[item] == right.terms[value]: 
                            return True 
                        return False 
            return False
        elif type(right) in [int,float]: 
            for i in self.terms.keys(): 
                key1.append(i)
            for item in key1: 
                if self.terms[item] == right: 
                    return True 
                return False 
        else: 
            raise TypeError('Right is not a Poly, int, or float')
            

    
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