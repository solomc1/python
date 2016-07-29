class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            if type(p) == int:
                if type(c) == int or type(c) == float:
                    if c == 0:
                        pass
                    elif p >= 0 and p not in self.terms.keys():
                        self.terms[p] = c
                    else:
                        raise AssertionError('Poly.__init__: illegal power in: ' + '('+ str(c) + ',' + str(p) + ')')
                        
                else:
                    if type(c) != int or type(c) != float:
                        raise AssertionError(str(c) + ' is not type int or float')         
            else:
                raise AssertionError(str(p) + ' is not type int')           

        
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
        return'Poly({x})'.format(x = ','.join(str(k) for k in list(self.terms.items())))
    

    
    def __len__(self):
        return max(list(self.terms.keys()))
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            answer =  (arg**k) * v
            total += answer
        return total 
    
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield (k,v)
            next(k,v)
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError(str(index) + ' is not an int or is not greater than 0')
        else:
            if index in self.terms.keys():
                return self.terms[index]
            else:
                return 0 
            

    def __setitem__(self,index,value): #index = power value = coeff
        if type(index) != int or index < 0:
            raise TypeError(str(index) + ' is not an int or is not greater than 0')
        else:
            if value == 0:
                del(self.terms[index])
            else:
                self.terms[index] = value 
                
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError(str(index) + ' is not type int or > 0')
        else:
            if index in self.terms.keys():
                del(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p) == int:
            if p >= 0:
                if p not in self.terms.keys() and c != 0:
                    self.terms[p] = c 
                elif p in self.terms.keys():
                    self.terms[p] = self.terms[p] + c 
                    if self.terms[p] == 0:
                        del(self.terms[p])
                    
                    
            
       

    def __add__(self,right):
        if type(right) == type(self): #or type(right) in (int,float):
            pass
        elif type(right) in (int,float):
            self.terms[0] = self.terms[0] + right
            pass
            

    
    def __radd__(self,left):
        if type(left) == type(self): #or type(right) in (int,float):
            pass
        elif type(left) in (int,float):
            pass
    
    

    def __mul__(self,right):
        if type(right) == type(self): #or type(right) in (int,float):
            pass
        elif type(right) in (int,float):
            self.terms[0] = self.terms[0] + right
            pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        match = True
        if type(right) == type(self):
            for i in range(len(self)):
                if i > len(self.terms.items()) or i > len(right.terms.items()):
                    match = False
                    return match
                elif sorted(self.terms.items())[i] != sorted(right.terms.items())[i]:
                    match = False
                    return match
        elif type(right) in (int,float):
            if len(self.terms.items()) == 1 and self.terms[0] == right:
                return match
        else:
            raise TypeError(str(self) + ' is not type int,float, or poly')

                

    
if __name__ == '__main__':
#     Some simple tests; you can comment them out and/or add your own before
#     the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()