# Thomas Nguyen 61879630 Lab 7 2014
class Poly:

    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for value_tuple in terms:
            if type(value_tuple[0]) not in (int, float):
                raise AssertionError('Coefficient is not of type int or float.')
            elif type(value_tuple[1]) != int or value_tuple[1] < 0:
                raise AssertionError('Power is not an integer that is greater than or equal to zero')
            elif value_tuple[0] == 0:
                pass
            elif value_tuple[1] in self.terms:
                if self.terms[value_tuple[1]] != 0:
                    raise AssertionError('Value with power {} and non-zero coefficient already exists'.format(value_tuple[1]))
            else:
                self.terms[value_tuple[1]] = value_tuple[0]
            
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
        value_tuples = ''
        for element in self.terms:
            value_tuples += '({}, {}),'.format(self.terms[element], element)
        return 'Poly({})'.format(value_tuples[:-1])

    
    def __len__(self):
        max_value = 0
        for element in self.terms:
            if element > max_value:
                max_value = element
        return max_value
    
    
    def __call__(self,arg):
        answer = 0
        for element in self.terms:
            answer += (self.terms[element])*(arg**element)
        return answer
    

    def __iter__(self):
        iterable_object = iter(sorted(self.terms, reverse=True))
        while True:
            answer = next(iterable_object)
            yield (self.terms[answer], answer)
        
    
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index is not an integer greater than zero.')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Power is not an integer greater than zero.')
        elif value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Power is not an integer greater than zero.')
        elif index in self.terms:
            del self.terms[index]
            
    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int or p < 0:
            raise TypeError('Coefficient is not an int/float or the power is not an int greater than zero.')
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            new_coefficient = self.terms[p]+c
            if new_coefficient == 0:
                del self.terms[p]
            else:
                self.terms[p] = new_coefficient
        
    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly object can only add to objects integer, float, or Poly type.')
        result = Poly()
        if type(right) in (int, float):
            for element in self.terms:
                result._add_term(self.terms[element], element)
            result._add_term(right, 0)
        elif type(right) == Poly:
            for element in self.terms:
                result._add_term(self.terms[element], element)
            for right_element in right.terms:
                result._add_term(right.terms[right_element], right_element)
        return result                

    def __radd__(self,left):
        return self.__add__(left)

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly can only multiply with integer object, float object, and Poly object')
        result = Poly()
        if type(right) in (int, float):
            for element in self.terms:
                result._add_term(self.terms[element]*right, element)
        if type(right) == Poly:
            for element in self.terms:
                for right_element in right.terms:
                    result._add_term(right.terms[right_element]*self.terms[element], element+right_element)
        return result

    def __rmul__(self,left):
        return self.__mul__(left)
    
    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly object can only relate to integer object, float object, or Poly object.')
        elif type(right) in (int, float):
            if 0 in self.terms:
                if self.terms[0] == right:
                    return True
                else:
                    return False
            else:
                return False
        elif type(right) == Poly:
            for element in self:
                if element in self and element in right:
                    if self.terms[element] != right.terms[element]:
                        return False
                else:
                    return False
            return True # returns true if none of the conditions for False were satisfied.

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