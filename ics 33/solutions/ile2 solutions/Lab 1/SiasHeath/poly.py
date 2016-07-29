class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        
#        self.terms = {power:coef for coef,power in terms if coef != 0 else ...}
        self.terms = {}
        for term in terms:
            assert type(term[0]) in (int,float), "incorrect type for coeff"
            assert type(term[1]) is int, "incorrect type for power "
            assert term[1] >= 0, "Power must be >= 0"
            assert term[1] not in self.terms.keys(), "Power already in dict"
            if term[0] != 0:
                self.terms[term[1]] = term[0]
        
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
        return "Poly({})".format(self.fill_repr())
    
    def fill_repr(self):
        ret_str = ""
        for item in self.terms.items():
            ret_str += "({},{}),".format(item[1], item[0])
        return ret_str

    
    def __len__(self):
        if not len(self.terms.keys()):
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) is int or float, "incorrect argument type"
        ret_val = 0
        for item in self.terms.items():
            ret_val += item[1] * arg**item[0]
        return ret_val
    

    def __iter__(self):
        item_list = [(coeff, power) for power, coeff in self.terms.items()]
        sorted_list = sorted(item_list, key = lambda x: -x[1])
        for item in sorted_list:
            yield item
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError("index must be int > 0")
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError("power must be int")
        if index < 0:
            raise TypeError("power must be >= 0")
        if value == 0:
            if index in self.terms:
                del self.terms[index]
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError("power must be int")
        if index < 0:
            raise TypeError("power must be >= 0")
        if index in self.terms:
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("coeff must be int or float")
        if type(p) is not int:
            raise TypeError("power must be int")
        if p < 0:
            raise TypeError("power must be >= 0")
        
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]


    def f_rep(self, d: dict):
        ret_str = ""
        for item in d.items():
            ret_str += "({},{}),".format(item[1], item[0])
        return ret_str
    
    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("argument must be Poly, int, or float")
        new_dict = self.terms
        if type(right) is Poly:
            for item in right.terms:
                if item in new_dict:
                    new_dict[item] += right.terms[item]
                    if new_dict[item] == 0:
                        del new_dict[item]
            return eval("Poly({})".format(self.f_rep(new_dict)))
        else:
            if '0' in new_dict:
                new_dict['0'] += right
                if new_dict['0'] == 0:
                    del new_dict['0']
 #           elif '0' not in new_dict:
 #               new_dict['0'] = right
            return eval("Poly({})".format(self.f_rep(new_dict)))
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("argument must be Poly, int, or float")
        if type(right) in (int, float):
            if len(self.terms.keys()) == 1 and '0' in self.terms.keys():
                return self.terms['0'] == right
            else:
                return False
        else:
            return self.terms.items() == right.terms.items()
        
    def __req__(self, left):
        return self.__eq__(left)

    
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