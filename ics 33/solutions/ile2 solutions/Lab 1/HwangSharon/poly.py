class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for term in terms:
            if type(term[0]) in [int,float]:
                if type(term[1]) == int:
                    if term[1] >= 0:
                        if term[1] in self.terms:
                            raise AssertionError('Poly.__init__:illegal power in: ' + str(term))
                        elif term[0] == 0:
                            pass
                        else:
                            self.terms[term[1]] = term[0]
                    else:
                        raise AssertionError('Poly.__init__:illegal power in: ' + str(term))
                else:
                    raise AssertionError('Poly.__init__:illegal power in: ' + str(term))
            else:
                raise AssertionError('Poly.__init__:illegal power in: ' + str(term)) 
        
                
            
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
        for item in self.terms:
            curr_term = '(' + str(self.terms[item]) + ',' + str(item) + '),'
            result += curr_term
        result = result.rstrip(',')
        result += ')'
        return result

    
    def __len__(self):
        count = 0
        for term in self.terms:
            if term > count:
                count = term
        return count
            
    
    def __call__(self,arg):
        total = 0
        for term in self.terms:
            temp = arg ** term
            temp = temp * self.terms[term]
            total += temp
        return total
    

    def __iter__(self):
        items = []
        for term in self.terms:
            items.append(term)
        items.sort(reverse = True)
        for item in items:
            yield((self.terms[item],item))

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__:illegal index: ' + str(index))
        elif index < 0:
            raise TypeError('Poly.__getitem__:illegal index: ' + str(index))
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Poly.__setitem__:illegal index: ' + str(index))
        elif index < 0:
            raise TypeError('Poly.__setitem__:illegal index: ' + str(index))
        elif index in self.terms:
            if self.terms[index] == 0:
                del self.terms[index]
            else:
                self.terms[index] = value
        else:
            self.terms[index] = value
        remove = []
        for item in self.terms:
            if self.terms[item] == 0:
                remove.append(item)
        for item in remove:
            del self.terms[item]
                
                
    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__delitem__:illegal index: ' + str(index))
        elif index < 0:
            raise TypeError('Poly.__delitem__:illegal index: ' + str(index))
        elif index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Poly._add_term:illegal coefficient: ' + str(c))
        elif type(p) != int:
            raise TypeError('Poly._add_term:illegal power: ' + str(p))
        elif p < 0:
            raise TypeError('Poly._add_term:illegal power: ' + str(p))
        else:
            if p not in self.terms:
                if c != 0:
                    self.terms[p] = c
            else:
                temp = self.terms[p]
                self.terms[p] = temp + c
        remove = []
        for item in self.terms:
            if self.terms[item] == 0:
                remove.append(item)
        for item in remove:
            del self.terms[item]
            

    def __add__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Poly.__add__:illegal term: ' + str(right))
        else:
            result = Poly()
            for item in self.terms:
                result._add_term(self.terms[item],item)
            if type(right) == Poly:
                for item in right.terms:
                    result._add_term(right.terms[item],item)
            else:
                result._add_term(right,0)
            return result
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Poly.__mul__:illegal term: ' + str(right))
        else:
            result = Poly()
            if type(right) == Poly:
                for term in self.terms:
                    for item in right.terms:
                        result._add_term(right.terms[item] * self.terms[term],item + term)
            else:
                for term in self.terms:
                    result._add_term(right*self.terms[term],term)
            return result
        
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Poly.__eq__:illegal term: ' + str(right))
        else:
            if type(right) == Poly:
                return self.terms == right.terms
            else:
                return self.terms == {0:right}
    
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