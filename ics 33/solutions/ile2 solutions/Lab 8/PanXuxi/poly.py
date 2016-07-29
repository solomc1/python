
class Poly:
      
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.p = terms
        for c, p in self.p:
            assert type(c) in [int, float], 'coefficient should be int and float'
            assert type(p) is int and p >= 0, 'power has be positive'
            self.terms[p]= c
         
        
               
              
          
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
        
        return "Poly(" + str(self.p)  + ')'
  
      
    def __len__(self):
        power = []
        for i in self.terms.keys():
            power.append(i)
        return max(power)
    
          
      
    def __call__(self,arg):
        result = []
        assert type(arg) in [int, float], "arg must be int or float"
        for x, y in self.terms.items():
            result.append(y* arg**x)
        return sum(result)
              
      
  
    def __iter__(self):
        
        new_terms = iter(self.p)
        for x, y in new_terms.items():
            result = (x,y)
        return result
              
  
    def __getitem__(self,index):
        if index is not int and index < 0:
            raise TypeError('index should be a positive integer')
        if index not in self.terms:
            return 0
        for i in self.terms.items():
            if index == i:
                result= self.terms[i]
        return result
          
          
              
              
  
    def __setitem__(self,index,value):
        if index is not int and index < 0:
            raise TypeError('index should be a positive integer')
        if value in self.terms.items():
            if value != 0:
                self.terms[index] = value
        return self.terms
        
                 
              
  
    def __delitem__(self,index):
        if index is not int and index<0:
            raise TypeError('Index should be a positive intefer')
        if index in self.terms:
            self.terms.pop(index)
            return self.terms
        else:
            return self.terms
             
             
              
  
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
#     print('  list collecting iterator results:',[t for t in p])
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