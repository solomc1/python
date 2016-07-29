from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c,p in terms:
            assert type(c) in (int,float), 'coefficient {} is not int or float'.format(c)
            assert type(p) is int and p >= 0, 'power {} is not int >= 0'.format(p)
            if p in self.terms:
                assert (p,c) in [(k,v) for k,v in self.terms.items()], 'cannot assign different coefficients to same value'
            if c != 0: self.terms[p] = c
            
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
        return 'Poly({})'.format(','.join([str((v,k)) for k,v in self.terms.items()]))

    
    def __len__(self):
        return max(list(self.terms)) if self.terms != {} else 0
    
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += v*arg**k
        return result
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), reverse=True):
            yield (v,k)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int or less than 0')
        return self.terms[index] if index in self.terms else 0
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int or less than 0')
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
                   

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('index is not int or less than 0')
        if index in self.terms:
            del self.terms[index]
                    

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('c is not int or float')
        if type(p) not in (int,float) or p < 0:
            raise TypeError('p is not int or float or less than 0')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unsupported operand type(s) for +: 'Poly' and '{}'".format(type_as_str(right)))
        result = Poly()
        for k,v in self.terms.items():
            result._add_term(v,k)
        if type(right) is Poly:
            for k,v in right.terms.items():
                result._add_term(v,k)
        else:
            result._add_term(right,0)
        return result
    
    
    def __radd__(self,left):
        if type(left) not in (int,float):
            raise TypeError("unsupported operand type(s) for +: '{}' and 'Poly'".format(type_as_str(left)))
        result = Poly()
        for k,v in self.terms.items():
            result._add_term(v,k)
        result._add_term(left,0)
        return result    
    

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unsupported operand type(s) for *: 'Poly' and '{}'".format(type_as_str(right)))
        result = Poly()
        for k,v in self.terms.items():
            if type(right) is Poly:
                for l,w in right.terms.items():
                    result._add_term(v*w,k+l)
            else:
                result._add_term(v*right,k)
        return result
            

    def __rmul__(self,left):
        if type(left) not in (Poly,int,float):
            raise TypeError("unsupported operand type(s) for *: '{}' and 'Poly'".format(type_as_str(left)))
        result = Poly()
        for k,v in self.terms.items():
                result._add_term(v*left,k)
        return result
        

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unequatable type(s): Poly() == {}()".format(type_as_str(right)))
        if type(right) is Poly:
            return self.terms == right.terms
        return self.terms == {0:right}
        
    
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