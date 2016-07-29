class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if type(i[0]) != int and type(i[0]) != float:
                raise AssertionError('Error')
            elif type(i[1]) != int:
                raise AssertionError('Error')
            elif i[1]<0:
                raise AssertionError('Error')
            elif i[0] == 0:
                pass
            elif i[1] in self.terms:
                raise AssertionError('Error')
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
        if self.terms == {}:
            return 'Poly()'
        else:
            result = 'Poly('
            for i in self.terms:
                result += '('+str(self.terms[i])+','+str(i)+')'+','
                return result[:-1] + ')'

    
    def __len__(self):
        list = []
        for i in self.terms:
            list.append(i)
        return max(list)
            
    
    def __call__(self,arg):
        result = 0
        for i in self.terms:
            sum = 1
            for j in range(i):
                sum *= i
            sum *= self.terms[i]
            result += sum
        return result
    

    def __iter__(self):
        for i in self.terms:
            yield (i,self.terms[i])
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Error')
        if index < 0:
            raise TypeError('Error')
        if index not in self.terms:
            return 0
        else:
            for i in self.terms:
                if self.terms[i] == 0:
                    del self.terms[i]
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Error')
        if index < 0:
            raise TypeError('Error')
        if index not in self.terms and value == 0:
            pass
        else:
            self.terms[index] = value
            for i in self.terms:
                if self.terms[i] == 0:
                    del self.terms[i]
        pass
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Error')
        if index < 0:
            raise TypeError('Error')
        if index not in self.terms:
            raise TypeError
        else:
            del self.terms[index]
        
            

    def _add_term(self,c,p):
        if type(c) != int and type(c)!= float:
            raise TypeError
        if type(p) !=int:
            raise TypeError
        if p < 0:
            raise TypeError
        if p in self.terms:
            self.terms[p] += c
        else:
            self.terms[p] = c
       

    def __add__(self,right):
        terms1 = self.terms
        if type(right) == int:
            terms1[0] += right
            result = Poly()
            for i in terms1:
                result._add_term(terms1[i],i)
        if type(right) == Poly:
            terms2 = right.terms
            for i in terms2:
                if i in self.terms:
                    terms1[i] += terms2[i]
                else:
                    terms1[i] = terms2[i]
            result = Poly()
            for i in terms1:
                result._add_term(terms1[i],i)
        return result

    
    def __radd__(self,left):
        terms1 = self.terms
        if type(left) == int:
            terms1[0] += left
            result = Poly()
            for i in terms1:
                result._add_term(terms1[i],i)
        return result
        
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            TF = True
            if self.terms == right.terms:
                for i in self.terms:
                    if self.terms[i] != right.terms[i]:
                        TF = False
                        return TF
            else:
                return False
        elif type(right) == int:
            return self.terms == {0:right}

    
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