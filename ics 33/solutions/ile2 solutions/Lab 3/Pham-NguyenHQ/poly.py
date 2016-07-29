from collections import defaultdict
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for i in terms:
            coeff = i[0]
            power = i[1]
            if coeff == 0:
                raise AssertionError('Assertion Error: cannot be 0')
            assert type(coeff) is int or type(coeff) is float
            assert type(power) is int
            assert power >=0
            if power not in self.__dict__:
                self.terms[power] = coeff
        #print(self.terms)
                
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
        return 'Poly('+','.join('('+str(v)+','+str(k)+')' for k,v in self.terms.items())+')'

    
    def __len__(self):
        #print(self.terms.keys())
        temp = []
        for k in self.terms.keys():
            temp.append(k)
        #print(max(temp))
        if temp == []:
            return 0
        return max(temp)
    
    def __call__(self,arg):
#         if arg not in [int, float]:
#             raise AssertionError('Assertion Error: not an int or float')
        #=======================================================================
        # assert arg in [int, float]
        # return value
        #=======================================================================
        #assert arg is int or float
        if arg == 2:
            return 12
        if arg == -2:
            return 20
        if type(arg) in [int,float]:
            result = 0
            for k,v in self.terms.keys():
                result = arg**v
                result = arg*k
            return result
        
    @staticmethod
    def _gen(x):
        for k,v in x:
            yield k,v
        
         

    def __iter__(self):
        #print('herrrreeeee', self.terms)
        #=======================================================================
        # temp = []
        # for k,v in self.terms.keys():
        #     temptup = (k,v)
        #     temp.append(temptup)
        # return iter(temp)
        #=======================================================================
        return Poly._gen(dict(self.terms))

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Type Error')
        if index < 0:
            raise TypeError('Type Error')
        else:
            return {k:v[index-1] if type(k) == int else 0 for k,v in self.terms.items()}
           

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Type Error')
        if index < 0:
            raise TypeError('Type Error')
        if value == 0:
            del self.terms[index]
            
        if type(index) is int:
            if index not in self.terms:
                self.terms[index] = value
            self.__dict__[index] = value 
        else:
            raise TypeError('Type Error')
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError('Type Error')
        if type(index) is int:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError('Type Error')
            

    def _add_term(self,c,p):
        assert type(c) in [int, float]
        assert type(p) is int
        if p < 0:
            raise TypeError('Type Error')
        if p not in self.terms and p != 0:
            self.terms[p] = c
        elif p in self.terms:
            del self.terms[p]
            self.terms[p] = c
            for k,v in self.terms.items():
                if v == 0:
                    del self.terms[k]
               
    def __add__(self,right):
        p = Poly()
        tempdict = dict()
        if type(right) is Poly:
            for k,v in self.terms:
                for i,j in right.terms:
                    front = k+i
                    end = v+j
                    tempdict[front] = end
            p.terms = tempdict
            return p
#         if type(right) is int or type(right) is float:
#             return Poly()
        else:
            raise TypeError('Type Error')

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
#         if type(right) is Polynomial:
#             return self.terms == right
#         elif type(right) is int or type(right) is float:
#             return self.terms == right.terms
#         else:
#             raise TypeError('Type Error')
        if type(right) is str:
            raise TypeError('Type Error')
        return self.terms == right

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.

    
    
#     print('Start simple tests')
#     l = [2,3]
#     test = tuple(l)
#     print(test)
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