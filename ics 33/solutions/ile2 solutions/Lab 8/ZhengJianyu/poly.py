class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {b: a for a,b in terms if a!= 0}
        for i in self.terms:
            assert type(self.terms[i]) == int or type(self.terms[i]) == float, 'The coefficient must be int or float'
            assert type(i) == int and i >= 0, 'The power must be an int whose value is >= 0'
        assert len([b for a,b in terms if a!= 0]) == len(list(set([b for a,b in terms if a!= 0]))),'Each power can only show up once.'
            
            
#             if self.terms[i] != 0:
#                 count = 0
#                 for x in self.terms:
#                     if x == i:
#                         count += 1
#                 assert count <= 1, 'Each power can only show up once.'

        
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
        result = ''
        for i in self.terms:
            if self.terms[i] != 0:
                result += '('+str(self.terms[i])+','+str(i)+'),'
        return 'Poly('+result[:-1]+')'
    

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        return max([i for i in self.terms.keys()])
    
    def __call__(self,arg):
        count = 0
        for i in self.terms:
            count += self.terms[i] * arg ** i
        return count
    

    def __iter__(self):
        result = [(self.terms[i], i) for i in self.terms]
        result.reverse()
        for i in result:
            yield i
        
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('The index should be integer')
        if index < 0:
            raise TypeError('The index should be less than 0')
        if index in [i for i in self.terms.keys()]:
            for i in self.terms:
                if index == i:
                    return self.terms[i]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('The index should be integer')
        if index < 0:
            raise TypeError('The index should be less than 0')
        if value != 0:
            self.terms[index] = value
        elif index in self.terms.keys():
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('The index should be integer')
        if index < 0:
            raise TypeError('The index should be less than 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not type(c) == int or type(c) == float:
            raise TypeError('The coefficient must be int or float')
        if not type(p) == int and p >= 0:
            raise TypeError('The power must be an int whose value is >= 0')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]


       

    def __add__(self,right):
        if type(right) == Poly:
            result = {}
            answer = ''
            for i in self.terms:
                for x in right.terms:
                    if i == x:
                        result[i] = self.terms[i] + right.terms[x]
            for i in self.terms:
                if i not in result:
                    result[i] = self.terms[i]
            for i in right.terms:
                if i not in result:
                    result[i] = right.terms[i]
            for i in result:
#                 if result != 0:
                answer += '('+str(result[i])+','+str(i)+'),'
            return eval('Poly('+answer[:-1]+')')
        elif type(right) == int or type(right) == float:
            for i in self.terms:
                if i == 0:
                    self.terms[0] += right
            return self
        else:
            raise TypeError('Invalid type')
            

    
    def __radd__(self,left):
        if type(left) == Poly:
            result = {}
            answer = ''
            for i in self.terms:
                for x in left.terms:
                    if i == x:
                        result[i] = self.terms[i] + left.terms[x]
            for i in self.terms:
                if i not in result:
                    result[i] = self.terms[i]
            for i in left.terms:
                if i not in result:
                    result[i] = left.terms[i]
            for i in result:
                if result != 0:
                    answer += '('+str(result[i])+','+str(i)+'),'
            return eval('Poly('+answer[:-1]+')')
        elif type(left) == int or type(left) == float:
            for i in self.terms:
                if i == 0:
                    self.terms[0] += left
            return self
        else:
            raise TypeError('Invalid type')
    

    def __mul__(self,right):
        result = {}
        answer = ''
        if type(right) == Poly:
            for i in self.terms:
                for x in right.terms:
                    if i+x not in result:
                        result[i+x] = self.terms[i]*right.terms[x]
                    else:
                        result[i+x] += self.terms[i]*right.terms[x]
            for i in result:
                if result != 0:
                    answer += '('+str(result[i])+','+str(i)+'),'
            return eval('Poly('+answer[:-1]+')')
        elif type(right) == int or type(right) == float:
            for i in self.terms:
                self.terms[i] *= right
            return self
        else:
            raise TypeError('Invalid type')
    

    def __rmul__(self,left):
        result = {}
        if type(left) == Poly:
            for i in self.terms:
                for x in left.terms:
                    if i+x not in result:
                        result[i+x] = self.terms[i]*left.terms[x]
                    else:
                        result[i+x] += self.terms[i]*left.terms[x]
            for i in result:
                if result != 0:
                    answer += '('+str(result[i])+','+str(i)+'),'
            return eval('Poly('+answer[:-1]+')')
        elif type(left) == int or type(left) == float:
            for i in self.terms:
                self.terms[i] *= left
            return self
        else:
            raise TypeError('Invalid type')
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) == int or type(right) == float:
            if len(self.terms) == 1 and 0 in self.terms:
                if self.terms[0] == right:
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise TypeError('Invalid type')

    
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