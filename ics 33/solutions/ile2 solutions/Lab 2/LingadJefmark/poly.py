class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for items in terms:
            assert type(items[0]) in (int, float), 'Poly.__init__' + str(items[0]) + 'must be an int or float but' + str(type(items[0])) + 'given.'
            assert type(items[1]) is int and items[1] >= 0, 'Poly.__init__: illegal power in :' + str(items)
            #if items[1] in self.terms.values and 
            if items[0] != 0:
                self.terms[items[1]] = items[0]

            
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
        terms = ''
        for p,c in self.terms.items():
            terms += str( (c,p) ) + ','
        #print('Poly('+terms[:-1]+')')#( str( (c,p) ) for c,p in self.terms.items() ) + ')')
        return 'Poly('+terms[:-1]+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max( self.terms.keys() )
    
    def __call__(self,arg):
        result = 0
        for pow,co in self.terms.items():
            result += co * arg**pow
        return result
    

    def __iter__(self):
        for pow,co in sorted( self.terms.items(), key = (lambda x:x[0]), reverse=True ):
            yield co,pow
            

    def __getitem__(self,index):
        if index < 0 or type(index) is not int : raise TypeError ( 'Poly.__getitem__: illegal index in : ' + str(index) + ' must be integer great than 0.' )
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        # index is power and value is coefficient
        # index will be key and value will be value
        if index < 0 or type(index) is not int: raise TypeError( 'Poly.__setitem__: illegal index in : ' + str(index) + ' must be an integer greater than 0.')
        
        if value == 0 and index in self.terms.keys():
            self.terms.pop(index)
        elif value != 0:
            self.terms[index] = value

            
    def __delitem__(self,index):
        if index < 0 or type(index) is not int : raise TypeError ( 'Poly.__delitem__: illegal index in : ' + str(index) + ' must be integer great than 0.' )
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('Poly._add_terms: illegal coefficient. ' + type(str(c)) + ' given but must be int or float.')
        elif type(p) is not int or p  < 0:
            raise TypeError('Poly._add_term: illegal power. ' + str(p) + ' given as ' + type(str(p)) +  ' but must be positive integer.')
       
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] = c + self.terms[p]
            if self.terms[p] == 0:
                self.terms.pop(p)
        
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError ('Poly.__add__: Polynomial, int or float type needed but ' + str(type(right)) + ' given.')
        
        if type(right) is Poly:
            resulting_poly = Poly()        
            for pow,coe in self.terms.items():
                if pow in right.terms.keys() and coe + right.terms[pow] != 0:
                    resulting_poly._add_term(coe + right.terms[pow], pow)
                elif pow not in right.terms.keys():
                    resulting_poly._add_term(coe, pow)

            return resulting_poly

            
    
    def __radd__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError ('Poly.__add__: Polynomial, int or float type needed but ' + str(type(left)) + ' given.')
        resulting_poly = Poly()
        if type(left) is Poly:
            for pow,coe in self.terms.items():
                if pow in left.terms.keys() and coe + left.terms[pow] != 0:
                    resulting_poly._add_term(coe + left.terms[pow], pow)
                elif pow not in left.terms.keys():
                    resulting_poly._add_term(coe, pow)
            return resulting_poly
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__eq__: illegal argument given. Must be Polynomial, int, or float but ' + str(type(right)) + ' given.')
        if type(right) is Poly:
            for pow,co in self.terms.items():
                if pow not in right.terms.keys():
                    return False
                elif pow in right.terms.keys() and co != right.terms[pow]:
                    return False
            return True
        elif type(right) in (int, float):
            if self.__len__() == 0:
                return self.terms[0] == right
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