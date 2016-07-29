class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[0]) not in (int,float) or type(i[1]) != int and i[1] < 0:
                raise AssertionError('Poly.__init__:illegal information in: {}'.format(i))
            if i[1] in self.terms and i[0] in self.terms.value():
                raise AssertionError('Poly.__init__:contain repeated information in: {}'.format(i)) 
            if i[0] != 0:
                self.terms[i[1]] = i[0]
        
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
        return 'Poly({})'.format(','.join(['('+str(k) +','+ str(v)+')' for v,k in self.terms.items()]))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max([v for v in self.terms])

    def __call__(self,arg):
        result = 0 
        for k,v in self.terms.items():
            result += arg **k *v
        return result 
    

    def __iter__(self):
        for i in sorted(self.terms, key = lambda x: -x):
            yield (self.terms[i],i)
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: contain illegal power. {}'.format(index))
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: contain illegal power. {}'.format(index))
        if value  == 0 :
            for k,v in self.terms.items():
                if v == 0 and index in self.terms:
                    del(self.terms[k])
                else:
                    self.terms[k] = v 
    
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__delitem__: contain illegal power. {}'.format(index))
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int , float) or type(p) != int and p < 0 :
            raise TypeError('Poly._add_term: contain illegal information')
        if p not in self.terms and p != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
        for i in self.terms:
            if self.terms[i] == 0:
                del(self.terms[i]) 
            

    def __add__(self,right):
        if type(right) not in (Poly,int, float):
            raise TypeError('Poly.__add__: contain illegal type')
        result = Poly()
        for i in self.terms:
            result._add_term(self.terms[i],i)
        if type(right) in (int,float):
            result._add_term(right,0)
        else:
            for i in right.terms:
                result._add_term(self.terms[i],i)
        return result
            
            
        
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (Poly,int, float):
            raise TypeError('Poly.__add__: contain illegal type')
        result = Poly()
        if type(right) in (int,float):
            for i in self.terms:
                result._add_term(self.terms[i]*right,i)
        else:
            for i in self.terms:
                for j in right.terms:
                    result._add_term(self.terms[i]*right.terms[j], i*j)
        return result
    

    def __rmul__(self,left):
        return self.__mul__(left)

    def __eq__(self,right):
        if type(right) not in (Poly,int, float):
            raise TypeError('Poly.__eq__: contain illegal type')
        if type(right) in (int,float):
            return self.terms[0] == right
        else:
            result = True
            for k,v in self.terms.items():
                for z,y in right.terms.items():
                    if k !=z or v !=y :
                        result = False
            return result
                    
        

    
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