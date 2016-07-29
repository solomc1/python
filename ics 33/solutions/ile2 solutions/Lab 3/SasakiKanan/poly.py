class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        l = []
        for t in terms:
            if(type(t[1]) in (int,float) and type(t[0]) in (int,float)):
                assert(type(t[1]) == int and type(int(t[0])) == int)
            else:
                raise AssertionError('not a valid type')
            assert(t[1] >= 0)
            if(t[1] not in l or t[0] <= 0):
                if(t[0] != 0):
                    self.terms.update({t[1] : t[0]})
            else:
                raise AssertionError('not a valid type')
            l.append(t[1])
        # Fill in the rest of this method, using *terms to intialize self.terms
  
    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        return 'Poly(' + ','.join(str((v,k)) for k,v in self.terms.items())  + ')'

    
    def __len__(self):
        if(len(self.terms) == 0):
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += (arg ** k) * v
        return total
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if(type(index) != int or index < 0):
            raise TypeError('invalid index')
        elif(index not in self.terms.keys()):
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if(type(index) != int or index < 0):
            raise TypeError('invalid index')
        elif(value == 0):
            if(index in self.terms.keys()):
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if(type(index) != int or index < 0):
            raise TypeError('invalid index')
        else:
            if(index in self.terms.keys()):
                del self.terms[index]
            

    def _add_term(self,c,p):
        if(type(c) not in (int,float) or type(p) != int or p  < 0):
            raise TypeError('invalid paramter')
        else:
            if(p not in self.terms.keys() and c != 0):
                self.terms.update({p : c})
            elif(p in self.terms.keys()):
                current = self.terms[p]
                newer = current + c
                if(newer != 0):
                    self.terms.update({p : newer})
                else:
                    if(p in self.terms.keys()):
                        del self.terms[p]
            else:
                if(c == 0):
                    if(p in self.terms.keys()):
                            del self.terms[p]
       

    def __add__(self,right):
        if(type(right) not in (Poly, int, float)):
            raise TypeError('Invalid addend type')
        else:
            newp = Poly()
            for c,p in self.terms.items():
                newp._add_term(p,c)
            if(type(right) == Poly):
                for k,v in right.terms.items():
                    newp._add_term(v,k)
                return newp
            else:
                old = self.terms[0]
                newer = old + right
                newp[0] = newer
                return newp

    
    def __radd__(self,left):
        if(type(left) not in (Poly, int, float)):
            raise TypeError('Invalid addend type')
        else:
            newp = Poly()
            for c,p in self.terms.items():
                newp._add_term(p,c)
            if(type(left) == Poly):
                for k,v in left.terms.items():
                    newp._add_term(v,k)
                return newp
            else:
                old = self.terms[0]
                newer = old + left
                newp[0] = newer
                return newp

    def __mul__(self,right):
        if(type(right) not in (Poly, int, float)):
            raise TypeError('Invalid addend type')
        else:
            newpol = Poly()
            if(type(right) == Poly):
                for k,v in right.terms.items():
                    for p,c in self.terms.items():
                        newc = c
                        newv = v
                        newk = k
                        newp = p
                        if(c == 0):
                            newc = 1
                        if(v == 0):
                            newv = 1
                        if(k == 0):
                            newk = 1
                        if(p == 0):
                            newp = 1
                        newco = newc * newv
                        newpow = newk + newp
                        newpol._add_term(newco,newpow)
                return newpol
            else:
                for p,c in self.terms.items():
                    newp = p
                    newc = c
                    if(p == 0):
                        newp = 1
                    if(c == 0):
                        newc = 1
                    newco = newc * newv
                    newpow = newk * newp
                    newpol._add_term(newco,newpow)
                return newpol

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if(type(right) not in (Poly,int,float)):
            raise TypeError('Invalid Type')
        else:
            if(type(right) in (int,float)):
                if(len(self.terms) == 1 and 0 in self.terms.keys()):
                    for c in self.terms.values():
                        return c == right
                else:
                    return False
            else:
                for k,v in self.terms.items():
                    if({k : v} not in right.terms.items()):
                        return False
                return True
                    

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()