class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for term in terms:
            coefficient,power = term
            if type(coefficient) not in (int,float) or type(power) != int or power < 0 or (power in self.terms and coefficient != 0):
                raise AssertionError
            if coefficient != 0:
                self.terms[power] = coefficient
        
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
        eval_str = 'Poly({})'
        value_str = ','.join(['({},{})'.format(self.terms[value],value) for value in self.terms])
        return eval_str.format(value_str)
        
    def __len__(self):
        powers = [power for power in self.terms]
        if powers == []:
            return 0
        lst = [power for power in self.terms]
        lst.sort(reverse=True)
        return lst[0]
    
    def __call__(self,arg):
        value = 0
        for power in self.terms:
            coefficient = self.terms[power]
            value += coefficient*(arg**power)
        return value
    

    def __iter__(self):
        powers = [power for power in self.terms]
        powers.sort(reverse=True)
        for power in powers:
            yield((self.terms[power],power))
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Type or Value of Index'+index+'is invalid')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Type or Value of Index'+index+'is invalid')
        if int(value) == 0:
            del self.terms[index]
        else:
            self.terms[int(index)] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Type or Value of Index'+index+'is invalid')
        powers = [power for power in self.terms]
        if index < len(powers)-1:
            value = powers[index]
            del self.terms[value]

    def _add_term(self,c,p):
        if type(c) not in (int,float) or type(p) != int or p < 0:
            raise TypeError('Values of c('+c+') or p('+p+') are of invalid form')
        if p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        elif p not in self.terms and c != 0:
            self.terms[p] = c
       

    def __add__(self,right):
        new_poly = Poly()
        self_values = self.terms
        for value in self_values:
                new_poly._add_term(self_values[value],value)
        if type(right) != type(self) and type(right) not in (int,float):
            raise TypeError('Type of right('+right+') is invalid')
        if type(right) in (int,float):
            new_poly.terms[0] += right
        elif type(self) == type(right):
            right_values = right.terms
            for value in right_values:
                new_poly._add_term(right_values[value], value)
        return str(new_poly)
                
        
    
    def __radd__(self,left):
        new_poly = Poly()
        self_values = self.terms
        for value in self_values:
                new_poly._add_term(self_values[value],value)
        if type(left) != type(self) and type(left) not in (int,float):
            raise TypeError('Type of right('+left+') is invalid')
        if type(left) in (int,float):
            new_poly.terms[0] += left
        elif type(self) == type(left):
            left_values = left.terms
            for value in left_values:
                new_poly._add_term(left_values[value], value)
        return str(new_poly)
    

    def __mul__(self,right):
        new_poly = Poly()
        if type(right) != type(self) and type(right) not in (int,float):
            raise TypeError('Type of right('+right+') is invalid')
        if type(right) in (int,float):
            self_values = self.terms
            for value in self_values:
                new_poly._add_term(self_values[value],value)
            for value in new_poly.terms:
                new_poly.terms[value] *= right
        elif type(right) == type(self):
            for r_power in right.terms:
                for s_power in self.terms:
                    new_poly._add_term(right.terms[r_power]*self.terms[s_power],r_power+s_power)
        return str(new_poly)

    def __rmul__(self,left):
        new_poly = Poly()
        if type(left) != type(self) and type(left) not in (int,float):
            raise TypeError('Type of right('+left+') is invalid')
        if type(left) in (int,float):
            self_values = self.terms
            for value in self_values:
                new_poly._add_term(self_values[value],value)
            for value in new_poly.terms:
                new_poly.terms[value] *= left
        elif type(left) == type(self):
            for r_power in left.terms:
                for s_power in self.terms:
                    new_poly._add_term(left.terms[r_power]*self.terms[s_power],r_power+s_power)
        return str(new_poly)
    

    def __eq__(self,right):
        flag = False
        if type(right) not in (Poly,int,float):
            raise TypeError('Type of right('+right+') is in valid')
        if type(right) == type(self):
            if all([self.terms[power]==right.terms[power] for power in self.terms]):
                flag = True
        elif type(right) in (int,float):
            if all([power==0 for power in self.terms]):
                flag = True
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