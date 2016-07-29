#Amy Quach 52471399 Lab 7

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for x,y in terms:
            if type(x) not in (int, float): raise AssertionError('Coefficient must be an int or float')
            elif type(y) != int: raise AssertionError('Power must be an int')
            elif y < 0: raise AssertionError('Power must be greater than or equal to 0')
            elif x == 0: continue
            elif y in self.terms.keys(): raise AssertionError('Duplicate terms with same power')
            else: self.terms[y] = x
        
        
        
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
        p = ''
        for x,y in self.terms.items():
            p += '({y},{x}),'.format(y=y,x=x)
        return 'Poly({x})'.format(x = p[:-1])
    
    def __len__(self):
        if self.terms == {}: return 0
        keys = list(self.terms.keys())
        return max(keys)
    
    def __call__(self,arg):
        result = 0
        items = self.terms.items()
        for x,y in items:
            result += y*(arg**x)
        return result
    

    def __iter__(self):
        powers = sorted(self.terms.keys(), reverse = True)
        co = []
        for i in powers:
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        if type(index) != int: raise TypeError('Power must be an int')
        elif index < 0: raise TypeError('Power must be >=0')
        elif index not in self.terms.keys(): return 0
        else: return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int: raise TypeError('Power must be an int')
        elif index < 0: raise TypeError('Power must be >=0')
        elif index not in self.terms.keys():
            if value == 0: pass
            else: self.terms[index] = value
        elif value == 0: del self.terms[index]
        else: self.terms[index] = value
        
            

    def __delitem__(self,index):
        if type(index) != int: raise TypeError('Power must be an int')
        elif index < 0: raise TypeError('Power must be >=0')
        elif index not in self.terms.keys(): pass
        else: del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int: raise TypeError('Power must be an int')
        elif p < 0: raise TypeError('Power must be >=0')
        elif type(c) not in (int,float): raise TypeError('Coefficient must be an int or float')
        elif c == 0: pass
        elif p not in self.terms.keys() and c != 0: self.terms[p] = c
        else:
            if self.terms[p] + c == 0: del self.terms[p] 
            else: self.terms[p] = self.terms[p] + c       
       

    def __add__(self,right):
        if type(right) not in (type(self), int, float): raise TypeError('The right operand must be int,float,or Poly')
        m = Poly()
        if type(right)== type(self):
            for x,y in self.terms.items():
                m.terms[x] = y
            for u,v in right.terms.items():
                m._add_term(v,u)
        else:
            for x,y in self.terms.items():
                m.terms[x] = y
            m._add_term(right,0)
        return m

    
    def __radd__(self,left):
        if type(left) not in (type(self), int, float): raise TypeError('The left operand must be int,float,or Poly')
        m = Poly()
        if type(left)== type(self):
            for x,y in self.terms.items():
                m.terms[x] = y
            for u,v in left.terms.items():
                m._add_term(v,u)
        else:
            for x,y in self.terms.items():
                m.terms[x] = y
            m._add_term(left,0)
        return m
    

    def __mul__(self,right):
        if type(right) not in (type(self), int, float): raise TypeError('The right operand must be int,float,or Poly')
        m = Poly()
        if type(right) == type(self):
            for x,y in self.terms.items():
                for u,v in right.terms.items():
                    if x+u in m.terms.keys(): m._add_term(y*v, x+u)
                    else: m.terms[x+u] = y*v
        else:
            for x,y in self.terms.items():
                m.terms[x] = y*right
        return m
        
            

    def __rmul__(self,left):
        if type(left) not in (type(self), int, float): raise TypeError('The left operand must be int,float,or Poly')
        m = Poly()
        if type(left) == type(self):
            for x,y in self.terms.items():
                for u,v in left.terms.items():
                    if x+u in m.terms.keys(): m._add_term(y*v, x+u)
                    else: m.terms[x+u] = y*v
        else:
            for x,y in self.terms.items():
                m.terms[x] = y*left
        return m

    def __eq__(self,right):
        if type(right) not in (type(self), int, float): raise TypeError('The right operand must be int,float,or Poly')
        if type(right) == type(self):
            right_items = sorted(list(right.terms.items()))
            s_items = sorted(list(self.terms.items()))
            return True if right_items == s_items else False
        else:
            s_val = sorted(list(self.terms.values()))
            if len(s_val) > 1: return False
            return True if s_val[0] == right else False

    
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