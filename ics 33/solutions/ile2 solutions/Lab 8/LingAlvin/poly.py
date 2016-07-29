class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[1] == int)
            assert type(i[0]) == int or type(i[0]) == float
            assert i[1] >=0 and type(i[1]) == int 
            if i[0] == 0:
                pass
            else:
                assert i[1] not in self.terms
                self.terms[i[1]] = i[0]

        
        
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
        resultstr = ''
        for k, v in self.terms.items():
            resultstr += '(' + str(v) +',' + str(k) + '),'
        return 'Poly(' + resultstr.strip(',') + ')'  

    
    def __len__(self):
        if len(self.terms) != 0:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        result = 0
        for p,c in self.terms.items():
            result += c * (arg**p)
        return result 
    

    def __iter__(self):
        for k, v in sorted(self.terms.items(), key = lambda x: x[0], reverse = True):
            yield tuple((v, k)) 


    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError
        elif value == 0 and index in self.terms:
            del self.terms[index]
        elif value == 0 and index not in self.terms:
            pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        elif index in self.terms:
            del self.terms[index]
        elif index not in self.terms:
            pass 
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError
        elif type(p) != int and p >=0 == False:
            raise TypeError
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]
        
       

    def __add__(self,right):
        result = Poly()
        if type(right) != float and type(right) != int and type(right) != Poly:
            raise TypeError
        if type(right) == int or type(right) == float:
            for p,c in self.terms.items():
                Poly._add_term(result, c, p)
                Poly._add_term(result, right, 0)
        elif type(right) == Poly:
            for p,c in self.terms.items():
                Poly._add_term(result, c, p)
            for p2, c2 in right.terms.items():
                Poly._add_term(result, c2, p2)
        return result
            
            
    
    def __radd__(self,left):
        result = Poly()
        if type(left) != float and type(left) != int and type(left) != Poly:
            raise TypeError
        if type(left) == int or type(left) == float:
            for p,c in self.terms.items():
                Poly._add_term(result, c, p)
                Poly._add_term(result, left, 0)
        elif type(left) == Poly:
            for p,c in self.terms.items():
                Poly._add_term(result, c, p)
            for p2, c2 in left.terms.items():
                Poly._add_term(result, c2, p2)
        return result
    

    def __mul__(self,right):
        result = Poly()
        if type(right) != float and type(right) != int and type(right) != Poly:
            raise TypeError
        if type(right) == int or type(right) == float:
            for p,c in self.terms.items():
                Poly._add_term(result, right * self.terms[p], p)
                Poly._add_term(result, self.terms[0] * right, 0)      
        else:
            pass
        return result
            
    

    def __rmul__(self,left):
        result = Poly()
        if type(left) != float and type(left) != int and type(left) != Poly:
            raise TypeError
        if type(left) == int or type(left) == float:
            for p,c in self.terms.items():
                Poly._add_term(result, left * self.terms[p], p)
                Poly._add_term(result, self.terms[0] * left, 0)      
        else:
            pass
        return result
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != int:
            raise TypeError
        if type(right) == Poly:
            for k,v, in self.terms.items():
                if k not in right.terms:
                    return False
                elif k in right.terms:
                    if self.terms[k] != right.terms[k]:
                        return False
        elif type(right) == int or type(right) == float:
            if 0 in self.terms:
                return self.terms[0] == right
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