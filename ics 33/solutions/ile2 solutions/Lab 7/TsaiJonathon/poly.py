class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for j,k in terms:
            if type(j) is not int and type(j) is not float:
                raise AssertionError('Coefficient must be type int or float')
            if type(k) is not int or k<0:
                raise AssertionError('Power must be greater than 0')
            if k in self.terms.keys():
                raise AssertionError('Power repeated')
            if j != 0 and k not in self.terms.items():
                self.terms[k]=j
        
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
        poly_rep = 'Poly(' 
        for j,k in self.terms.items():
            poly_rep += '(' + str(k) + ',' + str(j) + ')' + ','
        if poly_rep[-1] == ',':
            poly_rep = poly_rep[:-1]
        poly_rep += ')'
        return poly_rep
        

    
    def __len__(self):
        highest_power = 0
        for j,k in self.terms.items():
            if j> highest_power:
                highest_power = j
        return highest_power
    
    def __call__(self,arg):
        result = 0
        for j,k in self.terms.items():
                result += k*(arg**j)
        return result
    

    def __iter__(self):
        max_list = []
        for j in self.terms.keys():
            max_list.append(j)
        while len(max_list)!=0:
            highest_power = max(max_list)
            max_list.remove(highest_power)
            yield (self.terms[highest_power],highest_power)
            

    def __getitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError('Argument must be integer and greater than 0')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index <0:
            raise TypeError('Power value must be int and greater than 0')
        if value == 0 and index in self.terms.keys():
            del(self.terms[index])
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index <0:
            raise TypeError('Power should be int and greater than 0')
        if index in self.terms.keys():
            del(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) is not int and type(c) is not float:
            raise TypeError('Coefficent must be int or float')
        if p<0 or type(p) is not int:
            raise TypeError('Power must be greater than 0')
        if p not in self.terms.keys() and c != 0:
            self.terms[p]=c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del(self.terms[p])
        

    def __add__(self,right):
        if type(self) is not Poly:
            raise TypeError('Operand must be Poly')
        if type(right) is not int and type(right) is not float and type(right) is not Poly:
            raise TypeError('right operand must be int or float')
        if type(right) is int or type(right) is float:
            new_poly = Poly()
            for j,k in self.terms.items():
                new_poly._add_term(k,j)
            new_poly._add_term(right,0)
        else:
            new_poly = Poly()
            for j,k in right.terms.items():
                new_poly._add_term(k, j)
            for a,b in self.terms.items():
                new_poly._add_term(b,a)
            
        return new_poly
    
    def __radd__(self,left):
        new_poly = self
        if type(self) is not Poly:
            raise TypeError('Operand must be Poly')
        if type(left) is not int and type(left) is not float and type(left) is not Poly:
            raise TypeError('right operand must be int or float')
        if type(left) is int or type(left) is float:
            new_poly._add_term(left,0)
            for a,b in self.terms.items():
                new_poly._add_term(b,a)
        else:
            for j,k in left.terms.items():
                new_poly._add_term(k, j)
            for a,b in self.terms.items():
                new_poly._add_term(b,a)
        return new_poly
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(self) is not Poly:
            raise TypeError('Operand must be Poly')
        if type(right) is not int and type(right) is not float and type(right) is not Poly:
            raise TypeError('right operand must be int or float')
        if type(right) is int or type(right) is float:
            return right in self.terms[0]
        elif type(self) is int or type(self) is float:
            return self in right.terms[0]
        else:
            for j,k in right.terms.items():
                if k not in self.terms.keys():
                    return False
                if self.terms[k] != right.terms[k]:
                    return False
        return True

    
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