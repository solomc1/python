class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        # Fill in the rest of this method, using *terms to initialize self.terms
        
        #print('terms',*terms)
        #print('type', type(terms))
        # args[1] - power, args[0] - coefficient
        for args in terms:
            if args[1] not in self.terms:
                self.terms[args[1]] = args[0]
        #print('dict',self.terms)
        for keys in self.terms:
            #print(self.terms[keys])
            assert type(self.terms[keys]) == int or type(self.terms[keys]) == float, "coefficient is not an int or a float"
            assert type(keys) == int and keys >= 0, "power is not an int"
        #print('dict len',len(self.terms))
        
        
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
        for key in self.terms:
            return "Poly({},{},{})".format((self.terms[key],key), (self.terms[key+1],key+1), (self.terms[key+2],key+2))

    def __len__(self):
        if self != dict():
            keys = []
            for key in self.terms:
                keys.append(key)
            keys.sort(reverse = True)
            return keys[0]
        else:
            return 0
    
    
    def __call__(self,arg):
        #print('self',self)
        new = ''
        for i in str(self):
            if i == 'x':
                new += '*'
                new += str(arg)
            elif i == '^':
                new += '**'
            else:
                new += i
        #print('new', new)
        #print(new.split())
        for item in new.split():
            answer = 0
            if item != '-' and item != '+':
                answer += eval(item)
                #print(answer)
        #print('evaluated', eval(new))
        return eval(new)

    def __iter__(self):
        answer = []
        for i in str(self):
            if i == 'x':
                #print(str(self).find(i))
                answer.append((str(self).find(i)-1, str(self).find(i)+2))
        return iter(answer)


    def __getitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError("argument is less than 0 or is not an int")
        elif index not in self.terms:
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if index < 0 or type(index) != int:
            raise TypeError("argument is less than 0 or is not an int")
        elif value == 0:
            #print(value,self.terms[value])
            #del self.terms[value]
            #self.__delitem__(self.terms[value])
            pass

        else:
            self.terms[index] = value
            return self
            

    def __delitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError("argument is less than 0 or is not an int")
        elif index not in self.terms:
            pass
        else:
            del self.terms[index]
            return self
            
            

    def _add_term(self,c,p):
        if type(c) != int or type(c) != float:
            raise TypeError("argument is not an int or a float")
        elif type(p) != int and p >= 0:
            
       

    def __add__(self,right):
        pass

    
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