class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in [int, float], 'One or more of the coefficients was not an int or float.'
            assert type(term[1]) == int, 'One or more of the powers was not an int'
            assert term[1] >= 0, 'One or more of the powers was an int less than zero'
            assert term[1] not in self.terms, 'One or more of the powers was repeated'
            if term[0] != 0:
                self.terms[term[1]] = term[0]
        
        
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
        new = 'Poly('
        if self.terms == {}:
            return new + ')'
        for power, coeff in self.terms.items():
            new = new + '(' + str(coeff) + ',' + str(power) + ')' + ','
        return new[:-1] + ')'

    
    def __len__(self):
        high = 0
        if self.terms != {}:
            for item in self.terms.items():
                if item[0] > high:
                    high = item[0]
        return high
    
    def __call__(self,arg):
        assert type(arg) in [int, float], 'The argument must be an int or float'
        summation = 0
        if self.terms != {}:
            for power, coeff in self.terms.items():
                summation += coeff * ((arg)**power)
        return summation
        

    def __iter__(self):
        request = []
        count = self.__len__()
        if self.terms != {}:
            while True:
                for power, coeff in self.terms.items():
                    if power == count:
                        request.append((coeff, power))
                count -= 1
                if count == -1:
                    break
        return iter(request)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('The given index must be an int')
        elif index < 0:
            raise TypeError('The given index must be greater than zero')
        elif index in self.terms.keys():
            return self.terms.get(index)
        else:
            return 0
            
    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('The given index was not an int')
        elif index < 0:
            raise TypeError('The index provided was not greater than zero')
        elif type(value) not in [int, float]:
            raise TypeError('The value given was not an int or float')
        elif index in self.terms.keys(): 
            if value == 0:
                del self.terms[index]
            else:
                self.terms[index] = value
        else:
            if value != 0:
                self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('The given index was not an int')
        elif index < 0:
            raise TypeError('The index provided was not greater than zero')
        else:
            if index in self.terms.keys():
                del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError('The given index was not an int')
        elif p < 0:
            raise TypeError('The index provided was not greater than zero')
        elif type(c) not in [int, float]:
            raise TypeError('The value given was not an int or float')
        elif p not in self.terms.keys() and p != 0:
            self.terms[p] = c
        else:
            for power, coeff in self.terms.items():
                if power == p:
                    self.terms[p] = coeff + c 
            if self.terms.get(p) == 0:
                del self.terms[p]
       

    def __add__(self,right):
        new = []
        if type(right) in [int, float]:
            return None
            for item in self.terms.items():
                if item[0] == 0:
                    new.append((0, item[1] + right))
                else:
                    new.append(item)
            if 0 not in self.terms.keys():
                new.append(0, right)
        else:
            try:
                for power, coeff in self.terms.items():
                    for otherpow, othercoeff in right.terms.items():
                        if otherpow == power:
                            new.append((coeff + othercoeff, power + otherpow))
            except:
                raise TypeError('A Polynomial class must be added with an int or nother Polynomial')  
        evaluation = 'Poly('
        for coeff, power in new:
            evaluation = evaluation + '(' + str(coeff) + ',' + str(power) + '),'
        return exec(evaluation[:-1] + ')')
            
    
    def __radd__(self,left):
        new = []
        if type(left) in [int, float]:
            return None
            for item in self.terms.items():
                if item[0] == 0:
                    new.append((0, item[1] + left))
                else:
                    new.append(item)
            if 0 not in self.terms.keys():
                new.append(0, left)
        else:
            try:
                for power, coeff in self.terms.items():
                    for otherpow, othercoeff in left.terms.items():
                        if otherpow == power:
                            new.append((coeff + othercoeff, power + otherpow))
            except:
                raise TypeError('A Polynomial class must be added with an int or nother Polynomial')  
        evaluation = 'Poly('
        for coeff, power in new:
            evaluation = evaluation + '(' + str(coeff) + ',' + str(power) + '),'
        return exec(evaluation[:-1] + ')')
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) in [int, float]:
            for item in self.terms.items():
                if right == item[1]:
                    return True
            return False
        else:
            try:
                return self.terms == right.terms
            except:
                raise TypeError('The Polynomial class can only be compared to an int, float or another Polynomial')
            
            

    
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