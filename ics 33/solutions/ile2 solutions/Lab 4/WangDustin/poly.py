class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[1]) != int or i[1] < 0:
                raise AssertionError("Error, power must be an int")
            if i[1] in self.terms:
                raise AssertionError("Error, power already in dictionary")
            if type(i[0]) != int:
                if type(i[0]) != float:
                    raise AssertionError("Error, coefficient must be an int or float")
            if i[0] == 0:
                pass
            else:
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
        repr_str = "Poly("
        counter = 0
        for i in self.terms:
            counter += 1
            if counter == len(self.terms):
                repr_str  += "(" +str(self.terms[i])+','+str(i)+')'
            else:
                repr_str += "(" +str(self.terms[i])+','+str(i)+'),'
        return repr_str + ')'

    
    def __len__(self):
        try:
            result = max([i for i in self.terms])
        except ValueError:
            return 0
        else:
            return result
    
    def __call__(self,arg):
        answer = 0
        for i in self.terms:
            if i == 0:
                answer += self.terms[i] 
            else:
                answer += (arg**i)*self.terms[i]
        return answer
    
    def __iter__(self):
        for i in sorted(self.terms, key=None, reverse = True):
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        blank = 0
        if type(index) != int or index < 0:
            raise TypeError("Error, index is not an integer or is less than zero")
        for i in self.terms:
            if index == i:
                blank = self.terms[i]
        return blank
                
    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Error, index is not an integer or is less than zero")
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            
    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Error, index is not an integer or is less than zero") 
        if index in self.terms:
            del self.terms[index]
            
    def _add_term(self,c,p):
        if type(c) != int:
            if type(c) != float:
                raise TypeError ("Coefficient must be an int or a float")
        if type(p) != int or p<0:
            raise TypeError ("Power must be an int and greater or equal to 0")
        elif p in self.terms:
            self.terms[p] = self.terms[p]+ c
            if self.terms[p] == 0:
                del self.terms[p]
        else:
            if c != 0:
                self.terms[p] = c
        
    def __add__(self,right):
        new_poly = Poly()
        if type(right) == type(self):
            for i in self.terms:
                new_poly._add_term(self.terms[i],i)
            for i in right.terms:
                if i not in new_poly.terms:
                    new_poly.terms[i] = right.terms[i]
                else:
                    new_poly.terms[i] += right.terms[i]
            return new_poly
        elif type(right) == int or type(right) == float:
            for i in self.terms:
                new_poly._add_term(self.terms[i], i)
            new_poly.terms[0] += right
            return new_poly
        else:
            raise TypeError("Operands are not int/float or Poly")
        
    def __radd__(self,left):
        new_poly = Poly()
        if type(self) == type(left):
            for i in self.terms:
                new_poly._add_term(self.terms[i],i)
            for i in left.terms:
                if i not in new_poly.terms:
                    new_poly.terms[i] = left.terms[i]
                else:
                    new_poly.terms[i] += left.terms[i]
            return new_poly
        elif type(left) == int or type(left) == float:
            for i in self.terms:
                new_poly._add_term(self.terms[i], i)
            new_poly.terms[0] += left
            return new_poly
        else:
            raise TypeError("Operands are not int/float or Poly")

    def __mul__(self,right):
        new_poly = Poly()
        if type(right) == type(self): 
            for i in self.terms:
                new_poly._add_term(self.terms[i],i)
            for i in right.terms:
                for x in self.terms:
                    if i+x not in new_poly.terms:
                        new_poly.terms[i+x] = self.terms[x] 
                    else:
                        new_poly.terms[i+x]* right.terms[x]
            return new_poly

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == type(self):
            for i in self.terms:
                if i not in right.terms:
                    return False
                if self.terms[i] != right.terms[i]:
                    return False
            return True
        elif type(right) == int or type(right) == float:
            if len(self.terms)>1:
                return False
            else:
                if self.terms[0] != right:
                    return False
                else:
                    return True
        else:
            raise TypeError("Operand neither poly or int/float")
    
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