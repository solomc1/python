class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for each in terms:
            assert type(each[0]) is int or type(each[0]) is float, "Poly.__init__: " + str(each[0]) + " is not an int or float"
            assert type(each[1]) is int and each[1] >= 0, "Poly.__init__: " + str(each[1]) + " is less than 0 or not an int" 
            if each[1] in self.terms.keys():
                assert each[0] == 0 or self.terms[each[1]] == 0, "Poly.__init__: Cannot have multiples of a power " + str(each[1]) + " in the polynomial"
            self.__setitem__(each[1], each[0])
        
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
        if len(self.terms) == 0: return "Poly()"
        else:
            reprisent = "Poly(("
            for each in self.terms.items():
                reprisent += str(each[1]) + "," + str(each[0]) + "),("
            return reprisent[0:-2] + ")"
            
    
    def __len__(self):
        if len(self.terms) == 0: return 0
        else:
            high_power = 0
            for each in self.terms.keys():
                if each > high_power: high_power = each
            return high_power
    
    def __call__(self,arg):
        assert type(arg) is int or type(arg) is float, "Poly.__call__: " + str(arg) + " is not an int or flaot"
        answer = 0
        for each in self.terms.items():
            answer += each[1] * (arg ** each[0])
        return answer

    def __iter__(self):
        for each in sorted(self.terms.keys(), reverse = True):
            yield (self.terms[each], each)
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError("Poly.__getitem__: " + str(index) + "is not an int or is less than 0")
        elif index in self.terms.keys(): return self.terms[index]
        else: return 0

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0: raise TypeError("Poly.__setitem__: " + str(index) + "is not an int or is less than 0")
        if value == 0: 
            if index in self.terms.keys(): del(self.terms[index])
        else: self.terms[index] = value

    def __delitem__(self,index):
        if type(index) is not int or index < 0: raise TypeError("Poly.__delitem__: " + str(index) + "is not an int or is less than 0")
        elif index in self.terms.keys(): del(self.terms[index])

    def _add_term(self,c,p):
        if type(p) is not int or p < 0: raise TypeError("Poly._add_term: " + str(p) + "is not an int or is less than 0")
        if type(c) is not int and type(c) is not float: raise TypeError("Poly._add_term: " + str(c) + " is not an int or a float")
        if p not in self.terms.keys() and c != 0: self.terms[p] = c
        elif p in self.terms.keys(): 
            self.terms[p] += c
            if self.terms[p] == 0: self.__delitem__(p)


    def __add__(self,right):
        if type(right) is not Poly and type(right) is not int and type(right) is not float: raise TypeError("Poly.__add__: " + right + " is not an int, float, or polynomial")
        new_poly = Poly()
        if type(right) is not Poly:
            for each in self:
                if each[1] != 0: new_poly[each[1]] = each[0]
                else: new_poly[0] = each[0] + right
        else:
            count = []
            for each in self:
                new_poly[each[1]] = each[0]
                count.append(each[1])
            for each in right:
                if each[1] in count:
                    new_poly[each[1]] = new_poly[each[1]]+ each[0]
                else: new_poly[each[1]] = each[0]
        return new_poly
            
    
    def __radd__(self,left):
        return self.__add__(left)
    

    def __mul__(self,right):
        if type(right) is not Poly and type(right) is not int and type(right) is not float: raise TypeError("Poly.__mul__: " + right + " is not an int, float, or polynomial")
        new_poly = Poly()
        if type(right) is Poly:
            for each_r in right:
                for each_n in self:
                    new_poly[each_n[1] * each_r[1]] = each_n[0] * each_r[0]
        else:
            for each in self:
                new_poly[each[1]] = each[0] * right 
        return new_poly 
            

    def __rmul__(self,left):
        return self.__mul__(left)
    

    def __eq__(self,right):
        if type(right) is not Poly and type(right) is not int and type(right) is not float: raise TypeError("Poly.__eq__: " + right + " is not an int, float, or polynomial")
        if type(right) is Poly:
            answer = True
            for each_s,each_r in zip(self,right):
                if each_s != each_r: answer = False
                return answer
        else:
            if len(self.terms) == 1 and self[list(self.terms.keys())[0]] == right: return True
            else: return False
    
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
#    print('  p+p:',p+p)
#    print('  p+2:',p+2)
#    print('  p*p:',p*p)
#    print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()