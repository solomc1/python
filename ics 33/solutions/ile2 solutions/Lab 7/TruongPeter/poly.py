class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = dict()
        for value in terms:
            if type(value[0]) != int and type(value[0]) != float:
                raise AssertionError ("Coefficient is not int or float")
            if type(value[1]) != int:
                raise AssertionError ("Power is not int.")
            assert value[1] >= 0, "Power is less than 0"
            assert value[1] not in self.terms.keys(), "Power already exists"
            if value[0] == 0:
                pass
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
        new_str = ''
        count = 0
        for p, c in sorted(self.terms.items()):
            count += 1
            if count >= len(self.terms.items()):
                new_str += '({}, {})'.format(c, p)
            else:
                new_str += '({}, {}),'.format(c, p)
        return 'Poly(' + new_str + ')'

    
    def __len__(self):
        if self.terms == dict():
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        assert isinstance(arg, (int, float)), "Argument is not a int or float"
        sum_num = 0
        for p, c in self.terms.items():
            sum_num += c*(arg**p)
        return sum_num
    

    def __iter__(self):
        for p, c in iter(sorted(self.terms.items(), reverse=True)):
            yield (c, p)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Power is not an int')
        if index < 0:
            raise TypeError('Power is less than 0')
        for p, c in self.terms.items():
            if index == p:
                return c
        return 0    
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Power is not an int')
        if index < 0:
            raise TypeError('Power is less than 0')
        self.terms[index] = value
        if self.terms[index] == 0:
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Power is not an int')
        if index < 0:
            raise TypeError('Power is less than 0')
        self.terms[index] = 0
        del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Coefficient is not an int or float')
        if type(p) != int:
            raise TypeError('Power is not an int')
        if p < 0:
            raise TypeError('Power is less than 0')
        if p not in self.terms.keys():
            if c != 0:
                self.terms[p] = c
        elif p in self.terms.keys():
            self.terms[p] = self.terms[p] + c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        new_poly = Poly()
        if not isinstance(type(self), Poly) and not isinstance(right, (Poly, int, float)):
            raise TypeError('Operands are not int, float, or Poly')
        if type(right) == Poly:
            new_list = list(self.terms.keys())
            for p in right.terms.keys():
                if p not in new_list:
                    new_list.append(p)
            for p in new_list:
                if p not in self.terms.keys():
                    self.terms[p] = 0
                if p not in right.terms.keys():
                    right.terms[p] = 0
                new_poly._add_term(self.terms[p] + right.terms[p], p)
                if self.terms[p] == 0:
                    del self.terms[p]
                if right.terms[p] == 0:
                    del right.terms[p]
        elif type(right) == int or type(right) == float:
            if 0 not in self.terms.keys():
                new_poly = self
                new_poly.terms[0] = right
            else:
                new_poly = self
                new_poly.terms[0] = new_poly.terms[0]
        return new_poly
    
    def __radd__(self,left):
        new_poly = self
        if not isinstance(type(self), Poly) and not isinstance(left, (int, float)):
            raise TypeError('Operands are not int, float, or Poly')
        if 0 not in self.terms.keys():
            new_poly.terms[0] = 0
        else:
            new_poly.terms[0] = self.terms[0] + left
        return new_poly

    def __mul__(self,right):
        new_poly = Poly()
        if not isinstance(type(self), Poly) and not isinstance(right, (Poly, int, float)):
            raise TypeError('Operands are not int, float, or Poly')
        if type(right) == Poly:
            for p, c in self.terms.items():
                for value in right.terms.keys():
                    new_poly._add_term(c*right.terms[value], p+value)
        elif type(right) == int or type(right) == float:
            for p, c in self.terms.items():
                new_poly._add_term(c*right, p)
        return new_poly    
            

    def __rmul__(self,left):
        new_poly = Poly()
        if not isinstance(type(self), Poly) and not isinstance(left, (Poly, int, float)):
            raise TypeError('Operands are not int, float, or Poly')
        for p, c in self.terms.items():
            new_poly._add_term(c*left, p)
        return new_poly

    def __eq__(self,right):
        if not isinstance(type(self), Poly) and not isinstance(right, (Poly, int, float)):
            raise TypeError('Operands are not int, float, or Poly')
        if type(right) == Poly:
            for p, c in self.terms.items():
                if p not in right.terms.keys() or c not in right.terms.values():
                    return False
                if c != right.terms[p]:
                    return False
                return True
        elif type(right) == int or type(right) == float:
            if self.terms[0] == right:
                return True
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