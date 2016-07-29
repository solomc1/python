class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for item in terms:
            if type(item[0]) not in [int, float]:
                raise AssertionError('Poly.__init__: illegal coefficient type in ' + str(item)) 
            if type(item[1]) != int or item[1] < 0:
                raise AssertionError('Poly.__init__: illegal power in ' + str(item))
            if item[1] in self.terms:
                raise AssertionError('Poly.__init__: repeated power in ' + str(item))
            if item[0] != 0:
                self.terms[item[1]] = item[0]
                #print(self.terms)
            
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
        return 'Poly({})'.format(','.join('(' + str(self.terms[item]) + ',' + str(item) + ')' for item in self.terms.keys()))
    
    def __len__(self):
        highest = 0
        for item in self.terms.keys():
            if item > highest:
                highest = item
        return highest
    
    def __call__(self,arg):
        total = 0
        for key in self.terms.keys():
            total += (self.terms[key] * arg ** key)
        return total

    def __iter__(self):
        for key in self.terms.keys():
            return (key, self.terms[key])
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int 0 or greater')
        return_list = 0
        for key in self.terms.keys():
            if key == index:
                return_list = self.terms[key]
        return return_list
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an int 0 or greater')
        if value != 0:
            self.terms[index] = value
        else:
            self.terms.pop(index)
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be an integer 0 or greater')
        self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Coefficient must be an int or a float')
        if type(p) != int or p < 0:
            raise TypeError('Power must be an integer 0 or greater')
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        else:
            value = self.terms[p]
            new_val = value + c
            if new_val != 0:
                self.terms[p] = new_val
            else:
                self.terms.pop(p)
       

    def __add__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Right must be an int, float, or Poly')
        if type(right) == Poly:
            add_list = []
            for key in self.terms.keys():
                if key in right.terms.keys():
                    for k in right.terms.keys():
                        if key == k:
                            svalue = self.terms[key] + right.terms[k]
                            self.terms[key] = svalue
                        else:
                            add_list.append((right.terms[k], k))
            if add_list != []:
                for item in add_list:
                    self._add_term(item[0], item[1])
            return self
        else:
            new = Poly((right,0))
            add_list = []
            for key in self.terms.keys():
                if key in new.terms.keys():
                    for k in new.terms.keys():
                        if key == k:
                            svalue = self.terms[key] + new.terms[k]
                            self.terms[key] = svalue
                        else:
                            add_list.append((new.terms[k], k))
            if add_list != []:
                for item in add_list:
                    self._add_term(item[0], item[1])
            return self

    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError(str(right) + ' must be an int, float, or Poly class')
        if type(right) in [int, float]:
            if right in self.terms.values():
                return True
            else:
                return False
        else:
            equals = None
            for item in self.terms.keys():
                for key in self.right.keys():
                    if item == key:
                        if self.terms[item] == self.right[key]:
                            equals = True
                        else:
                            equals = False
                    else:
                        return False
            return equals

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    '''print('Start simple tests')
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
    print('End simple tests\n')'''

    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()