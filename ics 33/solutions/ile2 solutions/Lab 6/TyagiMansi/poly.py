class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.t = terms
        for i in self.t:
            if type(i[0]) not in (int,float) or type(i[1]) != int:
                raise AssertionError('coefficients must be int or float objects')
            elif i[0] == 0:
                del i
            elif i[1] < 0:
                raise AssertionError('power must be greater than or equal to 0')
            elif type(i[1]) !=int:
                raise AssertionError('power must be int greater than or equal to 0')            
            elif i[1] in self.terms.keys():
                if i[0] != 0:
                    raise AssertionError('there can only be one power of'+str(i[1]))
            elif i[1] not in self.terms.keys():
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
        return 'Poly'+str(self.t)

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            result = []
            for k in self.terms.keys():
                result.append(k)
            return max(result)
        
    
    def __call__(self,arg):
        term = self.__str__().replace('x','*2')
        return eval(term)
    

    def __iter__(self):
        i = iter(self.terms)
        return i

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('index must be int object')
        elif index < 0:
            raise TypeError('index must be greater than or equal to 0')
        else:
            if index not in self.terms.keys():
                return 0
            elif index in self.terms.keys():
                return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('power must be int object')
        elif index < 0:
            raise TypeError('power must be greater than or equal to 0')
        elif value == 0:
            del self.terms[index]
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        pass
            
    #helpermethod
    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError('power must be int object')
        elif p < 0:
            raise TypeError('power must be greater than or equal to 0')
        elif type(c) not in (int, float):
            raise TypeError('coefficient must be int or float object')
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        
       

    def __add__(self,right):
        new_dict = {}
        if type(self) not in (int,float,Poly) or type(right) not in (int,float,Poly):
            raise TypeError('must be int or float object or Poly')
        elif type(self) == Poly:
            if type(right) == Poly:
                for i in self.terms:
                    if i in right.terms:
                        new_dict[i] = self.terms[i] + right.terms[i]
                    else:
                        new_dict[i] = self.terms[i]
        elif type(self) in (int,float):
            pass
        return new_dict
                
    def __radd__(self,left):
        new_dict = {}
        if type(self) not in (int,float,Poly) or type(left) not in (int,float,Poly):
            raise TypeError('must be int or float object or Poly')
        elif type(self) == Poly:
            if type(left) == Poly:
                for i in self.terms:
                    if i in left.terms:
                        new_dict[i] = self.terms[i] + left.terms[i]
                    else:
                        new_dict[i] = left.terms[i]
        elif type(self) in (int,float):
            if type(left) == Poly:
                pass
        return new_dict  

    def __mul__(self,right):
        if type(self) not in (int,float,Poly) or type(right) not in (int,float,Poly):
            raise TypeError('must be int or float object or Poly')
        elif type(self) == Poly:
            if type(right) == Poly:
                pass
            else:
                pass    
        elif type(self) in (int,float):
            if type(right) == Poly:
                pass
            else:
                pass
            
    def __rmul__(self,left):
        if type(self) not in (int,float,Poly) or type(left) not in (int,float,Poly):
            raise TypeError('must be int or float object or Poly')
        elif type(self) == Poly:
            if type(left) == Poly:
                pass
            else:
                pass
        elif type(self) in (int,float):
            if type(left) == Poly:
                pass
            else:
                pass
            
    def __eq__(self,right):
        if type(self) not in (int,float,Poly) or type(right) not in (int,float,Poly):
            raise TypeError('must be int or float object or Poly')
        elif type(self) == Poly:
            if type(right) == Poly:
                return self.terms == right.terms
            else:
                return self.terms == right
        elif type(self) in (int,float):
            if type(right) == Poly:
                return self == right.terms
            else:
                return self == right

    
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