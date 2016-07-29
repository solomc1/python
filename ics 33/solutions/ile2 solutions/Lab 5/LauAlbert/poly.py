#Albert Lau, Lab 5
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for things in terms:
            if things[0] != 0:
                if not isinstance(things[0],float) and not isinstance(things[0],int):
                    assert False
                if not isinstance(things[1],int):
                    assert False
                if things[1] < 0:
                    assert False
                if things[1] in self.terms.keys():
                    assert False
                self.terms.update({things[1]:things[0]})
            
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
        relist = []
        for x,y in self.terms.items():
            relist.append((y,x))
        return 'Poly'+str(tuple(relist)) 

    
    def __len__(self):
        try:
            return max(self.terms.keys())
        except:
            return 0
    
    def __call__(self,arg):
        sum = 0
        if isinstance(arg,int) or isinstance(arg,float):
            for x,y in self.terms.items():
                sum += y*arg**x
            return sum
    

    def __iter__(self):
        for x,y in sorted(self.terms.items(), reverse = True):
            yield (y,x)

    def __getitem__(self,index):
        if not isinstance(index, int) or index<0:
            raise TypeError
        try:
            return self.terms[index]
        except KeyError:
            return 0
            

    def __setitem__(self,index,value):
        if not isinstance(index, int) or index<0:
            raise TypeError
        if value == 0:
            try:
                self.terms.pop(index)
            except KeyError:
                pass
        elif index not in self.terms.keys():
            self.terms.update({index:value})
        else:
            self.terms[index] = value

            

    def __delitem__(self,index):
        if not isinstance(index, int) or index<0:
            raise TypeError
        else:
            try:
                self.terms.pop(index)
            except KeyError:
                pass
            

    def _add_term(self,c,p):
        if isinstance(c, int) or isinstance(c, float):
            if c != 0:
                if p in self.terms.keys():
                    c = c + self.terms[p]
                    
                self.__setitem__(p,c)
       

    def __add__(self,right):
        if type(right) == Poly:
            k = {}
            for x,y in self.terms.items():
                k.update({x:y})
            for a,b in right.terms.items():
                if a in k.keys():
                    k[a] = b + k[a]
                else:
                    k.update({a:b})
            z = Poly()
            for x,y in k.items():
                z._add_term(y,x)
            
            return z
        elif type(right) == int:
            if 0 in self.terms.keys():
                self[0] = self[0] + right
                return self
#                 print(True)
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        if type(right) == Poly:
            k = {}
            for x,y in self.terms.items():
                k.update({x:y})
            for a,b in right.terms.items():
                if a in k.keys():
                    k[a] = b * k[a]
                else:
                    k.update({a:b})
            z = Poly()
            for x,y in k.items():
                z._add_term(y,x)
            
            return z
        elif type(right) == int:
            if 0 in self.terms.keys():
                self[0] = self[0] * right
                return self
        pass
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == int:
            return all(right == k for k in self.terms.values())
        else:
            raise TypeError

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