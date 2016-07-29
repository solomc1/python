from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for item in terms:
            if item[1] in self.terms:
                raise AssertionError('the given power in this item was already used: {}'.format(item))
            if type(item[0]) not in [int, float]:
                raise AssertionError('illegal coefficient in: {}'.format(item))
            if type(item[1]) is not int or item[1] < 0:
                raise AssertionError('illegal power in: {}'.format(item))
            if item[0] == 0:
                pass
            else:
                self.terms[item[1]] = item[0]
        
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
        result_string = ''
        count = 0
        for item in self.terms:
            result_string += '(' + str(self.terms[item]) + ',' + str(item) + ')'
            if count != len(self.terms) - 1:
                result_string += ','
            count += 1
        return 'Poly(' + result_string + ')'

    
    def __len__(self):
        if self.terms != {}:
            return max(self.terms.keys())
        else:
            return 0
    
    def __call__(self,arg):
        total = 0
        for item in self.terms:
            total += self.terms[item]*arg**item
        return total
    

    def __iter__(self):
        for item in sorted(self.terms,reverse = True):
            yield(self.terms[item], item)

    def __getitem__(self,index):
        if type(index) is not int:
            raise TypeError('unsupported type for __getitem__ :' + type_as_str(index))
        if index < 0:
            raise TypeError('given power was less than 0: ' + str(index))
        if index in self.terms:
            return self.terms[index]
        else:
            return 0            

    def __setitem__(self,index,value):
        if type(index) is not int:
            raise TypeError('unsupported type for __setitem__ :' + type_as_str(index))
        if index < 0:
            raise TypeError('given power was less than 0: ' + str(index))
        if value == 0:
            if value in self.terms.values():
                for item in self.terms:
                    if self.terms[item] == 0:
                        self.terms.pop(item)
            else:
                pass
        if index in self.terms:
            if value != 0:
                self.terms[index] = value
            else:
                self.terms.pop(index)
        else:
            if value != 0:
                self.terms[index] = value

    def __delitem__(self,index):
        if type(index) is not int:
            raise TypeError('unsupported type for __delitem__ :' + type_as_str(index))
        if index < 0:
            raise TypeError('given power was less than 0: ' + str(index))
        if index not in self.terms:
            pass
        else:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
            raise TypeError('unsupported type for polynomial coefficient:' + type_as_str(c))
        if type(p) is not int:
            raise TypeError('unsupported type for polynomial power:' + type_as_str(p))
        if p < 0:
            raise TypeError('given power was less than 0: ' + str(p))
        if p not in self.terms and c != 0:
            self.terms[p] = c
        elif p in self.terms:
            test_value = self.terms[p] + c
            if test_value == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = test_value
       

    def __add__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('unsupported type for +: ' + type_as_str(right) + ' and ' + type_as_str(self))
        result = Poly()
        for pair in self:
            result._add_term(pair[0],pair[1])
        if type(right) in [int,float]:
            result._add_term(right,0)
        elif type(right) == Poly:
            for pair in right:
                result._add_term(pair[0],pair[1])
        return result

    
    def __radd__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError('unsupported type for +: ' + type_as_str(left) + ' and ' + type_as_str(self))
        result = Poly()
        for pair in self:
            result._add_term(pair[0],pair[1])
        if type(left) in [int,float]:
            result._add_term(left,0)
        elif type(left) == Poly:
            for pair in left:
                result._add_term(pair[0],pair[1])
        return result
    

    def __mul__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('unsupported type for *: ' + type_as_str(right) + ' and ' + type_as_str(self))
        result = Poly()
        if type(right) == Poly:
            for pair1 in self:
                for pair2 in right:
                    result._add_term(pair1[0]*pair2[0],pair1[1] + pair2[1])
        elif type(right) in [int,float]:
            for pair in self:
                result._add_term(right*pair[0],pair[1])
        return result
    

    def __rmul__(self,left):
        if type(left) not in [int,float,Poly]:
            raise TypeError('unsupported type for *: ' + type_as_str(left) + ' and ' + type_as_str(self))
        result = Poly()
        if type(left) == Poly:
            for pair1 in self:
                for pair2 in left:
                    result._add_term(pair1[0]*pair2[0],pair1[1] + pair2[1])
        elif type(left) in [int,float]:
            for pair in self:
                result._add_term(left*pair[0],pair[1])
        return result
    

    def __eq__(self,right):
        if type(right) not in [int,float,Poly]:
            raise TypeError('unsupported type for ==: ' + type_as_str(self) + ' and ' + type_as_str(right))
        truth = True
        if type(right) == Poly:
            for pair in self:
                if pair[1] in right.terms:
                    if pair[0] == right.terms[pair[1]]:
                        truth = True
                    else:
                        truth = False
        elif type(right) in [int,float]:
            if len(self.terms) == 1:
                if 0 in self.terms:
                    if self.terms[0] == right:
                        truth = True
                    else:
                        truth = False
            else:
                truth = False
        return truth
            

    
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

    