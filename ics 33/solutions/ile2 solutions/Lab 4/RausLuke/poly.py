# Luke Raus lab 4, 30456893

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for each in terms:
            assert type(each[0]) == int or type(each[0]) == float, "I'm sorry coefficient must be type int or float not {}".format(type(each[0])) 
            assert type(each[1]) == int and each[1] >= 0, "I'm sorry but put must be an int greater than 0"
            if each[0] != 0:
                assert each[1] not in self.terms,"I'm sorry that power has already been assigned a value"
                self.terms[each[1]] = each[0]
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
        repr_str = "Poly("
        poly_items = list(self.terms.items())
        for each in range(len(poly_items)):
            if each < len(poly_items)-1:
                repr_str += "({},{})".format(str(poly_items[each][1]),str(poly_items[each][0]))
                repr_str += ","
            else:
                repr_str += "({},{})".format(str(poly_items[each][1]),str(poly_items[each][0]))
        repr_str += ")"
        return repr_str

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        assert type(arg) == int or type(arg) == float, "I'm sorry arg x must be of type int or float not {}".format(type(arg))
        result = 0
        for each in self.terms.items():
            result += (arg**each[0])*each[1]
        return result

    def __iter__(self):
        iter_list =[(each[1],each[0]) for each in self.terms.items()]
        iter_list.sort(key=lambda x : x[1], reverse=True)
        return iter_list.__iter__()
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("I'm sorry but index must be of type int and greater or equal to 0 not {}".format(index))
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("I'm sorry but index must be of type int and greater or equal to 0 not {}".format(index))
        if value == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index] = value    

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("I'm sorry but index must be of type int and greater or equal to 0 not {}".format(index))
        if index in self.terms:
            self.terms.pop(index)    

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError("I'm sorry but the coefficient must be of type int or float not {}".format(type(c)))
        elif type(p) != int and p < 0:
            raise TypeError("I'm sorry but power must be of type int and greater than or equal to 0 not {}".format(p))
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                self.terms.pop(p)

    def __add__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError("I'm sorry but can only add types(int, float or Poly) not {}".format(type(right)))
        result = Poly()
        if type(right) == int or type(right) == float:
            add_poly = Poly((right,0))
            for each in self:
                result._add_term(each[0], each[1])
            for every in add_poly:
                result._add_term(every[0], every[1])
        elif type(right) == Poly:
            for each in self:
                result._add_term(each[0],each[1])
            for every in right:
                result._add_term(every[0], every[1])
        return result
    
    def __radd__(self,left):
        if type(left) != int and type(left) != float and type(left) != Poly:
            raise TypeError("I'm sorry but can only add types(int, float or Poly) not {}".format(type(left)))
        result = Poly()
        if type(left) == int or type(left) == float:
            add_poly = Poly((left,0))
            for each in self:
                result._add_term(each[0], each[1])
            for every in add_poly:
                result._add_term(every[0], every[1])
        elif type(left) == Poly:
            for each in self:
                result._add_term(each[0],each[1])
            for every in left:
                result._add_term(every[0], every[1])
        return result
    

    def __mul__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError("I'm sorry but can only mul types(int, float or Poly) not {}".format(type(right)))
        result = Poly()
        if type(right) == int or type(right) == float:
            for each in self:
                result._add_term(right*each[0], each[1])
        elif type(right) == Poly:
            for each in self:
                for every in right:
                    result._add_term(each[0]*every[0], each[1]+every[1])
        return result
    

    def __rmul__(self,left):
        if type(left) != int and type(left) != float and type(left) != Poly:
            raise TypeError("I'm sorry but can only mul types(int, float or Poly) not {}".format(type(left)))
        result = Poly()
        if type(left) == int or type(left) == float:
            for each in self:
                result._add_term(left*each[0], each[1])
        elif type(left) == Poly:
            for each in self:
                for every in left:
                    result._add_term(each[0]*every[0], each[1]+every[1])
        return result
    
    def __eq__(self,right):
        if type(right) != int and type(right) != float and type(right) != Poly:
            raise TypeError("I'm sorry but can only == types(int, float or Poly) not {}".format(type(right)))
        if type(right) == Poly and type(self) == Poly:
            return right.terms == self.terms
        elif type(right) == int or type(right) == float:
            if len(list(self.terms.items())) == 1:
                return right == self.terms[0]
            else:
                return False

    
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