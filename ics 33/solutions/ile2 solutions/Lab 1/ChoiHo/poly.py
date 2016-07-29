
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        self.terms = dict()
        for k,v in terms:
            assert type(v) == type(int())
            assert v >= 0
            assert type(k) == type(int()) or type(k) == type(float())
            assert not (v in self.terms.keys())
            if k != 0:
                self.terms.update({v:k})
        # So __init__ should build this dictionary from terms
        
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
        return "Poly({})".format(",".join([str((v,k)) for k,v in self.terms.items()]))

    def __len__(self):
        if len(self.terms.keys())==0:
            return 0
        return sorted(self.terms.keys())[-1]
    
    def __call__(self,arg):
        result = 0
        for k,v in self.terms.items():
            result += v*(arg**k)
        return result

    def __iter__(self):
        result = sorted([(v,k) for k,v in self.terms.items()], key = lambda x : x[1], reverse = True)
        return iter(result)
    def __getitem__(self,index):
        if type(index) != type(int()) and type(index) != type(float()) or index < 0:
            raise TypeError
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError
        if index in self.terms.keys():
            self.terms[index] = value
            if value == 0:
                del self.terms[index]
        else:
            if value != 0 and index > 0:
                self.terms.update({index:value})
                

    def __delitem__(self,index):
        self.__getitem__(index)
        if index in self.terms.keys():
            del self.terms[index]


    def _add_term(self,c,p):
        if c != 0 and p >= 0:
            self.terms.update({p:c} if not(p in self.terms.keys()) else {p:(c+self.terms[p])})
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        result = eval(repr(self))
        if type(right) == type(self):
            for i in right:
                result._add_term(i[0],i[1])
        elif type(right)==type(int()) or type(right) == type(float()):
            result._add_term(right,0)
        else:
            raise TypeError
        return result
        
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        pside = Poly()
        if type(right) == type(int()) or type(right) ==  type(float()):
            right = Poly((right,0))
        if type(right) != type(Poly()):
            raise TypeError
        for p,c in self.terms.items():
            for po,con  in right.terms.items():
                pside.terms.update({p+po:c*con} if p+po not in pside.terms.keys() else {p+po:(c*con + pside.terms[p])})
        return pside

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == type(int()) or type(right) ==  type(float()):
            right = Poly((right,0))
        if type(right) != type(Poly()):
            raise TypeError
        for p,c in self.terms.items():
            try:
                if right[p] != c:
                    return False
            except:
                return False
        return True

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