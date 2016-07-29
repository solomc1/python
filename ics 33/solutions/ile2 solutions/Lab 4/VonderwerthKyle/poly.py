class Poly:
    
    def __init__(self,*tarms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in tarms:
            try:
                if term[1] < 0 or term[1] in self.terms.values():
                    raise AssertionError("Poly.__init__: illegal power in " +str(term))
            except: 
                raise AssertionError("Poly.__init__: illegal power in " +str(term))
            self.terms[term[0]] = term[1]
    
    def _check_pol(self, term):
        try:
            if term[1] < 0:
                raise TypeError("Poly.__init__: illegal power in " +str(term))
        except: 
            raise TypeError("Poly.__init__: illegal power in " +str(term))
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
        return ("Poly"+str((self.terms)))

    
    def __len__(self):
        highest = sorted(self.terms.values())
        return highest[-1]
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += (k*arg)**v
        return total
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(),key= lambda x: x[1], reverse = True):
            yield (k,v)

        


    def __getitem__(self,index):
        try:
            if index < 0:
                raise TypeError("Poly.__init__: illegal power " +str(index))
        except: 
            raise TypeError("Poly.__init__: illegal power " +str(index))
        
        if index in self.terms.values():
            for k,v in self.terms.items() :
                if v == index:
                    return k
        else:
            return 0
        
            
    def __setitem__(self,index,value):
        try:
            if index < 0 or value < 0 < value:
                raise TypeError("Poly.__init__: illegal power " +str(index))
        except: 
            raise TypeError("Poly.__init__: illegal power " +str(index))
        if value == 0:
            for k,v in self.terms.items() :
                if v == index:
                    del self.terms[k]
        self.terms[value] = index
         

    def __delitem__(self,index):
        try:
            if index < 0:
                raise TypeError("Poly.__init__: illegal power " +str(index))
        except: 
            raise TypeError("Poly.__init__: illegal power " +str(index))
        for k,v in self.terms.items() :
            if v == index:
                del self.terms[k]
            

    def _add_term(self,c,p):
        pass


    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
        terms = {}
        for term in left:
            try:
                if term[1] < 0 or term[1] in terms.values():
                    raise AssertionError("Poly.__init__: illegal power in " +str(term))
            except: 
                raise AssertionError("Poly.__init__: illegal power in " +str(term))
            terms[term[0]] = term[1]
        added = 0
        muled = 0
        new_poly = ()
        self_terms = sorted(self.terms.items(),key= lambda x: x[1], reverse = True)
        terms = sorted(terms.items(),key= lambda x: x[1], reverse = True)
        def gen_term(terms):
            for k,v in terms.items():
                yield (k,v)
        self_termas = gen_term(self_terms)
        for k,v in terms.items():
            termy = self_termas.next()
            if v in termy:
                added = termy[1]+v
                muled = term[0]*k
                new_poly+= (muled,added)
        return new_poly
                

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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