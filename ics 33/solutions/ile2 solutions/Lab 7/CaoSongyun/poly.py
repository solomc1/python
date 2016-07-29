#Songyun Cao Lab 7

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x,y in terms:
            if x != 0:
                assert type(x) in (int, float), 'illegal coefficient in: ({},{})'.format(x,y)
                assert y not in self.terms, 'illegal power in: ({},{})'.format(x,y)
                assert type(y) == int and y >= 0 , 'illegal power in: ({},{})'.format(x,y)
                self.terms[y] = x
        
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
        terms = ''
        for key, value in self.terms.items():
            terms += '({},{}),'.format(value, key)
        return 'Poly(' + terms[:-1] + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        assert type(arg) in (int, float), 'arg should be an int or float'
        result = 0
        for power,coefficient in self.terms.items():
            result += coefficient * arg ** power
        return result
    

    def __iter__(self):
        for x,y in sorted(self.terms.items(), reverse = True):
            yield (y,x)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Illegal Power: {}'.format(index))
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Illegal Power: {}'.format(index))
        assert type(value) in (int, float), 'illegal coefficient: {}'.format(value)
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Illegal Power: {}'.format(index))
        if index in self.terms:
            self.terms.pop(index)
        
    def _add_term(self,c,p):
        if type(p) != int or p < 0 or type(c) not in (int, float):
            raise TypeError('Illegal Power or coefficient: {}, {}'.format(p, c))
        if p in self.terms:
            self.terms[p] += c
        else:
            self.terms[p] = c
        if self.terms[p] == 0:
            self.terms.pop(p)

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('unsupported operand type(s) for +')
        new = eval(self.__repr__())
        if type(right) in (float, int):
            new._add_term(right, 0)
        else:
            for p, c in right.terms.items():
                new._add_term(c, p)
        return new

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('unsupported operand type(s) for *')  
        new = Poly()
        if type(right) in (float, int):  
            for p, c in self.terms.items():
                new._add_term(c * right, p)
        else:           
            for pr, cr in right.terms.items():
                for p, c in self.terms.items():
                    new._add_term(c * cr, p+pr)
        return new
                

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('unsupported operand type(s) for =')  
        if type(right) in (float, int):  
            return len(self.terms) == 1 and (0, right) in list(self.terms.items()) 
        else:
            return set(self.terms.items()) == set(right.terms.items())
    
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