class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        count = 0
        lst = []
        self.terms = {}
        for value in terms:
            if type(value[1]) == str:
                raise AssertionError
            assert type(value[0]) == int or type(value[0]) == float
            assert value[1] >= 0 and type(value[1]) == int
            if value[0] != 0:
                self.terms[value[1]] = value[0]

        

#             if value[1] == 0:
#                 self.terms[1] = value[0]
        
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
        x = []
        for key,value in self.terms.items():
            x.append((key,value))
        return 'Poly'+str(tuple(x))

    
    def __len__(self):
        lst = []
        for key in self.terms.keys():
            lst.append(key)
        if len(lst) == 0:
            return 0
        return max(lst)    
    def __call__(self,arg):
        first = 0
        for key,value in self.terms.items():
            first+=value*(arg**key)
        return first
    

    def __iter__(self):
        for key,value in sorted(self.terms.items(),reverse = True):
            yield(value,key)
            

    def __getitem__(self,index):
        if index < 0:
            raise TypeError
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        if value != 0:
            self.terms[index]=value

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        count = 0
        lst = []
        if p not in self.terms.keys():
            self.terms[p]=c
        elif p in self.terms.keys():
            count+=self.terms[p]
            count += c
            self.terms[p] = count
        for key,value in self.terms.items():
            if value == 0:
                lst.append(key)
        for value in lst:
            del self.terms[value]
       

    def __add__(self,right):
        count = 0
        lst1 = []
        lst2 = []
        final = []
        final2 = []
        returned = []
        for key in self.terms.keys():
            lst1.append(key)
        for key in right.terms.keys():
            lst2.append(key)
        for k1,k2 in zip(lst1,lst2):
            if k1==k2:
                final.append(k1)
        for value in final:
            returned.append((self.terms[value]+right.terms[value],value))
        for value in self.terms.keys():
            if value not in final:
                returned.append((self.terms[value],value))
        for value in right.terms.keys():
            if value not in final:
                returned.append((right.terms[value],value))
        return Poly(tuple(returned))
#         if type(right)!=int or type(right) != float:
#             raise TypeError

    
    def __radd__(self,left):
        pass
#         if type(right)!=int or type(right) != float:
#             raise TypeError    

    def __mul__(self,right):
        pass
            
            

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(self) == str or type(right) == str:
            raise TypeError

        if type(right) == int:
            return right in self.terms.values()
        lst1 = []
        lst2 = []
        for key in self.terms.keys():
            lst1.append(key)
        for key in right.terms.keys():
            lst2.append(key)
        return lst1 == lst2


    
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