class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if term[1] in self.terms.keys():
                raise AssertionError('power is already in dictionary')
            if type(term[0]) not in [int, float] or type(term[1]) != int or term[1] < 0:
                raise AssertionError('polynomials can only contain numerical types')
            if term[1] not in self.terms.keys() or term[0] != self.terms[term[1]]:
                if term[0] != 0:
                    self.terms[term[1]] = term[0]

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
        temp = ''
        for k,v in self.terms.items():
            temp += '({},{}),'.format(v, k)
        newtemp = temp.strip(',')
        return 'Poly('+ newtemp + ')'
    
    def __len__(self):
        temp = []
        for k in self.terms:
            temp.append(k)
        if len(temp) == 0:
            return 0
        else:
            return max(temp)
            
    
    def __call__(self,arg):
        s = str(self)
        newS = s.replace('x', '*(' + str(arg) + ')')
        print(newS)
        return(eval(newS))
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), key = lambda x: (x[0]), reverse = True):
            yield (v, k)
            
            
        
    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be a greater than 0')
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be a greater than 0')
        if value != 0:
            self.terms[index] = value
            if self.terms[index] == 0:
                del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('index must be an int')
        if index < 0:
            raise TypeError('index must be a greater than 0')
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError('index must be an int')
        if p < 0:
            raise TypeError('index must be a greater than 0')
        if p != 0:
#             if p not in self.terms:
#                 if self.terms[p] != c:
                if p in self.terms.keys():
                    self.terms[p] = p + self.terms[p]
                else:
                    self.terms[p] = c
       

    def __add__(self,right):
#         temp = {}
#         for k, v in self.terms.items():
#             for key, val in right.terms.items():
#                 if k == key:
#                     temp[k] = (v + val)
#                 else:
#                     temp[key] = val
#         return str(temp)
        pass
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass
        if type(right) != int:
            raise TypeError('comparison must be an int')      

    
if __name__ == '__main__':
#     # Some simple tests; you can comment them out and/or add your own before
#     # the driver is called.
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
    driver.batch_self_check(file_name='bsc.txt',\
                     seperator='-->',\
                     show_comment=True,\
                     show_all= True,\
                     show_traceback=True,\
                     show_exception=True,\
                     show_exception_message=True,
                     TA_info=None)