class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        for term in terms:
            assert type(term[0]) in (int, float)
            assert type(term[1]) == int
            assert term[1] >=0
            assert term[1]  not in self.terms
            if term[0] == 0:
                pass
            else:
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
        in_paren = [eval('({},{})'.format(co, power)) for power, co in self.terms.items()] 
        return 'Poly(' + str(in_paren)[1:-1] + ')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) in (int, float)
        total = 0
        for p,c in self.terms.items():
            total += c*(arg ** p)
        return total
    

    def __iter__(self):
        for p, c in sorted(self.terms.items(), reverse = True):
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms:
            pass
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c)  not in (int, float):
            raise TypeError
        if type(p) != int or p < 0:
            raise TypeError
        if p not in self.terms:
            self.terms[p] = c
        elif p in self.terms or p == 0:
            if p == 0:
                self.terms[p] += c
            else:
                self.terms[p] += c
            
        if self.terms[p] == 0:
            del self.terms[p]            ##############
            
        
       

    def __add__(self,right):
        if type(right) not in (Poly, int):
            raise TypeError
        po = Poly()
        if type(right) == Poly:
            for p,c in self.terms.items():
                po._add_term(c, p)
            for a, b in right.terms.items():
                po._add_term(b, a)
            return po
        elif type(right) == int:
            for p,c in self.terms.items():
                po._add_term(c,p)
            po._add_term(right, 0)
            return po
    def __radd__(self,left):
        if type(left) != int:
            raise TypeError
        po = Poly()
        for p,c in self.terms.items():
            po._add_term(c,p)
        po._add_term(left, 0)
        return po
        
    

    def __mul__(self,right):
        if type(right)  not in (Poly, int):
            raise TypeError
        po = Poly()
        if type(right) == Poly:
            for p,c in self.terms.items():
                for a,b in right.terms.items():
                    po._add_term(c*b, p + a)
            return po
        elif type(right) == int:
            for p,c in self.terms.items():
                po._add_term(c*right, p)
            return po
                    
    

    def __rmul__(self,left):
        if type(left) != int:
            raise TypeError
        po = Poly()
        for p,c in self.terms.items():
            po._add_term(c*left, p)
        return po
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) in (int, float):
            return self.terms[0] == right
        else:
            for p in self.terms:
                if self.terms[p] != right.terms[p]:
                    return False
            return True

    
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