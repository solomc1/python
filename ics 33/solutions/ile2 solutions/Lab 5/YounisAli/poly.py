class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        for valTup in terms:
            
            coeff,term = valTup
            
            if (type(coeff) != int) and (type(coeff) != float):
                raise AssertionError("Coeficient must be an int or a float in {}".format(valTup))
            
            if type(term) != int or term < 0 :
                raise AssertionError("Power Term must be an int greater than or equal to 0 in ".format(valTup)) 
            
            if term in self.terms.keys():
                raise AssertionError("Term {} defined more than once".format(term))
            
            if(coeff != 0):
                self.terms[term] = coeff
        
        
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
        
        if len(self.terms.keys()) <= 0:
            return "Poly()"
        
        poly_string = "Poly("
        
        for key in self.terms.keys():
            tup_packing_string = "({},{})".format(self.terms[key],key)
            poly_string += tup_packing_string + ","
        
        poly_string = poly_string[:-1] + ")"            
        return poly_string


    
    def __len__(self):
        if(len(self.terms.keys()) > 0):
            return max(self.terms.keys())
        return 0
    
    def __call__(self,arg):
        total = 0
        for key in self.terms.keys():
            inter_sum = arg ** key
            inter_sum = inter_sum * self.terms[key] 
            total += inter_sum
        return total
    

    def __iter__(self):
        def gener(self):
            for key in sorted(self.terms.keys(),reverse = True):
                yield (self.terms[key],key)
                
        return gener(self)
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("Index value :{} is not an int".format(index))
        if index < 0: 
            raise TypeError("Pndex : cannot be less than 0".format(index))
        
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("Power value :{} is not an int".format(index))
        if index < 0: 
            raise TypeError("Power : cannot be less than 0".format(index))
        
        if value == 0:
            if index in self.terms.keys():
                self.terms.pop(index)
        else:
            self.terms[index] = value
        
        

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("Power value :{} is not an int".format(index))
        if index < 0: 
            raise TypeError("Power : cannot be less than 0".format(index))
        
        if index in self.terms.keys():
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        
        if type(c) != int and type(c) != float:
            raise TypeError("Coefficient must be an int or a float")
        
        if type(p) != int:
            raise TypeError("Power value :{} is not an int".format(p))
        if p < 0: 
            raise TypeError("Power : cannot be less than 0".format(p))
        
        
        if p in self.terms.keys():
            if (self.terms[p] + c) == 0:
                self.terms.pop(p)
            else:
                self.terms[p] =  self.terms[p] + c
        elif c != 0:
            self.terms[p] = c

    def __add__(self,right):
        
        if type(right) == int or type(right) == float:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(self.terms[key], key)
                
            tmp_poly._add_term(right,0)
            return tmp_poly
            
        if type(right) == Poly:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(self.terms[key], key)
            
            for key in right.terms.keys():
                tmp_poly._add_term(right.terms[key], key)
            return tmp_poly
            
        raise TypeError("Right Operand must be either an int, float or Ploy")
        
        
        

    
    def __radd__(self,left):
        if type(left) == int or type(left) == float:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(self.terms[key], key)
                
            tmp_poly._add_term(left,0)
            return tmp_poly
            
        if type(left) == Poly:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(self.terms[key], key)
            
            for key in left.terms.keys():
                tmp_poly._add_term(left.terms[key], key)
            return tmp_poly
            
        raise TypeError("Left Operand must be either an int, float or Ploy")
    

    def __mul__(self,right):
        if type(right) == int or type(right) == float:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(right * self.terms[key], key)
            return tmp_poly
        
        
        if type(right) == Poly:
            tmp_poly = Poly()
            
            for key in self.terms.keys():
                for rkey in right.terms.keys():
                    tmp_poly._add_term(self.terms[key] * right.terms[rkey], key + rkey)
                    
            return tmp_poly
            
        raise TypeError("Right Operand must be either an int, float or Ploy")
        
    

    def __rmul__(self,left):
        if type(left) == int or type(left) == float:
            tmp_poly = Poly()
            for key in self.terms.keys():
                tmp_poly._add_term(left * self.terms[key], key)
            return tmp_poly
         
         
        if type(left) == Poly:
            tmp_poly = Poly()
            for key in self.terms.keys():
                for lkey in left.terms.keys():
                    tmp_poly._add_term(self.terms[key] * left.terms[lkey], key + lkey)
            return tmp_poly
             
        raise TypeError("Left Operand must be either an int, float or Ploy")
        
    

    def __eq__(self,right):
        
        if type(right) == Poly:
            if len(right.terms.keys()) != len(self.terms.keys()):
                return False
            for key in self.terms.keys():
                if key not in right.terms.keys():
                    return False
            
            for key in self.terms.keys():
                if self.terms[key] != right.terms[key]:
                    return False
                
            return True
        
        if type(right) == int or type(right) == float:
            if len(self.terms.keys()) != 1:
                return False
            keys = list(self.terms.keys())
            if keys[0] != 0:
                return False
            if self.terms[keys[0]] != right:
                return False
            return True
        
        raise TypeError("Right operand must be an int, float or Poly type")
            
            

    
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