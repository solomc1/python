class Poly:
    
    def __init__(self, *terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        #self.terms = {}
        self.terms = {j:i for i, j in terms if i != 0}
        
        if(not all(type(j) is int for i, j in terms) or not all(j >= 0 for i, j in terms)):
            raise AssertionError('Each power must be an int whose value is >= 0')
        if(not all(type(i) in (int, float) for i, j in terms)):
            raise AssertionError('Each coefficient must be an int or float value.')
        elif(not all(self.terms[j] == i for i, j in terms if i!=0)):
            raise AssertionError('A power cannot appear as a later term if it appears as an earlier term.')
        

        
        # Fill in the rest of this method, using *terms to intialize self.terms

            
    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. Notice that it assumes that
    #   every Poly object stores a dict whose keys are powers and whose
    #   associated values are coefficients. This function does not depend
    #   on any other method in this class being written correctly.   
    def __str__(self):
        def term(c, p, var):
            return (str(c) if p == 0 or c != 1 else '') + \
                   ('' if p == 0 else var + ('^' + str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c, p, 'x') for p, c in sorted(self.terms.items(), reverse=True)]).replace('+ -', '- ')
    
    def __repr__(self):
        nstring= []
        for i in self.terms:
            nstring.append('('+str(self.terms[i])+','+str(i)+')')
        return('Poly('+ ','.join(nstring)+')')

    
    def __len__(self):
        x = [y for y in self.terms]
        if(len(x)!=0):
            return(max(x))
        else:
            return 0
    
    def __call__(self, arg):
        answer = 0
        for i in self.terms:
            answer += self.terms[i]*(arg**i)
        return answer
    

    def __iter__(self):
        ntuples = []
        for i in self.terms:
            ntuples.append((self.terms[i], i))
        ntuples = sorted(ntuples, key = lambda x: x[1], reverse = True)
        return iter(ntuples)
            

    def __getitem__(self, index):
        if(type(index)!=int):
            raise TypeError("Index = "+str(index)+" must be an integer.")
        elif(index < 0):
            raise TypeError("Index = "+str(index)+" must be greater than 0.")
        else:
            try:
                return (self.terms[index])
            except:
                return 0
            

    def __setitem__(self, index, value):
        if(type(index)!=int):
            raise TypeError('The power argument='+str(index)+' must be an integer.')
        elif(index<0):
            raise TypeError('The power argument='+str(index)+' must be >= 0.')
        else:
            if(value == 0):
                try:
                    self.terms.pop(index)
                except:
                    pass
            else:
                self.terms[index]=value
            

    def __delitem__(self, index):
        if(type(index)!=int):
            raise TypeError('The power argument='+str(index)+' must be an integer.')
        elif(index<0):
            raise TypeError('The power argument='+str(index)+' must be >= 0.')
        else:
            try:
                self.terms.pop(index)
            except:
                pass
            
            

    def _add_term(self, c, p):
        if(type(p)!=int):
            raise TypeError('The power argument='+str(p)+' must be an integer.')
        elif(p<0):
            raise TypeError('The power argument='+str(p)+' must be >= 0.')
        elif(type(c) not in (int, float)):
            raise TypeError('The coefficient='+str(c)+' must be an integer or a float.')
        else:
            if(p not in list(self.terms) and c != 0):
                self.terms[p] = c
            elif(p in list(self.terms)):
                self.terms[p]+=c
                if(self.terms[p]==0):
                    self.terms.pop(p)
       

    def __add__(self, right):
        if(type(right) not in (Poly, int, float)):
            raise TypeError("The operand must be either a Polynomial, integer, or float.")
        elif(type(right)==Poly):
            answer = eval(repr(self))
            for t in right:
                answer._add_term(t[0], t[1])
            return answer
        elif(type(right) in (int, float)):
            answer = eval(repr(self))
            answer._add_term(right, 0)
            return answer

    
    def __radd__(self, left):
        if(type(left) not in (Poly, int, float)):
            raise TypeError("The operand must be either a Polynomial, integer, or float.")
        elif(type(left)==Poly):
            answer = eval(repr(self))
            for t in left:
                answer._add_term(t[0], t[1])
            return answer
        elif(type(left) in (int, float)):
            answer = eval(repr(self))
            answer._add_term(left, 0)
            return answer
    

    def __mul__(self, right):
        if(type(right) not in (Poly, int, float)):
            raise TypeError("The multiplicand must be either a Polynomial, integer, or float.")
        elif(type(right)==Poly):
            answer = eval(repr(self))
            test = Poly()
            for t in right:
                for y in answer:
                    test._add_term(t[0]*y[0], t[1]+y[1])
            return test
        elif(type(right) in (int, float)):
            answer = eval(repr(self))
            test = Poly()
            for y in answer:
                test._add_term(y[0]*right, y[1])
            return test
    

    def __rmul__(self, left):
        if(type(left) not in (Poly, int, float)):
            raise TypeError("The multiplicand must be either a Polynomial, integer, or float.")
        elif(type(left)==Poly):
            answer = eval(repr(self))
            test = Poly()
            for t in left:
                for y in answer:
                    test._add_term(t[0]*y[0], t[1]+y[1])
            return test
        elif(type(left) in (int, float)):
            answer = eval(repr(self))
            test = Poly()
            for y in answer:
                test._add_term(left*y[0], y[1])
            return test
    

    def __eq__(self, right):
        if(type(right) not in (Poly, int, float)):
            raise TypeError("The comparator must be either a Polynomial, integer, or float.")
        elif(type(right)==Poly):
            checker = True
            for t in self.terms:
                try:
                    if(right.terms[t]!= self.terms[t]):
                        checker = False
                except:
                    checker = False
            return checker
        
        elif(type(right) in (int, float)):
            if(len(self.terms)==1 and self.terms[0]==right):
                return True
            else:
                return False

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,0))
    p1 = Poly((3, 2), (-2, 1), (4, 0))
    
    print(p==3)



    
    
    
    #print('  For Polynomial: 3x^2 - 2x + 4')
    #print('  str(p):', p)
    #print('  repr(p):', repr(p))
    #print('  len(p):', len(p))
    #print('  p(2):', p(2))
    #print('  list collecting iterator results:', [t for t in p])
    #print('  p+p:', p + p)
    #print('  p+2:', p + 2)
    #print('  p*p:', p * p)
    #print('  p*2:', p * 2)
    #print('End simple tests\n')
    
    import driver
    # driver.default_show_exception=True
    # driver.default_show_exception_message=True
    # driver.default_show_traceback=True
    driver.driver()
