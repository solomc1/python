class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) is int or float
            assert type(term[1]) is int
            assert term[1] >= 0
            assert term[1] not in self.terms.keys()
            if term[0] == 0:
                pass
            else:
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
        reprList = []
        for k,v in self.terms.items():
            reprList.append('('+str(k)+','+str(v)+')')
        return 'Poly('+','.join(item for item in reprList)+')'
    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        value = 0
        for c,p in sorted(self.terms.items(),reverse=True):
            value += (p*arg**c)
        return value
    

    def __iter__(self):
        for item in sorted(self.terms.items(),reverse=True):
            yield (item[1],item[0])
            
    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Index value ('+str(index)+') is not valid type: type '+str(type(index)+'. Must be int > 0.'))
        else:
            if index in self.terms.keys():
                return self.terms[index]
            else:
                return 0

    def __setitem__(self,index,value):
        if type(index) is not int or index <= 0:
            raise TypeError('Index value ('+str(index)+') is not valid type: type '+str(type(index)+'. Must be int > 0.'))
        elif index not in self.terms.keys():
            self.terms[index] = value
        elif index in self.terms.keys() and self.terms[index] != 0:
            self.terms[index] = value
        elif index in self.terms.keys() and self.terms[index] == 0:
            del self.terms[index]
                        
    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Index value ('+str(index)+') is not valid type: type '+str(type(index)+'. Must be int > 0.'))
        else:
            if index in self.terms.keys():
                del self.terms[index]
            else:
                pass

    def _add_term(self,c,p):
        if type(c) is not int or float and type(p) is not int and p < 0:
            raise TypeError
        else:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p] += c
                if self.terms[p] == 0:
                    del self.terms[p]
            else:
                pass

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError('Value must be of type: int, float, or Poly. Value type was: '+str(type(right)))
        else:
            if type(right) is Poly:
                for p in right.terms.keys():
                    return Poly(self._add_term(right.terms[p], p))
            else:
                return Poly(self._add_term(right,0))
    
    def __radd__(self,left):
        if type(left) not in (int,float,Poly):
            raise TypeError('Value must be of type: int, float, or Poly. Value type was: '+str(type(left)))
        else:
            if type(left) is Poly:
                for p in left.terms.keys():
                    return Poly(self._add_term(left.terms[p], p))
            else:
                return Poly(self._add_term(left,0))

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError
        else:
            if type(right) is Poly:
                for k in self.terms.keys():
                    for p in right.terms.keys():
                        if self.terms[k] != right.terms[p]:
                            return False
                return True
            else:
                return self.terms[0] == right

    
if __name__ == '__main__':
    #===========================================================================
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    # print('Start simple tests')
    # p = Poly((3,2),(-2,1), (4,0))
    # print('  For Polynomial: 3x^2 - 2x + 4')
    # print('  str(p):',p)
    # print('  repr(p):',repr(p))
    # print('  len(p):',len(p))
    # print('  p(2):',p(2))
    # print('  list collecting iterator results:',[t for t in p])
    # print('  p+p:',p+p)
    # print('  p+2:',p+2)
    # print('  p*p:',p*p)
    # print('  p*2:',p*2)
    # print('End simple tests\n')
    # 
    #===========================================================================
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()