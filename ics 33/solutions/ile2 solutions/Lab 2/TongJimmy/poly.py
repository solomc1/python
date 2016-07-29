class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.lst_terms = [x for x in terms]
        for co, power in self.lst_terms:
            self.terms[co] = power
            if type(power) != int:
                raise AssertionError('power must be an int')
            if type(co) == str or type(power) == str:
                raise AssertionError('coeffcient not an int or float')
            elif power < 0:
                raise AssertionError('power must be greater than 0')        
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
            return ' + '.join([term(p,c,'x') for p,c in sorted(self.terms.items(),reverse=True, key = lambda x :x[1])]).replace('+ -','- ')
    
    def __repr__(self):
        returnthis = 'Poly('
        for tuples in self.lst_terms:
            returnthis += str(tuples) + ','
        return returnthis.rstrip(',') + ')'

    def __len__(self):
        values = []
        for co, power in self.lst_terms:
            values.append(power)
        return max(values)
    
    def __call__(self,arg):
        value = 0
        for co, power in self.lst_terms:
            value += (int(arg)**int(power))* int(co)
        return value

    def __iter__(self):
        iterable = iter(self.lst_terms)
        for i in range (len(self.lst_terms)):
            nxt = next(iterable)
            yield(nxt)
            
    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError(index, "is not an int or is less than 0")
        for tuples in self.lst_terms:
            if tuples[1] == index:
                x = tuples[0]
        return x
            
    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError(index, "is not an int or is less than 0")
        newitem = (value,index)
        self.lst_terms.append(newitem)
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError(index, "is not an int or is less than 0")        
        for tuples in self.lst_terms:
            if tuples[1] == index:
                self.lst_terms.remove((tuples[0],tuples[1]))

    def _add_term(self,c,p):
        if type(c) == str:
            raise TypeError(c, "is not an int or float") 
        elif type(p) != int or p <0:
            raise TypeError(p, "is not an int or is less than 0")
       

    def __add__(self,right):
        pass

    
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
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()