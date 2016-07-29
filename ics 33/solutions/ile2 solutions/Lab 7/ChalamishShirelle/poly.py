from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        for coef, power in terms:
            if type(power) != int:
                raise AssertionError('Poly.__init__: illegal power in {}.'.format(type_as_str(coef, power)))
            if type(coef) not in (int, float):
                raise AssertionError('Coefficient is wrong type. Should be int/float, not {}.'.format(type_as_str(type(coef))))
            
            if power <0:
                raise AssertionError('Power must be >= 0. {} is less than 0'.format(type_as_str(power)))
            if power in self.terms.keys():
                raise AssertionError('Power already in dictionary.')
            
            else:
                if coef == 0:
                    continue
                else:
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
        lst = []
        for k, v in self.terms.items():
            lst.append('('+ str(v)+ ','+str(k)+')')
        string = ','.join(lst)
            
        return 'Poly('+string+')'
            
      
    def __len__(self):
        if len(self.terms.items()) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) not in (int, float):
            raise AssertionError('Wrong argument type. Type was {}, must be int or float.'.format(type_as_str(type(arg))))
        func = str(self).replace('x',str(arg))
        
        return eval(func)

    def __iter__(self):
        iterable = [power for power in self.terms.keys()]
        maxim= 0
        while len(iterable) != 0:
            maxim= max(iterable)
            yield (self.terms[maxim],maxim)
            iterable.remove(maxim)
            
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Index must be type int. Type {} given.'.format(type_as_str(type(index))))
        if index < 0:
            raise TypeError('Index must be greater than 0. {} < 0.'.format(type_as_str(index)))
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Index must be type int. Type {} given.'.format(type_as_str(type(index))))
        if index < 0:
            raise TypeError('Index must be greater than 0. {} < 0.'.format(type_as_str(index)))
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            self.terms[index] = value
       
        
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Index must be type int. Type {} given.'.format(type_as_str(type(index))))
        if index < 0:
            raise TypeError('Index must be greater than 0. {} < 0.'.format(type_as_str(index)))
        if index in self.terms.keys():
            del self.terms[index]
        
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('Coefficient must be int or float, not type {}.'.format(type_as_str(type(c))))
        if type(p) != int:
            raise TypeError('Power must be type int. Type {} given.'.format(type_as_str(type(p))))
        if p < 0:
            raise TypeError('Power must be greater than 0. {} < 0.'.format(type_as_str(p)))
        if p not in self.terms.keys():
            self.terms[p] = c
        if p in self.terms.keys():
            self.terms[p] = c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Incorrect type given. Must be int, float, or Polyl. Type {} given.'.format(type_as_str(type(right))))
        if type(right) == Poly:
            new = Poly()
            if len(right.terms.items()) == 0:
                for power in self.terms.keys():
                    new [power] = self.terms[power]
            for power in self.terms.keys():
                for other_power in right.terms.keys():
                    if other_power == power:
                        new_power = 0
                        new_power += self.terms[power] + right.terms[power]
                        if new_power == 0:
                            continue
                        else:
                            new.terms[power] = new_power
                    else:
                        new.terms[other_power] = right.terms[other_power]
                        new.terms[power] = self.terms[power]
            return new
        if type(right) in (int, float):
            new = Poly()
            for power in self.terms.keys():
                new[power] = self.terms[power]
            new[0] += right
            return new
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Incorrect type given. Must be int, float, or Polyl. Type {} given.'.format(type_as_str(type(right))))
        if type(right) == Poly:
            new = Poly()
            if len(right.terms.items()) == 0:
                return 0
            for power, coef in self.terms.items():
                for key, val in right.terms.items():
                    new_power = 0 
                    new_power += power*key
                    new_coef = 0 
        if type(right) in (int, float):
            new = Poly()
            for power in self.terms.keys():
                new_c = 0
                new_c += self.terms[power] * right
                if new_c == 0:
                    continue
                else:
                    new[power] = new_c
        return new
            
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Incorrect type given. Must be int, float, or Polyl. Type {} given.'.format(type_as_str(type(right))))
        if type(right) == Poly:
            flag = True
            while flag:
                for power, coef in self.terms.items():
                    for key, val in right.terms.items():
                        if power == key:
                            if coef == val:
                                flag = True
                            else:
                                flag = False
                        else:
                            flag = False
            return flag
                

    
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