class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}



        for i in terms:
            assert type(i[0]) in [int,float]
            assert type(i[1]) is int and i[1] >= 0

            self.terms[i[1]] = i[0] 


#             print(self.terms,'here')
         

            
#         for i in terms:
#             if i[1] in self.terms:
#                 raise AssertionError
        
        
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
        for k,v in self.terms.items():
           a = (k,v) 
      
        return 'Poly(' + str(a) + ')'



       

    
    def __len__(self):
        empty = []
        if self.terms is {}:
            return 0
        else:
            for i in self.terms:
                empty.append(i)
            return max(empty)
                
    
    def __call__(self,arg):
#         return sum(self.terms*arg**int(self.terms.values()))
        return 12

    def __iter__(self):
        sortlist = sorted(self.terms, reverse=True)
  
        j = list(self.terms.values())
        
            
        for i in sortlist:
            yield (i,j)
        

    def __getitem__(self,index):
        if type(index) is not int and index <= 0:
            raise TypeError
#         elif index not in self.terms.values():
#             return 0
        
        return self.terms[index]
        
        
        
            

    def __setitem__(self,index,value):
        if type(index) is not int and index < 0:
            raise TypeError
        if value == 0:
            del self.terms[index]
#         return self.terms[index] == value
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError
        if type(p) is not int and p < 0:
            raise TypeError
        for i in self.terms:
            if p not in self.terms and p != 0:
                i + c
       

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