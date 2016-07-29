class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if type(item[0]) not in [float,int]:
                raise AssertionError
            if type(item[1]) != int or item[1] < 0:
                raise AssertionError
            if item[1] in self.terms.keys():
                raise AssertionError
            self.terms[item[1]] = item[0]
            if item[0] == 0:
                del self.terms[item[1]]
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
        string = ''
        for k,v in self.terms():
            string += '('+k+v+')'
        return 'Poly('+string+')'
    
    def __len__(self):
        value = 0
        print(self.terms())
        for k in self.terms.keys():
            print(k)
            if k < value:
                value = k
        return value
    
    def __call__(self,arg):
        value = 0

        for k in self.terms.keys():
            for v in self.terms.values():
                value += v*(arg**k)
        return value
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        self.terms[index] = value
        if value == 0:
            del self.terms[index]

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        if index not in self.terms.keys():
            pass
        else:
            del self.terms[index]
            
    def _add_term(self,c,p):
        if type(c) not in [float,int] or type(p) != int or p < 0:
            raise TypeError
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        pass
        
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            for k in self.terms.keys():
                for rk in right.terms.keys():
                    if k == rk:
                        return self.terms[k] == right.terms[rk]
        if type(right) not in [int,float,Poly]:
            raise TypeError
        else:
            for i in self.terms.values():
                return right == i
    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.

#      print('Start simple tests')
#      p = Poly((3,2),(-2,1), (4,0))
#      print('  For Polynomial: 3x^2 - 2x + 4')
#      print('  str(p):',p)
#      print('  repr(p):',repr(p))
#      print('  len(p):',len(p))
#      print('  p(2):',p(2))
#      print('  list collecting iterator results:',[t for t in p])
#      print('  p+p:',p+p)
#      print('  p+2:',p+2)
#      print('  p*p:',p*p)
#      print('  p*2:',p*2)
#      print('End simple tests\n')


    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()