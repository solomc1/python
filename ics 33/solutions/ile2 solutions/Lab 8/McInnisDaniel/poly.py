class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        term_dict = dict()
        for item in terms:
            if type(item[0]) not in (int, float):
                raise AssertionError("Coefficient must be int of float")
            elif (type(item[1]) != int):
                raise AssertionError("Coefficient must be int and greater than 0")
            elif item[1] in term_dict.keys():
                raise AssertionError("That power already exists")
            elif item[1] < 0:
                raise AssertionError("Power has to be greater than zero")
            elif item[0] == 0:
                pass
            else:
                term_dict[item[1]] = item[0]
        self.terms = term_dict
        
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
        str_to_return = "Poly("
        tuple_list = []
        for k,v in self.terms.items():
            tuple_list.append("({},{})".format(v,k))
        tuple_list = ",".join(tuple_list)
        str_to_return += tuple_list
        str_to_return += ")"
        return str_to_return

    
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            highest = 0
            for i in self.terms.keys():
                if i > highest:
                    highest = i
            return highest
    
    def __call__(self,arg):
        if type(arg) not in (int,float):
            raise AssertionError("Wrong argument type, need int or float")
        else:
            result = 0
            for k,v in self.terms.items():
                if k == 0:
                    result += 1*v
                else:
                    result += (arg**k)*v
        return result
                    
    

    def __iter__(self):
        def _gen(iterable):
            for_iter = sorted(iterable.items())
            iter_items = []
            for item in for_iter:
                iter_items.append((item[1],item[0]))
            for value in sorted(iter_items, key = lambda x: x[1], reverse = True):
                yield value
        return _gen(self.terms)               

    def __getitem__(self,index):
        if (type(index) != int) or index < 0:
            raise TypeError("Invalid index argument")
        else:
            if index not in self.terms.keys():
                return 0
            else:
                return self.terms[index]
            

    def __setitem__(self,index,value):
        if (type(index) != int) or index < 0:
            raise TypeError("Invalid index argument")
        else:
            if (value == 0) and (index in self.terms.keys()):
                del self.terms[index]
            elif (value == 0) and (index not in self.terms.keys()):
                pass
            else:
                self.terms[index] = value
                    

    def __delitem__(self,index):
        if (type(index) != int) or index < 0:
            raise TypeError("Invalid index argument")
        else:
            if index not in self.terms.keys():
                pass
            else:
                del self.terms[index]            

    def _add_term(self,c,p):
        if type(c) not in (int, float):
            raise TypeError("Incorrecet type for coefficient")
        elif (type(p) != int) or p < 0:
            raise TypeError("Invalid power argument, needs to be > 0 and int")
        else:
            if (p not in self.terms.keys()) and (c != 0):
                self.terms[p] = c
            else:
                if (p in self.terms.keys()):
                    self.terms[p] = (self.terms[p] + c)
            if self.terms[p] == 0:
                del self.terms[p]      

    def __add__(self,right):
        pass
#         if type(right) not in (Poly, int, float):
#             raise TypeError("Unsupported operand types for +")
#         else:
#             new_poly = eval("Poly()")
#             if type(right) == Poly:
#                 for value in right.terms.keys():
#                     if value[0] in self.terms.keys():
#                         
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Unsupported operand types for ==")
        else:
            if type(right) == Poly:
                return (self.terms.items() == right.terms.items())
            else:
                if len(self.terms.keys()) == 1:
                    return self.terms[0] == right
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