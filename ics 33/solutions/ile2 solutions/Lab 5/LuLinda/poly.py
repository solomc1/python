class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for i in terms:
            assert type(i[0]) in [int , float], 'Poly.__init__: illegal coefficient in: '+str(i)
            assert type(i[1]) == int and i[1] >= 0, 'Poly.__init__: illegal power in: '+str(i) 
            if i[0] == 0:
                continue
            assert i[1] not in self.terms.keys(), 'Poly.__init__: illegal power in: '+str(i)
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
        term_str = ''
        for i in self.terms:
            term_str += str(i)
        return 'Poly('+term_str+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k, v in self.terms.items():
            total += arg**k*v
        return total
    

    def __iter__(self):
        lst= []
        for k in sorted(self.terms.keys(), reverse=True):
            lst.append((self.terms[k], k))
        return iter(lst)

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('argument is not type int or is less than 0')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('power argument is not type int or is less than 0')
        elif value == 0:
            if index not in self.terms.keys():
                pass
            else:
                del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('power argument is not type int or is less than 0')
        if index in self.terms.keys():
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in [int, float] and type(p) != int and p < 0:
            raise TypeError('coefficient is not type int or float, power is not type int, or power is less than 0')
        if p not in self.terms.keys():
            if c == 0:
                pass
            else:
                self.terms[p] = c
        elif p in self.terms.keys():
            if self.terms[p] + c == 0:
                del self.terms[p]
            else:
                self.terms[p] = self.terms[p] + c
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('operand is not polynomial or numeric type')
        p = Poly()
        if type(right) == int or type(right) == float:
            p._add_term(right, 0)
        else:
            for i in right:
                p._add_term(i[0], i[1])
        for i in self:
            p._add_term(i[0], i[1])
        return p

    
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('operand is not polynomial or numeric type')
        p = Poly()
        if type(left) == int or type(left) == float:
            p._add_term(left, 0)
        else:
            for i in left:
                p._add_term(i[0], i[1])
        for i in self:
            p._add_term(i[0], i[1])
        return p
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('operand is not polynomial or numeric type')
        p = Poly()
        if type(right) == int or type(right) == float:
            for i in self:
                p._add_term(i[0]*right, i[1])
        else:
            for i in self:
                for j in right:
                    p._add_term(i[0]*j[0], i[1]+j[1])
        return p
    

    def __rmul__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError('operand is not polynomial or numeric type')
        p = Poly()
        if type(left) == int or type(left) == float:
            for i in self:
                p._add_term(i[0]*left, i[1])
        else:
            for i in self:
                for j in left:
                    p._add_term(i[0]*j[0], i[1]+j[1])
        return p

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('operand is not polynomial or numeric type')
#         if type(right) == Poly:
#             for i in range(len(self.terms)):
#                 if self.terms.items() != right.terms.items():
#                     return False
#             return True
#         else:
#             return self == right
        

    
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