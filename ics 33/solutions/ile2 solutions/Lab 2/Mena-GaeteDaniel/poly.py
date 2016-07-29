from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for c,p in terms:
            if type(c) not in (int, float):
                raise AssertionError('Poly.__init__: c({}) is not int or float ({})'.format(c, type_as_str(c)))
            if type(p) is not int:
                raise AssertionError('Poly.__init__: p({}) is not int({})'.format(p, type_as_str(p)))
            if p < 0:
                raise AssertionError('Poly.__init__: p({}) must be zero or positive'.format(p))
            if p in self.terms:
                raise AssertionError('Poly.__init__: p({}) has already been specified'.format(p))
            elif c != 0:
                self.terms[p] = c
        
        
            
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
        param = []
        for p,c in self.terms.items():
            param.append((c,p))
        param = str(param)[1:-1]
        return 'Poly({})'.format(param)

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            max = -1
            for p,c in self.terms.items():
                if p > max:
                    max = p
            return p
    
    def __call__(self,arg):
        sum = 0
        for p,c in self.terms.items():
            sum += c*(arg**p)
        return sum

    def __iter__(self):
        for p,c in sorted(self.terms.items(), reverse=True):
            yield (c,p)

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__getitem__:index({}) is not int({})'.format(index, type_as_str(index)))
        if index < 0:
            raise TypeError('Poly.__getitem__:index({}) must be greater or equal to 0'.format(index))
        for p,c in self.terms.items():
            if p == index:
                return c
        return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('Poly.__setitem__:index({}) is not int({})'.format(index, type_as_str(index)))
        if index < 0:
            raise TypeError('Poly.__setitem__:index({}) must be greater or equal to 0'.format(index))       
        if index in self.terms:
            if value != 0:
                self.terms[index] = value
            else:
                del self.terms[index]
        else:
            if value != 0:
                self.terms[index] = value
            else:
                pass
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('Poly.__delitem__:index({}) is not int({})'.format(index, type_as_str(index)))
        if index < 0:
            raise TypeError('Poly.__delitem__:index({}) must be greater or equal to 0'.format(index))       
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(p) is not int:
            raise TypeError('Poly._add_term: p({}) is not int({})'.format(p, type_as_str(p)))
        if p < 0:
            raise TypeError('Poly._add_term: p({}) must be greater or equal to 0'.format(p)) 
        if type(c) not in (int, float):
            raise TypeError('Poly._add_term: c({}) must be int or float ({})'.format(c, type_as_str(c)))
        if p not in self.terms:
            if c != 0:
                self.terms[p] = c
        else:
            newC = self.terms[p] + c
            if newC != 0:
                self.terms[p] = newC
            else:
                del self.terms[p]
            

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__add__: right({}) must be int, float, or Poly ({})'.format(right, type_as_str(right)))
        
        if type(right) in (int, float):
            right = Poly((right, 0))
        
        selfParam = []
        for p,c in self.terms.items():
            selfParam.append((c,p))
        
        rightParam = []
        for p,c in right.terms.items():
            rightParam.append((c,p))
        
        paramFinal = []
        for p,c in self.terms.items():
            if p in right.terms:
                paramFinal.append( (self.terms[p]+right.terms[p], p) )
            else:
                paramFinal.append( (self.terms[p],p) )
                
        for p,c in right.terms.items():
            if p not in self.terms:
                paramFinal.append( (right.terms[p],p) )
                
        paramFinal = str(paramFinal)[1:-1]
        #print(selfParam)
        return eval('Poly({})'.format(paramFinal))
        
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__: right({}) must be int, float, or Poly ({})'.format(right, type_as_str(right)))
        if type(right) in (int, float):
            if len(self.terms) == 1:
                for p,c in self.terms.items():
                    if p == 0:
                        return c == right
                    else:
                        return False
            else:
                return False
        else:
            if len(self.terms) == len(right.terms):
                for p,c in self.terms.items():
                    if p in right.terms:
                        if self.terms[p] != right.terms[p]:
                            return False
                    else:
                        return False
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