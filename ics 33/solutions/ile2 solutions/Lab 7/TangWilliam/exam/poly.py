class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.term = terms
        for k,v in terms:
            assert type(k) in [float,int]
            assert type(v) in [float,int]
            assert v >= 0
            if k not in self.terms.keys():
                self.terms[v]= k
            
        
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
        def eval():
            p = Poly(self.term)
            return p
        string = ''
        for k,v in self.terms.items():
            string += '({},{})'.format(v,k)
        return 'Poly('+ string +')'
        pass

    
    def __len__(self):
        largest = 0
        for item in self.terms.keys():
            if item > largest:
                largest = item
        return largest
        pass
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += v*(arg**k)
        return total
        pass
    

    def __iter__(self):
        def Poly_iter(self,*terms):
            def __init__(self):
                self.d = list(self.terms.items())
                self.count = 0
            def __next__(self):
                if self.count == len(self.terms.items()):
                    yield 0
                else:
                    self.count+=1
                    yield self.d[self.count-1]
                                 
                

        pass
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        for k,v in self.terms.items():
            if k == index:
                return v      
        if index not in list(self.terms.values()):
            return 0


        pass
            

    def __setitem__(self,power,coefficient):
        if type(power) != int or power <0:
            raise TypeError
        if power not in self.terms.values():
            if coefficient == 0:
                for k,v in self.terms.items():
                    if v == 0:
                        self.terms.remove[k]
            else:
                self.terms[coefficient]= power
        

            
    pass
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('Not greater than 0 or is not a int type')
        if index in self.terms.keys(0):
            self.terms.remove[index]
        pass
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError('Not int or float')
        if p >= 0:
            raise TypeError('not greater than 0')
        if p not in self.terms.keys() and p != 0:
            self.terms[c]= p
        if p in self.terms.keys():
            b = self.terms[p]+c
            if b == 0:
                self.terms.remove[p]
            else:
                self.terms[p]= b
            
   
       

    def __add__(self,right):
        if type(right)not in [float,int, Poly]:
            raise TypeError('Object is not a int of float')
        if type(right)== Poly:
            d = {}
            for k,v in list(right.terms.items()):
                if k in self.terms.keys():
                    self.terms[k]+= k
                else:
                    self.terms[k]=v
            return self.terms
        if type(right)== int or type(right)== float:
            if 0 not in self.term.keys():
                self.terms[0]= right
            else:
                self.terms[0]+= right
            return self.terms
                
                

                    
        pass

    
    def __radd__(self,left):
        if type(left)not in [float,int, Poly]:
            raise TypeError('Object is not a int of float')
        if type(left)== Poly:
            d = {}
            for k,v in list(left.terms.items()):
                if k in self.terms.keys():
                    self.terms[k]+= k
                else:
                    self.terms[k]=v
            return self.terms
        if type(left)== int or type(left)== float:
            if 0 not in self.term.keys():
                self.terms[0]= left
            else:
                self.terms[0]+= left
            return self.terms
                
        pass
    

    def __mul__(self,right):
        if type(right)not in [float,int, Poly]:
            raise TypeError('Object is not a int of float')
        if type(right)== Poly:
            d = {}
            for k,v in right.terms.items():
                for p,c in self.terms.items():
                    d[k+p]= v*c
            return d
        if type(right) in (float,int):
            for k,v in self.terms.items():
                self.terms[k]= v*right
                
                
        pass
    

    def __rmul__(self,left):
        if type(left)not in [float,int, Poly]:
            raise TypeError('Object is not a int of float')
        if type(left)== Poly:
            d = {}
            for k,v in left.terms.items():
                for p,c in self.terms.items():
                    d[k+p]= v*c
            return d
        if type(left) in (float,int):
            for k,v in self.terms.items():
                self.terms[k]= v*left
        pass
    

    def __eq__(self,right):
        if type(right)not in [float,int, Poly]:
            raise TypeError('Object is not a int of float')
        if type(right)== Poly:
            if len(right.terms.items())!= len(self.terms.items()):
                return False
            for item in self.terms.items():
                if item not in right.terms.items():
                    return False
            return True
        if type(right)== int or type(right)== float:
            if len(self.terms.items())!= 1:
                return False
            else:
                return self.terms[0]== right
                
            
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