class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[1]) != int:
                raise AssertionError
            assert type(i[0]) in [int,float], 'coefficient must be of type int or float'
            assert i[1] >= 0 , 'power must be type int and greater than 0'
            assert i[1] not in self.terms.keys(), 'This power has already been used'
            if i[0] != 0:
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
        return "Poly({})".format(','.join(['('+str(v)+','+str(k)+')' for k,v in self.terms.items()]))
    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            keys = []
            for k in self.terms.keys():
                keys.append(k)
            return keys[-1]
            
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            if k == 0:
                total += v
            else:
                total += v*(arg**k)
        return total

    def __iter__(self):
        tup = []
        for k,v in self.terms.items():
            tup.append((k,v))
        for i in sorted(tup, reverse = True):
            yield (i[1],i[0])
            
    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError(type(index)+'Index is cannot be less than 0 or index is not in Poly')
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError(str(index)+'Index is cannot be less than 0')
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]
            else:
                pass
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if index < 0:
            raise TypeError(str(index)+'Index is cannot be less than 0')
        else:
            if index in self.terms.keys():
                del self.terms[index]


    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError
        if type(c) not in [int,float]:
            raise TypeError 
        if p < 0:
            raise TypeError
        else: 
            if p not in self.terms.keys() and c !=0:
                self.terms[p]=c
            elif p in self.terms.keys():
                if self.terms[p] +c == 0:
                    self.__delitem__(p)
                else:
                    self.terms[p] = self.terms[p]+c
            
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError
        if type(right) == int or type(right) == float:
            if 0 in self.terms.keys():
                self.terms[0] = self.terms[0] + right
            else:
                self.terms[0] = right
            return self.__str__()
        elif type(right) == Poly:

            for k,v in right.terms.items():
                self._add_term(v,k)
            return self.__str__()
         
            

    
    def __radd__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError
        if type(left) == int or type(left) == float:

            if 0 in self.terms.keys():
                self.terms[0] = self.terms[0] + left
            else:
                self.terms[0] = left
            return self.__str__()
    

    def __mul__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError
        if type(right) == int or type(right) == float:
            for k,v in self.terms.items():
                self.terms[k] = v*right
            return self.__str__()
        elif type(right) == Poly:
            pass

    def __rmul__(self,left):
        if type(left) not in [Poly, int, float]:
            raise TypeError
        if type(left) == int or type(left) == float:
            for k,v in self.terms.items():
                self.terms[k] = v*left
            return self.__str__()
    

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