class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}

        for i in terms:
            assert type(i[0]) in (int, float), "Only int and float accepted for coefficients"
            assert type(i[1]) is int, "Invalid power"
            assert i[1] >= 0, "Power must be >= 0"
            
            if i[1] in self.terms.keys():
                assert i[0] == self.terms[i[1]], "Cannot input the same power multiple times"
            
            if i[0] != 0:
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
        contents = []
        
        for pow,coef in self.terms.items():
            contents.append('({c},{p})'.format(c = str(coef), p = str(pow)))
        
        return 'Poly(' + ','.join(contents) + ')'

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        else:
            return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        result = 0
        
        for pow,coef in self.terms.items():
            result += coef * (arg ** pow)
        
        return result
    

    def __iter__(self):
        for pow,coef in sorted(self.terms.items(), reverse = True):
            yield (coef, pow)
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Invalid power, only positive ints allowed')
        if index < 0:
            raise TypeError('Invalid power, only positive ints allowed')
        
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Invalid power, only positive ints allowed')
        if index < 0:
            raise TypeError('Invalid power, only positive ints allowed')
        
        if type(value) not in (int, float):
            raise TypeError('Invalid coefficient, only positive ints allowed')
        
        if value == 0:
            if index in self.__dict__['terms'].keys():
                self.__dict__['terms'].pop(index)
        else:
            self.__dict__['terms'][index] = value
        

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Invalid power, only positive ints allowed')
        if index < 0:
            raise TypeError('Invalid power, only positive ints allowed')
        
        if index in self.__dict__['terms'].keys():
            self.__dict__['terms'].pop(index)
            

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError('Invalid power, only positive ints allowed')
        if p < 0:
            raise TypeError('Invalid power, only positive ints allowed')
        
        if type(c) not in (int, float):
            raise TypeError('Invalid coefficient, only positive ints allowed')
        
        if p not in self.terms.keys():
            self.terms[p] = c
        else:
            self.terms[p] += c
            
        if self.terms[p] == 0:
            self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid addition, only int, float, and Poly allowed')
        
        if type(right) in (int, float):
            right = Poly((right, 0))
        
        result = Poly()
        
        for p,c in self.terms.items():
            result[p] = c
        
        for p,c in right.terms.items():
            result._add_term(c,p)
            
        return result

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid multiplication, only int, float, and Poly allowed')
        
        if type(right) in (int, float):
            right = Poly((right, 0))
            
        result = Poly()
        
        for sp,sc in self.terms.items():
            for rp,rc in right.terms.items():
                result._add_term(sc * rc, sp + rp)
                
        return result
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Invalid comparison, only int, float, and Poly allowed')
        
        if type(right) in (int, float):
            right = Poly((right, 0))
            
        return self.terms == right.terms
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
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