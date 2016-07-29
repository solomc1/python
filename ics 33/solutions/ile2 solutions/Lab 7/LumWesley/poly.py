class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if i[0] != 0:
                if type(i[0]) != int and type(i[0]) != float:
                    raise AssertionError('Poly.__init__: coefficient (' + str(i[0]) + ') must be an int or float')
                elif type(i[1]) != int or i[1] < 0:
                    raise AssertionError('Poly.__init__: power (' + str(i[1]) + ') must be an int whose value is >= 0')
                for power, coeff in self.terms.items():
                    if i[1] == power:
                        raise AssertionError('Poly.__init__: every input power must be different')
                self.terms[i[1]] = i[0]
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
        return_value = set()
        for power, coeff in self.terms.items():
            return_value.add((power, coeff))
        return('Poly' + str(tuple(return_value)))
    
    def __len__(self):
        length = 0
        for power, coeff in self.terms.items():
            if power > length:
                length = power
        return(length)
    
    def __call__(self,arg):
        total = 0
        if type(arg) != float and type(arg) != int:
            raise AssertionError
        for power, coeff in self.terms.items():
            number = arg**power
            temp_total = coeff*number
            total += temp_total
        return(total)

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: index (' + str(index) + ') must be an integer less than 0')
        for power, coeff in self.terms.items():
            if index == power:
                return(coeff)
        return(0)
            

    def __setitem__(self,index,value):
        print(self.terms)
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: power (' + str(index) + ') must be an positive integer')
        print(index, value)
        if value in self.terms.values():
            self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitem__: index (' + str(index) + ') must be an integer less than 0')
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != float and type(c) != int:
            raise TypeError('Poly._add_term(self,c,p): coefficient (' + str(c) + ') must be an int or float')
        elif type(p) != int or p <0:
            raise TypeError('Poly._add_term(self,c,p): power (' + str(p) + ') must be an integer >= 0')
        if p in self.terms.keys():
            result = self.term[p] + c
            if result == 0:
                self.terms.pop(p)
            print(result)
            self.term[p] = result
        elif p not in self.terms.keys() and c != 0:
            print('hello')
            self.terms[p] = c

    def __add__(self,right):
        if type(right) == Poly:
            total = set()
            for power, coeff in self.terms.items():
                print(power,coeff)
                for rpower, rcoeff in right.terms.items():
                    if rpower == power:
                        new = rcoeff + coeff
                        if new != 0:
                            total.add((power, new))
                total.add((power, coeff))
            x = (tuple(total))
        elif type(right) == int or type(right) == float:
            total = self.terms[0] + right
            if total != 0:
                self.terms[0] = right
                return(self.terms)
            else:
                self.pop(0)
                return(self.terms)
        else:
            raise TypeError('Poly.__add__: type(' + str(right) + ') must be Poly, int or float')

    
    def __radd__(self,left):
        return(self + left)
    

    def __mul__(self,right):
        
        return_value = ()
        if type(right) == Poly:
            pass
        elif type(right) == int or type(right) == float:
            print(right, self.terms)
            for power, coeff in self.terms.items():
                self.terms[power] = coeff*2
        print(self.terms)
        for power, coeff in self.terms.items():
            return_value += (power, coeff)
        print(return_value)
    

    def __rmul__(self,left):
        return(self * left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            if len(self.terms) != len(right.terms):
                return(False)
            return(self.terms.items() == right.terms.items())
        elif type(right) == int or type(right) == float:
            if len(self.terms) != 1:
                return(False)
            for power, coeff in self.terms.items():
                if coeff != right:
                    return(False)
                elif power != 0:
                    return(False)
            return(True)
        else:
            raise TypeError('Poly.__eq__: type(' + str(right) + ') must be Poly, int or float')

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    '''print('Start simple tests')
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
    print('End simple tests\n')'''
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()