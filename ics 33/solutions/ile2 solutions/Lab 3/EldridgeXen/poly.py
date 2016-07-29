class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for k in terms:
            if type(k[0]) not in (int, float):
                raise AssertionError('coefficiient must be of type int or float')
            if type(k[1]) != int or k[1] < 0:
                raise AssertionError('power must be a positive integer')
            if k[1] in self.terms.keys() and k[1] != 0:
                raise AssertionError('redundant power')
            else:
                if k[0] == 0:
#                     self.terms.update({k[1]:None})
                    pass
                else:
                    self.terms.update({k[1]:k[0]})
                    
        self.sortedterms  = []
        for p,c in self.terms.items():
            self.sortedterms.append((c, p))
        self.sortedterms.sort(key= lambda x: x[1], reverse = True)
        self.sortedterms = iter(self.sortedterms)
            
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
        returnstr = ''
        for p,c in self.terms.items():
            returnstr += '({},{}),'.format(c,p)
        returnstr = returnstr[:-1]
        return 'Poly({})'.format(returnstr)

    
    def __len__(self):
        if len(self.terms.items()) == 0:
            return 0
        else:
            return max(list(self.terms.keys()))
    
    def __call__(self,arg):
        answer = 0
        for p, c in self.terms.items():
            
            answer += c*arg**p
        return answer
    

    def __iter__(self):
#         sortedterms  = []
#         for p,c in self.terms.items():
# #             if p == 0:
# #                 sortedterms.append((c,0))
# #             else:
#             sortedterms.append((c, p))
#         print('sort =', sortedterms)
#         sortedterms.sort(key= lambda x: x[1], reverse = True)
#         print('sortedafter = ', sortedterms)
#         x = [i for i in (iter(sortedterms))]
#         print(x)
        yield next(self.sortedterms)
            
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError('index cannot be less than 0')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('power must be a positive integer')
        if value == 0 :
            try:
                removed = self.terms.pop(index)
            except:
                pass
        else:
            self.terms.update({index:value})
            
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be positive integer')
        if index in self.terms.keys():
            removed = self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('must be int or float')
        if type(p) != int or p < 0:
            raise TypeError('must be positive int')
        if p not in self.terms.keys() and c != 0:
            self.terms.update({p:c})
        if p in self.terms.keys():
            if self.terms[p] + c == 0:
                removed = self.terms.pop(c)
            else:          
                self.terms.update({p:c})
       

    def __add__(self,right):
        if type(right) not in (Poly,int, float):
            raise TypeError('issues')
        for p,c in right.terms.items():
            self._add_term(self,c,p)

    
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