class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if item[0] == 0:
                pass
            elif not isinstance(item[0], (int,float)):
                raise AssertionError('Coefficient must be an into or float, was type', str(type(item[0])))
            elif item[1] < 0 or not isinstance(item[1], int):
                raise AssertionError('Power must be an int greater than or equal to 0.')
            if item[1] not in self.terms and item[0] != 0:
                self.terms[item[1]] = item[0]
            else:
                raise AssertionError('Cannot contain the same power more than once.')
        
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
        tup = set()
        for key in self.terms:
            tup.add((self.terms[key],key))
        return 'Poly('+str(tup)+ ')'


    
    def __len__(self):
        max_list = []
        for key in self.terms:
            max_list.append(key)
        if len(max_list) == 0:
            return 0
        else:
            return max(max_list)
            
    
    def __call__(self,arg):
        count = 0
        for key in self.terms:
            count += ((arg**key) *self.terms[key])
        return count
        
    

    def __iter__(self):
        l = []
        for key in self.terms:
            l.append((self.terms[key], key))
        l.sort()
        for item in l:
            yield item
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than or equal to 0.')
        for key in self.terms:
            if key == index:
                return self.terms[key]
            elif index not in self.terms.keys():
                return int(0)

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than or equal to 0.')
        if index in self.terms.keys():
            del self.terms[index]
            self.terms[index] = value
        elif value != 0:
            self.terms[index] = value


    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int greater than or equal to 0.')
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p) != int or p < 0:
            raise TypeError('Power must be an int greater than or equal to 0.')
        if not isinstance(c, (int, float)):
            raise TypeError('Coefficient must be an int or float')
        if p in self.terms.keys():
            self.terms[p] = c + self.terms[p]
        elif c != 0:
            self.terms[p] = c
        if self.terms[p] == 0:
            del self.terms[p]

    def __add__(self,right):
        if not isinstance(right, (Poly, int, float)):
            raise TypeError('Must be adding a Poly, int or float')
        if type(right) == int or type(right) == float:
            for key in self.terms:
                if key == 0:
                    self.terms[key] == self.terms[key] + right


    
    def __radd__(self,left):
        self.__add__(left)
    

    def __mul__(self,right):
        if not isinstance(right, (Poly, int, float)):
            raise TypeError('Must be multiplying a Poly, int or float')
    

    def __rmul__(self,left):
        self.__mul__(left)
    

    def __eq__(self,right):
        if not isinstance(right, (Poly, int, float)):
            raise TypeError('Must be comparing to a Poly int or float')
        if type(right) == Poly:
            if self.terms == right.terms:
                return True
        

    
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