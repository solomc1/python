class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if i[0] != 0:
                self.terms[i[1]] = i[0]
            assert type(i[0]) in [int, float], 'Poly.__init__: Unsupported operand, '+ i[0]+'must be int or float'
            assert type (i[1]) == int or i[1] >= 0, 'Poly.__:nit__; Unsupported operand, '+ i[0]+'mus be int and >= 0'
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
            print([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)])
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        def term(c, p):
            return '('+str(p)+','+str(c)+')'
        f = ','.join([term(k,v) for k ,v in self.terms.items()])
        return 'Poly('+f+')'

    
    def __len__(self):

        if self.terms == None:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        count = 0
        for k, v in self.terms.items():
            count += (arg**k)*v
        return count

    def __iter__(self):
        for k,v in sorted(self.terms.items(), key = lambda x: x[0], reverse = True):
            yield (v, k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: The index '+str(index)+' must be integer or positive')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
                

    def __setitem__(self,index,value):
        if type(value) == int or value < 0:
            raise TypeError('Poly.__getitem__: The index '+str(value)+' must be integer or positive')
        elif value == 0:
            del self.terms[index]
        else:
            if 'terms' in self.__dict__:
                self.terms[index] = value
            self.__dict__[index] = value
            

    def __delitem__(self,index):
        del self.items[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int, float] or type(p) != int or p < 0:
            raise TypeError('Poly.__getitem__: The index '+str(c)+ 'and'+ str(p)+' is an illegal combination')
        elif p in self.terms:
            if int(self[p])+int(c) == 0:
                del self[p]
            else:
                self[p] += int(c)
        else:
            self[p] = c
    def __add__(self,right):
        if right in [Poly, int, float]:
            raise TypeError('Poly.__getitem__: The index '+str(right)+' must be integer or Poly or float')
        elif type(right) == int:
            for i in self:
                if i[0] == 0:
                    i[1] += right
            
        else:
            for k in self:
                for j in right:
                    if k[0] == j[0]:
                        k[1]+j[1]
        return self
                    
    
    def __radd__(self,left):
        self.__radd__(left)
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if not right in [Poly, int, float]:
            raise TypeError('Poly.__getitem__: The index '+str(right)+' must be integer or Poly or float')
        else:
            return self.keys() == right.keys()
    
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