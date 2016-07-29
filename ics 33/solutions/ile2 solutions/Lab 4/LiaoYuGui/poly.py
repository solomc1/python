class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        samepower = []
        acount = 0
        for i in terms:
            if type(i[0]) in [int, float]:
                if type(i[1]) is int:
                    if i[1] < 0:
                        raise AssertionError('Power cannot be less than 0.')
                    self.terms[i[1]] = i[0] 
                    if i[0] == 0:
                        del self.terms[i[1]]
                    #===========================================================
                    # if i[0] != 0:
                    #     samepower.append(i[1])
                    # if i[1] in samepower:
                    #     acount +=1
                    #     if acount >= 2:
                    #         raise AssertionError('Multiple identical powers not valid.')  
                    #===========================================================
                else:
                    raise AssertionError('Power is not an int.')
            else:
                raise AssertionError('Coefficient is not an int or float.')
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
        alist = []
        for k,v  in self.terms.items():
            alist.append((v, k))
        return "Poly(" + str(alist).strip('[]') +')'

    
    def __len__(self):
        if self.terms == None:
            return 0
        else:
            max = 0
            for k, v in self.terms.items():
                if k > max:
                    max = k
            return max
    def __call__(self,arg):
        sumtotal = 0
        if type(arg) in [int, float]:
            for k, v in self.terms.items():
                sumtotal += (arg ** k) * v
        return sumtotal
               
    

    def __iter__(self):
        for k, v in sorted(self.terms.items(), key = None, reverse = True):
            yield (v, k)
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError('Power cannot be less than 0')
        if type(index) is int:
            if index in self.terms:
                return self.terms[index]
            else:
                return 0

        else:
            raise TypeError('Power is not an int.')

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError('Power cannot be less than 0.')
        if type(index) is int:
            if value == 0:
                del self.terms[index]
            else:
                self.terms[index] = value
        else:
            raise TypeError('Power is not an int.')
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError('Power cannot be less than 0')
        if type(index) is int:
            for i in self.terms:
                if i == index:
                    del self.terms[index]
        else:
            raise TypeError('Power is not an int.')    

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Coefficient not an int or float.')
        if type(p) != int:
            raise TypeError('Power not an int.')
        if p in self.terms:
            self.terms[p] += c
            
        if p not in self.terms and c != 0:
            self.terms[p] = c
    def __add__(self,right):
        #return Poly._add_term(self, right[0], right[1])
        pass
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) is Poly:
            for k, v in self.terms.items():
                for keys, values, in right.terms.items():
                    return k == keys and v == values
        if type(right) in [int, float]:
            for k, v in self.terms.items():
                return v == right
        else:
            raise TypeError('Right is not a Poly, int, or float.')       

    
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