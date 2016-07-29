class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            # term[0] is the coefficient
            # term[1] is the power
            if type(term[0]) != int and type(term) != float:
                raise AssertionError('Poly.__init__: illegal power in :', term)
            if type(term[1]) != int or term[1] < 0:
                raise AssertionError('Poly.__init__: illegal power in :', term)
            if term[0] != 0:
                if term[1] in self.terms.keys():
                    raise AssertionError('Poly.__init__: illegal power in :', term)
                self.terms[term[1]] = term[0]
        
        # Fill in the rest of this method, using *terms to initialize self.terms

            
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
        result_str = 'Poly('
        count = 0
        for term in self.terms:
            count += 1
            if count == 1:
                result_str += '(' + str(self.terms[term]) + ',' + str(term) + ')'
            else:
                result_str += ',(' + str(self.terms[term]) + ',' + str(term) + ')'
        result_str += ')'
        return result_str
            

    
    def __len__(self):
        highest = 0
        for term in self.terms:
            if term > highest:
                highest = term
        return highest
            
    
    def __call__(self,arg):
        result = 0
        for term in self.terms:
            result += (arg ** term) * self.terms[term]
        return result
            
    

    def __iter__(self):
        append_list = []
        for term in self.terms:
            append_list.append((self.terms[term], term))
        append_list = sorted(append_list, key = lambda x : x[1], reverse = True)
        for element in append_list:
            yield element
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be non-negative integer')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('index must be non-negative integer')
        if value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be non-negative integer')
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Coefficient must be either an int or a float')
        if type(p) != int or p < 0:
            raise TypeError('Power must be a non-negative integer')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
            
       

    def __add__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError('The operand must be an int, float, or polynomial')
        result_poly = Poly()
        if type(right) == Poly:
            for term in self.terms:
                result_poly._add_term(self.terms[term], term)
            for term in right.terms:
                result_poly._add_term(right.terms[term], term)
        if type(right) == int or type(right) == float:
            for term in self.terms:
                result_poly._add_term(self.terms[term], term)
            result_poly._add_term(right, 0)
        return result_poly

    
    def __radd__(self,left):
        if type(left) != int and type(left) != float and type(left) != Poly:
            raise TypeError('The operand must be an int, float, or polynomial')
        result_poly = Poly()
        if type(left) == Poly:
            for term in self.terms:
                result_poly._add_term(self.terms[term], term)
            for term in left.terms:
                result_poly._add_term(left.terms[term], term)
        if type(left) == int or type(left) == float:
            for term in self.terms:
                result_poly._add_term(self.terms[term], term)
            result_poly._add_term(left, 0)
        return result_poly
    

    def __mul__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError('The operand must be an int, float, or polynomial')
        result_poly = Poly()
        if type(right) == Poly:
            for term in self.terms:
                power = term + right[term]
    

    def __rmul__(self,left):
        if type(left) != int and type(left) != float and type(left) != Poly:
            raise TypeError('The operand must be an int, float, or polynomial')
    

    def __eq__(self,right):
        pass

    
if __name__ == '__main__':
    p = Poly((3,2),(4,0))
    print(p)
    print(p + 1)
    print()
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