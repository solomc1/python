class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        if terms != None:
            for i in terms:
                assert isinstance(i[0], (int, float)), "Coefficient must be int or float"
                assert isinstance(i[1], (int)) and i[1] >= 0, "Power must be int and positive"
            power_list = [i[1] for i in terms]
            for i in power_list:
                assert power_list.count(i) == 1, "Powers must be unique."
            self.terms = {d[1]: d[0] for d in terms if d[0] != 0}
                
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
        tup_list = []
        for i in self.terms:
            tup_list.append((self.terms[i], i))
        edit_tup = str(tup_list)
        return 'Poly(' + edit_tup[1:-1] + ')'

    
    def __len__(self):
        if self.terms == None:
            return 0
        else:
            power_list = [d for d in self.terms.keys()]
            if len(power_list) == 0:
                return 0
            else:
                return max(power_list)
    
    def __call__(self,arg):
        if self.terms == None:
            return 0
        else:
            total = 0 
            for i in self.terms:
                total += self.terms[i]*(arg**i)
            return total
    

    def __iter__(self):
        key_list = [d for d in self.terms.keys()]
        while len(key_list) != 0:
            for i in self.terms:
                try:
                    yield (self.terms[max(key_list)], key_list.pop(max(key_list)))
                except StopIteration:
                    pass
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError ('Index must be a positive integer.')
        if not index in self.terms.keys():
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError ('Index must be a positive integer.') 
        if value == 0:
            if index in self.terms.keys():
                del self.terms[index]  
        else:
            self.terms[index] = value
                         

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError ('Index must be a positive integer.') 
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if not isinstance(c, (int, float)):
            raise TypeError ('Coefficient must be an int or float')
        elif type(p) != int or not p >=0:
            raise TypeError ('Coefficient must be an int or float')
        else:
            if p not in self.terms and c != 0:
                self.terms[p] = c
            elif p in self.terms:
                self.terms[p] += c
                if self.terms[p] == 0:
                    del self.terms[p]

    def __add__(self,right):
        if type(right) == Poly:
            copy_list = [(self.terms[i], i) for i in self.terms]
            copy = Poly(*copy_list)
            for i in right.terms:
                copy._add_term(right.terms[i], i)
            return copy
        elif isinstance(right, (int, float)):
            sum_list = [(self.terms[i] + right, i) for i in self.terms]
            return Poly(*sum_list)
        else:
            raise TypeError('Addend must be an int, float, or Poly class')
        
    def __radd__(self,left):
        if type(right) == Poly:
            copy_list = [(self.terms[i], i) for i in self.terms]
            copy = Poly(*copy_list)
            for i in right.terms:
                copy._add_term(right.terms[i], i)
            return copy
        elif isinstance(right, (int, float)):
            sum_list = [(self.terms[i] + right, i) for i in self.terms]
            return Poly(*sum_list)
        else:
            raise TypeError('Addend must be an int, float, or Poly class')
    

    def __mul__(self,right):
        if type(right) == Poly:
            if right.terms == None:
                return 0
            else:
                copy_list = [(self.terms[i], i) for i in self.terms]
                copy = Poly(*copy_list)
                for i in right.terms:
                    copy[i+i] *= right[i]
                return copy
        elif isinstance(right, (int, float)):
            product = [(self.terms[i]*right, i) for i in self.terms]
            return Poly(*product)
    

    def __rmul__(self,left):
        if isinstance(left, (int, float)):
            product = [(self.terms[i]*left, i) for i in self.terms]
            return Poly(*product)
    

    def __eq__(self,right):
        if type(right) == int or type(right) == float:
            key_list = [d for d in self.terms.keys()]
            if key_list == [0]:
                return self.terms[0] == right
            else:
                return False
        elif type(right) == Poly:
            if self.__len__() == right.__len__():
                for i in self.terms:
                    if i not in right.terms:
                        return False
                    else:
                        return self.terms[i] == right.terms[i]
            else:
                return False
        else:
            raise TypeError('Right must be an int, float or Poly class')
    
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