# MAHYAR KATIRACHI 72531960
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) == int or type(i[0]) == float
            assert type(i[1]) == int and i[1]>=0
            assert i[1] not in self.terms
            if i[0] != 0:
                self.terms[i[1]]=i[0]
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
        return 'Poly{}'.format(tuple((i[1],i[0]) for i in self.terms.items()))

    
    def __len__(self):
        if len(self.terms):
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for i in self.terms.items():
            result += i[1]*(arg**i[0])
        return result
    

    def __iter__(self):
        for i in reversed(sorted(self.terms.items())):
            yield (i[1],i[0])
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError
        if value == 0 and index in self.terms:
            del self.terms[index]
        if value !=0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError
        if type(p) != int or p<0:
            raise TypeError
        deleted = False
        if c != 0:
            if p in self.terms:
                self.terms[p] += c
                if self.terms[p]== 0:
                    del self.terms[p]
                    deleted = True
            if p not in self.terms and not deleted:
                self.terms[p] = c
       

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError
        if type(right) in (int,float):
            right = Poly((right,0))
        result = eval(repr(self))
        for x in right:
            result._add_term(x[0],x[1])
        return result
        
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError
        if type(right) in (int,float):
            right = Poly((right,0))
        result = Poly()
        for i in self:
            for j in right:
                result._add_term(i[0]*j[0],i[1]+j[1])
        return result
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError
        if type(right) in (int,float):
            right = Poly((right,0))
        if sorted(self.terms.items()) == sorted(right.terms.items()):
            return True
        return False
            

    
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