class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms\
        self.terms = {}
        for term in terms:
            assert type(term[0]) in [int,float], 'Poly.__init__ error: coefficients must be of type int or float'
            assert term[1] >= 0, 'Poly.__init__ error: Powers must be greater than or equal to \'0\''
            assert term[1] not in self.terms.keys(), 'Poly.__init__ error: Power can only be used once!'
            assert type(term[1]) == int, 'Poly.__init__ error: power must be of type int!'
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
        final_str = 'Poly'
        key_len = len(self.terms.keys())
        count = 0
        for key in self.terms.keys():
            final_str += '(' + str(self.terms[key]) + ',' + str(key)
            count += 1
            if count != key_len:
                final_str += '),'
            else:
                final_str += ')'
        final_str += ')'
        return final_str

    
    def __len__(self):
        key_list = []
        if len(self.terms.keys()) == 0:
            return 0
        for key in self.terms.keys():
            key_list.append(key)
        maximum = max(key_list)
        return maximum
    
    def __call__(self,arg):
        sum_of_poly = 0
        for key in self.terms.keys():
            arg_raised = arg
            if key == 0:
                arg_raised = 1
            else:
                for i in range(key-1):
                    arg_raised *= arg
            sum_of_poly += self.terms[key] * arg_raised
        return sum_of_poly
    

    def __iter__(self):
        key_list = []
        for key in self.terms.keys():
            key_list.append(key)
        key_list.sort(reverse = True)
        for key in key_list:
            yield(self.terms[key],key)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Poly.__getitem__ error: power must be type int!')
        if index < 0:
            raise TypeError('Poly.__getitem__ error: power must be greater than or equal to \'0\'')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Poly.__setitem__ error: power must be type int!')
        if index < 0:
            raise TypeError('Poly.__setitem__ error: power must be greater than or equal to \'0\'')
        if value == 0 and value in self.terms.values():
            for key in self.terms.keys():
                if self.terms[key] == value:
                    del self.terms[key]
        else:
            if index in self.terms.keys():
                self.terms.update(index = value)
        self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError('Poly.__delitem__ error: power must be greater than or equal to \'0\'')
        if index in self.terms.keys():
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Poly._add_term error: coefficient must be a numeric value!')
        if p < 0:
            raise TypeError('Poly._add_term error: power must be greater than or equal to \'0\'')
        if ((p not in self.terms.keys()) and (c != 0)):
            self.terms[p] = c
        elif p in self.terms.keys():
            curr_coeff = self.terms[p]
            final_coeff = curr_coeff + c
            if final_coeff == 0:
                del self.terms[p]
            else:
                self.terms[p] = final_coeff
        
       

    def __add__(self,right):
        if type(right) == int:
            pass
        else:
            for key in right.terms.keys():
                self._add_term(right.terms[key],key)
        return self
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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