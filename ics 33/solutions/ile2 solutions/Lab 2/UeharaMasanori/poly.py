class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if isinstance(item[0], (int, float)) and isinstance(item[1], int) and \
            item[1] >= 0 and item[1] not in self.terms:
                if item[0] != 0:
                    self.terms[item[1]] = item[0]
            else:
                raise AssertionError("Poly.__init__: illegal power in :" + str(item[0]) + ":" + str(item[1]))
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
        for item1, item2 in self.terms.items():
            result += '({}, {})'.format(item1, item2)
        result += ')'
        return result

    
    def __len__(self):
        result = 0
        for item in self.terms.keys():
            if result < item:
                result = item
        return result
    
    def __call__(self,arg):
        result = 0
        if isinstance(arg, (int, float)):
            for k, v in self.terms.items():
                result += v * (arg**k)
        return result
    

    def __iter__(self):
        return iter(sorted(((item2, item1) for item1, item2 in self.terms.items())))
        
            

    def __getitem__(self,index):
        if isinstance(index, int) and index >= 0:
            return self.terms[index] if index in self.terms else 0
        else:
            raise TypeError('invalid index')
            

    def __setitem__(self,index,value):
        if isinstance(index, int) and index >= 0:
            self.terms[index] = value
            temp_list = []
            for k, v in self.terms.items():
                if v == 0:
                    temp_list.append(k)
            for item in temp_list:
                del self.terms[item]
        else:
            raise TypeError('invalid index')
            

    def __delitem__(self,index):
        if isinstance(index, int) and index >= 0:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError('invalid index')
            

    def _add_term(self,c,p):
        if isinstance(c, (int, float)) and isinstance(p, int) and \
        p >= 0:
            if p not in self.terms:
                self.terms[p]= c
            else:
                self.terms[p] += c
            temp_list = []
            for k, v in self.terms.items():
                if v == 0:
                    temp_list.append(k)
            for item in temp_list:
                del self.terms[item]
        else:
            raise TypeError('Error adding poly')
       

    def __add__(self,right):
        if isinstance(right, Poly):
            result = Poly()
            for k, v in self.terms.items():
                result._add_term(v, k)
            for k, v in right.terms.items():
                result._add_term(v, k)
            return result
        elif isinstance(right, (int, float)):
            result = Poly()
            for k, v in self.terms.items():
                result._add_term(v, k)
            result._add_term(right, 0)
            return result
        else:
            raise TypeError('invalid addition')

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if isinstance(right, Poly):
            if not len(right.terms):
                return 0
            result = Poly()
            for p1, v1 in self.terms.items():
                for p2, v2 in right.terms.items():
                    result.terms[p1+p2] = v1*v2
            return result
        elif isinstance(right, (int, float)):
            result = Poly()
            for k, v in self.terms.items():
                result._add_term(v, k)
            for p, v in result.terms.items():
                result.terms[p] = right*v
            return result
        else:
            raise TypeError('invalid addition')
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if isinstance(right, Poly):
            return self.terms == right.terms
        elif isinstance(right, (int, float)):
            if self.terms[0]:
                if self.terms[0] == right:
                    return True
                else:
                    return False
        else:
            raise TypeError('invalid compare')

    
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