class Poly:
    """batch_self_check("bsc.txt")"""
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:
            if (type(x[0]) != float and type(x[0]) != int):
                raise AssertionError("Improper Coefficient")
            if x[1] < 0 or type(x[1]) != int or type(x[0]) == str:
                raise AssertionError("Improper Power")
            if x[0] == 0:
                pass
            else:
                self.terms[x[1]] = x[0] 
        
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
        string = "Poly("
        for x in self.terms:
            string = string + "(" + str(self.terms[x]) + "," + str(x) + ")" + ")"
        return string
        
    def __len__(self):
        size = 0
        if self.terms == None:
            return 0
        else:
            for x in self.terms:
                if x > size:
                    size = x
        return size
    
    def __call__(self,arg):
        value = 0
        for x in self.terms:
            value = value + self.terms[x]*arg**x
        return value
    

    def __iter__(self):
        sorts = []
        if type(self.terms) != dict:
            return 0
        for x in self.terms:
            sorts.append((x, self.terms[x]))
        sorts.sort(reverse = True)
        for x in range(len(sorts)):
            sorts[x] = (sorts[x][1], sorts[x][0])
        return iter(sorts)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        elif index not in self.terms:
            return 0
        else:
            for x in self.terms:
                if x == index:
                    return self.terms[x]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        elif index in self.terms and value == 0:
            del(self.terms[index])
        elif value == 0:
            pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError
        else:
            for x in self.terms:
                if self.terms[x] == index:
                    del(self.terms[x])
            

    def _add_term(self,c,p):
        if type(p) != int and type(p) != float:
            raise TypeError
        elif type(p) != int or c < 0:
            raise TypeError
        else:
            if p not in self.terms.items():
                self.terms[p] = c
            elif p in self.terms.items():
                for x in self.terms:
                    if p == self.terms[x]:
                        del(self.terms[x])
                        self.terms[x + p] = c
                
       

    def __add__(self,right):
        new_poly = Poly()
        if type(right) == Poly:
            for x in right.terms:
                new_poly._add_term(x, right.terms[x])
            for y in self.terms:
                new_poly._add_term(y, self.terms[y])
        elif type(right) == int or type(right) == float:
            for z in self.terms:
                new_poly._add_term(z, self.terms[z])
            new_poly._add_term(0, right)
        else:
            raise TypeError
        return new_poly

    
    def __radd__(self,left):
        new_poly = Poly()
        if type(left) == Poly:
            for x in left.terms:
                new_poly._add_term(x, left.terms[x])
            for y in self.terms:
                new_poly._add_term(y, self.terms[y])
        elif type(left) == int or type(left) == float:
            for z in self.terms:
                new_poly._add_term(z, self.terms[z])
            new_poly._add_term(left,0)
        else:
            raise TypeError
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