from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for x in terms:
            coefficient = x[0]
            power = x[1]
            
            assert type(coefficient) in (int, float), 'Coefficient must be type int or float'
            assert type(power) == int and power >= 0, 'Power must be a positive integer'
            assert power not in self.terms, 'Duplicate powers'
            
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
        repr_string = ''
        for p, c in self.terms.items():
            repr_string += '({},{}),'.format(str(c), str(p))
        return 'Poly({})'.format(repr_string.strip(','))
    
    def __len__(self):
        powers = [x for x in self.terms]
        return 0 if powers == [] else max(powers)
    
    def __call__(self,arg):
        result = 0
        for p, c in self.terms.items():
            result += pow(arg, p) * c
        return result
    
    def __iter__(self):
        for p in sorted(self.terms.keys(), reverse = True):
            yield (self.terms[p], p)

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index out of range, {} is not a positive integer'.format(index))
        return 0 if index not in self.terms else self.terms[index]
            
    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index out of range, {} is not a positive integer'.format(index))
        elif value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value
            
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index out of range, {} is not a positive integer'.format(index))
        elif index in self.terms:
            self.terms.pop(index)
            
    def _add_term(self,c,p):
        if type(c) not in (int,float) or (type(p) != int or p < 0):
            raise TypeError('Cannot add {}x^{}, coefficient must be type int or float and power must be a positive integer'.format(c,p))
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if c == 0 or self.terms[p] + c == 0:
                self.terms.pop(p)
            else:
                self.terms[p] += c

    def __add__(self,right):
        if type(right) == Poly:
            result = Poly()
            for p, c in self.terms.items():
                result._add_term(c, p)
            for p, c in right.terms.items():
                result._add_term(c, p)
            return result
        elif type(right) in (int, float):
            result = Poly()
            for p, c in self.terms.items():
                result._add_term(c, p)
            result._add_term(right, 0)
            return result
        else:
            raise TypeError('Cannot add type {} to type Poly'.format(type_as_str(right)))
    
    def __radd__(self,left):
        if type(left) in (int, float):
            result = Poly()
            for p, c in self.terms.items():
                result._add_term(c, p)
            result._add_term(left, 0)
            return result
        else:
            raise TypeError('Cannot add type {} to type Poly'.format(type_as_str(left)))

    def __mul__(self,right):
        if type(right) == Poly:
            result = Poly()
            for p1, c1 in self.terms.items():
                for p2, c2 in right.terms.items():
                    result._add_term(c1 * c2, p1 + p2)
            return result
        elif type(right) in (int, float):
            result = Poly()
            for p, c in self.terms.items():
                result._add_term(c * right, p)
            return result
        else:
            raise TypeError('Cannot multiply type {} to type Poly'.format(type_as_str(right)))
    

    def __rmul__(self,left):
        if type(left) in (int, float):
            result = Poly()
            for p, c in self.terms.items():
                result._add_term(c * left, p)
            return result
        else:
            raise TypeError('Cannot multiply type {} to type Poly'.format(type_as_str(left)))

    def __eq__(self,right):
        if type(right) == Poly:
            return self.__repr__() == right.__repr__()
        elif type(right) in (int, float):
            return self.__len__() == 0 and self.terms[0] == right
        else:
            raise TypeError('Cannot compare type Poly to type {}'.format(type_as_str(right)))

    
if __name__ == '__main__':
    #Some simple tests; you can comment them out and/or add your own before
    #the driver is called.
     
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