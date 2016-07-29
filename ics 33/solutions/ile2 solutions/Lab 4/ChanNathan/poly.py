class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for i,j in terms:
            assert type(i) in (int,float),'Poly.__init__: illegal coefficient in :{}'.format((i,j))
            assert (type(j) == int),"Poly.__init__: power in: {} must be an integer".format((i,j))
            assert j >= 0, 'Poly.__init__: power in {} must be greater than or equal to zero'.format((i,j))
            assert j not in self.terms.keys(),"Poly.__init__: power in {} is already defined".format((i,j))
            if i != 0:
                self.terms.update({j:i})
            
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
        return 'Poly{}'.format(tuple((i,j) for j,i in self.terms.items()))

    
    def __len__(self):
        if len(list(self.terms)) == 0:
            return 0
        return max(list(i for i in self.terms.keys()))
    
    def __call__(self,arg):
        ret=0
        for pow,coe in self.terms.items():
            ret+=(coe*(arg**pow))
        return ret


    def __iter__(self):
        # result of power in decreasing order
        ret=sorted(list((i,j) for j,i in self.terms.items()),key=lambda x:x[-1],reverse=True)
        return iter(ret)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Poly.__getitem__: {} must be of int type".format(index))
        if index < 0:
            raise TypeError("Poly.__getitem__: {} must be greater than or equal to 0".format(index))
        if index not in self.terms:
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__setitem__: {} must be int and less than 0".format(index))
        # del from dict if coefficient argumnt is = 0, then del from dict if present
        if value == 0 and 0 in self.terms.values():
            for i,j in tuple(self.terms.items()):
                if j == 0:
                    self.terms.pop(i)
        else:
            self.terms[index]=value


    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__: {} must be a power greater than or equal to 0".format(index))
        if index in self.terms.keys():
            self.terms.pop(index)

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError("Poly._add_term: coefficient {} must be an integer or float".format(c))
        if type(p) != int and p < 0:
            raise TypeError("Poly._add-term: power {} must be an integer greater than or equal to 0".format(p))
        # if pow not in polynomial, coefficient != 0
        # if pow in polynomial, coefficient added to existing coefficient for that power
        # if the resultant coefficient is 0, pow deleted
        if p not in self.terms.keys() and c != 0:
            self.terms.update({p:c})
        elif p in self.terms.keys():
            if int(self.terms[p])+c == 0:
                self.terms.pop(p)
            else:
                coef=int(self.terms[p])+c
                self.terms[p]=coef

    def __add__(self,right):
        ret=eval(repr(self))
        if type(right) == int:
            ret._add_term(0,right)
        elif type(right) == Poly:
            for i,j in right.terms.items():
                ret._add_term(j,i)
        return ret

    
    def __radd__(self,left):
        return self.__add__(left)

    def __mul__(self,right):
        ret=eval(repr(self))
        if type(right) == int:
            for i,j in tuple(ret.terms.items()):
                ret.terms[i]=j*right
        elif type(right) == Poly:
            for i in self.terms.items():
                for k,l in right.terms.items():
                    ret._add_term(l,k)
        return ret
                        
    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly,int):
            raise TypeError("Poly.__eq__ must be in Poly or int type")
        if type(right) == int:
            return list(self.terms.values())[0] == right
        return all(i in right.terms.keys() for i in self.terms.keys()) and len(list(right.terms.keys()) == len(list(self.terms.keys())))

    
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