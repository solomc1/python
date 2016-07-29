from collections import defaultdict
class Poly:
    
    def __init__(self,*terms):
        #  (coefficient, power)
        # power = key, coefiicent = value
        #Poly((3,2),(-2,1)) = 3x^2 - 2z
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        tuple_lst = []
        for tup in terms:
            if tup[0] != 0:
                tuple_lst.append(tup)
        self.tuple_lst = tuple_lst
#         print('tuple_lst =', tuple_lst)
        for item in tuple_lst:
            key = item[1] #power
            value = item[0] #coefficient
            p = key
            c = value
            if type(value) != int and type(value) != float:
                raise AssertionError('coefficient must be a float or int')
            if type(p) != int:
                raise AssertionError('the power must be an integer')
            if p < 0:
                raise AssertionError('the power must be greater than or equal to 0')                
            if value == 0:
                None
            else:
                if key in self.terms:
                    raise AssertionError('you cannot use the same power more than once')
                self.terms[key] = value
#         print('self.terms =', self.terms)

        
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
        if self.terms == {}:
            return 'Poly()'
        string = 'Poly('
        for item in self.tuple_lst:
            if int(item[0]) == 0:
                None
            elif item != self.tuple_lst[-1]:
                string += str(item) +','
            else:
                string += str(item) + ')'
#         print('repr returned:', string)
        string = string.replace('0x +', '')
        return string

    
    def __len__(self):
        max = 0
        for power, coef in self.terms.items():
            if int(power) >= max:
                max = int(power)
        return max
    
    def __call__(self,arg):
        my_string = self.__str__()
#         print(my_string)
        total = 0
        for power, coef in self.terms.items():
            total += float(coef) * (float(arg) ** int(power))
        return int(total)
#         my_string = my_string.replace('x', '*'+str(arg))
#         my_string = my_string.replace('^', '**')
#         print("__call__ will eval:", my_string)
#         return eval(my_string)
    

    def __iter__(self):
#         print('__iter__')
        iterable = self.terms
        new_tuple_lst = [((y,x)) for x, y in iterable.items()]
        new_tuple_lst = sorted(new_tuple_lst, key = lambda x:x[1], reverse=True)
#         print(new_tuple_lst)
        iterable = iter(new_tuple_lst)
        while True:
            next_val = next(iterable)
            if next_val != None:
                yield next_val
            else:
                raise StopIteration
            

    def __getitem__(self,index):
        #power = key, coef = value
        if type(index) != int:
            raise TypeError('the index of getitem must be an integer')
        if index < 0:
            raise TypeError('the index of getitem must be >= 0')
        if index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        power = index
        coef = value
        if type(power) != int:
            raise TypeError('the index of setitem must be an integer')
        elif power < 0:
            raise TypeError('the index of setitem must not be less than 0')
        elif coef == 0:
            new_dict = {}
            for p, c in self.terms.items():
                if p != power:
                    new_dict[p] = c
            self.terms = new_dict
        else:
            try:
                self.terms[power] = coef
            except:
                None
            

    def __delitem__(self,index):
        power = index
        if type(power) != int:
            raise TypeError('the index of setitem must be an integer')
        elif power < 0:
            raise TypeError('the index of setitem must not be less than 0')
        new_dict = {}
        for p, c in self.terms.items():
            if p != power:
                new_dict[p] = c
        self.terms = new_dict
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise AssertionError('coefficient must be a float or int')
        if type(p) != int:
            raise AssertionError('the power must be an integer')
        if p < 0:
            raise AssertionError('the power must be greater than or equal to 0')                
        if c == 0:
            None
        else:
            if p in self.terms:
                val = self.terms[p]
                self.terms[p] = val + c
            else:
                self.terms[p] = c

    def __add__(self,right):
        if type(self)!= type(right) and type(right) != int and type(right) != float:
            raise TypeError('you can only add other polynomials or numbers to polynomials')
        elif type(self) == type(right):
            duplicate = eval(self.__repr__())
            for power, coef in right.terms.items():
                duplicate._add_term(coef, power)
            return duplicate
        else:
            duplicate = eval(self.__repr__())
            duplicate._add_term(right, 1)
            return duplicate
                
                    
            
        
        
        

    
    def __radd__(self,left):
        if type(self)!= type(left) and type(left) != int and type(left) != float:
            raise TypeError('you can only add other polynomials or numbers to polynomials')
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(self)!= type(right) and type(right) != int and type(right) != float:
            raise TypeError('you can only add other polynomials or numbers to polynomials')
        if right == Poly():
            return 0
    

    def __rmul__(self,left):
        if type(self)!= type(left) and type(left) != int and type(left) != float:
            raise TypeError('you can only add other polynomials or numbers to polynomials')
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(self)!= type(right) and type(right) != int and type(right) != float:
            raise TypeError('you can only add other polynomials or numbers to polynomials')
        if type(self) == type(right):
            if (self.__repr__()) == (right.__repr__()):
                return True
            else:
                return False
        if type(right) == int or type(right) == float:
            return True

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    for i in p:
        print(i)
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
    #check setitem how i pop it