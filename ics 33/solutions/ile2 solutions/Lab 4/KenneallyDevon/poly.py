class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        #print(terms)
        #assert (type(x[0]) == int or type(x[0]) == float for x in terms), 'poly.__init__ :Coefficient must be int or float'
        #assert (type(x[1]) == int and x[1] >= 0 for x in terms), 'poly.__init__ :power must be int >=0'
        self.terms = {}
        for coefficient, power in terms:
            assert (type(coefficient) == int or type(coefficient) == float), 'poly.__init__ :Coefficient must be int or float'
            assert (type(power) == int and power>=0), 'poly.__init__ :power must be int >=0'
            if power in self.terms.keys():
                if self.terms[power] == 0:
                    self.terms[power] = coefficient
                else:
                    assert (power not in self.terms.keys()), 'poly.__init__ :power cannot appear as a later term if it appears with a non zero coefficient as an erlier term'
            elif coefficient !=0:
                self.terms[power] = coefficient
                #print(self.terms)
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
        result = 'Poly('
        for power,coefficient in self.terms.items():
            result += '({},{}),'.format(coefficient,power)
        if len(list(self.terms.items())) >0:
            result = result[:-1]
        result += ')'
        return result

    
    def __len__(self):
        result = 0
        for power, coefficient in self.terms.items():
            if power > result:
                result = power
        return result
        
    
    def __call__(self,arg):
        result = 0
        for power, coefficient in self.terms.items():
            result += (coefficient* (arg**power))
        return result
        
    

    def __iter__(self):
        sorted_t = list(self.terms.items())
        sorted_t.sort(reverse =True)
        for power, coefficient in sorted_t:
            yield (coefficient,power)
        
            

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Poly.__getitem__: index must be int greater then 0')
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError('Poly.__setitem__: index must be int greater then 0')
        elif value ==0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index]= value
            

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Poly.__delitem__: index must be int greater then 0')
        elif index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(p) != int or type(c) != int and type(c) != float or p<0:
            raise TypeError('Poly.__delitem__: power must be int greater then 0 and coefficient must be int or float')
        elif p not in self.terms.keys() and p >=0:
            self.__setitem__(p,c)
        elif p in self.terms.keys() and p>=0:
            self.__setitem__(p,(c+self.terms[p]))
       

    def __add__(self,right):
        empty = Poly()
        if type(right) ==int or type(right)== float:
            for power, coefficient in self.terms.items():
                empty._add_term(coefficient,power)
            empty._add_term(right,0)
            return empty
        elif type(right) == Poly:
            for power, coefficient in self.terms.items():
                empty._add_term(coefficient,power)
            for power, coefficient in right.terms.items():
                empty._add_term(coefficient,power)
            return empty
        else:
            raise TypeError('Invalid operands for + : Poly and {}'.format(right))
        

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        empty = Poly()
        if type(right) ==int or type(right)== float:
            for power, coefficient in self.terms.items():
                empty._add_term(coefficient*right,power)
            return empty
        elif type(right) == Poly:
            for power, coefficient in self.terms.items():
                for rpower,rcoefficient in right.terms.items():
                    empty._add_term(coefficient*rcoefficient, power+rpower)
            return empty
        else:
            raise TypeError('Invalid operands for * : Poly and {}'.format(right))

    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) ==int or type(right)== float:
            if str(self) == str(right):
                return True
            return False
        elif type(right) == Poly:
            if str(self) == str(right):
                return True
            else:
                return False
        else:
            raise TypeError('Invalid operands for == : Poly and {}'.format(right))

    
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