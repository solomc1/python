from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        powers = []
        for term in terms:
            if not type(term[0]) in [int, float]:
                raise AssertionError('Type {} not supported for Polynomial. Must be int or float.'.format(type_as_str(term[0])))
            if type(term[1]) != int:
                raise AssertionError('Power must be of type int; type {} given.'.format(type_as_str(term[1])))
            if term[1] < 0:
                raise AssertionError('Powers must be greater than 0.')
            if not term[0] == 0:
                if term[1] in powers:
                    raise AssertionError('Power cannot be used more than once')
                powers.append(term[1])
                self.terms[term[1]] = term[0]
            
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
        result = 'Poly('
        count = 1
        for term in self.terms:
            result += '({}, {})'.format(self.terms[term], term)
            if count != len(list(self.terms.keys())):
                result += ', '
            count += 1
        result.strip()
        return result + ')'
    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        big = 0
        for term in self.terms:
            if term > big:
                big = term
        return big
    
    def __call__(self,arg):
        total = 0
        for term in self.terms:
            total += ((arg**term) * self.terms[term])
        return total
    

    def __iter__(self):
        powers = []
        for term in self.terms:
            powers.append(term)
        powers.sort(reverse = True)
        for power in powers:
            yield (self.terms[power], power)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Power must be of type int; type {} given.'.format(type_as_str(index)))
        if index < 0:
            raise TypeError('Power must be greater than 0.')
        if index not in self.terms:
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Power must be of type int; type {} given.'.format(type_as_str(index)))
        if index < 0:
            raise TypeError('Power must be greater than 0.')
        if not value == 0:
            self.terms[index] = value
        elif index in self.terms:
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Power must be of type int; type {} given.'.format(type_as_str(index)))
        if index < 0:
            raise TypeError('Power must be greater than 0.')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not type(c) in [int, float]:
            raise TypeError('Type {} not supported for Polynomial. Must be int or float.'.format(type_as_str(c)))
        if type(p) != int:
            raise TypeError('Power must be of type int; type {} given.'.format(type_as_str(p)))
        if p < 0:
            raise TypeError('Power must be greater than 0.')
        if not p in self.terms:
            self.terms[p] = c
        else:
            self.terms[p] += c
        if self.terms[p] == 0:
            del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Unsupported opperand type: {} + {}'.format(type_as_str(self), type_as_str(right)))
        if type(right) in [int, float]:
            right = Poly((right, 0))
        result = Poly()
        for term in self.terms:
            result._add_term(self.terms[term], term)
        for term in right.terms:
            result._add_term(right.terms[term], term)
        return result
    
    def __radd__(self,left):
        return self.__add__(left)

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Unsupported opperand type: {} * {}'.format(type_as_str(self), type_as_str(right)))
        if type(right) in [int, float]:
            right = Poly((right, 0))
        result = Poly()
        for term2 in right.terms:
            for term in self.terms:
                result._add_term(self.terms[term] * right.terms[term2], term + term2)
        return result

    def __rmul__(self,left):
        return self.__mul__(left)

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Unsupported opperand type: {} == {}'.format(type_as_str(self), type_as_str(right)))
        if type(right) in [int, float]:
            right = Poly((right, 0))
        self_powers = sorted(list(self.terms.keys()))
        right_powers = sorted(list(right.terms.keys()))
        self_vals = []
        right_vals = []
        if len(self_powers) != len(right_powers):
            return False
        else:
            for pow in self_powers:
                self_vals.append(self.terms[pow])
            for pow in right_powers:
                right_vals.append(right.terms[pow])
        return self_powers == right_powers and self_vals == right_vals

    
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