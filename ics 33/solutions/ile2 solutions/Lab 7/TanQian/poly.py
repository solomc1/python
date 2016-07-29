class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for tuples in terms:
            assert type(tuples[0]) is int or type(tuples[0]) is float, 'illegal power in: ' + str(tuples)
            assert type(tuples[1]) is int and tuples[1] >= 0, 'power must be an integer'
            if tuples[1] in self.terms:
                assert tuples[0] == self.terms[tuples[1]], 'illegal power in: ' + tuples
            elif tuples[0] == 0:
                pass
            else:
                self.terms[tuples[1]]=tuples[0]
        
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
        tuple_format = []
        for k, v in self.terms.items():
            tuple_format.append('({}, {})'.format(v, k))
        final_str = 'Poly('
        for length in range(len(tuple_format)):
            if length < len(tuple_format)-1:
                final_str += tuple_format[length] + ', '
            else:
                final_str += tuple_format[length]
        return final_str + ')'
            

    
    def __len__(self):
        if self.terms is {}:
            return 0
        else:
            answer = 0
            for k in self.terms.keys():
                if k > answer:
                    answer = k
        return answer
    
    def __call__(self,arg):
        equation = self.__str__()
        equation = equation.replace('x', "*(" +str(arg)+")")
        equation = equation.replace('^', '**')
        return eval(equation)
    

    def __iter__(self):
        tuple_list = []
        for k, v in sorted(self.terms.items(), reverse = True):
            tuple_list.append((v, k))
        return iter(tuple_list)
            
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Indexing value is not integer.')
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Cannot set a non-integer.')
        elif value == 0:
            pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Cannot delete non-integers.')
        elif index not in self.terms.keys():
            pass
        else:
            del self.terms[index]
            
        
            

    def _add_term(self,c,p):
        if c == 0:
            pass
        elif p not in self.terms:
            self.terms[p] = c
        else:
            for k, v in self.terms.items():
                if p == k:
                    self.terms[k] = c + v
       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError()
        elif type(right) is Poly:
            return 

    
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