from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c,p in terms:
            assert type(c) in (int, float), 'Poly.__init__: coefficient('+str(c)+') must be of type int or float'
            assert type(p) is int and p >= 0, 'Poly.__init__: illegal power in: ('+str(c)+', '+str(p)+').'
            assert p not in self.terms, 'Poly.__init__: illegal power('+str(c)+'), cannot appear as a later term with a non-zero coefficient'
            self.terms[p] = c
            if self.terms[p] == 0:
                del self.terms[p]

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
        repr_str = ''
        for p,c in self.terms.items():
            repr_str += '('+str(c)+', '+str(p)+'),'
        return 'Poly({})'.format(repr_str.strip(','))

    
    def __len__(self):
        len_list = [k for k in self.terms]
        return 0 if len_list == [] else max(self.terms.keys()) 
         
            
    
    def __call__(self,arg):
        sum = 0
        for p,c in self.terms.items():
            sum += c*(arg)**p
        return sum

    def __iter__(self):
        for p,c in sorted(self.terms.items(), reverse=True):
            yield (c, p) 
            
            
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: power/index('+str(index)+') must be a positive integer')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: power('+str(index)+') must be a positive integer')
        elif value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: power('+str(index)+') must be a positive integer')
        elif index in self.terms:
            del self.terms[index]
        

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('Poly._add_term: coefficient must be an integer or float')
        elif type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: power must be a positive integer')
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) in (int, float):
            right = Poly((right, 0))
        if type(right) is Poly:
            result = Poly()
            for p,c in self.terms.items():
                Poly._add_term(result, c, p)
            for p,c in right.terms.items():
                Poly._add_term(result, c, p)
            return result
        else:
            raise TypeError('unsupported operand type(s) for +: \'Poly\' and '+"'"+type_as_str(right)+"'")

     
    
    def __radd__(self,left):
        if type(left) in (int, float):
            left = Poly((left, 0))
        if type(left) is Poly:
            return left + self
    

    def __mul__(self,right):
        if type(right) in (int, float):
            right = Poly((right, 0))
        if type(right) is Poly:
            result = Poly()
            for p,c in self.terms.items():
                for p1,c1 in right.terms.items():
                    Poly._add_term(result, c*c1, p+p1)
            return result
        else:
            raise TypeError('unsupported operand type(s) for *: \'Poly\' and '+"'"+type_as_str(right)+"'")


    def __rmul__(self,left):
        if type(left) in (int, float):
            left = Poly((left, 0))
        if type(left) is Poly:
            return left * self
    

    def __eq__(self,right):
        if type(right) is Poly:
            for p,c in sorted(self.terms.items()):
                for p1,c1 in sorted(right.terms.items()):
                    if (p,c) != (p1,c1):
                        return False
            return True
        if type(right) in (int, float):
            return all(c==right for p,c in self.terms.items())
        else:
            raise TypeError('Poly.__eq__: cannot compare between \'Poly\' and \''+type_as_str(right)+'\' objects')

    
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
    \
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()