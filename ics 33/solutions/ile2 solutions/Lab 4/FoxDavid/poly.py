class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for term in terms:
            assert type(term[0]) in [int,float], 'coefficient must be int or float'
            assert type(term[1]) == int, 'power must be int'
            assert term[1] >= 0, "invalid power, must be greater than or equal to zero"
            assert term[1] not in self.terms, 'invalid power, a term has already been assigned with that power'
            if term[0] != 0:
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
        items = []
        for item in self.terms.items():
            items.append(str((item[1],item[0])))
        return 'Poly({})'.format(','.join(items))

    
    def __len__(self):
        if self.terms != {}:
            return max(self.terms.items())[0]
        else: return 0
    
    def __call__(self,arg):
        result = int()
        for power in self.terms:
            result += (self.terms[power] * (arg ** power))
        return result
    

    def __iter__(self):
        def _gen(d):
            for item in sorted(list(d.items()), key = lambda x: x[0], reverse = True):
                yield item[1],item[0]
        return _gen(self.terms)

    def __getitem__(self,index):
        if index >= 0 and type(index) == int:
            if index in self.terms:
                return self.terms[index]
            else: return 0
        elif type(index) != int:
            raise TypeError('argument must be integer')
        else:
            raise TypeError('argument must be greater or equal to than zero')

            

    def __setitem__(self,index,value):
        if index >= 0 and type(index) == int and value != 0:
            if value != 0:
                self.terms[index] = value
        elif index < 0:
            raise TypeError('first argument must be greater than or equal to zero')
        elif type(index) != int:
            raise TypeError('first argument must be type int')
            

    def __delitem__(self,index):
        if index >= 0 and type(index) == int and index in self.terms:
            del self.terms[index]
        elif index not in self.terms and index >= 0:
            pass
        elif type(index) != int:
            raise TypeError('argument must be integer')
        else:
            raise TypeError('argument must be greater or equal to than zero')

            

    def _add_term(self,c,p):
        if type(c) in [int,float] and type(p) == int and p >= 0:
            if p in self.terms:
                self.terms[p] += c
            if p not in self.terms:
                    self.terms[p] = c
            if self.terms[p] == 0:
                    del self.terms[p]
        elif type(c) not in [int,float]:
            raise TypeError('type of first argument must be int or float')
        elif type(p) != int:
            raise TypeError('second argument must be type int')
        else:
            raise TypeError('second argument must be >= 0')
       

    def __add__(self,right):
        result = Poly()
        if type(right) == Poly:
            for term in self:
                result._add_term(*term)
            for term in right:
                result._add_term(*term)
            return result
        elif type(right) in [int,float]:
            for term in self:
                result._add_term(*term)
            result._add_term(right,0)
            return result
        else:
            raise TypeError('invalid operand types for +: Poly and {}'.format(type(right)))

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        result = Poly()
        if type(right) == Poly:
            for selfterm in self:
                for term in right:
                    result._add_term(selfterm[0]*term[0],selfterm[1]+term[1])
            return result
        elif type(right) in [int,float]:
            for term in self:
                result._add_term(term[0]*right,term[1])
            return result
        else:
            raise TypeError('invalid operand types for *: Poly and {}'.format(type(right)))


    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) in [int,float]:
            return self.terms[0] == right
        else:
            raise TypeError('invalid operand types for ==: Poly and {}'.format(type(right)))

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()