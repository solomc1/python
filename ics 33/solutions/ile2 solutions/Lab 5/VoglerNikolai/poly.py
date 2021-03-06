from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coeff, power in terms:
            assert type(coeff) in (int, float), 'Poly.__init__: coefficient({}) of type({}) with power({}) must be of type int or float'.format(coeff,type_as_str(coeff),power)
            assert type(power) is int and power >= 0, 'Poly.__init__: power({}) of type({}) must be of type int or float'.format(power, type_as_str(power))
            if coeff != 0:
                assert power not in self.terms, 'Poly.__init__: power({}) already appears as a term associated with a coefficient'.format(power)
                self.terms[power] = coeff
        
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
        return 'Poly({})'.format( ','.join('('+str(c)+','+str(p)+')' for p,c in self.terms.items()) )

    
    def __len__(self):
        return max(k for k in self.terms.keys()) if len(self.terms.keys()) > 0 else 0
    
    def __call__(self,arg):
        total = 0
        for power, coeff in self.terms.items():
            total += coeff*arg**power
        return total
    

    def __iter__(self):
        def gen(t):
            for p,c in sorted(t.items(), reverse = True):
                yield (c,p)
        return gen( dict(self.terms) )
                
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError( 'Poly.__getitem__: index({}) of type({}) must be of type int and >= 0'.format(index, type_as_str(index)) )
        return self.terms[index] if index in self.terms else 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError( 'Poly.__setitem__: index({})  of type({}) must be of type int and >= 0'.format(index,type_as_str(index)) )
        if value == 0:
            if value in self.terms.values():
                del self.terms[index]
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
        

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError( 'Poly.__delitem__: index({}) of type({}) must be of type int and >= 0'.format(index, type_as_str(index)) )
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError( 'Poly._add_term: c({}) of type({}) must be of type int or float'.format(c, type_as_str(c)) )
        if type(p) is not int or p < 0:
            raise TypeError( 'Poly._add_term: p({}) of type({}) must be a of type int and >= 0'.format(p, type_as_str(p)) )
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if c == 0 or self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right:'Poly/int/float'):
        if type(right) not in (Poly, int, float):
            raise TypeError( 'Poly.__add__: right({}) of type {} must be of type Poly, int, or float'.format(right, type_as_str(right)) )
        if type(right) in (int, float):
            right = Poly((right, 0))
        pol = Poly()
        for p, c in self.terms.items():
            pol._add_term(c, p)
        for p, c in right.terms.items():
            pol._add_term(c, p)
        return pol
        
    
    def __radd__(self,left:'int/float'):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError( 'Poly.__add__: right({}) of type {} must be of type Poly, int, or float'.format(right, type_as_str(right)) )
        if type(right) in (int, float):
            right = Poly((right, 0))
        pol = Poly()
        for p1, c1 in self.terms.items():
            for p2, c2 in right.terms.items():
                pol._add_term(c1*c2, p1+p2)
        return pol
            
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError( 'Poly.__eq__: right({}) of type {} must be of type Poly, int, or float'.format(right, type_as_str(right)) )
        if type(right) == Poly:
            if len(self.terms) != len(right.terms):
                return False
            else:
                return all( p in right.terms and right.terms[p] == c for p, c in self.terms.items() )
        else:
            return True if 0 in self.terms and self.terms[0] == right else False
        
    
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
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()