class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        checkset = set()
        for i in terms:
            assert i[1] not in checkset, "Power specified more than once with: "+str(i)
            assert type(i[0]) in (int, float), "Illegal coefficient in: "+str(i)
            assert type(i[1]) is int and i[1] >= 0, "Illegal power in: "+str(i)
            if i[0] > 0:
                checkset.add(i[1])
        self.terms = {i[1]:i[0] for i in terms if i[0] != 0}
        
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
        items = ''
        for i in self.terms:
            items += '({c},{p}),'.format(p = str(i), c = str(self.terms[i]))
        return "Poly("+items.strip(',')+")"

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
        
    
    def __call__(self,arg):
        assert type(arg) in (int,float), "Polynomial object may only be called with a single numeric argument: "+str(arg)
        answer = 0
        for i in self.terms:
            answer += (self.terms[i]*(arg**i))
        return answer
    

    def __iter__(self):
        for i in sorted(self.terms, reverse = True):
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        if (not type(index) is int) or (index<0):
            raise TypeError(str(index) +" is not a valid index Type, must be int > 0.")
        if index not in self.terms:
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if (not type(index) is int) or (index<0):
            raise TypeError(str(index) +" is not a valid index Type, must be int > 0.")
        if value == 0:
            if index not in self.terms:
                return None
            self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if (not type(index) is int) or (index<0):
            raise TypeError(str(index) +" is not a valid index Type, must be int > 0.")
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("The coefficient must be Type int or float: "+str(c))
        if (not type(p) is int) or p < 0:
            raise TypeError("The power must be an int that is equal or greater than 0: "+str(p))
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            newC = self.terms[p] + c
            if newC == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = newC
        
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError(str(type(right))+" unsupported operand type with + and Poly object.")
        if type(right) is Poly:
            newPoly = Poly()
            powers = set(self.terms.keys()).union(set(right.terms.keys()))
            for p in powers:
                newPoly._add_term(self.terms[p], p)
                newPoly._add_term(right.terms[p], p)
        if type(right) in (int,float):
            newPoly = Poly((right, 0))
            for p in self.terms:
                newPoly._add_term(self.terms[p],p)
        return newPoly

    
    def __radd__(self,left):
        if type(left) not in (Poly,int,float):
            raise TypeError(str(type(left))+" unsupported operand type with + and Poly object.")
        newPoly = Poly()
        if type(left) is Poly:
            newPoly = Poly()
            powers = set(self.terms.keys()).union(set(left.terms.keys()))
            for p in powers:
                newPoly._add_term(self.terms[p], p)
                newPoly._add_term(left.terms[p], p)
        if type(left) in (int,float):
            newPoly = Poly((left, 0))
            for p in self.terms:
                newPoly._add_term(self.terms[p],p)
        return newPoly
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
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