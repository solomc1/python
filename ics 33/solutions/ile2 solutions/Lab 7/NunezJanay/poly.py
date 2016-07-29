class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            #print(type(c))
            assert type(c) in [int,float] and type(p) is int,"The coefficent must be a numeric value"
            assert p >= 0, "The power cannot be a negative number"
            assert p not in self.terms, "You cannot have terms with the same power"
            if c != 0:
                self.terms[p] = c
        #print(self.terms)
        
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
        return "Poly({})".format(",".join("(%s,%s)" % (v,k) for k,v in self.terms.items()).rstrip(','))
    
    def __len__(self):
        if len(self.terms) > 0:
            return max([p for p in self.terms.keys()])
        else:
            return 0
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += (v*(arg**k))
        return total
    

    def __iter__(self):
        for k,v in sorted(self.terms.items(), reverse = True):
            yield v,k
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Index must be a numeric value greater than 0")
        elif index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Index must be a numeric value greater than 0")
        if value == 0:
            if value in self.terms.items():
                del self.terms[index]
        self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Index must be a numeric value greater than 0")
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in [int,float] and type(p) != int and p < 0:
            raise TypeError("Power must be a numeric value greater than 0")
        if p not in self.terms and c != 0:
            self.terms[p] = c
        else:
            list = [(k,v) for k,v in self.terms.items()]
            for k,v in list:
                if p == k:
                    total = v+c
                    if total == 0:
                        del self.terms[k]
                    else:
                        self.terms[k] = total
        
       

    def __add__(self,right):
        if type(self) != Poly or type(right) not in [int,float,Poly]:
            raise TypeError("Operand must be a numeric value or Poly object")
        if type(right) in [int,float]:
            empty = Poly(right,0)
        else:
            empty = Poly()   
        for k,v in self.terms.items():
            empty._add_term(v,k)
        for k,v in right.terms.items():
            empty._add_term(v,k)
        print(empty)
        return empty

    
    def __radd__(self,left):
        empty = Poly()
        if type(self) != Poly or type(left) not in [int,float,Poly]:
            raise TypeError("Operand must be a numeric value or Poly object")
        if type(left) in [int,float]:
            empty._add_term(left,0)
        else:               
            for k,v in left.terms.items():
                empty._add_term(v,k) 
        for k,v in self.terms.items():
            empty._add_term(v,k)
        
        print(empty)
        return empty

    def __mul__(self,right):
        if type(self) != Poly or type(right) not in [int,float,Poly]:
            raise TypeError("Operand must be a numeric value or Poly object")
        empty = Poly()
#         for k,v in self.terms.items():
#             empty.terms[k] = v
#         print(empty)
        for k,v in self.terms.items():
            for p,c in right.terms.items():
                empty.terms[k*p] = v*c
        return empty
#         for c,p in right.terms.items():
#             if p in empty.terms:
#                 #empty = 
    

    def __rmul__(self,left):
         if type(self) != Poly or type(right) not in [int,float,Poly]:
            raise TypeError("Operand must be a numeric value or Poly object")
    

    def __eq__(self,right):
        if type(self) != Poly or type(right) not in [int,float,Poly]:
            raise TypeError("Operand must be a numeric value or Poly object")
        if type(right) == Poly and type(self) == Poly:
            return all(i == p for i in sorted(self.terms.items()) for p in sorted(right.terms.items()))
        elif type(right) in [int,float]:
            if right in self.terms.values():
                return True
            else:
                return False
        elif type(self) in [int,float]:
            if self in self.terms.values():
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