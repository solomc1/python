
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) in (int,float), 'Poly.__init__: ' + str(i[0]) + ' is not int or float'
            assert type(i[1]) == int and i[1] >= 0, "Poly.__init__: illegal power in: " + str(i)
            if i[0] != 0:
                self.terms[i[1]] = i[0]

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
        string = 'Poly('
        for k,v in self.terms.items():
            string += '({},{})'.format(k,v)
        string += ')'
        return string

    
    def __len__(self):
        return max(self.terms.keys()) if len(self.terms) != 0 else 0
    
    def __call__(self,arg):
        value = 0
        for power,coef in self.terms.items():
            value += coef*(arg**power)
        return value
    

    def __iter__(self):
#         sorted_power_list = sorted(list(self.terms.keys()), key = lambda(i: i[1]), reverse = True)
        sorted_list = sorted(list(self.terms.items()), key = lambda i: i[0], reverse = True)
        for power,coef in sorted_list:
            yield (coef, power)
             

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__getitem__: illegal power' + str(index))
        elif index not in self.terms.keys():
            return 0
        else:
            for i in self.terms.items():
                if index in i:
                    return i[1] 
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Poly.__setitem__: illegal power ' + str(index))
        if value == 0:
            del self.terms[index]
        else:
            self.terms.pop(index)
            self.terms[index] = value
            

    def __delitem__(self,index):
        pass
            

    def _add_term(self,c,p):
        if type(c) in (int, float) and type(p) == int and p >= 0 :
            if p in self.terms:
                self.terms[p] = self.terms[p] +  c
            else:
                self.terms[p] = c
        else:
            raise TypeError('Poly._add_term: illegal coefficient: ' + str(c) + ' or power: ' + str(p))
       

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