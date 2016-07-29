class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            assert type(c) in (int, float)
            assert type(p) is int and p >= 0
            assert p not in self.terms# or c != self.terms[p]
            if c != 0:
                self.terms[p] = c
            
        
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
        s = []
        for p,c in self.terms.items():
            s.append((c,p))
        return 'Poly{}'.format(tuple(s))
    

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        lst = list(self.terms.keys())
        return max(lst)
    
    def __call__(self,arg):
        result = 0
        for p in self.terms:
            if p != 0:
                result += self.terms[p]*(arg**p)
            else:
                result += self.terms[p]
        return result
    

    def __iter__(self):
        l = [(c,p) for p, c in self.terms.items()]
        l = sorted(l, key= lambda x: -x[1])
        for i in l:
            yield i
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError 
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        elif value == 0:
            self.terms.pop(index)
        else:
            if 'terms' in self.__dict__:
                self.terms[index] = value
            self.__dict__[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            if index in self.terms:
                self.terms.pop(index)

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int:
            raise TypeError
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            for p in self.terms:
                if self.terms[p] == 0:
                    self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) is Poly:
            result = {p:c for p,c in self.terms.items()}
            for p1, c1 in right.terms.items():
                if p1 in result:
                    result [p1] += c1
                else:
                    result[p1] = c1
        elif type(right) in (int, float):
            result = {p:c for p,c in self.terms.items()}
            result[0] += right
            
        lst = []
        for p,c in result.items():
             lst.append((c,p))
        return Poly(*lst)
            
                
                

    
    def __radd__(self,left):
        if type(left) is Poly:
            result = {p:c for p,c in self.terms.items()}
            for p1, c1 in left.terms.items():
                if p1 in result:
                    result [p1] += c1
                else:
                    result[p1] = c1
        elif type(left) in (int, float):
            result = {p:c for p,c in self.terms.items()}
            result[0] += left
        lst = []
        for p,c in result.items():
            lst.append((c,p))
        return Poly(*lst)
    

    def __mul__(self,right):
        if type(right) is Poly:
            if len(right) == 0:
                return 0
        elif type(right ) in (int, float):
            result = {p:c for p,c in self.terms.items()}
            for p in result:
                result[p] *= right
            lst = []
            for p,c in result.items():
                lst.append((c,p))
            return Poly(*lst)    

    def __rmul__(self,left):
        if type(left) is Poly:
            if len(left) == 0:
                return 0
        elif type(left) in (int, float):
            result = {p:c for p,c in self.terms.items()}
            for p in result:
                result[p] *= left
        lst = []
        for p,c in result.items():
            lst.append((c,p))
        return Poly(*lst)          
    

    def __eq__(self,right):
        if type(right) is Poly:
            return self.terms == right.terms
        elif type(right) in (int, float):
            return len(self.terms) == 1 and 0 in self.terms and self.terms[0] == right
        else:
            raise TypeError

    
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