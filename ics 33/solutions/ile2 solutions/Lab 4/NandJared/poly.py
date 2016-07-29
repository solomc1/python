class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            if term[0] != 0:
                assert type(term[0]) in [int,float], 'Coefficient must be an int or a float'
                assert type(term[1]) == int and term[1] >= 0, 'Power must be an int and must be 0 or greater than 0'
                assert term[1] not in self.terms, 'Power must not already be in the dict'
                self.terms.update({term[1]:term[0]})
        
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
        
        l = []
        for item in self.terms:
            l.append((self.terms[item],item))
        return 'Poly{}'.format(tuple(l))
        
    
    def __len__(self):
        
        l = []
        if len(self.terms) == 0:
            return 0
        else:
            for item in self.terms:
                l.append(item)
            return max(l)
            
    def __call__(self,arg):
        total = 0
        for item in self.terms:
            total += self.terms[item]*((arg)**item)
        return total
    

    def __iter__(self):
        for item in sorted(self.terms, reverse = True):
            yield (self.terms[item],item)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be 0 or greater than 0')
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index must be 0 or greater than 0')
        if index in self.terms:
            if value == 0:
                self.terms.pop(index)
            else:
                self.terms[index] = value
        else:
            if value != 0:
                self.terms[index] = value
            
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be 0 or greater than 0')
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if c not in [int,float]:
            raise TypeError
        if type(p) != int:
            raise TypeError
        if p < 0:
            raise TypeError
        
        if p not in self.terms and p != 0:
            self.terms.update({p:c})
        if p in self.terms:
            val = self.terms[c] + c
            if val == 0:
                self.terms.pop(p)
            else:
                self.terms[p]+=c

    def __add__(self,right):
        new_dic = {}
        if type(right) == Poly:
            for item in self.terms:
                if item in right:
                    new_dic.update({item:self.terms[item] + right.terms[item]})
                else:
                    new_dic.update({item:self.terms[item]})
        elif type(right) in [int,float]:
            new_dic.update()
        else:
            raise TypeError
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) == Poly:
            return self.terms == right.terms
        elif type(right) in [int,float]:
            l = []
            for item in self.terms:
                if item == 0:
                    l.append(self.terms[item])
            return right in l
        else:
            raise TypeError
    
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
    