class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.numbers = terms
        self.terms = {}
        for i in terms:
            if i[1] < 0 or type(i[0]) not in (int,float) or type(i[1]) is not int:
                raise AssertionError
            elif i[1] in self.terms.keys():
                raise AssertionError
            elif i[0] == 0:
                pass
            else:
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
        return 'Poly{}'.format(self.numbers)

    
    def __len__(self):
        poss_max = []
        for i in self.terms.keys():
            poss_max.append(i)
        return max(poss_max)
    
    def __call__(self,arg):
        eq = self.__str__()
        eq = eq.replace('x','*'+str(arg))
        eq = eq.replace('^','**')
        return eval(eq)
        
            
    

    def __iter__(self):
        for i,j in sorted(self.terms.items(),reverse = True):
            yield '({},{})'.format(j,i)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError()
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index][0]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError
        elif value == 0:
            self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError
        else:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int,float) or p < 0:
            raise TypeError
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.term.keys():
            self.terms[p] = c
        elif c == 0:
            self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError
        else:
            pass

    
    def __radd__(self,left):
        if type(left) not in (Poly,int,float):
            raise TypeError
        else:
            pass
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError
        else:
            pass
    

    def __rmul__(self,left):
        if type(left) not in (Poly,int,float):
            raise TypeError
        else:
            pass
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError
        else:
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