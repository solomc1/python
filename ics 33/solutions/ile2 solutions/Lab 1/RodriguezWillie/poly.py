class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        power_list = []
        for i in terms:
            assert type(i[0]) in (int, float)
            assert type(i[1]) == int
            assert i[1] >= 0
            if i[0] < 0 or i[1] not in power_list:
                power_list.append(i[1])
            else:
                raise AssertionError
            
                
            if i[0] != 0:
                self.terms[i[1]] = i[0]
            
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
        tuple_list = []
        tuples = ''
        for i,v in self.terms.items():
            tuple_list.append((v,i))
        for j in tuple_list:
            tuples += '{},'.format(j)
        return "Poly({tup})".format(tup = tuples)

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            power_list = [i for i in self.terms.keys()]
            return max(power_list)
    
    def __call__(self,arg):
        result = 0
        for i,v in self.terms.items():
            result += v*(arg**i)
        return result
    

    def __iter__(self):
        tuple_list = []
        new_list = []
        for i,v in self.terms.items():
            tuple_list.append((v, i))
        for i in sorted(tuple_list, key = lambda x: x[1], reverse = True):
            new_list.append(i)
        it = iter(new_list)
        for j in new_list:
            yield j
            
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Not an integer type")
        elif index < 0:
            raise TypeError("Value cannot be less than 0")
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
        

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Not an integer type or value was less than 0")
        elif value == 0:
            self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Not an integer type or value was less than 0")
        else:
            self.terms.pop(index)       

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Value is not an int or float")
        elif type(p) != int or p < 0:
            raise TypeError("Value is not an integer or is less than 0")
        else:
            if c != 0:
                if p not in self.terms.keys():
                    self.terms[p] = c
                elif p in self.terms.keys():
                    c += self.terms[p]
                    self.terms[p] = c
       
    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        else:
            if type(right) == Poly:
                self._add_term(right[0], right[1])
            elif type(right) in (int, float):
                print(right)
                self._add_term(right)

    
    def __radd__(self,left):
        self.__add__(left)
    

    def __mul__(self,right):
        d = dict()
        for i,v in right.terms.items():
            for j, k in self.terms.items():
                d[j+i] ==v*k
        self.terms = d
        return self.terms
                
        
        
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) in (int,float):
            return self.terms == right
        else:
            raise TypeError
                            

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()