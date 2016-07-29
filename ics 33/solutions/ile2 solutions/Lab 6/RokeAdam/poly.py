class Poly:
    
    def __init__(self,*terms):
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coeff, power in terms:
            if type(coeff) in (int, float):
                if type(power) == (int) and power >= 0:
                    if power not in (self.terms.keys()):
                        if coeff != 0:
                            self.terms[power] = coeff
                    else:
                        if self.terms[power] != coeff:
                            raise AssertionError('power referenced after establishment: powers cannot re-appear as later terms. power = ' +str(power))
                else:
                    raise AssertionError('invalid power value: powers must be integers greater than or equal to zero; ' + str(power) + ' given.')
            else:
                raise AssertionError('invalid coefficient value: coefficient must be type (int, float) and greater than zero')
            
    
    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        final = ''
        for power, coeff in self.terms.items():
            final += '(' + str(coeff) + ', ' + str(power) + '), '
        final = final[0:-2]
        return 'Poly(' + final + ')'

    
    def __len__(self):
        return max(self.terms.keys()) if self.terms != {} else 0
    
    
    def __call__(self,arg):
        if type(arg) in (int, float):
            final = 0
            for power, coeff in self.terms.items():
                final += ((arg**power) * coeff)
        return final
    

    def __iter__(self):
        def simple_gen():
            for power, coeff in self.terms.items():
                yield((coeff, power))
        
        for the_tuple in sorted(simple_gen(), key=(lambda x : x[1]), reverse=True):
            yield the_tuple #BOOM

    def __getitem__(self,index): # index is a power
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError('invalid index: index must be a positive integer but ' + str(index) + ' given.')
            

    def __setitem__(self,index,value): # index is a power, value is its associated coefficient
        if type(index) == int and index >= 0:
            if value != 0:
                self.terms[index] = value
            else:
                if index in self.terms.keys():
                    del self.terms[index]
        else:
            raise TypeError('invalid index: index must be a positive integer but ' + str(index) + ' given.')
            

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            raise TypeError('invalid index: index must be a positive integer but ' + str(index) + ' given.')
            

    def _add_term(self,c,p):
        if type(c) in (int, float) and type(p) == int and p >= 0:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p] += c
                if self.terms[p] == 0:
                    del self.terms[p]
        else:
            raise TypeError('invlaid coefficient or power value: coeff must be numeric and power must be a positive int')
       

    def __add__(self,right):
        if type(right) == Poly or type(right) in (int, float):
            if type(right) == Poly:
                result = Poly()
                for p, c in self.terms.items():
                    result._add_term(c, p)
                for p2, c2 in right.terms.items():
                    if p2 in result.terms.keys():
                        result[p2] += c2
                    else:
                        result[p2] = c2
                return result
            else:
                result = Poly()
                for p, c in self.terms.items():
                    result._add_term(c, p)
                result._add_term(right, 0)
                return result
        else:
            raise TypeError("invalid operand type. cannot add 'Poly' and '" + str(right) + "'")

    
    def __radd__(self,left):
        return self+left
    

    def __mul__(self,right):
        if type(right) == Poly or type(right) in (int, float):
            if type(right) != Poly:
                right = Poly((right, 0))
            
            result = Poly() # the new Poly object constructed to be returned
            # now do the calculation
            for p, c in self.terms.items():
                for p2, c2 in right.terms.items():
                    if (p+p2) in result.terms.keys():
                        result[p+p2] += (c*c2)
                    else:
                        result._add_term(c * c2, p+p2)
            return result
        else:
            raise TypeError("invalid operand type. cannot add 'Poly' and '" + str(right) + "'")

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) == Poly or type(right) in (int, float):
            if type(right) != Poly:
                right = Poly((right, 0))
            
            for p, c in self.terms.items():
                for p2, c2 in right.terms.items():
                    if not (p == p2) or not (c == c2):
                        return False
                    if not (p is p2) or not (c is c2):
                        return False
            return True
        else:
            raise TypeError("invalid operand types for Poly.__eq__: cannot compare 'Poly' and '" + type(right) + "'")

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
    
    
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