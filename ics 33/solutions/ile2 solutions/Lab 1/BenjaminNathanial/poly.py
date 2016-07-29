class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        _temp = []
        for i in terms:
            if type(i[0]) not in [int, float]:
                raise AssertionError("All coefficients must be of type int or float")
            if i[1] <0 or type(i[1]) not in [int]:
                print(i[0])
                raise AssertionError("Powers must be equal to or greater than Zero, and of type int")
            if i[1] in _temp and i[1] !=0:
                raise AssertionError("Powers cannot appear multiple times")
            _temp.append(i[1])
        self.terms = {i[1]:i[0] for i in terms}
        print(self.terms)
        
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
        _temp = [(self.terms[i],i) for i in self.terms.keys()]
        #print("Poly{}".format(tuple(_temp)))
        return "Poly{}".format(tuple(_temp))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return(max(self.terms.keys()))
        
    
    def __call__(self,arg):
        if type(arg) not in [int, float]:
            raise AssertionError("Argument nust be of type int or float")
        result =0
        for i in sorted(self.terms.keys()):
            if i ==0:
                result += self.terms[i]
                print(self.terms[i])
            else:
                result += self.terms[i]*(arg**i)
                print(self.terms[i]*(arg**i))
        return result
    

    def __iter__(self):
        for i in sorted(self.terms.items(),reverse=True):
            yield i
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('index must be int and >=0')
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError('index must be int and >=0')
        if value == 0:
            self.terms.__delitem__(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('index must be int and >=0')
        if index in self.terms.keys():
            self.terms.__delitem__(index)
            

    def _add_term(self,c,p):
        if type(c) not in  [int,float] or type(p) != int or p < 0:
            raise TypeError("coefficient must be an int or float, and power must be int and greater than 0")
        if p not in self.terms.keys() or p != 0:
            self.__setitem__(p,c)
        if p in self.terms.keys():
            if self.terms[p] + c == 0:
                self.__delitem__(p)
            else:
                self.terms[p] += c
       

    def __add__(self,right):
        pass

    
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
    p1 = Poly()
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