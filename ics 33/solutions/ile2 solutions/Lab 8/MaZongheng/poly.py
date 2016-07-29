class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        assert all([type(i[0]) in [int, float] for i in terms]), 'all coefficients must be integers or floats'
        assert all([(type(i[1]) == int) and (i[1] >= 0) for i in terms]), 'all powers must be integers and > 0'
        assert len(set(i[1] for i in terms if i[0] != 0)) == len([i[1] for i in terms if i[0] != 0]),'powers cannot repeat'
        self.terms = {i[1]:i[0] for i in terms if i[0] != 0}
        
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
        result = 'Poly('
        for i in self.terms:
            result += '(' + str(self.terms[i]) + ',' + str(i) + '),'
        if len(self.terms) != 0:
            result = result[:-1]
        result += ')'
        return result

    
    def __len__(self):
        return max([i for i in self.terms]) if len(self.terms) != 0 else 0
    
    def __call__(self,arg):
        result = 0
        for i in self.terms:
            result += self.terms[i] * (arg ** i)
        return result
    

    def __iter__(self):
        ref = sorted([(self.terms[i], i) for i in self.terms], key = lambda x: x[1], reverse = True)
        for i in ref:
            yield i
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly index must be integers and > 0')
        try:
            return self.terms[index]
        except KeyError:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly index must be integers and > 0')
        if value != 0:
            self.terms[index] = value
        else:
            if index in self.terms.keys():
                del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly index must be integers and > 0')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0 or type(c) not in [int, float]:
            raise TypeError('Wrong attribute: p must be integer and > 0, and c must be integer or float')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        if type(right) == Poly:
            result_d = {}
            for i in {i for i in self.terms}.union({i for i in right.terms}):
                if i in self.terms and i in right.terms:
                    result_d[i] = self.terms[i] + right.terms[i]
                else:
                    if i in self.terms:
                        result_d[i] = self.terms[i]
                    else:
                        result_d[i] = right.terms[i]
        elif type(right) in [int,float]:
            result_d = {i: self.terms[i] for i in self.terms}
            if 0 in result_d:
                result_d[0] += right
            else:
                result_d[0] = right
        else:
            raise TypeError('Unsupported type for operator +: Poly and {}'.format(type(right)))
        
        for i in result_d:
            if result_d[i] == 0:
                del result_d[i]
        
        return Poly(*[(result_d[i], i) for i in result_d])

    
    def __radd__(self,left):
        if type(left) in [int,float]:
            result_d = {i: self.terms[i] for i in self.terms}
            if 0 in result_d:
                result_d[0] += left
            else:
                result_d[0] = left
            for i in result_d:
                if result_d[i] == 0:
                    del result_d[i]
            return Poly(*[(result_d[i], i) for i in result_d])
        else:
            raise TypeError('Unsupported type for operator +: Poly and {}'.format(type(left)))
    

    def __mul__(self,right):
        result_d = {}
        
        if type(right) == Poly:
            for i in self.terms:
                for n in right.terms:
                    if (i+n) not in result_d:
                        result_d[(i+n)] = self.terms[i] * right.terms[n]
                    else:
                        result_d[(i+n)] += self.terms[i] * right.terms[n]
        
        elif type(right) in [int,float]:
            result_d = {i: self.terms[i] for i in self.terms}
            for i in result_d:
                result_d[i] *= right      
        else:
            raise TypeError('Unsupported type for operator *: Poly and {}'.format(type(right)))
        
        for i in result_d:
            if result_d[i] == 0:
                del result_d[i]
        
        return Poly(*[(result_d[i], i) for i in result_d])

        
        

    def __rmul__(self,left):
        if type(left) in [int,float]:
            result_d = {i: self.terms[i] for i in self.terms}
            for i in result_d:
                result_d[i] *= left
            for i in result_d:
                if result_d[i] == 0:
                    del result_d[i]
            return Poly(*[(result_d[i], i) for i in result_d]) 
        else:
            raise TypeError('Unsupported type for operator *: Poly and {}'.format(type(left)))
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) in [int,float]:
            return list(self.terms.keys()) == [0] and self.terms[0] == right
        else:
            raise TypeError('Unsupported type for operator ==: Poly and {}'.format(type(right)))
    
if __name__ == '__main__':
#     Some simple tests; you can comment them out and/or add your own before
#     the driver is called.
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