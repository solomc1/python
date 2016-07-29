class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            if type(x[1]) == int and x[1] >= 0:
                if x[0] != 0:
                    if type(x[0]) in (int,float):
                        if x[1] not in self.terms.keys():
                            self.terms[x[1]] = x[0]
                        else:
                            raise AssertionError('Poly.__init__: illegal repeated power in: ({},{})'.format(
                                    x[0], x[1]))
                    else:
                        raise AssertionError('Poly.__init__: illegal coefficient in: ({},{})'.format(
                                    x[0], x[1]))
                else:
                    pass
            else:
                raise AssertionError('Poly.__init__: illegal power in: ({},{})'.format(
                                    x[0], x[1]))
                

                    
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
        itemstring = ''
        
        l_dict = list(self.terms.items())
        for t in l_dict:
            if t == l_dict[-1]:
                itemstring += str((t[1],t[0]))
            else:    
                itemstring += str((t[1],t[0])) + ','

        return 'Poly({})'.format(itemstring)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for t in self.terms.items():
            result += ((arg**t[0])*t[1])
        return result
    
    def __iter__(self):
        l_terms = list(self.terms)
        for t in sorted(l_terms, reverse = True):
            yield (self.terms[t], t)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('TypeError: Poly.__getitem__: illegal power {}'.format(index))
        
        if index not in self.terms.keys():
            return 0
        
        return self.terms[index]
            
            
    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('TypeError: Poly.__setitem__: illegal power {}'.format(index))
        
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
            return self

        self.terms[index] = value
            
        return self
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitem__: illegal power {}'.format(index))
        
        if index in self.terms.keys():
            self.terms.pop(index)
        return self
        

    def _add_term(self,c,p):        
#         if type(c) not in (int,float):
#             raise TypeError('Poly._add_term: illegal coefficient {}'.format(c))
# 
#         if type(p) != int or p < 0:
#             raise TypeError('Poly._add_term: illegal power {}'.format(c))
#         
#         if p not in self.terms.keys():
#             if c != 0:
#                 self.terms[p] = c
#         else:
#             if sum(self.terms[p],c) == 0:
#                 self.terms.pop(p)
#             else:
#                 self.terms[p] = self.terms[p]+c
#         return self
        pass
        
        
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('illegal addition type: {}'.format(right))

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__eq__: illegal comparison {}'.format(right))
        
        if type(right) == Poly:
            for item in self.terms.keys():
                if self.terms[item] == right.terms[item]:
                    return True
                else:
                    return False
        
        if type(right) in (int, float):
            for item in self.terms.keys():
                if self.terms[item] == right:
                    return True
                else:
                    return False
    
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