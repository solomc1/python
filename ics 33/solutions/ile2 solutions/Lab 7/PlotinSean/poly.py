#Sean Plotin Lab 7
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[0]) not in (int, float):
                raise AssertionError('Poly.__init__:coefficient not an int or float')
            elif type(i[1]) != int or i[1] < 0:
                raise AssertionError('Poly.__init__:power not int that is greater than 0')
            elif i[1] in self.terms and self.terms[i[1]] != 0:
                raise AssertionError('Poly.__init__:power already has a value') 
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
        return('Poly' + str(((v,k) for k,v in self.terms.items())))

    
    def __len__(self):
        high = 0
        if self.terms == {}:
            return 0
        else:
            for k,v in self.terms.items():
                if int(k) > high:
                    high = int(k)
        return high
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += (v*arg**k)
        return result
    

    def __iter__(self):
        for k,v in self.terms.items():
            yield (v,k)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__:index is not an int greater than 0')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__:index is not an int greater than 0')
        elif value == 0:
            del(self.terms[index])
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__:index is not an int greater than 0')
        elif index not in self.terms:
            pass
        else:
            del(self.terms[index])
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise AssertionError('Poly.__init__:coefficient not an int or float')
        elif type(p) != int or p < 0:
            raise AssertionError('Poly.__init__:power not int that is greater than 0')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                if self.terms[p] + c == 0:
                    del(self.terms[p])
                else:
                    self.terms[p] += c

    def __add__(self,right):
        result = Poly()
        result.terms = self.terms
        if type(right) not in (Poly,int,float):
            raise TypeError('Poly.__add__:argument is not a Polynomial or int or float')
        if type(right) in (int, float):
            result._add_term(right, 0)
        elif type(right) == Poly:
            for k,v in right.terms.items():
                result._add_term(v,k)
        return result

    
    def __radd__(self,left):
        result = Poly()
        result.terms = self.terms
        if type(left) not in (Poly,int,float):
            raise TypeError('Poly.__add__:argument is not a Polynomial or int or float')
        if type(left) in (int, float):
            result._add_term(left, 0)
        elif type(left) == Poly:
            for k,v in left.terms.items():
                result._add_term(v,k)
        return result
    

    def __mul__(self,right):
        result = Poly()
        if type(right) not in (Poly,int,float):
            raise TypeError('Poly.__add__:argument is not a Polynomial or int or float')
    

    def __rmul__(self,left):
        result = Poly()
        if type(left) not in (Poly,int,float):
            raise TypeError('Poly.__add__:argument is not a Polynomial or int or float')
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('Poly.__add__:argument is not a Polynomial or int or float')
        if type(right) == Poly:
            for k,v in right.terms.items():
                if self.terms[k] != v:
                    return False
                else:
                    return True
        elif type(right) in (int,float):
            if len(self) == 0:
                return self.term[0] == right

    
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