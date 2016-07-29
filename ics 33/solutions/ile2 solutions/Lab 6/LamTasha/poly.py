class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms

        for term in terms:        
            for t in term:
                if type(t) != int and type(t) != float:
                    raise AssertionError("Error. Tuple is not an int or float.")
        for x, y in terms:
            if type(x) != int and type(x) != float:
                raise AssertionError("Error. Tuple is not an int or float.")
        

#         for x,y in terms:
#             if type(x) != int or type(y) != int or type(y) != float or type(y) != float:
#                 print(x, y)
#                 raise AssertionError("Error. Tuple is not an int or float.")
#         if terms[1] < 0:
#             raise AssertionError("Error. Coefficent is less than 0.")

        self.terms = {}
        for term in terms:
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
        test = set()
        test_2 = {}
        for k, v in self.terms.items():
            test_2[v]=k
        for i in test_2.items():
            test.add(i)
        return "Poly" + str(tuple(test))

    def __len__(self):
        check_list = []
        for k, v in self.terms.items():
            check_list.append(k)
        return max(check_list)
    
    def __call__(self,arg):
        total = 0
        for k, v in self.terms.items():
            t = (v) * (arg^k)
            total += t
        return total
    

    def __iter__(self):
        def _gen(iterable):
            yield iterable
            

    def __getitem__(self,index):
        pass
            

    def __setitem__(self,index,value):
        pass
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        pass
       

    def __add__(self,right):
        if type(right) == int or type(right) == float:
            pass
        elif type(right) == Poly:
            pass

    
    def __radd__(self,left):
        return self.terms + left
    

    def __mul__(self,right):
        if type(right) == int or type(right) == float:
            pass
        elif type(right) == Poly:
            pass
    

    def __rmul__(self,left):
        return self.terms * left
    

    def __eq__(self,right):
        if type(right) == int or type(right) == float:
            return self.terms == right
        elif type(right) == Poly:
            check_1 = {}
            check_2 = {}
            for k, v in self.terms.items():
                check_1[v] = k
            for k, v in self.right.items():
                check_2[v] = k
            return sorted(check_1) == sorted(check_2)      
        else:
            raise TypeError("Error. Ints, floats, and Polys only.")

    
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