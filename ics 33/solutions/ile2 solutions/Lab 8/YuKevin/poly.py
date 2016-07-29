class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for each in terms:
            assert(type(each[0]) in (int,float))
            assert(type(each[1]) == int and each[1] >= 0)
            assert(each[1] not in self.terms)
            if each[0] != 0:
                self.terms.update({each[1]: each[0]})
            
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
        string = 'Poly('
        for each in self.terms:
            if each != len(self.terms)-1:
                string += '('+str(self.terms[each])+','+str(each)+')'+','
            else:
                string += '('+str(self.terms[each])+','+str(each)+')'
        return string + ')'

    
    def __len__(self):
        max = 0
        for each in self.terms:
            if each > max:
                max = each
        return max
    
    def __call__(self,arg):
        sum = 0
        for each in self.terms:
            sum += self.terms[each] * (arg**each)
        return sum
    

    def __iter__(self):
        iter = sorted(self.terms.items(), reverse = True)
        for each in iter:
            yield (each[1],each[0])
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('unsupported operand type(s) for: < 0 and not int')
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('unsupported operand type(s) for: < 0 and not int')
        if value == 0:
            if index in self.terms:
                #self.terms.__delitem__(index)
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('unsupported operand type(s) for: < 0 and not int')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (float,int) or type(p) != int or p < 0:
            raise TypeError('unsupported operand type(s) for: < 0 and not int')
        if p not in self.terms:
            if c != 0:
                self.terms[p] = c
        else:
            if self.terms[p] + c != 0:
                self.terms[p] = self.terms[p] + c
            else:
                del self.terms[p]
       

    def __add__(self,right):
#         if type(right) not in (Poly, int, float):
#             raise TypeError('unsupported operand type(s) for: < 0 and not int')
#         Test = Poly()
#         for each in self.terms:
#             Test._add_term( self.terms[each],each)
#         if type(right) in (int, float):
#             if 0 in Test.terms:
#                 Test[0] = self.terms[0] + right
#         else:
#             for each in Test.terms:
#                 Test[each] = self.terms[each] + Poly(right).terms[each]
#         return Test

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
#         if type(right) not in (Poly, int, float):
#             raise TypeError('unsupported operand type(s) for: < 0 and not int')
#         if type(right) in (float,int):
#             if self.terms.keys() == [0]:

    
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