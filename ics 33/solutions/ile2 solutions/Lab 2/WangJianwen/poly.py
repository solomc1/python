class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for Tuple in terms:
            if type(Tuple[0]) not in [int,float] or type(Tuple[1]) not in [int] or Tuple[1] < 0:
                raise AssertionError
            elif Tuple[1] in self.terms:
                raise AssertionError
            elif Tuple[0] == 0:
                continue
            self.terms[Tuple[1]] = Tuple[0]
        
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
        def dict_to_tuple(d):
            new_str = ''
            for key in d:
                new_str += ',({},{})'.format(d[key],key)
            new_str = new_str.replace(',', '', 1)
            return new_str
        return "Poly({})".format(dict_to_tuple(self.terms))

    
    def __len__(self):
        number = 0
        for key in self.terms:
            if key > number:
                number = key
        return number
    
    def __call__(self,arg):
        number = 0
        for key in self.terms:
            number += arg**key * self.terms[key]
        return number
    

    def __iter__(self):
        new_list = []
        for key in self.terms:
            new_list.append((self.terms[key],key))
        new_list = sorted(new_list, key = lambda x: x[1], reverse = True)
        Iterable = iter(new_list)
        for item in Iterable:
            yield item

    def __getitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError
        elif index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) not in [int] or index < 0:
            raise TypeError
        elif value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) not in [int] or index < 0:
            raise TypeError
        elif index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float] or type(p) not in [int] or p < 0:
            raise TypeError
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms and c != 0:
            x = self.terms[p]
            self.terms[p] = x + c
            if self.terms[p] == 0:
                del self.terms[p]
       

    def __add__(self,right):
        print(self)
        new_Poly = eval(self.__repr__())
        if type(right) not in [Poly,int,float]:
            raise TypeError
        elif type(right) in [int,float]:
            if 0 in new_Poly.terms:
                print(new_Poly)
                print(new_Poly.terms[0])
                new_Poly.terms[0] = new_Poly.terms[0] + right
                return new_Poly
            else:
                new_Poly.terms[0] = right
                return new_Poly
        else:
            for item in right.terms:
                new_Poly._add_term(right.terms[item],item)
            return new_Poly

    
    def __radd__(self,left):
        new_Poly = eval(self.__repr__())
        if type(left) not in [Poly,int,float]:
            raise TypeError
        elif type(left) in [int,float]:
            if 0 in new_Poly.terms:
                new_Poly.terms[0] = new_Poly.terms[0] + left
                return new_Poly
            else:
                new_Poly.terms[0] = left
                return new_Poly
        else:
            for item in left.terms:
                new_Poly._add_term(left.terms[item],item)
            return new_Poly
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError
        elif type(right) in [int,float]:
            new_Poly = eval(self.__repr__())
            for key in new_Poly.terms:
                new_Poly.terms[key] = new_Poly.terms[key] * right
            return new_Poly
        else:
            new_Poly = Poly()
            for item in self.terms:
                for term in right.terms:
                    new_power = item + term
                    new_coeff = self.terms[item] * right.terms[term]
                    new_Poly._add_term(new_coeff,new_power)
            return new_Poly
                    
    

    def __rmul__(self,left):
        if type(left) not in [Poly,int,float]:
            raise TypeError
        elif type(left) in [int,float]:
            new_Poly = eval(self.__repr__())
            for key in new_Poly.terms:
                new_Poly.terms[key] = new_Poly.terms[key] * left
            return new_Poly
        else:
            new_Poly = Poly()
            for item in self.terms:
                for term in left.terms:
                    new_power = item + term
                    new_coeff = self.terms[item] * left.terms[term]
                    new_Poly._add_term(new_coeff,new_power)
            return new_Poly
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly] or type(self) not in [int, float, Poly]:
            raise TypeError
        elif type(self) == Poly and type(right) == Poly:
            if len(self.terms) != len(right.terms):
                return False
            for item in self.terms:
                if item not in right.terms:
                    return False
                elif self.terms[item] != right.terms[item]:
                    return False
            return True
        elif type(right) in [int, float] and type(self) == Poly:
            if self.__len__() > 0:
                return False
            elif self.terms[0] == right:
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