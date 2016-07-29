class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}        
            
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for item in terms:
            assert type(item[0]) == int or type(item[0]) == float, '\n\tclass:  Poly\n\tmethod:  __init__\n\terror:  coefficient must be an int or a float value.'
            assert type(item[1]) == int and item[1] >= 0, '\n\tclass:  Poly\n\tmethod:  __init__\n\terror:  power must be an int whose value is >= 0.'
            if item[1] in self.terms:
                if self.terms[item[1]] != 0:
                    raise AssertionError('\n\tclass:  Poly\n\tmethod:  __init__\n\terror:  illegal power in:  ' + str(terms) + '.')
            elif item[0] != 0:
                self.terms[item[1]] = item[0]

            
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
        return 'Poly({})'.format(','.join('(' + str(self.terms[item]) + ',' + str(item) + ')' for item in self.terms))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else: return max(self.terms)
    
    def __call__(self,arg):
        assert type(arg) == int or type(arg) == float, '\n\tclass:  Poly\n\tmethod:  __call__\n\terror:  ' + str(arg) + ' must be an int or a float value.'
        result = 0
        for item in self.terms:
            result += (arg**item) * self.terms[item]
        return result
    

    def __iter__(self):
        keys = list(self.terms.keys())
        keys.sort(reverse = True)
        for item in keys:
            yield (self.terms[item], item)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('\n\tclass:  Poly\n\tmethod:  __getitem__\n\terror:  ' + str(index) + ' must be an int and > 0.')
        if index not in self.terms:
            return 0
        return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index < 0: raise TypeError('\n\tclass:  Poly\n\tmethod:  __setitem__\n\terror:  ' + str(index) + ' must be an int and > 0.')
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else: self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0: raise TypeError('\n\tclass:  Poly\n\tmethod:  __delitem__\n\terror:  ' + str(index) + ' must be an int and > 0.')
        if index in self.terms:
            self.terms.pop(index)
        

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float: raise TypeError('\n\tclass:  Poly\n\tmethod:  _add_term\n\terror:  ' + str(c) + ' must be an int or a float value.')
        if type(p) != int or p < 0: raise TypeError('\n\tclass:  Poly\n\tmethod:  _add_term\n\terror:  ' + str(p) + ' must be an int and > 0.')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c == 0:
                self.terms.pop(p)
            else: self.terms[p] += c
       

    def __add__(self,right):
        if type(right) == Poly:
            result = Poly()
            selfiter = iter(self)
            while True:
                try:
                    item = selfiter.__next__()
                    result._add_term(item[0],item[1])
                except:
                    break
            rightiter = iter(right)
            while True:
                try:
                    item = rightiter.__next__()
                    result._add_term(item[0],item[1])
                except:
                    break
            return result
        if type(right) == int or type(right) == float:
            result = Poly()
            selfiter = iter(self)
            while True:
                try:
                    item = selfiter.__next__()
                    result._add_term(item[0],item[1])
                except:
                    break
            result._add_term(right, 0)
            return result
        else:
            raise TypeError('\n\tclass:  Poly\n\tmethod:  __add__\n\terror:  ' + str(right) + ' must be a Poly or an int or a float value.')

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) == Poly:
            result = Poly()
            selfiter = iter(self)
            while True:
                try:
                    selfitem = selfiter.__next__()
                    rightiter = iter(right)
                    while True:
                        try:
                            rightitem = rightiter.__next__()
                            result._add_term(selfitem[0] * rightitem[0], selfitem[1] + rightitem[1])
                        except:
                            break
                except:
                    break
            return result
        elif type(right) == int or type(right) == float:
            result = Poly()
            selfiter = iter(self)
            while True:
                try:
                    selfitem = selfiter.__next__()
                    result._add_term(selfitem[0] * right, selfitem[1])
                except:
                    break
            return result
        else:
            raise TypeError('\n\tclass:  Poly\n\tmethod:  __mul__\n\terror:  ' + str(right) + ' must be a Poly or an int or a float value.')
                    
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) == Poly:
            return str(self) == str(right)
        elif type(right) == int or type(right) == float:
            if self.__len__() == 0:
                return self[0] == right
            else:
                return False
        else:
            raise TypeError('\n\tclass:  Poly\n\tmethod:  __eq__\n\terror:  ' + str(right) + ' must be a Poly or an int or a float value.')
        

    
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