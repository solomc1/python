# Edited Efren Aguilar 76323142 Lab 6

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if type(item) != tuple: raise AssertionError("All parameters must be of type tuple")
            if len(item) != 2: raise AssertionError("Tuples must all be of size 2")
            if type(item[0]) not in (int, float): raise AssertionError("First value must be of type int or float")
            if type(item[1]) != int: raise AssertionError("Second value must be an int")
            if item[1] <0: raise AssertionError("Second value be >= 0")
            if item[1] in self.terms: raise AssertionError("More than one value for the power{} was used".format(item))
            if item[0] != 0:
                self.terms[item[1]] = item[0]
                
        
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
        param_str = ""
        for value in self.terms:
            param_str += "({},{}),".format(self.terms[value], value)
        param_str = param_str [:-1]
        return "Poly({})".format(param_str)
            
            

    
    def __len__(self):
        if len(self.terms) == 0: return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) not in (int, float):
            raise AssertionError("Value must be of type int or float")
        return_val = 0
        for item in self.terms:
            return_val += ((arg**item) * self.terms[item])
        return return_val
            
    

    def __iter__(self):
        for i in sorted(self.terms, reverse = True):
            yield (self.terms[i], i)
            

    def __getitem__(self,index):
        if type(index) != int: raise TypeError("Index must be of type int")
        if index <0: raise TypeError("Index must be >= 0")
        return self.terms[index] if index in self.terms else 0
            

    def __setitem__(self,index,value):
        if type(index) != int: raise TypeError("Index must be of type int")
        if index <0: raise TypeError("Index must be >= 0")
        if index in self.terms:
            if value == 0:
                self.terms.pop(index)
        if value == 0: return
        self.terms[index] = value
        
        
            

    def __delitem__(self,index):
        if type(index) != int: raise TypeError("Index must be of type int")
        if index <0: raise TypeError("Index must be >= 0")
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float): raise TypeError("c must be of type int or float")
        if type(p) != int: raise TypeError("p must be of type int")
        if p <0: raise TypeError("p must be >= 0")
        if c == 0:return
        if p not in self.terms:
            self.terms[p] = c
            return
        self.terms[p] = self.terms[p] + c
        if self.terms[p] == 0:
            self.terms.pop(p)
        
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Addition type must be of type Poly, int or float")
        if type(right) in (int, float):
            right = Poly((right, 0))
        return_poly = Poly()
        for item in self.terms:
            if item in right.terms:
                return_poly._add_term(self.terms[item] + right.terms[item], item)
            else:
                return_poly._add_term(self.terms[item], item)
        for item in right.terms:
            if item not in return_poly.terms:
                return_poly._add_term(right.terms[item], item)
        return return_poly

    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Mutliplication type must be of type Poly, int or float")
        if type(right) in (int, float):
            right = Poly((right, 0))
        return_poly = Poly()
        for item in self.terms:
            for other in right.terms:
                return_poly._add_term(self.terms[item] * right.terms[other], item + other)
        return return_poly
    

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError("Equality type must be of type Poly, int or float")
        if type(right) in (int, float):
            right = Poly((right, 0))
        if len(self.terms) != len(right.terms) : return False
        for item in self.terms:
            if not (item in right.terms and self.terms[item] == right.terms[item]):
                return False
        return True

    
if __name__ == '__main__':
    #Some simple tests; you can comment them out and/or add your own before
    #the driver is called.
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