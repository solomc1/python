from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        ''' coefficient, power '''
        self.terms = {}
        history_list = []
        for key, val in terms:
            assert type_as_str(key) in {'int','float'}
            assert type_as_str(val) == 'int'
            assert val >= 0
            if key != 0:
                history_list.append(val)
            assert history_list.count(val) <= 1
            if key != 0:
                self.terms[val] = key
        
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
        items = []
        for k,v in self.terms.items():
            items.append((v,k))
        return "Poly{}".format(str(tuple(items)))

    
    def __len__(self):
        if len(self.terms.keys()) != 0:
            return max(self.terms.keys())
        return 0
    
    def __call__(self,arg):
        counter = 0
        for power,co in self.terms.items():
            counter += co * arg**power
        return counter
    

    def __iter__(self):
#         print(self.terms.items())
        for key,val in sorted(self.terms.items(), reverse=True):
            yield val,key
            

    def __getitem__(self,index):
        if type_as_str(index) != 'int':
            raise TypeError("{} is not an int".format(str(index)))
        elif index < 0:
            raise TypeError("{} is < 0".format(str(index)))
        elif index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
#         print(self.terms) #test
        if type_as_str(index) != 'int':
            raise TypeError("{} is not an int".format(str(index)))
        elif index < 0:
            raise TypeError("{} is < 0".format(str(index)))
        elif index == 0:
            del self.terms[index]
        else:
            self.terms[index] = value
#         for item in self.terms:
#             if self.terms[item] == 0:
#                 self.terms.pop(item)
            

    def __delitem__(self,index):
        if type_as_str(index) != 'int':
            raise TypeError("{} is not an int".format(str(index)))
        elif index < 0:
            raise TypeError("{} is < 0".format(str(index)))
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type_as_str(c) not in ["int",'float']:
            raise TypeError("{} is not int or float".format(str(c)))
        elif type_as_str(p) != 'int':
            raise TypeError("{} is not an int".format(str(p)))
        elif p < 0:
            raise TypeError("{} is < 0".format(str(p)))
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p] + c == 0:
                self.terms.pop(c)
            else:
                self.terms[p] += c
       

    def __add__(self,right):
        if type(right) is Poly:
            for k,v in right.terms.items():
                if k in self.terms:
#                     return self.terms[k] + v
                    self.terms[k] += v
#                 return v
                self.terms[k] = v
        elif type_as_str(right) in ['int','float']:
            if 0 in self.terms:
#                 return self.terms[0] + right
                self.terms[0] += right
#             return right
            self.terms[0] = right
        else:
            raise TypeError("{} is not Polynomial, int, or float".format(str(right)))

    
    def __radd__(self,left):
        if type_as_str(left) in ['int','float']:
            if 0 in self.terms:
#                 return self.terms[0] + left
#             return left
                self.terms[0] += left
            self.terms[0] = left
        else:
            raise TypeError("{} is not Polynomial, int, or float".format(str(left)))
    

    def __mul__(self,right):
        if type(right) is Poly:
            pass
        elif type_as_str(right) in ['int','float']:
            pass
        else:
            raise TypeError("{} is not Polynomial, int, or float".format(str(right)))
    

    def __rmul__(self,left):
        if type_as_str(left) in ['int','float']:
            pass
        else:
            raise TypeError("{} is not Polynomial, int, or float".format(str(left)))
    

    def __eq__(self,right):
        if type_as_str(right) in ['int','float']:
            if 0 in self.terms:
                return self.terms[0] == right 
        elif type(right) is Poly:
            for k,v in right.items():
                if k not in self.terms: 
                    return False
                elif self.terms[k] != v:
                    return False
                return True 
        else:
            raise TypeError("{} is not Polynomial, int, or float".format(str(right)))

    
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