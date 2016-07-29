#Malvin Tanbun, Lab #1
#ICS 33 Spring 2014
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        if len(*terms) > 1:
            for i in terms:
                assert i[0] in [int,float], 'Coefficient ' + str(i[0]) + ' is not numeric'
                assert i[1] >= 0, 'Power ' + str(i[1]) + ' is not valid because it is not positive'
                assert (i[1] in self.terms.keys() and i[0] == self.terms[i[1]]), 'The power ' + str(i[1]) + ' cannot be added because it is already inside the dictionary'
                self.terms.update({i[1] : i[0]})
        else:
            assert terms[0] in [int,float], 'Coefficient ' + str(terms[0]) + ' is not numeric'
            assert terms[1] >= 0, 'Power ' + str(terms[1]) + ' is not valid because it is not positive'
            assert (terms[1] in self.terms.keys() and terms[0] == self.terms[terms[1]]), 'The power ' + str(i[1]) + ' cannot be added because it is already inside the dictionary'
            self.terms.update({terms[1] : terms[0]})
        
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
        strA = ''
        for i in self.terms.items():
            strA += i
            
        return 'Poly('+str(strA)+')'
        pass

    
    def __len__(self):
        highest = 0
        if self.terms == None:
            return 0
        for i in self.terms.keys():
            if i < highest:
                highest = i
        return highest
        pass
    
    def __call__(self,arg):
        total = 0
        for i in self.terms.keys():
            total += (arg**i)*self.terms[i]
        return total
        pass
    

    def __iter__(self):
        for i in self.terms.items().sort(reverse = True):
            return i
        pass
            

    def __getitem__(self,index):
        if (index not in [int,float] and index < 0):
            raise TypeError('Value ' + str(index) + 'must be numeric and positive number')
        else:
            if index not in self.terms.keys():
                return 0
            else:
                return self.terms[index]
        pass
            

    def __setitem__(self,index,value):
        if (index not in [int,float] and index < 0):
            raise TypeError('Value ' + str(index) + 'must be numeric and positive number')
        else:
            if value == 0:
                self.terms.pop(index)
            else:
                self.terms.update({index : value})
        pass
            

    def __delitem__(self,index):
        if (index not in [int,float] and index < 0):
            raise TypeError('Value ' + str(index) + 'must be numeric and positive number')
        else:
            if index in self.terms.keys():
                self.terms.pop(index)
        pass
            

    def _add_term(self,c,p):
        if p not in self.terms.keys() and p != 0:
            self.terms.__setitem__(p,c)
        else:
            if self.terms[p] + c == 0:
                self.__delitem__(p)
            else:
                self.terms.__setitem__(p, c+self.terms[p])
        pass
       

    def __add__(self,right):
        if type(right) == [int,float]:
            self.__radd__(right)
        else:
            for i in self.terms.items():
                for j in right.terms.items():
                    if i[0] == j[0]:
                        i[1] += j[1]
        pass

    
    def __radd__(self,left):
        if type(left) != [int, float]:
            raise TypeError('Variable is not numeric')
        else:
            for i in self.terms.values():
                i += left
        pass
    

    def __mul__(self,right):
        if type(right) == [int,float]:
            self.__rmul__(right)
        else:
            for i in self.terms.items():
                for j in right.terms.items():
                    i[0] += j[0]
                    i[1] *= j[1]
        pass
    

    def __rmul__(self,left):
        if type(left) != [int, float]:
            raise TypeError('Variable is not numeric')
        else:
            for i in self.terms.values():
                i *= left
        pass
    

    def __eq__(self,right):
        if right in [int,float]:
            return self.terms[0] == right
        else:
            condition = True
            for i in self.__iter__():
                for j in right.__iter():
                    if i == j:
                        condition = True
                        break
                    else:
                        condition = False
                if condition == False:
                    return condition
            return condition
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