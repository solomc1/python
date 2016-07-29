class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for each in terms:
            if type(each[0]) not in (int, float):
                raise AssertionError("Coefficient was not an int or a float.")
            if type(each[1]) != int:
                raise AssertionError("Power must be an int.")
            if each[1] < 0:
                raise AssertionError("Power must be more than or equal to 0")
            if each[1] in self.terms:
                raise AssertionError("A power was repeated more than once.")
            if each[0] != 0:
                self.terms[each[1]] = each[0] 
        self.termtuple = terms
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
        strterm = str(self.termtuple)
        return 'Poly{}'.format(strterm)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for power, coefficient in self.terms.items():
            if power == 0:
                total += coefficient
            else:
                total += coefficient*(arg**power)
        return total
            
    

    def __iter__(self):
        sorted_power = sorted(self.terms.keys(), reverse = True)
        for each in sorted_power:
            yield (self.terms[each], each)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Argument was not an int.")
        if index < 0:
            raise TypeError("Argument must be greater than 0.")
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Argument was not an int.")
        if index < 0:
            raise TypeError("Argument must be greater than 0.")
        if value == 0:
            self.terms[index]= value
            del self.terms[index]
        if value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Argument was not an int.")
        if index < 0:
            raise TypeError("Argument must be greater than 0.")
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(c) not in (int, float):
                raise AssertionError("Coefficient was not an int or a float.")
        if type(p) != int:
                raise AssertionError("Power must be an int.")
        if p < 0:
                raise AssertionError("Power must be more than or equal to 0")
        if p in self.terms:
            if c == 0:
                del self.terms[p]
            else:
                self.terms[p] = self.terms[p] + c
                if self.terms[p] == 0:
                    del self.terms[p]
        if p not in self.terms and p != 0:
            self.terms[p] = c  
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Right must be a Poly, int, or a float")
        if type(right) in (int, float):
            self.terms[0] == right
        if type(right) == Poly:
            for each in right.terms:
                if each not in right.terms:
                    self.terms[each] = right.terms[each]
                else:
                    self.terms[each] = self.terms[each] + right.terms[each]
        alist = []
        for each in self.terms:
            alist.append((self.terms[each], each))
        atuple = tuple(alist)
        print(atuple)
        return eval ("Poly"+str(atuple))

    
    def __radd__(self,left):
         if type(left) not in (Poly, int, float):
            raise TypeError("Right must be a Poly, int, or a float")
        if type(left) in (int, float):
            self.terms[0] == right
        if type(left) == Poly:
            for each in left.terms:
                if each not in left.terms:
                    self.terms[each] = left.terms[each]
                else:
                    self.terms[each] = self.terms[each] + left.terms[each]
        alist = []
        for each in self.terms:
            alist.append((self.terms[each], each))
        atuple = tuple(alist)
        print(atuple)
        return eval ("Poly"+str(atuple))

    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("right must be a Poly")
        if type(right) == Poly:
            return self.term == right.terms
        else:
            if 0 in self.terms:
                self.terms[0] == right
        
        

    
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