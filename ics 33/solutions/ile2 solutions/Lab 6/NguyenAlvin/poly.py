class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coef, power in terms:
            if type(coef) != int and type(coef) != float:
                raise AssertionError('Illegal coefficient in ({},{})'.format(coef, power))
            if type(power) != int or power < 0:
                raise AssertionError('Illegal power in ({},{})'.format(coef, power))
            if power in self.terms.keys():
                raise AssertionError('Illegal power in ({},{})'.format(coef, power))
            if coef != 0:
                self.terms[power] = coef
        
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
        terms = []
        for power, coef in self.terms.items():
            terms.append((coef,power))
        terms = str(terms).strip('[').strip(']')
        return 'Poly({})'.format(terms)

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max(power for power in self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) != int and type(arg) != float:
            raise AssertionError
        result = 0
        for power, coef in self.terms.items():
            result += (arg**power)*coef
        return result
    

    def __iter__(self):
        items = sorted(self.terms.items(), key = lambda x: x[0], reverse = True)
        for item in items:
            yield (item[1],item[0])
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index has to be an int and greater than 0.')
        if index in self.terms:
            return self.terms[index]
        else:
            return int(0)
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index has to be an int and greater than 0.')
        if value != 0:
            self.terms[index] = value
        else:
            if index in self.terms:
                self.terms.pop(index)
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index has to be an int and greater than 0.')
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise AssertionError('Illegal coefficient in ({},{})'.format(c, p))
        if type(p) != int or p < 0:
            raise AssertionError('Illegal power in ({},{})'.format(c, p))
        if c != 0:
            if p in self.terms.keys():
                self.terms[p] += c
                if self.terms[p] == 0:
                    self.terms.pop(p)
            else:
                self.terms[p] = c

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly can only be added with other polies, int, or float.')
        new = eval(self.__repr__())
        if type(right) == Poly:
            for power, coef in right.terms.items():
                new._add_term(coef, power)
        else:
            new._add_term(right, 0)
        return new

    
    def __radd__(self,left):
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError('Poly can only be added with other polies, int, or float.')
        new = eval(self.__repr__())
        if type(left) == Poly:
            for power, coef in left.terms.items():
                new._add_term(coef, power)
        else:
            new._add_term(left, 0)
        return new

    

    def __mul__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly can only be multiplied with other polies, int, or float.')
        new = Poly()
        if type(right) == Poly:
            for power, coef in right.terms.items():
                for power2, coef2 in self.terms.items():
                    new._add_term((coef*coef2), (power+power2))
        else:
            for power, coef in self.terms.items():
                new._add_term((right*coef), (power))
        return new
    

    def __rmul__(self,left):
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError('Poly can only be multiplied with other polies, int, or float.')
        new = Poly()
        if type(left) == Poly:
            for power, coef in left.terms.items():
                for power2, coef2 in self.terms.items():
                    new._add_term((coef*coef2), (power+power2))
        else:
            for power, coef in self.terms.items():
                new._add_term((left*coef), (power))
        return new

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly can only be related with other polies, int, or float.')
        if type(right) == Poly:
            return self.terms == right.terms
        else:
            if len(self.terms) == 1 and 0 in self.terms.keys():
                return self.terms[0] == right
            else:
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