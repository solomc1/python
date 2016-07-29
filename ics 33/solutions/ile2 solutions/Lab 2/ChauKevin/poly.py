class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        if terms != ():
            for i in terms:
                if i[0] == 0 and i[1] != 0:
                    raise AssertionError("Poly.__init__:illegal coefficient in : "+str(i))
                if type(i[0]) not in [int,float]:
                    raise AssertionError("Poly.__init__:illegal coefficient in : "+str(i))
                if type(i[1]) != int:
                    raise AssertionError("Poly.__init__:illegal power in : "+str(i))
                if i[1] < 0:
                    raise AssertionError("Poly.__init__:illegal power in : "+str(i)+"must be greater than or equal to 0")
                if i[1] in self.terms.values():
                    raise AssertionError("Poly.__init__:power cannot appear more than once: "+ str(i[1]))
                self.terms[i[1]]=i[0]
            #print(self.terms)
        else:
            self.terms = {}
            
            
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
        result = ""
        for k,v in self.terms.items():
            result += "("+str(v)+","+str(k)+")"+","
        return "Poly({})".format(result[:-1])

    
    def __len__(self):
        if self.terms == {}:
            return 0
        list_of_powers=[]
        for p in self.terms:
            list_of_powers.append(p)
        return max(list_of_powers)
    
    def __call__(self,arg):
        if type(arg) not in [int,float]:
            raise AssertionError("Poly.__call__:illegal argument in : "+str(arg))
        list_to_add = []
        print(self.terms)
        for k,v in self.terms.items():
            if k == 0:
                list_to_add.append(v)
                pass
            else:
                list_to_add.append((float(arg)**k)*v)
        return sum(list_to_add)
    

    def __iter__(self):
        list_in_order = []
        for i in self.terms:
            list_in_order.append(i)
        new = sorted(list_in_order,reverse=True)
        for i in new:
            yield (self.terms[i],i)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__getitem__:illegal index: "+str(index)+"must be an int and greater than or equal to 0")
        if index not in self.terms:
            return 0
        if index in self.terms:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__setitem__:illegal index: "+str(index)+"must be an int and greater than or equal to 0")
        if value == 0:
            self.__delitem__(index)
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Poly.__delitem__:illegal index: "+str(index)+"must be an int and greater than or equal to 0")
        result_dict={}
        for k,v in self.terms.items():
            if k != index:
                result_dict[k] = v
        self.terms = result_dict

    def _add_term(self,c,p):
        if type(c) not in [int,float]:
                    raise TypeError("Poly.__add_term__:illegal coefficient in : "+str(c)+ "must be an int or float")
        if p < 0:
                    raise TypeError("Poly.__add_term__:illegal coefficient in : "+str(p)+"must be positive or zero")
        if p not in self.terms and c != 0:
            self.terms[p] = c
        if p in self.terms:
            if self.terms[p]+c == 0:
                self.__delitem__(p)
            self.terms[p] = self.terms[p]+c
       

    def __add__(self,right):
        new = eval(right.__repr__())
        
    
    def __radd__(self,left):
        new = eval(left.__repr__())
    

    def __mul__(self,right):
        new = eval(right.__repr__())
    

    def __rmul__(self,left):
        new = eval(left.__repr__())
    

    def __eq__(self,right):
        if type (right)== Poly:
            
            return self.terms == right
        else:
            raise TypeError()

    
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