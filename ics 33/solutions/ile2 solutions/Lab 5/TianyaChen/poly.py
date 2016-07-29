class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if (type(term[0]) not in (int,float)) or (type(term[1]) != int) or term[1] < 0:
                raise AssertionError('invalid arguments')
            if term[0] != 0:
                if term[1] not in self.terms:
                    self.terms[term[1]] = term[0]
                else:
                    raise AssertionError('invalid arguments')
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
        return 'Poly('+str(','.join(str((c,p)) for p,c in self.terms.items()))+')'

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        for item in self.terms:
            result += self.terms[item]*(arg**item)
        return result
    

    def __iter__(self):
        for key in sorted(self.terms,key=lambda x:x,reverse=True):
            yield (self.terms[key],key)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('It is not a valid index!')
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('It is not a valid index!')
        if value == 0 and index in self.terms:
            self.__delitem__(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('It is not a valid index!')
        if index in self.terms:
            del self.terms[index]        
            

    def _add_term(self,c,p):
        if type(c) not in (int,float) or type(p) != int or p < 0:
            raise TypeError('Invalid arguments!')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.__delitem__(p)
        
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('Invalid type of the argument!')
        result = Poly()
        for i in self.terms:
            result._add_term(self.terms[i],i)
        if type(right) in (int,float):
            result._add_term(right,0)
        else:
            for p in right.terms:
                result._add_term(right.terms[p],p)
        return result

    
    def __radd__(self,left):
        return self.__add__(left)


    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('Invalid type of the argument!')
        result = Poly()
        if type(right) in (int,float):
            for i in self.terms:
                result._add_term(self.terms[i]*right,i)     
        else:
            for p1 in self.terms:
                for p2 in right.terms:
                    result._add_term(self.terms[p1]*right.terms[p2],p1+p2)
        return result
                                           
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError('The type is not valid!')
        if type(right) in (int,float):
            if len(self.terms)==1 and 0 in self.terms:
                return self.terms[0] == right
            else:
                return False
        else:
            if len(self.terms) != len(right.terms):
                return False
            for p in self.terms:
                if p not in right.terms or self.terms[p] != right.terms[p]:
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