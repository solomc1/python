class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for coefficient,power in terms:
            assert type(coefficient) in (int,float), "illegal coefficient ({})".format(coefficient)
            assert type(power) is int and power>=0, "illegal power ({})".format(power)
            assert power not in self.terms, "cannot assign multiple coefficients to same power ({})".format(power)
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
        string = "Poly("
        terms = ''
        for co,power in self:
            terms += "({},{}),".format(co,power)
        return string+terms[:-1]+")"
        

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for power,co in self.terms.items():
            result += (arg**power)*co
        return result
    

    def __iter__(self):
        for term in sorted(self.terms.items(),reverse=True):
            yield term[1],term[0]
            

    def __getitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError("illegal power ({})".format(index))
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index<0:
            raise TypeError("illegal power ({})".format(index))
        if value==0 and index in self.terms:
            del self.terms[index]
        elif value!=0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index<0:
            raise TypeError("illegal power ({})".format(index))
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("illegal coefficient ({})".format(c))
        if type(p) is not int or p<0:
            raise TypeError("illegal power ({})".format(p))
        
        if p not in self.terms:
            if c!=0:
                self.terms[p] = c
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        result = Poly()
        if type(right) in (int,float):
            for co,power in self:
                result._add_term(co,power)
            result._add_term(right,0)
        elif type(right) is Poly:
            for co,power in self:
                result._add_term(co,power)
            for co,power in right:
                result._add_term(co,power)
        else:
            from goody import type_as_str
            raise TypeError("unsupported operand type(s) for +: 'Poly' and '{}'".format(type_as_str(right)))
        return result

    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        result = Poly()
        if type(right) in (int,float):
            for co,power in self:
                result._add_term(co*right,power)
        elif type(right) is Poly:
            for co1,pow1 in self:
                for co2,pow2 in right:
                    result._add_term(co1*co2,pow1+pow2)
        else:
            from goody import type_as_str
            raise TypeError("unsupported operand type(s) for *: 'Poly' and '{}'".format(type_as_str(right)))
        return result
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) is Poly:
            if len(self.terms)==len(right.terms):
                for co,power in self:
                    if power not in right.terms or co != right[power]:
                        return False
                return True
        elif type(right) in (int,float):
            if len(self.terms)==1 and 0 in self.terms and self.terms[0]==right:
                return True
        else:
            from goody import type_as_str
            raise TypeError("cannot equate type(s): 'Poly' and '{}'".format(type_as_str(right)))
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