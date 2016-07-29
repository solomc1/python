class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.termlist = terms
        self.terms = {} #power as key
        for value in self.termlist:
            if (type(value[0]) != int and type(value[0]) != float) or type(value[1]) != int:
                raise AssertionError('Values must be int type')
            elif value[1] < 0:
                raise AssertionError('Power must be greater than or equal to 0')
            elif value[1] in self.terms.keys():
                raise AssertionError('Power already in dict')
            elif value[0] == 0:
                value[0] 
            else:
                self.terms[value[1]] = value[0]
        
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
        returnstr = ''
        for value in self.termlist:
            returnstr += ',('+str(value[0])+','+str(value[1])+')'
        return 'Poly('+returnstr.strip(',')+')'

    
    def __len__(self):
        returnvalue = 0
        if self.terms == {}:
            return 0
        for values in self.terms:
            if values > returnvalue:
                returnvalue = values
        return returnvalue
            
        
    
    def __call__(self,arg):
        #if type(arg) != int or type(arg) != float:
        pass
            
    

    def __iter__(self):
        pass
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('Not a valid power')
        for items in self.termlist:
            if items[1] == index:
                return items[0]
        return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError('Not a valid power')
        if index in self.terms:    
            for values in self.terms:
                if index == values:
                    self.terms[index] = value
        if self.terms.get(index) == 0:
            self.terms.pop(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError('Not a valid power')
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if (type(c) != int and type(c) != float) or type(p) != int or not p >= 0:
            raise TypeError('Invalid entry values')
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = c+self.terms.get(p)
        if self.terms.get(p) == 0:
            del self.terms[p]
        
        
       

    def __add__(self,right):
        d = {}
        terms = self.terms
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError('Wrong Type')
        for values in terms:
            for others in right.terms:
                if values == others:
                    d[values] = terms.get(values) + right.terms.get(values)
        return str(d)
                    
        

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        return 0
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError('Wrong Type')
        if type(right) == Poly:
            for values in self.termlist:
                for values in right:
                    if values[0] == right[0]:
                        if values[1] == right[1]:
                            return True
        return False
            

    
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