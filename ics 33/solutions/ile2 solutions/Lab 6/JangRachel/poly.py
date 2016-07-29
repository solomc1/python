class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.t = terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i in range(len(terms)):
            c,p = terms[i][0], terms[i][1]
            assert type(c) is int or type(c) is float
            assert type(p) is int and p >= 0
            assert p not in self.terms
            if c != 0:
                self.terms[terms[i][1]] = terms[i][0]

            
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
        return 'Poly' + str(self.t)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms)
    
    def __call__(self,arg):
        answer = 0
        for p,c in self.terms.items():
            answer += (arg**p * c)
        return answer
    

    def __iter__(self):
        for i in sorted(self.terms.items(), reverse=True):
            yield (i[1], i[0])
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: illegal index')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: illegal index')
        elif value == 0:
            if value in self.terms:
                self.terms.__delitem__(value)
        else:
            self.terms[value] = index
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: illegal index')
        elif index not in self.terms:
            return self.__str__()
        else:
            self.terms.__delitem__(index)
            

    def _add_term(self,c,p):
        if type(c) is not int and type(c) is not float:
            raise TypeError('Poly._add_term: illegal coefficient')
        if type(p) is not int or p < 0:
            raise TypeError('Poly._add_term: illegal power')
        if p != 0:
            if p not in self.terms:
                self.terms[p] = c
            else:
                self.terms[p]+=c

       

    def __add__(self,right):
        result = Poly()
        if type(right) is Poly:
            for p,c in self.terms.items():
                result._add_term(c,p)
            for p,c in right.terms.items():
                result._add_term(c,p)
            return result
        elif type(right) is int or type(right) is float:
            result._add_term(0, right)
            return result
        else:
            raise TypeError('Poly.__add__: right is illegal')

    
    def __radd__(self,left):
        result = Poly()
        if type(left) is Poly:
            for p,c in self.terms.items():
                result._add_term(c,p)
            for p,c in left.terms.items():
                result._add_term(c,p)
            return result  
        elif type(left) is int or type(left) is float:
            result._add_term(0, left)
            return result
        else:
            raise TypeError('Poly.__add__: left is illegal')
    

    def __mul__(self,right):
        result = Poly()
        if type(right) is Poly:
            for p,c in self.terms.items():
                result._add_term(c,p)
            return result
        elif type(right) is int or type(right) is float:
            for p,c in self.terms.items():
                result._add_term(c*right, p)
            return result
        else:
            raise TypeError('Poly.__mul__: right is illegal')
    

    def __rmul__(self,left):
        result = Poly()
        if type(left) is Poly:
            for p,c in self.terms.items():
                result._add_term(c,p)
            return result
        elif type(left) is int or type(left) is float:
            for p,c in self.terms.items():
                result._add_term(c*left, p)
            return result
        else:
            raise TypeError('Poly.__mul__: left is illegal')
    

    def __eq__(self,right):
        if type(right) is Poly:
            return self.terms == right.terms
        elif type(right) is int or type(right) is float:
            for p,c in self.terms.items():
                if p > 0:
                    return False
                else:
                    return c == right
        else:
            raise TypeError('Poly.__eq__: right is illegal')

    
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