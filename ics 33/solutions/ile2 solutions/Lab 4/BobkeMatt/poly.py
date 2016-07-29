class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        
        for term in terms:
            assert type(term[0]) in [int, float], 'coefficient must be an int or float'
            assert type(term[1]) == int and term[1] >= 0, 'powers must be ints greater than or equal to zero'
            assert term[1] not in self.terms.keys(), 'cannot have two of the same power'
            
            if term[0] == 0:
                pass
            else:
                self.terms[term[1]] = term[0]
            
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
        arg_list = [(y,x) for x,y in self.terms.items()]
        
        return 'Poly({})'.format(",".join(str(item) for item in arg_list))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) in [int, float], 'argument must be an int or float'
        
        result = 0
        for item in self.terms.items():
            result += item[1] * (arg ** item[0])
            
        return result
    

    def __iter__(self):
        
        class Poly_iter:
            def __init__(self, item_dict):
                self.item_list = [(y,x) for x,y in item_dict.items()]
                self.nums = sorted(self.item_list, key = lambda x: x[1], reverse = True)
                self.count = 0
                
            def __next__(self):
                
                if self.count >= len(self.nums):
                    
                    raise StopIteration
                
                else:
                    
                    result = self.nums[self.count]
                    self.count += 1
                    return result
        
        return Poly_iter(self.terms)

    def __getitem__(self,index):
        
        if type(index) != int or index < 0:
            raise TypeError('index must be an int greater than or equal to zero')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        
        if type(index) != int or index < 0:
            raise TypeError('power must be an int greater than or equal to zero')
        elif value == 0:
            try:
                removed = self.terms.pop(index)
            except:
                pass
        else:
            self.terms[index]=value
            

    def __delitem__(self,index):
        
        if type(index) != int or index < 0:
            raise TypeError('power must be an int greater than or equal to zero')
        elif index in self.terms.keys():
            removed = self.terms.pop(index)
            

    def _add_term(self,c,p):
        
        if type(c) not in [int, float]:
            raise TypeError('coefficient must be an int or float')
        elif type(p) != int or p < 0:
            raise TypeError('power must be an int greater than or equal to zero')
        else:
            
            if p not in self.terms.keys() and c != 0:
                
                self.terms[p] = c
                
            elif p in self.terms.keys():
                
                self.terms[p] += c
                
                if self.terms[p] == 0:
                    self.__delitem__(p)
       

    def __add__(self,right):
        
        if type(right) not in [int, float, Poly]:
            raise TypeError('operator must be an int, float, or Poly')
        elif type(right) in [int, float]:
            
            new_poly = Poly()
            for term in self:
                new_poly._add_term(term[0], term[1])
            
            new_poly._add_term(right, 0)
            
            return new_poly
        
        else:
            
            new_poly = Poly()
            for term in self:
                new_poly._add_term(term[0], term[1])
            
            for term in right:
                new_poly._add_term(term[0], term[1])
                
            return new_poly

    
    def __radd__(self,left):
        
        return self + left
    

    def __mul__(self,right):
        
        if type(right) not in [int, float, Poly]:
            raise TypeError('operator must be an int, float, or Poly')
        elif type(right) in [int, float]:
            
            new_poly = Poly()
            
            for p,c in self.terms.items():
                
                new_poly._add_term(c * right, p)
            
            return new_poly
        
        else:
            
            new_poly = Poly()
            
            for p1,c1 in self.terms.items():
                for p2,c2 in right.terms.items():
                    
                    new_poly._add_term(c1*c2, p1+p2)
            
            return new_poly
    

    def __rmul__(self,left):
        
        return self * left
    

    def __eq__(self,right):
        
        if type(right) not in [int, float, Poly]:
            raise TypeError('operator must be an int, float, or Poly')
        
        elif type(right) == Poly:
            
            if sorted(self.terms.keys()) != sorted(right.terms.keys()):
                return False
            
            elif sorted(self.terms.values()) != sorted(right.terms.values()):
                return False
            
            return True
        
        else:
            
            new_poly = Poly()
            
            new_poly._add_term(right, 0)
            
            return self.terms == new_poly.terms

    
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