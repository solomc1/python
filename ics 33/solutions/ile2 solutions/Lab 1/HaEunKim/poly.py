class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for i in terms:
            if type(i[0]) not in (int, float):
                raise AssertionError('coefficient must be an int or float')
            if type(i[1]) is not int or i[1] < 0:
                raise AssertionError('power must be a nonnegative int')
#             if i[1] < 0:
#                 raise AssertionError('power must be a nonnegative int')
        
            if type(i[0]) in (int, float) and type(i[1]) is int and i[1] >= 0:
                if i[0] == 0:
                    pass 
                else:
                    if i[1] not in self.terms:
                        
                        self.terms[i[1]] = i[0]
                    else:
                        raise AssertionError('A power cannot appear as a later term')
        
    
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
        l = []
        for k,v in self.terms.items():
            l.append('('+str(v)+','+str(k)+')')
        return 'Poly('+','.join(l)+')'

    
    def __len__(self):
        l = [k for k in self.terms.keys()]
        if l == []:
            max_p = 0
        else:
            max_p = max(l)
        
        return max_p
    
    def __call__(self,arg):
        answer = 0
        for k,v in self.terms.items():
            answer += v*(arg**k)
        return answer
    

    def __iter__(self):
        def _gen(terms):
            for k,v in terms.items():
                yield (v,k)
        
        return _gen(self.terms)
        
    

    def __getitem__(self,index):
        if type(index) != int or int(index) < 0: 
            raise TypeError('argument is not an appropriate type')
        elif type(index) == int or index >= 0:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or int(index) < 0:
            raise TypeError('argument is not an appropriate type')
        elif type(index) == int or index >= 0:
            return self.__dict__[index] == value
        
            

    def __delitem__(self,index):
        
        if type(index) != int or index < 0:
            raise TypeError('argument is not an approrpriate type')
        else:
            if index in self.terms:
                del self.terms[index]
            else:
                pass
                
        
            return self.__dict__[index]
                
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('Inappropriate type')
        elif type(p) != int:
            raise TypeError('Inappropriate type')
        else:
            pass
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Inappropriate type')
        elif type(right) in (int, float):
            return self.terms + right
        elif type(right) is Poly:
            return self.terms + right.terms 
            
    
    def __radd__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Inappropriate type')
        elif type(left) in (int, float):
            return self.terms + left
        elif type(left) is Poly:
            return self.terms + left.terms 
    

    def __mul__(self,right):
        if type(right) not in (int, float):
            raise TypeError('Inappropriate type')
        elif type(right) in (int, float):
            for k,v in self.terms.items():
                v = v*right
            return self.terms 
        elif type(right) == str:
            return self.terms*right.terms

    def __rmul__(self,left):
        if type(left) not in (int, float):
            raise TypeError('Inappropriate type')
        elif type(left) in (int, float):
            for k,v in self.terms.items():
                v = v*left
            return self.terms 
        elif type(left) == str:
            return self.terms*left.terms
    

    def __eq__(self,right):
        if type(right) in (int, float):
            return self.terms == right
        elif type(right) is Poly:
            return self.terms == right.terms
        else:
            raise TypeError('Inappropriate type')

    
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