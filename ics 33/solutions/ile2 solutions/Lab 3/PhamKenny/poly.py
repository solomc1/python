# Kenny Pham, Lab 3

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for args in terms:
            if args[0] == 0:
                pass
            elif args[1] in self.terms.keys():
                raise AssertionError
            elif type(args[0]) == float and type(args[1]) == float:
                self.terms[args[1]] = args[0]
            elif type(args[0]) == int and type(args[1]) == int:
                self.terms[args[1]] = args[0]
                
            else:
                raise AssertionError("Poly.__init__: illegal power in:", args)
            
        
        
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
        result = []
        
        for k,v in self.terms.items():
            result.append((v,k))
            
        return 'Poly' + str(tuple(result))

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result = 0
        
        if type(arg) == int or type(arg) == float:
            for k,v in self.terms.items():
                result += v * (arg**(k))
                
            return result
        
        
    

    def __iter__(self):
        for arg in self.terms.items():
            yield (arg[0],arg[1])
            

    def __getitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if index < 0 or type(index) != int:
            raise TypeError
        
        elif value == 0:
            self.terms.pop(index)

        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
            
        elif p in self.terms.keys():
            if self.terms[p] + c != 0:
                self.terms[p] = self.terms[p] + c
            elif self.terms[p] + c == 0:
                self.terms.pop(p)
       

    def __add__(self,right):
        newPoly = Poly()
        
        for k, v in self.terms.items():
            newPoly._add_term(v, k)
            
        if type(right) == int or type(right) == float:
            newPoly._add_term(right, 0)
            
        else:
            for k,v in right.terms.items():
                newPoly._add_term(v,k)
        
        return newPoly
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        newPoly = Poly()
        if type(right) == int or type(right) == float:
            for p,c in self.terms.items():
                newPoly._add_term(c*right, p)
            return newPoly
            
        else:
            for p,c in self.terms.items():
                for p2, c2 in right.terms.items():
                    newPoly._add_term(c*c2, p+p2)
                
                
                
            return newPoly
                
    

    def __rmul__(self,left):
        return self * left
    

    def __eq__(self,right):
        if type(right) == int or type(right) == float:
            for p,c in self.terms.items():
                if c == right:
                    return True
                else:
                    return False
            
        else:
            raise TypeError
                

    
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