class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for tups in terms:
            if type(tups[0]) not in (int, float):
                raise AssertionError('The coefficient is not an int or a float value')
            elif tups[0] == 0:
                pass
            elif type(tups[1]) is not int or tups[1] < 0:
                raise AssertionError('The power is not a positive integer')
            elif tups[1] in self.terms.keys():
                raise AssertionError('That power is already in the dictionary')
            else:
                self.terms[tups[1]] = tups[0]
        
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
        return 'Poly('+','.join('('+str(self.terms[i])+','+str(i)+')' for i in self.terms.keys())+')'

    
    def __len__(self):
        power_list = []
        for power in self.terms.keys():
            power_list.append(power)
        if power_list == []:
            return 0
        else:
            return max(power_list)
    
    def __call__(self,arg):
        if type(arg) not in (int, float):
            raise AssertionError('Input value is not an int or a float')
        else:
            answer = 0
            for power in self.terms.keys():
                answer += self.terms[power]*(arg**power)
            return answer
    

    def __iter__(self):
        for power in sorted(self.terms.keys(), reverse = True):
            yield (self.terms[power], power)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('The index is not a positive integer')
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('The index is not a positive integer')
        elif value == 0:
            if value in self.terms.values():
                del self.terms[index]
            else:
                pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('The index is not a positive integer')
        elif index not in self.terms.keys():
            pass
        else:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError('The coefficient is not an int or float')
        elif type(p) is not int or p < 0:
            raise TypeError('The power is not a positive integer')
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            new_val = self.terms[p] + c
            if new_val == 0:
                del self.terms[p]
            else:
                self.terms[p] = new_val
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('The argument is not a valid type')
        elif type(right) is int or type(right) is float:
            new_poly = []
            for power in self.terms.keys():
                if power == 0:
                    new_poly.append((self.terms[power] + right, power))
                else:
                    new_poly.append((self.terms[power], power))
            new_terms = (i for i in new_poly)
            return Poly(*new_terms)
        else:
            new_poly = []
            for power in self.terms.keys():
                if power in right.terms.keys():
                    new_poly.append((self.terms[power] + right.terms[power], power))
                else:
                    new_poly.append((self.terms[power], power))
            new_terms = (i for i in new_poly)
            return Poly(*new_terms)

    
    def __radd__(self,left):
        if type(left) not in (int, float):
            raise TypeError('The argument is not a valid type')
        else:
            new_poly = []
            for power in self.terms.keys():
                if power == 0:
                    new_poly.append((self.terms[power] + left, power))
                else:
                    new_poly.append((self.terms[power], power))
            new_terms = (i for i in new_poly)
            return Poly(*new_terms)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('The second argument is not an int, float, or Poly type')
        elif type(right) is int or type(right) is float:
            new_poly = []
            for power in self.terms.keys():
                new_poly.append((self.terms[power]*right, power))
            new_terms = (i for i in new_poly)
            return Poly(*new_terms)
    

    def __rmul__(self,left):
        if type(left) not in (int, float):
            raise TypeError('Left argument is not an int or float')
        else:
            new_poly = []
            for power in self.terms.keys():
                new_poly.append((self.terms[power]*left, power))
            new_terms = (i for i in new_poly)
            return Poly(*new_terms)
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('The second argument is not a Poly, int, or float')
        elif type(right) is int or type(right) is float:
            if len(self.terms.keys()) == 1 and 0 in self.terms.keys():
                if self.terms[0] == right:
                    return True
                else: return False
            else: return False
        else:
            if self.terms.keys() == right.terms.keys():
                for power in self.terms.keys():
                    if self.terms[power] == right.terms[power]:
                        return True
                    else: return False
            else: return False

    
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