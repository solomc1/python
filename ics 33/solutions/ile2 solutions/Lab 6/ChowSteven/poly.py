class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        #second number in the tuple is the key
        self.terms = {}
        for i in terms:
            if type(i[0]) == str or type(i[1]) not in (int, float):
                raise AssertionError("The coefficient and power must be either a float or an int")
            if i[1] < 0:
                raise AssertionError("The power must be greater than or equal to 0")
            else: 
                if i[1] not in self.terms.keys():
                    if i[0] != 0:
                        self.terms[i[1]] = i[0]
                else:
                    raise AssertionError("You can not repeat a value with the same power of x")
        print ('dictionary created', self.terms)
        
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
        #return ('Poly('+[p,',',c+'),'for p,c in sorted(self.terms.items())])
        #return 'Poly('+ [str(p)+str(c) for p, c in sorted(self.terms.items())]
        #return str(self.terms.items())
        return str(('Poly(',[ '('+str(i)+','+str(j)+')' for i, j in self.terms.items()],')'))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            print(sorted(self.terms.items()))
            sorts = sorted(self.terms.items(), reverse = True)
            return sorts[0][0]

    
    def __call__(self,arg):
        value = 0
        for i, j in self.terms.items():
            value += (j*(arg**i))
        return value
    

    def __iter__(self):
        i = iter(self.terms)
        return i
            

    def __getitem__(self,index):
        if type(index)!= int or index < 0:
            raise TypeError("The index must be an integer and be greater than 0")
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!= int or index < 0:
            raise TypeError("The index must be an integer and be greater than 0")
        else:
            if value != 0:
                self.terms[index] = value
            else:
                if index in self.terms.keys():
                    del(self.terms[index])
            
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("The index must be an integer and be greater than 0")
        else:
            if index in self.terms.keys():
                del(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('The coefficient must be an integer or a float')
        if type(p) != int or p < 0:
            raise TypeError("The power must be an integer and greater than 0")
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del(self.terms[p])
        
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('The operand must be either class Poly or class int or class float')
        else:
            value = Poly()
            if type(right) == (int or float):
                value._add_term(right, 0)
                for i, j in self.terms.items():
                    value._add_term(j, i)
                return value
                print (value)
                
            else:
                for i, j in right.terms.items():
                    self.terms[i] += j
            return self
                

    
    def __radd__(self,left):
        if type(left) != Poly() or type(left) not in (int, float):
            raise TypeError('The operand must be either class Poly or class int or class float')
        else:
            if type(left) in (int, float):
                self.terms[0] += left
            else:
                for i, j in left.items():
                    self.terms[i] += j
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('The operand must be either class Poly or class int or class float')
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError("The compared value must be either an int, float, or Poly")
        if type(right) in (int,float):
            if self.terms[0] == right:
                return True
            else:
                return False
        else:
            for i, j in zip(self.terms, right.terms):
                if i != j:
                    return False
            return True

    
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