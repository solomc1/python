class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for coeff, power in terms:
            assert (power not in self.terms.keys()) and type(power) == int and power >= 0 and (type(coeff) == int or type(coeff) == float)
            if coeff != 0:
                self.terms[power] = coeff
            
                
            
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
        s = ""
        for p, c in self.terms.items():
            s += str((c,p)) + ","
        return "Poly({})".format(s.strip(","))

    
    def __len__(self):
        powers = self.terms.keys()
        if len(powers) == 0:
            return 0
        else:
            return max(powers)
    
    def __call__(self,arg):
        evaluated = 0
        for p,c in self.terms.items():
            evaluated += c*(arg**p)
        return evaluated
    

    def __iter__(self):
        return iter(sorted([(c,p) for p,c in self.terms.items()], key=lambda x:x[1], reverse=True))
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        elif index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError
        elif value != 0:
            self.terms[index] = value
        elif index in self.terms.keys():
            del self.terms[index]
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        elif index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if (type(c) != int and type(c) != float) or type(p) != int or p < 0:
            raise TypeError
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys() and c != 0:
            self.terms[p] += c
        if p in self.terms.keys() and (c == 0 or self.terms[p] == 0):
            del self.terms[p]
            
       

    def __add__(self,right):
        summed = {}
        for p,c in self.terms.items():
            summed[p] = c
        if type(right) == Poly:
            for p,c in right.terms.items():
                if p in summed.keys():
                    summed[p] += c
                else:
                    summed[p] = c
                if summed[p] == 0:
                    del summed[p]
        elif type(right) == int or type(right) == float:
            if 0 in summed.keys():
                summed[0] += right
            else:
                summed[0] = right
            if summed[0] == 0:
                del summed[0]
        s = ""
        for p,c in summed.items():
            s += str((c,p)) + ","
        return eval("Poly({})".format(s.strip(",")))
                

    
    def __radd__(self,left):
        if type(left) != int and type(left) != float:
            raise TypeError
        else:
            summed = {p:c for p,c in self.terms.items()}
            if 0 in summed.keys():
                summed[0] += left
            else: summed[0] = left
            
            if summed[0] == 0:
                del summed[0]
            s = ""
            for p,c in summed.items():
                s += str((c,p)) + ","
            return eval("Poly({})".format(s.strip(",")))
                
           
    

    def __mul__(self,right):
        multiplied = {}
        if type(right) == Poly:
            for p1,c1 in self.terms.items():
                for p2,c2 in right.terms.items():
                    if p1+p2 in multiplied:
                        multiplied[p1+p2] += c1*c2
                    else:
                        multiplied[p1+p2] = c1*c2
                        
                    if multiplied[p1+p2] == 0:
                        del multiplied[p1+p2]
        elif type(right) == int or type(right) == float:
            for p,c in self.terms.items():
                multiplied[p] = c*right
        else:
            raise TypeError
        
        s = ""
        for p,c in multiplied.items():
            s += str((c,p)) + ","
        return eval("Poly({})".format(s.strip(",")))
    

    def __rmul__(self,left):
        if type(left) != int and type(left) != float:
            raise TypeError
        else:
            multiplied = {}
            for p,c in self.terms.items():
                multiplied[p] = c*left
        s = ""
        for p,c in multiplied.items():
            s += str((c,p)) + ","
        return eval("Poly({})".format(s.strip(",")))
        

    def __eq__(self,right):
        equal = True
        if type(right) == Poly:
            if len(self.terms.keys()) != len(right.terms.keys()):
                equal = False
            else:
                for p,c in self.terms.items():
                    if (p not in right.keys()) or self.terms[p] != right[p]:
                        equal = False
                        break
        elif type(right) == int or type(right) == float:
            if len(self.terms.keys()) != 1:
                equal = False
            else:
                for p,c in self.terms.items():
                    if self.terms[p] != right:
                        equal = False
        else:
            raise TypeError
        return equal

    
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