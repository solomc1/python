class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for element in terms:
            if type(element[0]) not in (int,float):
                raise AssertionError("Poly.__init__: illegal coefficient type in : {}".format(element))
            elif type(element[1]) is int:
                if element[1] >= 0:
                    if element[1] not in self.terms.keys():
                        self.terms[element[1]] = element[0] 
                    else:
                        raise AssertionError("Poly.__init__: illegal power in : {}".format(element))
                else:
                    raise AssertionError("Poly.__init__: illegal power value in : {}".format(element))
            else:
                raise AssertionError("Poly.__init__: illegal power value type in : {}".format(type(element)))
        
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
        result = []
        for key in self.terms.keys():
            result.append((self.terms[key], key))
        result_str = ",".join([str(i) for i in result])
        return "Poly({})".format(result_str)

    
    def __len__(self):
        result = []
        for i in self.terms.values():
            result.append(i)
        return max(result)
    
    def __call__(self,arg):
        result = ''
        for i in str(self):
            if i == 'x':
                result += '*{}'.format(str(arg))
            else:
                result += i
        return result
                
                
    

    def __iter__(self):
        result = []
        for k,v in self.terms.items():
            result.append(k)
            result.sort(reverse= True)
        for i in result:
            yield(self.terms[i],i)
            
            

    def __getitem__(self,index):
        if type(index) is int:
            if index < 0:
                raise TypeError("__getitem__: illegal index value: {}".format(index))
            else:
                if index not in self.terms.keys():
                    return 0
                else:
                    return self.terms[index]
        else:
            raise TypeError("__getitem__: illegal index value type: {}".format(type(index)))

    def __setitem__(self,index,value):
        if type(index) is int:
            if index < 0:
                raise TypeError("__setitem__: illegal index value: {}".format(index))
            elif value == 0:
                for k,v in self.terms.items():
                    if value == v:
                        del self.terms[k]
            else:
                self.terms[index] = value
        else:
            raise TypeError("__setitem__: illegal index value type: {}".format(type(index)))

            

    def __delitem__(self,index):
        if type(index) is int:
            if index < 0:
                raise TypeError("__delitem__: illegal index value: {}".format(index))
            else:
                if index in self.terms.keys():
                    del self.terms[index]
        else:
            raise TypeError("__delitem__: illegal index value type: {}".format(type(index)))
                
            

    def _add_term(self,c,p):
        if type(c) in (int, float):
            if type(p) is int:
                if p < 0:
                    raise TypeError("_add_term: illegal power value: {}".format(p))
                else:
                    if (p not in self.terms.keys()):
                        if c != 0:
                            self.terms[p] = c
                            
                    else:
                        for k,v in self.terms.items():
                            if p == k:
                                self.terms[k] += c
                                if self.terms[k] == 0:
                                    del self.terms[k]
            else:
                raise TypeError("_add_term: illegal power value type: {}".format(type(p)))
        else:
            raise TypeError("_add_term: illegal coefficient value type: {}".format(type(c)))
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("__add__: illegal right value type: {}".format(type(right)))
        else:
            new_Poly = Poly()
            if type(right) is Poly:
                for k,v in self.terms.items():
                    new_Poly._add_term(v,k)
                for a,b in right.terms.items():
                    new_Poly._add_term(b,a)
            else:
                for k,v in self.terms.items():
                    new_Poly._add_term(v,k)
                new_Poly._add_term(right,0)
        return new_Poly
                
                
    
    def __radd__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError("__add__: illegal right value type: {}".format(type(left)))
        else:
            new_Poly = Poly()
            if type(left) is Poly:
                for k,v in self.terms.items():
                    new_Poly._add_term(v,k)
                for a,b in left.terms.items():
                    new_Poly._add_term(b,a)
            else:
                for k,v in self.terms.items():
                    new_Poly._add_term(v,k)
                new_Poly._add_term(left,0)
        return new_Poly
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("__mul__: illegal right value type: {}".format(type(right)))
        else:
            new_Poly = Poly()
            final = []
            if type(right) is Poly:
                for k,v in self.terms.items():
                    for a,b in right.terms.items():
                        final.append((k*a,v*b))
                for i in final:
                    new_Poly._add_term(i[1],i[0])
            else:
                for k,v in self.terms.items():
                    final.append((k*1,v*right))
                for i in final:
                    new_Poly._add_term(i[1],i[0])
            return new_Poly
                        

    def __rmul__(self,left):
        if type(left) not in (Poly, int, float):
            raise TypeError("__mul__: illegal right value type: {}".format(type(left)))
        else:
            new_Poly = Poly()
            final = []
            if type(left) is Poly:
                for k,v in self.terms.items():
                    for a,b in left.terms.items():
                        final.append((k*a,v*b))
                for i in final:
                    new_Poly._add_term(i[1],i[0])
            else:
                for k,v in self.terms.items():
                    final.append((k*1,v*left))
                for i in final:
                    new_Poly._add_term(i[1],i[0])
            return new_Poly
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("__eq__: illegal right value type: {}".format(type(right)))
        else:
            valid = []
            if type(right) is Poly:
                if len(right.terms) == len(self.terms):
                    for k,v in right.terms.items():
                        if right[k] == self[k]:
                            valid.append(True)
                        else:
                            valid.append(False)
                    return all(valid)
                else:
                    return False
            else:
                if len(self.terms) == len(right):
                    return self.terms[1] == right
                else:
                    return False
                    
                 

    
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