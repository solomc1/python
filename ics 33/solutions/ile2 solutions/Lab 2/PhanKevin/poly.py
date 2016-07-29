class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
        self.terms = {}
        for value,key in terms:
            assert type(value) in [int,float],type(value) +' must be int or float'
            assert type(key) in [int], 'Power cannot be '+type(key)
            assert key >= 0, 'Power cannot be less than 0'
            assert key not in self.terms,'power of ' + str(key) +' cannot appear later if it already appeared earlier'
            if value == 0:
                continue
            self.terms[key] = value
        
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
        return 'Poly(' +', '.join(['('+str(value)+','+str(key)+')' for key,value in self.terms.items()])+')'

    
    def __len__(self):
        return (max(self.terms) if len(self.terms) > 0 else 0)
    
    def __call__(self,arg):
        if type(arg) not in [int,float]:
            return ValueError('Poly.__call__ '+ type(arg) +' must be int or float') 
        total = 0
        for key,value in self.terms.items():
            total_term = 0
            if key == 0:
                total_term = 1 
            else:
                total_term += arg**key
            total += value * total_term
        return total
                

    def __iter__(self):
        terms = self.terms
        for key,value in sorted(terms.items(),key = lambda x: x[0],reverse = True):
            yield (value,key)
            

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__getitem__:' +str(index) + 'must be an int')
        if index < 0:
            raise TypeError('Poly.__getitem__:' +str(index) + 'must be greater than 0')
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Poly.__setitem__: '+str(index)+ ' must be an integer')
        if index < 0:
            raise TypeError('Poly.__setitem__: '+str(index)+ ' must be greater than 0')
        if value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__delitem__: '+str(index)+ ' must be an integer')
        if index < 0:
            raise TypeError('Poly.__delitem__: '+str(index)+ ' must be greater than 0')
 
        if index in self.terms.keys():
            del self.terms[index]    

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError(str(c) +' must be an int or float')
        if type(p) is not int:
            raise TypeError('Poly._add_term: '+str(p)+ ' must be an integer')
        if p < 0:
            raise TypeError('Poly._add_term__: '+str(p)+ ' must be greater than 0')
        if p not in self.terms.keys() and p != 0:
            self.terms[p] = c
        if p in self.terms.keys():
            self.terms[p] += c
        else:
            del self.terms[p]
          
       

    def __add__(self,right):
        add_poly = []
        if type(right) is Poly:
            
            for key in self.terms:
                for ikey in right:
                    if key == ikey:
                        self.terms[key] += right[ikey]
                        add_poly.append(key,self.terms[key])
            

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        if type(right) is Poly:
            for key,value in self.terms.items():
                for ikey in right.terms:
                    if key == ikey:
                        
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [int,float]:
            raise TypeError('Poly.__eq__: '+str(right)+' must be an int or float')
        if type(right) in [int,float]:
            return right in self.terms
        if type(right) is Poly:
            check = [poly1 == poly2 for poly1 in self.terms for poly2 in right.terms]
            return check  

    
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
    
    x = {3:"y",2:'x'}
    del x[3]
    print(x)
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()