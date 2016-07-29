class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for poly_tuple in terms:
            assert type(poly_tuple[0]) in (int, float), 'The coefficient must be of the int or float class'
            assert type(poly_tuple[1]) == int, 'The power must be of the int class'
            assert poly_tuple[1]>=0, 'The power must be >= 0'
            assert poly_tuple[1] not in self.terms, 'Cannot have more than one of the same power'
            if poly_tuple[0]!=0:
                self.terms[poly_tuple[1]]=poly_tuple[0]
        
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
        poly_tuple_list=[]
        for power, coefficient in self.terms.items():
            poly_tuple_list.append((coefficient,power))
        return 'Poly{}'.format(tuple(poly_tuple_list))

    
    def __len__(self):
        max=0
        for power in self.terms.keys():
            if power> max:
                max=power
        return max
    
    def __call__(self,arg):
        result=0
        for power, coefficient in self.terms.items():
            result+= coefficient*(arg**power)
        return result
    

    def __iter__(self):
        poly_tuple_list=[]
        for power, coefficient in self.terms.items():
            poly_tuple_list.append((coefficient,power))
        poly_tuple_list.sort(key=lambda x: (x[-1],x[0]),reverse=True)
        return iter(poly_tuple_list)
            

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('index must be an integer greater than or equal to 0')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index)!= int or index<0:
            raise TypeError('index must be an int and greater than or equal to 0')
        else:
            self.terms[index]=value
        if value ==0 and index in self.terms:
            del self.terms[index]
        return 
            

    def __delitem__(self,index):
        if type(index)!= int or index<0:
            raise TypeError('index must be an int and greater than or equal to 0')
        elif index in self.terms:
            del self.terms[index]
        return 
            

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p)==int and p>=0:
            if p not in self.terms and c!=0:
                self.terms[p]=c
            elif p in self.terms:
                new_co=self.terms[p]+c
                if new_co==0:
                    del self.terms[p]
                else:
                    self.terms[p]=new_co
        else:
            raise TypeError('The coefficient must be an int or float, the power must be an int greater than or equal to 0')
       

    def __add__(self,right):
        if type(right) in (Poly,int,float):
            new_poly=Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient,power)
            if type(right)==Poly:
                for power,coefficient in right.terms.items():
                    new_poly._add_term(coefficient,power)
            else:
                new_poly._add_term(right,0)
            return new_poly
        else:
            raise TypeError('')

    
    def __radd__(self,left):
        if type(left) in (int,float):
            new_poly=Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient,power)
            new_poly._add_term(left,0)
            return new_poly
        else:
            raise TypeError('')
    

    def __mul__(self,right):
        if type(right) in (Poly,int,float):
            new_poly=Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient,power)
            if type(right)==Poly:
                for poewr,coefficient in right.terms.items():
                    for p in list(new_poly.terms.keys()):
                        new_poly._add_term(coefficient,p+power)
                return new_poly
            else:
                for power,coefficient in new_poly.terms.items():
                    new_poly.terms[power]=coefficient*right
                    return new_poly
        else:
            raise TypeError('')

    def __rmul__(self,left):
        if type(left) not in (int,float):
            raise TypeError('')
        else:
            new_poly=Poly()
            for power, coefficient in self.terms.items():
                new_poly._add_term(coefficient,power)
            for power,coefficient in new_poly.terms.items():
                    new_poly.terms[power]=coefficient*left
            return new_poly
    

    def __eq__(self,right):
        if type(right) in (float, Poly, int):
            if type(right)==Poly:
                if len(self.terms)==len(right.terms):
                    for coefficient,power in self.terms.items():
                        if power not in right.terms or right.terms[power]==coefficient:
                            return False
                    return True
                else:
                    return False
            else:
                if len(self.terms)==1 and 0 in self.terms:
                    return self.terms[0]== right
                else:
                    return False
            
        else:
            raise TypeError('')

    
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