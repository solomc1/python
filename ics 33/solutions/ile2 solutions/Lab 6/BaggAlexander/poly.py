class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            if type(t[0]) != int and t[0] != float:
                raise AssertionError('Coefficient values must be type int or float')
            elif type(t[1]) != int:
                raise AssertionError('Power values must be type int')
            elif t[1] < 0:
                raise AssertionError('Power values must be greater than or equal to zero')
            elif t[1] in self.terms.keys():
                raise AssertionError('Cannot repeat multiple power values')
            else: 
                self.terms[t[1]]=t[0]
        
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
        return 'Poly'+str(tuple((v,k) for k,v in self.terms.items()))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            if k == 0:
                total += v
            else:
                total += v*(arg**k)
        return total
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(),reverse=True):
            yield (v,k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Power index must be an int that is greater than or equal to zero')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Power index must be an int that is greater than or equal to zero')
        elif value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Power index must be an int that is greater than or equal to zero')
        else:
            if index in self.terms.keys():
                self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise AssertionError('Coefficient values must be type int or float')
        elif type(p) != int or p < 0:
            raise TypeError('Power index must be an int that is greater than or equal to zero')
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if c+self.terms[p] == 0:
                self.terms.pop(p)
            else:
                self.terms[p] += c
        

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly object can only add other Poly objects, ints, or floats')
        elif type(right) == Poly:
            poly_add = self
            for k,v in right.terms.items():
                if k in self.terms.keys():
                   poly_add.terms[k] += v
                else:
                   poly_add.terms[k] = v
            return  poly_add
        else:
            poly_add = self
            poly_add.terms[0] += right
            return poly_add
            
            
    
    def __radd__(self,left):
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError('Poly object can only add other Poly objects, ints, or floats')
        elif type(left) == Poly:
            poly_add = self
            for k,v in left.terms.items():
                if k in self.terms.keys():
                   poly_add.terms[k] += v
                else:
                   poly_add.terms[k] = v
            return  poly_add
        else:
            poly_add = self
            poly_add.terms[0] += left
            return poly_add
    

    def __mul__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly object can only add other Poly objects, ints, or floats')
        elif type(right) == Poly:
            pass
        else:
            poly_mul = self
            for k,v in poly_mul.terms.items():
               poly_mul.terms[k] *= right
            return poly_mul 

    def __rmul__(self,left):
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError('Poly object can only add other Poly objects, ints, or floats')
        elif type(left) == Poly:
            pass
        else:
            poly_mul = self
            for k,v in poly_mul.terms.items():
               poly_mul.terms[k] *= left
            return poly_mul
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Poly object can only add other Poly objects, ints, or floats')
        elif type(right) == Poly:
            return sorted(self.terms) == sorted(right.terms)
        else:
            if len(self.terms) == 1:
                if list(self.terms.keys())[0] == 0:
                    return self.terms[0] == right
            else:
                return False

    
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