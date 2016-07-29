class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.origin = terms
        self.terms = {}
        for value, power in self.origin:
            if type(value) not in (int, float):
                raise AssertionError("Poly.__init__: illegal coefficient in:",terms)
            elif type(power) is not int or power < 0 or power in self.terms.keys():
                raise AssertionError("Poly.__init__: illegal power in:",terms)
            else:
                if value != 0:
                    self.terms[power] = value
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
        return "Poly(" + ",".join(("(" + str(value) + "," + str(power) + ")") for value, power in self.origin) + ")"

    
    def __len__(self):
        if list(self.terms.keys()) == []:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) in (int, float):
            total = 0
            for power, value in self.terms.items():
                total += (arg**power)*value       
            return total

    def __iter__(self):
        check = self.terms
        while check != {}:
            yield (check[max(check.keys())],max(check.keys()))
            del check[max(check.keys())]

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError("index should be a positive integer")
        else:
            if index not in self.terms.keys():
                return 0
            else:
                return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError("index should be a positive integer") 
        elif value == 0:
            for power, value in self.terms.items():
                if power == index:
                    del self.terms[power]   
        else:
            self.terms[index] = value  
 

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError("index should be a positive integer") 
        else:
            if index in self.terms.keys():
                del self.terms[index]

    def _add_term(self,c,p):
        if type(p) is not int or p < 0:
            raise TypeError("power should be a positive integer") 
        elif type(c) not in (int, float):
            raise TypeError("illegal coefficient type")
        else:
            if p in self.terms.keys():
                self.terms[p] = self.terms[p] + c
                if self.terms[p] == 0:
                    del self.terms[p]
            else:
                if c != 0:
                    self.terms[p] = c
               

    def __add__(self,right):
        if type(right) == Poly:
            for power, value in right.terms.items():
                if power in self.terms.keys():
                    self.terms[power] = self.terms[power] + value
                else:
                    self.terms[power] = value
#        else:
#            raise TypeError()             

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    '''
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
'''
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()