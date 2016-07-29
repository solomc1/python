class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for t in terms:
            assert (type(t[0]) in [int,float]), 'Illegal coefficient in: {}'.format(t)
            assert (type(t[1]) == int), 'Illegal power in: {}'.format(t)
            assert (t[1] >= 0), 'Illegal power in: {}'.format(t)
            assert (t[1] not in self.terms.keys()), 'Illegal power in: {}'.format(t)
            if t[0] != 0:
                self.terms[t[1]] = t[0]
        
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
        counter = 0
        for k in self.terms.keys():
            result += '({},{})'.format(self.terms[k],k)
            result += ('' if counter == len(self.terms.keys()) - 1 else ',')
            counter += 1
        return 'Poly({})'.format(result)

    
    def __len__(self):
        c_list = []
        for k in self.terms.keys():
            c_list.append(k)
        return (0 if c_list == [] else max(c_list))
    
    def __call__(self,arg):
        result = 0
        for k in self.terms.keys():
            result += self.terms[k] * arg**k
        return result
    

    def __iter__(self):
        p_list = [k for k in self.terms.keys()]
        p_list.sort(reverse=True)
        for p in p_list:
            yield (self.terms[p],p)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Illegal index type: {}'.format(type(index)))
        if index < 0:
            raise TypeError('Illegal index value: {}'.format(index))
        return (self.terms[index] if index in self.terms.keys() else 0)

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Illegal index type: {}'.format(type(index)))
        if index < 0:
            raise TypeError('Illegal index value: {}'.format(index))
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Illegal index type: {}'.format(type(index)))
        if index < 0:
            raise TypeError('Illegal index value: {}'.format(index))
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('Illegal c type: {}'.format(type(c)))
        if type(p) != int:
            raise TypeError('Illegal p type: {}'.format(type(p)))
        if p < 0:
            raise TypeError('Illegal p value: {}'.format(p))
        if c != 0:
            if p in self.terms.keys():
                if -c == self.terms[p]:
                    self.terms.pop(p)
                else:
                    old_c = self.terms[p]
                    self.terms[p] = c + old_c
            else:
                self.terms[p] = c
       

    def __add__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Illegal types: {} + {}'.format(type(self),type(right)))
        p_obj = eval(self.__repr__())
        if type(right) == Poly:
            for k in right.terms.keys():
                p_obj._add_term(right.terms[k],k)
        else:
            p_obj._add_term(right,0)
        return p_obj

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Illegal types: {} * {}'.format(type(self),type(right)))
        p_obj = Poly()
        if type(right) == Poly:
            for k1 in self.terms.keys():
                for k2 in right.terms.keys():
                    p_obj._add_term(self.terms[k1] * right.terms[k2], k1 + k2)
        else:
            for k in self.terms.keys():
                p_obj._add_term(self.terms[k] * right, k)
        return p_obj

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in [Poly,int,float]:
            raise TypeError('Illegal types: {} == {}'.format(type(self),type(right)))
        if type(right) == Poly:
            p1_list = [k for k in self.terms.keys()]
            p2_list = [k for k in right.terms.keys()]
            c1_list = [self.terms[k] for k in self.terms.keys()]
            c2_list = [right.terms[k] for k in right.terms.keys()]
            return p1_list == p2_list and c1_list == c2_list
        else:
            counter = 0
            for k in self.terms.keys():
                if self.terms[k] == right:
                    counter += 1
            return counter == 1
    
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