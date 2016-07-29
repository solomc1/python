class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for x in terms:
            if type(x[0]) not in (int,float) or type(x[1]) != int:
                raise AssertionError()
            elif x[1] < 0:
                raise AssertionError()
            elif x[0] == 0:
                pass
            elif x[1] not in self.terms.keys():
                self.terms[x[1]] = x[0]
            else:
                raise AssertionError()
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
        return "Poly(" + ','.join('('+str(v)+','+str(k)+')' for k,v in self.terms.items()) + ')'

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total = total + (arg**k)*v
        return total
    

    def __iter__(self):
        temp = sorted(self.terms.items(), reverse = True)
        for sub in temp:
            yield (sub[1],sub[0])
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('class poly. arg not int or < 0')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('class poly.')
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(self.terms[index])
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError()
        else:
            if index not in self.terms.keys():
                pass
            else:
                self.terms.remove(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError
        elif type(p) != int or p<0:
            raise TypeError
        else:
            if p not in self.terms.keys() and c !=0:
                self.terms[p] = c
            elif p in self.terms.keys():
                if (self.terms[p] + c) == 0:
                    self.terms.pop(self.terms[p])
                else:
                    self.terms[p] = self.terms[p] + c
       

    def __add__(self,right):
        temp = []
        if type(right) is Poly:
            for k, v in self.terms.items():
                for x, y in right.terms.items():
                    if k == x:
                        temp.append((v+y, k))
        return temp
        
        

    
    def __radd__(self,left):
        temp = []
        if type(left) is Poly:
            for k, v in self.terms.items():
                for x, y in left.terms.items():
                    if k == x:
                        temp.append((v+y, k))
        return temp
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
       if type(right) is Poly:
           pass
       elif type(right) in (int,float):
           if self.terms.keys() == right:
               return True
       else:
           raise TypeError()

    
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