class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {item[0] : item[1] for item in terms}
        
#         assert type(self.terms[item[0]]) in ['int','float'], '__init__.' + str(self.terms[item[0]]) + ': Not an int or a float'
#         assert type(self.terms[item[0]]) is 'int', '__init__.' + str(self.terms[item[0]]) + ': Must be an int'
#         assert self.terms[item[0]] >= 0, '__init__.' +str(self.terms[item[0]]) + ': power must be greater than or equal to 0'
#         

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
        ans = []
        for c,p in self.terms.items():
            p_item = (c,p)
            ans.append(p_item)
        return 'Poly(' + str(ans) + ')'
        

    
    def __len__(self):
        for v in self.terms.values():
            return v
    
    def __call__(self,arg):
        poly_ans = 0
        for c,p in self.terms.items():
            answer = c * (p^arg)
            return answer + poly_ans
    

    def __iter__(self):
        next_item = next(iter(self.terms.items()))
        for item in self.terms.items():
            yield item
            

    def __getitem__(self,index):
        if type(index) is not 'int':
            raise TypeError('__getitem__('+str(index)+'): Must be an int')
        if index < 0:
            raise TypeError('__getitem('+str(index)+'): Must be greater than 0')
        return self.terms[index]
              

    def __setitem__(self,index,value):
        if type(index) is not 'int':
            raise TypeError('__setitem__('+str(index)+'): Must be an int')
        if value < 0:
            raise TypeError('__setitem-_('+str(value)+'): Must be greater than 0')
        if index == 0:
            del[self.terms[index]]
              

    def __delitem__(self,index):
        if type(index) is not 'int':
            raise TypeError('__delitem__('+str(index)+'): Must be an int')
        if index < 0:
            raise TypeError('__delitem__('+str(index)+'): Must be greater than 0')
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in ['int', 'float']:
            raise TypeError('_add_term(:'+str(c)+'): Must be an int or a float')
        if type(p) !='int' and p < 0:
            raise TypeError('_add_term(:'+str(p)+'): Must be an int greater than or equal to 0')
        if p not in self.terms.values() and p != 0:
            self.terms[c] = p
        if p in self.terms.values():
            self.terms[p] 
            

    def __add__(self,right):
        calc = []
        for c,p in self.terms.items():
            for co, power in right.terms.items():
                if p == power:
                    new_c = c + co
                    calc.append(str(new_c) + 'x^' + str(p))
        
        for item in calc:
            return str(item) + '+'
                
    
    def __radd__(self,left):
        for c,p in self.terms.items():
            for co, power in left.terms.items():
                if p == power:
                    new_c = c + co
                    return (new_c, p)
                    
    

    def __mul__(self,right):
        for c,p in self.terms.items():
            for co, power in right.terms.items():
                return (c*co,p+power)
    

    def __rmul__(self,left):
        for c,p in self.terms.items():
            for co,power in left.terms.items():
                return(c*co,p+power)
    

    def __eq__(self,right):
        if type(right) not in ['int','float','Poly']:
            raise TypeError('__eq__('+str(right)+'): Must be an int, float, or Poly object')
        eq_list = []
        for c,p in self.terms.items():
            for co,power in right.terms.items():
                if c == co and p == power:
                    eq_list.append(True)
                else:
                    eq_list.append(False)
                    
        if False in eq_list:
            return False
        else:
            return True

    
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
    
    #import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    #driver.driver()