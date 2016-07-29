class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        self.sequence = terms
        for i, j in terms:
            assert type(i) in [int, float], '__init__: coefficient must be an int or float: ' + str(i)   
            assert type(j) is int and j >= 0, '__init__: power must be an int which >= 0: ' + str(j)
            if i != 0:
                if j not in self.terms:
                    self.terms[j] = i  
                else:
                    raise AssertionError('__init__: A power cannot appear twice: ' + str(j))
            else:
                pass
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
        return 'Poly(' + ','.join(['(' + str(self.terms[k]) + ',' + str(k) + ')' for k in self.terms]) +')'

    
    def __len__(self):
        return 0 if self.terms == {} else max(self.terms.keys())
    
    def __call__(self,arg):
        answer = 0
        for k, v in self.terms.items():
            answer += (arg**k) * v
        return answer
    

    def __iter__(self):
        for c, p in self.sequence:
            yield (c, p)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('__getitem__: the index must be an integer that is not negative: ' + str(index))
        return self.terms[index] if index in self.terms else 0    

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('__setitem__: the index must be an integer that is not negative: ' + str(index))
        if value != 0:
            self.terms[index] = value  
        else:
            if index in self.terms:
                del self.terms[index]    

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('__deltitem__: the index must be an integer that is not negative: ' + str(index))
        if index in self.terms:
            del self.terms[index]    
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('_add_term: the power must be an integer that is not negative: ' + str(p))
        if type(c) not in [int, float]:
            raise TypeError('_add_term: the coefficient must be an integer that is not negative: ' + str(c))
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]
        
            
    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('__add__: the right operand illegal: ' + str(right))
        if type(right) in [int, float]:
            answer = Poly()
            for k, v in self.terms.items():
                answer._add_term(v, k)
            if 0 in answer.terms:
                answer.terms[0] += right
            else:
                answer.terms[0] = right
        else:
            answer = Poly()
            for p, c in self.terms.items():
                for P, C in right.terms.items():
                    if p == P:
                        answer._add_term(c + C, p)
        return answer

    
    def __radd__(self,left):
        if type(left) not in [int, float]:
            raise TypeError('__radd__: the left operand illegal: ' + str(left))
        answer = Poly()
        for k, v in self.terms.items():
            answer._add_term(v, k)
        answer._add_term(left, 0)
        return answer
    

    def __mul__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('__mul__: the right operand illegal: ' + str(right))
        if type(right) in [float, int]:
            answer = Poly()
            for k, v in self.terms.items():
                answer.terms[k] = v * right
        if type(right) is Poly:
            answer = Poly()
            for k, v in self.terms.items():
                for K, V in right.terms.items():
                    answer._add_term(V * v, K + k)
        return answer
                

    def __rmul__(self,left):
        if type(left) not in [int, float]:
            raise TypeError('__rmul__: the left operand illegal: ' + str(left))
        answer = Poly()
        for k, v in self.terms.items():
            answer.terms[k] = v * left
        return answer
    

    def __eq__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('__eq__: the right operand illegal: ' + str(right))
        if type(right) in [int, float]:
            return len(self.terms) == 1 and right in self.terms.values()
        
        a = set(self.terms.keys()) == set(right.terms.keys()) 
        if type(right) is Poly:
            answer = []
            for k, v in self.terms.items():
                for K, V in right.terms.items():
                    if k == K:
                        answer.append(v == V)
                        break
        return a and all(answer)
    
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