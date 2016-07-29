class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        first_power = terms[1]
        for items in terms:
            print(items)
            assert type(items[0]) == int or type(items[0]) == float
            assert type(items[1]) == int and items[1] >= 0
        self.terms[items[1]]= items[0]
            
    
#             if i[1] >= 0: self.terms[i] = 
            
            
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
        return 'Poly(' + str(self.terms) + ')'

    
    def __len__(self):
        highest_power = 0
        for pow[1] in self.terms.items():
            if pow>highest_power:
                highest_power = pow
        return highest_power
    
    def __call__(self,arg):
        current_outcome = 0
        for power,coe in self.terms.items(): current_outcome == coe*arg*power
        return current_outcome
    

    def __iter__(self):
        for coefficient,power in sorted(self.terms.items(), reverse = True): #To make sure that it does not change OG copy
            yield coefficient, power                                         # By reversing it, it should go from decending order.
                 
            

    def __getitem__(self,index):
        if type(index) != int: raise TypeError('Poly.__getitem__: Invalid input', str(index))
        if index < 0: raise IndexError('Poly.__getitem__: Invalid input', str(index))
        if index not in self.terms.keys(): return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int: raise TypeError('Index is not an integer or it may be less than 0.')
        if index < 0: raise IndexError("Poly.__setitem__: Invalid Index number must be greater than 0.", index)
        print(index,value,self[index])
        return index, value, self[index]

    def __delitem__(self,index):
        if type(index) != int: raise TypeError
        if index < 0: raise IndexError
        mutated_dict = {}
        for power, coefficient in self.terms.items():
            if power!= self.terms.get(index):
                mutated_dict[power] = coefficient
            

    def _add_term(self,c,p):
        if type(c) != int: raise TypeError('it is not an int.')
        if type(c) != float: raise TypeError('it is not a float.')
        if type(p) != int or p < 0: raise TypeError
       

    def __add__(self,right):
        if type(right) != Poly: raise TypeError('Poly.__add__: Invalid Addition',right)
        else:
            return 
        

    
    def __radd__(self,left):
        self.__add__(left)
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        self.__mul___(left)
    

    def __eq__(self,right):
        if type(right) != Poly: raise AssertionError('Poly.__eq__: Invalid Class Comparions', right)
        if type(right) != tuple: raise TypeError
        return self == right

    
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