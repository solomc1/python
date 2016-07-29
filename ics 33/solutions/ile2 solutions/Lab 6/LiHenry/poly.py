from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for key, value in terms:
            if value not in (int or float):
                raise AssertionError("Poly__init__:illegal(" + str(value) + ") must be an int or float(" + type_as_str(key)+ ")")
            if key is not int or value >= 0:
                raise AssertionError("Poly__init__:illegal(" + str(key) + ") must be greater then zero(" + str(key)+ ")")
            if key not in self.terms:
                self.terms[key] = value

#             else:
#                 raise AssertionError("Poly__init__:illegal(" + str(key) + ") powers can not repeat)")

            
 
            
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
        result = ""
        for element in self.terms.items():
            result += "Poly(({}), ({}), ({}))".format(element[0], element[1])
        return result

    
    def __len__(self):
        print (self.terms)
        result = []
        for element in self.terms.keys():
            print (element)
            result.append(element)
        return max(result)
    
    def __call__(self,arg):
        pass
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) is int and index > 0:
            return self.terms[index]
        else:
            raise TypeError("Poly.__getitem__index:(" + str(index) + "must be an int or less than zero")
        
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError("Poly.__getitem__index:(" + str(index) + "must be an int or less than zero") 
        if value == 0:
            del self.terms[index]
            
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        pass
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass

    
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