class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {terms}
        for each in terms:

            assert type(each) is tuple, "Argument entered is not in correct tuple format"
            assert type(each[0]) is int and each[-1] >= 0,"Power is not an int; Power is negative"
            assert type(each[-1]) is int,"Coefficient is not an int" 
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
        return "Poly({})".format(str(self.terms))
    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return self.terms[0][-1]
    
    def __call__(self,arg):
        assert type(arg) is int or type(arg) is float,"Argument is not int/float type"
        

    def __iter__(self):
        for each in self.terms:
            return each
            

    def __getitem__(self,index):
        assert type(index) is int or index > 0,""
        if index not in self.terms.values():
            return 0
            

    def __setitem__(self,index,value):
        assert type(index) is int or index > 0,""
        if value == 0:
            self.terms.pop(value)
            

    def __delitem__(self,index):
        assert type(index) is int or index >0,""
        if index in self.terms.values():
            self.terms.popitem(index)
            

    def _add_term(self,c,p):
        assert type(c) is int or type(c) is float, "Coefficient is not int or float"
        assert type(p) is int and p>=0, "Power is not int; Power is negative"
        if p not in self.terms and p != 0:
            self.terms.update(c,p)


    def __add__(self,right):
        assert type(self.terms) is Poly,"item on left is not a Polynomial"
        assert type(right) is Poly or int or float,"Item on the right is not a Polynomial or Int or Float"

    
    def __radd__(self,left):
        assert type(self.terms) is Poly,"item on left is not a Polynomial"
        assert type(left) is Poly or int or float,"Item on the left is not a Polynomial or Int or Float"
        

    def __mul__(self,right):
        assert type(self.terms) is Poly,"item on left is not a Polynomial"
        assert type(right) is Poly or int or float,"Item on the right is not a Polynomial or Int or Float"
    

    def __rmul__(self,left):
        assert type(self.terms) is Poly,"item on left is not a Polynomial"
        assert type(left) is Poly or int or float,"Item on the left is not a Polynomial or Int or Float"
    

    def __eq__(self,right):
        assert type(right) is Poly,""
        assert type(self.terms) is Poly,""

    
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