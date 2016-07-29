class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coe,pow in terms:
            assert type(coe) is float or int, 'coefficient is not an int or float object'
            assert type(pow) is int and pow >= 0, 'power is not an int object or the value of power is not greater or equal to zero'
            if coe != 0:
                assert pow not in self.terms.keys(), 'earlier power term has already appeared'
                self.terms[pow] = coe
        
        
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
        return 'Poly('+', '.join(['('+str(k)+','+str(i)+')' for i,k in sorted(self.terms.items(), reverse = True)])+')'

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        answer = 0
        if arg < 0:
            raise TypeError()
        for pow,coe in self.terms.items():
            answer += coe*(arg**pow)
        return answer
    

    def __iter__(self):
        for pow,coe in sorted(self.terms.items(), reverse = True):
            yield (coe,pow)
            

    def __getitem__(self,index):
        if type(index) is not int and index < 0:
            raise TypeError('Index is not an int object or index is not greater than zero')
        if index < 0:
            raise TypeError()
        if index not in self.terms.keys():
            return 0 
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Index is not an int object or index is not greater than zero')
        if index < 0:
            raise TypeError()
        if value == 0:
            for pow,coe in self.terms.items():
                if value == coe:
                    del self.terms[pow]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Index is not an int object or index is not greater than zero')
        if index < 0:
            raise TypeError()
        assert index in self.terms.keys()
        del self.terms[index]    

    def _add_term(self,c,p):
        if type(c) is not int:
            raise TypeError('Coefficient is not an int or a float object')
        if type(p) is not int and p < 0:
            raise TypeError('Index is not an int object or index is not greater than zero')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]    

    def __add__(self,right):
        result = Poly()
        for pow,coe in self.terms.items():
            result[pow] = coe
        if type(right) is Poly:
            for pow,coe in right.terms.items():
                if pow in result.terms.keys():
                    result.terms[pow] += coe
                else:
                    result.terms[pow] = coe
            return result.__str__()
        elif type(right) is int or float:
            result.terms[0] += right
            return result.__str__()
        else:
            raise TypeError('Argument is not a Polynoimal or an int or a float')

    
    def __radd__(self,left):
        result = Poly()
        for pow,coe in self.terms.items():
            result[pow] = coe
        if type(left) is int or float:
            result.terms[0] += left
            return result.__str__()
        else:
            raise TypeError('Argument is not an int or a float')
    

    def __mul__(self,right):
        result = Poly()
        for pow,coe in self.terms.items():
            result[pow] = coe
        if type(right) is Poly:
            for pow,coe in self.terms.items():
                for p,c in right.terms.items():
                    if pow+p not in result.terms.keys():
                        result[pow+p] = coe*c
                    else:
                        value = coe*c
                        result[pow+p] += value
        elif type(right) is int or float:
            for pow,coe in self.terms.items():
                value = coe*right
                result[pow] = value
        return result.__str__()
                    
    

    def __rmul__(self,left):
        result = Poly()
        for pow,coe in self.terms.items():
            result[pow] = coe
        if type(left) is int:
            
    

    def __eq__(self,right):
        if type(right) is Poly:
            for pow,coe in right.terms.items():
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