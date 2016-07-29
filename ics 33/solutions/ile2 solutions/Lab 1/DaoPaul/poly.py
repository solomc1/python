class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0]) in (int, float), 'Coefficient must be type int or type float, not type {}'.format(type(term[0]))
            assert type(term[1]) == int, 'Coefficient must be type int, not type {}'.format(type(term[0]))
            assert term[1] >= 0, 'Power must be an int whose value is >= 0'
            if term[0] != 0:
                assert term[1] not in self.terms, 'Repetition of terms with the same power is forbidden'
                self.terms[term[1]] = term[0]
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
#         jack = set()
#         for k in self.terms:
#             jack.add((k, self.terms[k]))
#         return "Poly({})".format(','.join(str(term) for term in jack))
        return "Poly({})".format(','.join(str((k, self.terms[k])) for k in sorted(self.terms, reverse = True)))

    
    def __len__(self):
        if len(self.terms) != 0:
            return max((power for power in self.terms))
        else:
            return 0
    
    def __call__(self,arg):
        total = 0
        for power in sorted(self.terms, reverse =True):
            total += (self.terms[power] * (arg ** power))
        return total
    

    def __iter__(self):
        for term in sorted(self.terms, reverse = True):
            yield (self.terms[term], term)
        pass
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError('Index must be type int, not type{}'.format(type(index)))
        elif index < 0:
            raise TypeError('Index cannot be negative')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError('Index must be type int, not type{}'.format(type(index)))
        elif index < 0:
            raise TypeError('Index cannot be negative')
        elif index in self.terms:
            if value == 0:
                self.terms.pop(index)
            else:
                self.terms[index] = value
        else:
            if value != 0:
                self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError('Index must be type int, not type{}'.format(type(index)))
        elif index < 0:
            raise TypeError('Index cannot be negative')
        elif index in self.terms:
            self.terms.pop(index)
            

#     def _add_term(self,c,p):
#         if type(p) != int:
#             raise TypeError('Power must be type int, not type{}'.format(type(p)))
#         elif p < 0:
#             raise TypeError('Power cannot be negative')
#         elif type(c) not in (int, float):
#             raise TypeError('Coefficient must be type int or type float, not type{}'.format(type(p)))
#         elif 
#         pass
       

    def __add__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('unsupported operand types Poly and {}').format(type(right))
        else:
            d = dict()
            if type(right) == Poly:
                for power in self.terms:
                    if power in right.terms:
                        d[power] = (self.terms[power] + right.terms[power])
                    else:
                        d[power] = self.terms[power]
                for powers in right.terms:
                    if powers not in self.terms:
                        d[powers] = right.terms[powers]
            else:
                d[0] = right + self.terms[0]            
            return eval("Poly({})".format(','.join(str((k, self.terms[k])) for k in sorted(self.terms, reverse = True))))

    
    def __radd__(self,left):
        return self + left
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) in (Poly, int, float):
            if type(right) == Poly:
                for power in self.terms:
                    if power in right.terms and self.terms[power] == right.terms[power]:
                        return True
                for powers in self.right:
                    if powers in self.terms and right.terms[powers] == self.terms[powers]:
                        return True
            else:
                for power in self.terms:
                    if right in self.terms[power]:
                        return True
        else:
            raise TypeError('A Poly object can only be compared with another Poly object or object of type int or type float')
        pass

    
if __name__ == '__main__':
#     Some simple tests; you can comment them out and/or add your own before
#     the driver is called.
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