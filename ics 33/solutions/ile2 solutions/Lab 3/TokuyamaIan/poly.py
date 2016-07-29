class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
#             print(self.terms.keys())
#             print(t[1])
#             assert t[1] in list(self.terms.keys()), 'power cannot be repeated'
            self.terms[t[1]] = t[0]
            assert type(t[0]) in [int, float], 'coefficient is not a numeric'
            assert type(t[1]) is int, 'power is not an integer'
            assert t[1] >= 0, 'power cannot be a negative number'
            
            
        
        
        
        
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
        print(self.repr_helper())
        l = []
        for a in self.repr_helper():
            l.append(a)
#         k,v = k,v in list(self.terms)
        return 'Poly(' + str(l) + ')'
    
    def repr_helper(self):
        l = []
        for x in list(self.terms.items()):
#             print('asdf')
#             print(x)
            l.append(x)
#             l.append(x)
        return l

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            num_list = []
            for t in self.terms.keys():
                num_list.append(t)
            return max(num_list)
    
    def __call__(self,arg):
        co = []
        power = []
        for x in self.terms.keys():
            power.append(x)
        for x in self.terms.values():
            co.append(x)
        power.sort(reverse = True)
        co.reverse()
        
        print(co)
        print(power)
        
        total = 0
        
        for x in range(len(co)):
            total += co[x]*(arg^power[x])
        return total
    

    def __iter__(self):
        power = list(self.terms.keys())
        power.reverse()
        for x in range(len(self.terms.keys())):
            print(self.terms[x], power[x])
            

    def __getitem__(self,index):
        pass
            

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
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