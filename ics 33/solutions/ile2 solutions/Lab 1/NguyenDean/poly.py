class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.list = list()
        self.terms = {}
        
        for i in terms:
            for element in i:
                if type(element) == int() or type(element) == float():
                    raise AssertionError('Terms are not integer or float')
        for i in range(len(terms)):
            self.list.append(terms[i])
            self.terms[terms[i][1]] = terms[i][0]
        
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
        return 'Poly{}'.format(tuple(self.list))

    
    def __len__(self):
        if self.list == []:
            return 0
        else:
            self.list.sort()
            return abs(self.list[0][1])
    
    def __call__(self,arg):
        count = 0
        for i in self.list:
            count += (i[0]*arg)**i[1]
        return count
    

    def __iter__(self):
        return iter(self.list)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Argument is not an integer or is less than 0')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Argument is not an integer or is less than 0')
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Argument is not an integer or is less than 0')
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
#        if type(right) == Poly:
#             return Poly(self.terms + right.terms)
#        else:
#            pass
        pass
    

    
    def __radd__(self,left):
#        if type(left) == Poly:
#             return Poly(self.terms + left.terms)
#        else:
#            pass
        pass
    

    def __mul__(self,right):
#        if type(right) == Poly:
#             return Poly(self.terms * right.terms)
#        else:
#            pass
        pass
    

    def __rmul__(self,left):
#        if type(right) == Poly:
#             return Poly(self.terms * left.terms)
#        else:
#            pass
        pass

    def __eq__(self,right):
#         return Poly(self.terms) == Poly(right.terms)
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