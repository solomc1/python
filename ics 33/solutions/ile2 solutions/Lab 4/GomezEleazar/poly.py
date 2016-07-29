from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for value in terms:
            
            if type_as_str(value[0]) not in ['int', 'float']:
                raise AssertionError('Coefficient value must be of type int or float')
            
            elif type_as_str(value[1]) != 'int' or value[1] < 0:
                raise AssertionError('Power must be an int with value greater than or equal to 0')
            
            elif value[1] in self.terms:
                raise AssertionError("Polynomial cannot contain duplicate powers")
                                                                 
            elif value[0] != 0:
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
        
        pass
        

    
    def __len__(self):
        
        powers = []
        
        if self.terms == {}:
            return 0
        else:
            for power in self.terms:
                powers.append(power)
                
        powers.sort(reverse=True)
        return powers[0]
    
    def __call__(self,arg):
        
        answer = 0
        
        for power in self.terms:
            value = (arg**power) * self.terms[power]
            answer += value
            
        return answer
    

    def __iter__(self):
        
        powers = []
        
        for power in self.terms:
            powers.append(power)
            
        powers.sort(reverse=True)
            
        
            
        for power in powers:
            yield (self.terms[power], power)
                
            

    def __getitem__(self,index):
        
        if type_as_str(index) != 'int' or index < 0:
            raise TypeError('Value must be an integer that is greater than or equal to 0')
        
        elif index in self.terms:
            return self.terms[index]
        
        else:
            return 0
            

    def __setitem__(self,index,value):
        
        if type_as_str(index) != 'int' or index < 0:
            raise TypeError('Value must be an integer that is greater than or equal to 0')
        
        elif value != 0:
            self.terms[index] = value
            
        else:
            try:
                self.terms.pop(index)
            except KeyError:
                pass
        
            

    def __delitem__(self,index):
        
        if type_as_str(index) != 'int' or index < 0:
            raise TypeError('Value must be an integer that is greater than or equal to 0')
        
        else:
            try:
                self.terms.pop(index)
            except KeyError:
                pass
            

    def _add_term(self,c,p):
        
        if type_as_str(c) not in ['int', 'float']:
            raise AssertionError('Coefficient value must be of type int or float')
            
        elif type_as_str(p) != 'int' or p < 0:
            raise AssertionError('Power must be an int with value greater than or equal to 0')
        
        elif p not in self.terms and c != 0:
            self.terms[p] = c
        
        elif p in self.terms:
            self.terms[p] += c
            
            if self.terms[p] == 0:
                self.terms.pop(p)
       

    def __add__(self,right):
        
        answer = Poly()
        
        if 'Poly' not in type_as_str(self) or type_as_str(right) not in ['int', 'float']\
         and 'Poly' not in type_as_str(right):
            
            raise TypeError('Operands must be of type Poly and Poly or int or float')
        
        elif 'Poly' in type_as_str(self) and 'Poly' in type_as_str(right):
            for power in self.terms:
                answer._add_term(self.terms[power], power)
            for power in right.terms:
                if power in answer.terms:
                    answer.terms[power] += right.terms[power]
                else:
                    answer._add_term(right.terms[power], power)
                    
        else:
            for power in self.terms:
                answer._add_term(self.terms[power], power)
            
            if 0 in answer.terms:
                answer.terms[0] += right
            else:
                answer._add_term(right,0)
                
        return answer
        

    
    def __radd__(self,left):
        
        answer = Poly()
        
        if 'Poly' not in type_as_str(self) or type_as_str(left) not in ['int', 'float']\
         and 'Poly' not in type_as_str(left):
            
            raise TypeError('Operands must be of type Poly and Poly or int or float')
        
        elif 'Poly' in type_as_str(self) and 'Poly' in type_as_str(left):
            for power in self.terms:
                answer._add_term(self.terms[power], power)
            for power in left.terms:
                if power in answer.terms:
                    answer.terms[power] += left.terms[power]
                else:
                    answer._add_term(left.terms[power], power)
                    
        else:
            for power in self.terms:
                answer._add_term(self.terms[power], power)
            
            if 0 in answer.terms:
                answer.terms[0] += left
            else:
                answer._add_term(left,0)
                
        return answer
    

    def __mul__(self,right):
        
        answer = Poly()
        
        if 'Poly' not in type_as_str(self) or type_as_str(right) not in ['int', 'float']\
         and 'Poly' not in type_as_str(right):
            
            raise TypeError('Operands must be of type Poly and Poly or int or float')
        
        elif 'Poly' in type_as_str(self) and 'Poly' in type_as_str(right):
            pass
                    
        else:
            for power in self.terms:
                answer._add_term(self.terms[power] * right, power)
                
        return answer
    

    def __rmul__(self,left):
        
        answer = Poly()
        
        if 'Poly' not in type_as_str(self) or type_as_str(left) not in ['int', 'float']\
         and 'Poly' not in type_as_str(left):
            
            raise TypeError('Operands must be of type Poly and Poly or int or float')
        
        elif 'Poly' in type_as_str(self) and 'Poly' in type_as_str(left):
            pass
                    
        else:
            for power in self.terms:
                answer._add_term(self.terms[power] * left, power)
                
        return answer
    

    def __eq__(self,right):
        
        if 'Poly' not in type_as_str(self) or type_as_str(right) not in ['int', 'float']\
         and 'Poly' not in type_as_str(right):
            
            raise TypeError('Operands must be of type Poly and Poly or int or float')
        
        
    
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