class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coe, pow in terms:
            assert type(coe) in (int, float), "Poly.__init__: Coeffiecent is {} but must be an int or float.".format(coe)
            assert type(pow) == int and pow >= 0, "Poly.__init__: Power is {} but must be equal or greater then 0".format(pow)
            if coe != 0:
                assert pow not in self.terms, "Poly.__init__: Power is repeated"
                self.terms[pow] = coe
            
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
        answer = []
        for pow,coe in self.terms.items():
            answer.append((coe,pow))
        return 'Poly('+str(answer)[1:-1]+')'

    
    def __len__(self):
        lst = []
        if len(self.terms) == 0:
            return 0
        else:
            for pow in self.terms.keys():
                lst.append(pow)
            return max(lst)
    
    def __call__(self,arg):
        answer = 0
        for pow, coe in self.terms.items():
            answer += ((arg**pow)*coe)
        return answer
    

    def __iter__(self):
        answer = []
        if self == 0:
            return answer
        else:
            for pow, coe in self.terms.items():
                answer.append((coe, pow))
        answer.sort(key = lambda x: x[1], reverse = True)
        for item in answer:
            yield item
        
        

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: Illegal Index")
        else:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: Illegal Index")
        elif value != 0:
            self.terms[index] = value
        
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__: Illegal Index")
        elif index in self.terms:
            self.terms.pop(index)
            
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
                raise TypeError("Poly._add_term: Illegal Entry of Coefficent")
        elif type(p) != int or p < 0:
            raise TypeError("Poly._add_term: Illegal Entry of Power")
        elif c != 0:
            if p not in self.terms:
                self.terms[p] = c
            elif (self.terms[p] + c) == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = self.terms[p] + c


    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError("Poly.__add__: Illegal Entry")
        elif type(right) == Poly:
            for pow, coe in right.terms.items():
                return self._add_term(coe, pow)
        else:
            return self._add_term(right, 0)

     
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError("Poly.__eq__: Illegal Entry")
        elif type(right) ==  Poly:
            if len(self.terms) == len(right.terms):
                for pow, coe in self.terms.items():
                    if pow not in right.terms or self.terms[pow] != right.terms[coe]:
                        return False
                    else:
                        return True
            else:
                return False
        else:
            pass

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#    print('Start simple tests')
#   p = Poly((3,2),(-2,1), (4,0))
#    print('  For Polynomial: 3x^2 - 2x + 4')
#    print('  str(p):',p)
#    print('  repr(p):',repr(p))
#    print('  len(p):',len(p))
#    print('  p(2):',p(2))
#    print('  list collecting iterator results:',[t for t in p])
#    print('  p+p:',p+p)
#   print('  p+2:',p+2)
#   print('  p*p:',p*p)
#    print('  p*2:',p*2)
#   print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()