class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:

            if type(x[0]) is not int and type(x[0]) is not float: raise AssertionError('Coefficients must be int or float type.')
            if type(x[1]) is not int: raise AssertionError('Power must be an integer.')
            if not x[1] >= 0: raise AssertionError('Power must be greater than or equal to zero.')
            if x[1] in self.terms.keys() and self.terms[x[1]] != x[0]: raise AssertionError('A power cannot appear as a later term if it appears at earlier term.')
            if not x[0] == 0:
                self.terms[x[1]] = x[0]
        
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
        if self.terms == {}:
            return 'Poly()'
        else:
            return ('Poly(' + ''.join(['(' + str(self.terms[x]) + ',' + str(x) + '),' for x in self.terms]))[:-1] + ')'

    
    def __len__(self):
        if len(self.terms.keys()) != 0:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        total = 0
        for key in self.terms.keys():
            total += (pow(arg, key) * self.terms[key])
        return total

    def __iter__(self):
        k_lst = [k for k in self.terms.keys()]
        for k in sorted(k_lst, reverse = True):
            yield ( self.terms[k],k)
            
    def __getitem__(self,index):
        if type(index) is not int: raise TypeError('Index must be an integer.')
        if index < 0: raise TypeError('Index cannot be less than zero.')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int: raise TypeError('Index must be an integer.')
        if index < 0: raise TypeError('Index cannot be less than zero.')
        for k in self.terms:
            if self.terms[k] == 0:
                self.terms.pop(k)
        self.terms[index] = value

    def __delitem__(self,index):
        if type(index) is not int: raise TypeError('Index must be an integer.')
        if index < 0: raise TypeError('Index cannot be less than zero.')
        if index in self.terms:
            self.terms.pop(index)
        
            
    def _add_term(self,c,p):
        if type(c) is not int and type(c) is not float: raise TypeError('Coefficients must be int or float type.')
        if not p >= 0: raise TypeError('Power must be >= 0.')
        if p in self.terms.keys():
            new_c = c + self.terms[p]
            self.terms[p] = new_c
        else:
            self.terms[p] = c
            
        return str(self)
        
    
    def __add__(self,right):
        if type(right) == Poly:
            for x in right.terms.keys():
                if x in self.terms.keys():
                    new_c = right.terms[x] + self.terms[x]
                    self.terms[x] = new_c
                else:
                    self.terms[x] = right.terms[x]
                    
            return str(self)
            
        elif type(right) == int or type(right) == float:
            new_c =  self.terms[0] + right
            self.terms[0] = new_c
            return str(self)
    
        else:
            raise TypeError('Must be int, float or Poly type.')
    
    
        
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) == int or type(right) == float:
            if right != 0:
                for x in self.terms:
                    self.terms[x] = right * self.terms[x]
                return str(self)
            else:
                return 0
        elif type(right) == Poly:
            if right.terms == {}:
                return 0
            
            #else:
            
            
        else:
            raise TypeError('must be in integer , float or poly type.')
    

    def __rmul__(self,left):
        return self.__mul__(left)
    
    def __eq__(self,right):
        if type(right) == Poly:
            for x in right.terms.keys():
                if not right.terms[x] == self.terms[x]:
                    return False
            return True
        elif type(right) == int or type(right) == float:
            if len(self.terms.keys()) == 1 and self.terms[0] == right:
                return True
            else:
                return False
        else:
            raise TypeError('Must be in int , float or Poly type.')

    
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