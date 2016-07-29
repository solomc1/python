## Name: Desmond Garrido
## SID: 78457276 
## Lab 1

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for term in self.terms:
            if term != tuple:
                raise TypeError('Must input a tuple whose first number is the coefficient and second number it the power')
            for coef in terms:
                if coef[0] == 0:
                    raise AssertionError('Coefficient cannot be 0')
                elif coef[0] != float or int:
                    raise AssertionError('Coefficient must be float or int')
                elif coef[1] != int:
                    raise AssertionError('Power must be int')
                elif coef[1]  < 0:
                    raise AssertionError('Power must be an int greater than or equal to 0')
                elif coef[1] in terms:
                    raise AssertionError('Combine all like terms')
                
        
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
    
    def __repr__(self) -> str:
        return '{}'.format(p)

    
    def __len__(self):
        for keys in sorted(self.terms, reverse = True):
            return keys[0]
        if len(p) == 0:
            return 0
    
    def __call__(self,arg):
        for calling in p:
            if calling == 'x':
                calling.replace(arg)
                return p
    
    def __iter__(self):
        for variable in p:
            if variable == 'x':
                p('x').replace()

    def __getitem__(self,index):
        for key,value in self.terms:
            if index == value:
                return key
            elif index < 0:
                raise TypeError('Power cannot be lower than 0')
            elif index != value:
                return int(0)
            

    def __setitem__(self,index,value):
        if index < 0:
            raise TypeError('Power cannot be lower than 0')
        elif index != type(int):
            raise TypeError('Power must be an integer')
        elif index == 0:
            del(index,value)
        else:
            return (index,value)

    def __delitem__(self,index):
        if index < 0 or index != type(int):
            raise TypeError('Power must be an integer greater than or equal to 0')
        elif index in p:
            p.remove(index)

    def _add_term(self,c,p):
        if c != type(int) or c != type(float):
            raise TypeError('Coefficient must be an integer')
        elif p < 0 or p != type(int):
            raise TypeError('Power must be an integer greater than or equal to 0')
        for key,val in self.terms:
            if key == p:
                val + c
                if key == 0:
                    del(key,val)
           

    def __add__(self,right):
        if right != type(int) or right != type(float):
            raise TypeError('Must be integer or float')
        return p + right

    
    def __radd__(self,left):
        if left != type(int) or left != type(float):
            raise TypeError('Must be integer or float')
        return left + p
    

    def __mul__(self,right):
        if right != type(int) or right != type(float):
            raise TypeError('Must be integer or float')
        return p * right
    

    def __rmul__(self,left):
        if left != type(int) or left != type(float):
            raise TypeError('Must be integer or float')
        return left * p
    

    def __eq__(self,right):
        if right != type(int) or right != type(float):
            raise TypeError('Must be integer or float')
        elif p == right:
            return True
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