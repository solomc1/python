class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for x in terms:
            if type(x[0]) in (int, float):
                if type(x[1]) is int:
                    if x[1] >= 0 and x[1] not in self.terms.keys():
                        self.terms[x[1]] = x[0]
                    else:
                        raise AssertionError("Poly.__init__:illegal power in" + str(x))
                else:
                    raise AssertionError("Poly.__init__:illegal power in " + str(x))
            else:
                raise AssertionError("Poly.__init__:illegal type in " + str(x))
            
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
        if self.terms != {}:
            return "Poly((" + ",(".join(str(y) + ',' + str(x) + ')' for x,y in self.terms.items()) + ')'
        else:
            return "Poly()"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(x for x in self.terms.keys())
    
    def __call__(self,arg):
        
        sum = 0
        for x, y in self.terms.items():
            sum += (y * (arg ** x))
        
        return sum
            
    def __iter__(self):
        for x,y in sorted(self.terms.items(), reverse = True):
            yield (y,x)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError("Poly.__getitem__:illegal index " + str(index))
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError("Poly.__setitem__:illegal index " + str(index))
        else:
            self.terms[index] = value 
        
        if self.terms[index] == 0:
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError("Poly.__delitem__:illegal index " + str(index))
        elif index in self.terms.keys():
            del self.terms[index]
        else:
            pass
            

    def _add_term(self,c,p):
        if type(p) is not int or p < 0:
            raise TypeError("Poly._add_term:illegal index " + str(p))
        
        if type(c) not in (float, int):
            raise TypeError("Poly._add_term:illegal index " + str(c))
        
        if p not in self.terms.keys():
            self.__setitem__(p, c)
        else:
            self.terms[p] += c
            
            if self.terms[p] == 0:
                self.__delitem__(p)


    def __add__(self,right):
        temp = Poly()
        left = iter(self.terms)
        right = iter(right)
        
        while True:
            try:
                if left[1] == right[1]:
                    temp[left[1]] = left[0] + right[0]
                else:
                    temp[left[1]] = left[0]
                    temp[right[1]] = right[0]
                
                left.next
                right.next
                
            except StopIteration:
                pass
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        flag = False
        
        #while True:
        

    
if __name__ == '__main__':
    
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-1,1), (4,0))
    x = Poly()
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  len(x):',len(x))
    print('  p(2):',p(2))
    print('  list collecting iterator results:',[t for t in p])
    print('  get item:',p.__getitem__(5))
    #print('  p+p:',p+p)
    #print('  p+2:',p+2)
    #print('  p*p:',p*p)
    #print('  p*2:',p*2)
    #print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
