class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:
            if type(x[0]) not in (int,float):
                raise AssertionError('Poly.__init__: '+str(x[0])+' coefficient must be either an int or a float')
            elif type(x[1]) != int or x[1] < 0:
                raise AssertionError('Poly.__init__: '+str(x[1])+' Power must be a int greater than or equal to than 0')
            elif x[0] == 0:
                pass
            elif x[1] in self.terms.keys():
                raise AssertionError('Poly.__init__: '+str(x[1])+' Is already in the dictionary.')
            else:
                try:
                    self.terms[x[1]] = x[0]
                except:
                    self.terms[0] = 0
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
        Str = 'Poly('
        for x,y in zip(self.terms.keys(),self.terms.values()):
            Str+=str(y)+','+str(x)+'),('
        Str = Str.rstrip(",(")+')'
        return Str

    
    def __len__(self):
        if len(list(self.terms.keys())) == 1 and self.terms.keys()[0] == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        Sum = 0
        for x,y in zip(self.terms.keys(),self.terms.values()):
            Sum+=((arg**x)*y)
        return Sum
    

    def __iter__(self):
        for x in sorted(self.terms.keys(),reverse=True):
            yield (self.terms[x],x)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: '+'illegal index value: '+str(index)+' is not an integer > 0')
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: illegal power value: '+str(index)+' is not an integer > 0')
        if index in self.terms.keys():
            if value == 0:
                self.terms.pop(index)
            else:
                self.terms[index] = value
        else:
            if value == 0:
                pass
            else:
                self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitem__: illegal index: '+str(index)+' is not a integer > 0') 
        elif index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Poly._add_term: illegal coefficient '+str(c)+' must be either a int or a float')
        elif type(p) != int or p < 0:
            raise TypeError('Poly._add_term: illegal power '+str(c)+' is not a integer > 0')
        else:
            if p not in self.terms.keys() and c != 0:
                self.terms[p] = c
            elif p in self.terms.keys():
                self.terms[p]+=c
                if self.terms[p] == 0:
                    self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError("unspported operand type(s) for +: "+"'Poly' and "+str(type(right)).strip("<> class"))
        elif type(right) == Poly:
            NewP = Poly()
            for x in self:
                NewP._add_term(x[0], x[1])
            for y in right:
                NewP._add_term(y[0],y[1])
            return NewP
        elif type(right) == int or float:
            NewP = Poly()
            for x in self:
                NewP._add_term(x[0],x[1])
            NewP._add_term(right,0)
            return NewP
            

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError("unspported operand type(s) for *: "+"'Poly' and "+str(type(right)).strip("<> class"))
        elif type(right) == Poly:
            NewP = Poly()
            for x in self:
                for y in right:
                    NewP._add_term(x[0]*y[0], x[1]+y[1])
            return NewP
        elif type(right) == int or float:
            NewP = Poly()
            for x in self:
                pass

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (int,float,Poly):
            raise TypeError("unspported operand type(s) for =: "+"'Poly' and "+str(type(right)).strip("<> class"))
        elif type(right) == Poly:
            result = True
            for x,y in zip(self,right):
                if x[1] == y[1]: 
                    if x[0] == y[0]:
                        result = True
                    else:
                        return False
                else:
                    return False
            return result
        elif type(right) == int or float:
            if len(self) != 0:
                return False
            else:
                for x in self:
                    if x[0] == right:
                        return True
                    else:
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