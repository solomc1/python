class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i in terms:
            if type(i[1]) is not int:
                raise AssertionError()
            if i[1] < 0:
                raise AssertionError()
            if type(i[0]) not in [int, float]:
                raise AssertionError()
            if i[1] in self.terms.keys() and i[0] != 0:
                raise AssertionError()
            if i[0] != 0:
                self.terms[i[1]] = i[0]

            
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
        if self == 'Poly()':
            return 'Poly()'
        else:
            string = 'Poly('
            for k,v in self.terms.items():
                string += ('(' + str(v) + ',' + str(k) + '),')
            return string + ')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        answer = 0
        for k,v in self.terms.items():
            answer += v * (arg**k)
        return answer
    

    def __iter__(self):
        lst = []
        for k,v in self.terms:
            lst.append((v,k))
        yield lst.sorted(key = lambda x : x[1])
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError()
        if index < 0 :
            raise TypeError()
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError()
        if index < 0:
            raise TypeError()
        self.terms[index] = value
        if value == 0:
            del self.terms[index]

            
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError()
        if index < 0:
            raise TypeError()
        if index not in self.terms.keys():
            pass
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError()
        if p < 0:
            raise TypeError()
        if type(c) not in [int, float]:
            raise TypeError()
        if p not in self.terms.keys():
            self.terms[p] = c
            if c == 0:
                del self.terms[p]
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        pass
#         if type(right) is Poly:
#             for k,v in right.terms:
#                 if k in self.terms.keys():
#                     self.terms[k] += v
#                     if self.terms[k] == 0:
#                         del self.terms[k]
#                 else

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) is Poly:
            return self.terms is right.terms
        elif type(right) in [int, float]:
            return self.__call__(0) == right

    
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