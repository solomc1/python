class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for num in terms:
            assert type(num[0]) in (int,float) and type(num[1]) == int, 'terms must be int or float'
            assert num[1] >= 0, 'Power must be greater than or equal to 0'
            if num[1] < 0:
                pass
            elif num[0] != 0:
                assert num[1] not in self.terms, 'cannot have repeated powers'
                self.terms[num[1]] = num[0] #key = power value = number times x power
            
        
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
        rstring = ''
        counter = 1
        if len(self.terms) == 0:
            return 'Poly()'
        for key in self.terms:
            if counter != len(self.terms):
                rstring += '({},{})'.format(self.terms[key],key) + ','
            else:
                rstring += '({},{})'.format(self.terms[key],key) + ')'
            counter +=1
        return 'Poly(' + rstring

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms)
    
    def __call__(self,arg):
        assert arg not in (int,float), 'arguement must be either type int or float not: {}'.format(type(arg))
        answer = 0
        for key in self.terms:
            answer += self.terms[key]*(arg**key)
        return answer
    
    

    def __iter__(self):
        order_it = []
        for key in self.terms:
            order_it.append((self.terms[key],key))
        for tple in sorted(order_it,key=lambda x:x[1],reverse=True):
            yield tple
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Must be type: int')
        elif index < 0:
            raise TypeError('Must be greater than 0')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError('Must be greater than 0')
        self.terms[index] = value
        if value == 0:
            for key in self.terms:
                if self.terms[key] == 0:
                    self.__delitem__(key)
                    break
            

    def __delitem__(self,index):
        if index < 0:
            raise TypeError('Must be greater than 0')
        elif index in self.terms:
            del(self.terms[index])
        
            

    def _add_term(self,c,p):
        if type(c) not in (int,float) and type(p) != int and p < 0:
            raise TypeError('coefficent must be type int or float, power must be int greater than 0')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c == 0:
                del(self.terms[p])
            else:
                self.terms[p] = self.terms[p] + c
       

    def __add__(self,right):
        if type(self) != Poly and type(right) not in (int,float,Poly):
            raise TypeError('Must be Poly + int/float')
        if type(right) in (int,float):
            new_Poly = Poly()
            for key in self.terms:
                new_Poly._add_term(self.terms[key], key)
            new_Poly._add_term(right,0)
        elif type(self) == Poly and type(right) == Poly:
            new_Poly = Poly()
            for key in self.terms:
                new_Poly._add_term(self.terms[key], key)
            for key in right.terms:
                new_Poly._add_term(right.terms[key], key)
        
        return new_Poly
            
        

    
    def __radd__(self,left):
        if type(self) != Poly and type(left) not in (int,float):
            raise TypeError('Must be int/float + Poly')
        if type(left) in (int,float):
            new_Poly = Poly()
            for key in self.terms:
                new_Poly._add_term(self.terms[key], key)
            new_Poly._add_term(left,0)
        
        return new_Poly
        
    

    def __mul__(self,right):
        if type(self) != Poly and type(right) not in (int,float):
            raise TypeError('Must be Poly * int/float')
        if type(right) in (int,float):
            new_Poly = Poly()
            for key in self.terms:
                new_Poly._add_term(self.terms[key]*right,key)
        elif type(self) == Poly and type(right) == Poly:
            if self == Poly() or right == Poly():
                return 0
            
            new_Poly = Poly()
            for skey in self.terms:
                for rkey in right.terms:
                    new_Poly._add_term(self.terms[skey]*right.terms[rkey],skey+rkey)
        
        return new_Poly

    def __rmul__(self,left):
        if type(self) != Poly and type(left) not in (int,float):
            raise TypeError('Must be int/float * Poly')
        if type(left) in (int,float):
            new_Poly = Poly()
            for key in self.terms:
                new_Poly._add_term(self.terms[key]*left,key)
        return new_Poly

    def __eq__(self,right):
        if type(self) not in (int,float,Poly) or type(right) not in (int,float,Poly):
            raise TypeError('Must be Poly == int/float or int == Poly')
        
        if type(right) in (int,float):
            for key in self.terms:
                if self.terms[key] == right:
                    return True
        elif type(self) == Poly and type(right) == Poly:
            return self.terms.items() == right.terms.items()
        
        
        
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