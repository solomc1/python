class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for item in terms:
            assert type(item[0]) in (int,float), 'must be of type float or int'
            assert type(item[1]) == int, 'power must be of type int'

            assert item[1] >= 0, 'power must be greater than or equal to 0'
            assert item[1] not in self.terms, 'cannot have repeating powers'
            self.terms.update({item[1]:item[0]})
        
        

            
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
        list_of_terms = [(self.terms[index],index) for index in self.terms]
        argument = str(list_of_terms).strip('[]')
        return 'Poly('+argument+')'


    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max(self.terms)
    
    def __call__(self,arg):
        answer = 0
        for item in self.terms:

            answer += (int(arg)**item) * (self.terms[item]) 
        
        return answer

    def __iter__(self):
        term_index = list(self.terms.items())
        term_index.sort(key=lambda x: x[0], reverse=True)
        for item in term_index:
            yield (item[1], item[0])
            
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be of powers(int) and greater than or equal to 0')
        elif index in self.terms:
            return self.terms[index]
        else:
            return 0
            
            
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('index must be of powers(int) and greater than or equal to 0')
        elif index == 0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms.update({index:value}) 

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('index must be of powers(int) and greater than or equal to 0')
        elif index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int, float) or type(p) != int or p < 0:
            raise TypeError('coefficent must be either int or float and power must be strictly int')
        else:
            if p in self.terms:
                new_coe = self.terms[p] + c
                if new_coe == 0:
                    self.terms.pop(p)
                else:  
                    self.terms.update({p: self.terms[p]+c})
            else:
                self.terms.update({p:c})
       

    def __add__(self,right):
        if type(right) == int:
            x = eval(self.__repr__())
            x._add_term(right,0)
            return x
        elif type(right) == Poly:
            x = eval(self.__repr__())
            for item in right:
                x._add_term(item[0], item[1])
            return x
                
            

    
    def __radd__(self,left):
        if type(left) == int:
            x = eval(self.__repr__())
            x._add_term(left,0)
            return x
        elif type(left) == Poly:
            x = eval(self.__repr__())
            for item in left:
                x._add_term(item[0], item[1])
            return x
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        pass
    

        

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    print('Start student Test')
    p = Poly((3,2),(-2,1),(4, 3))
    x = eval(p.__repr__())
    y = Poly((1,2), (2,3))
    print('repr test:', x)
    print('len test:', len(x))
    print('call test:', x.__call__(2))
    print('iter test:')
    for i in x:
        print(i)
        
    print('get item test:', x[3])
    print('test set attr')
    x.__setitem__(3,10)
    x.__setitem__(4,10)
    x.__setitem__(0,10)
    print(x)
    print('test del item')
    x.__delitem__(4)
    x.__delitem__(10)
    print(x)
    print('testing add term')
    x._add_term(-10, 3)
    print(x)
    x._add_term(10, 3)
    print(x)
    print('testing +')
    z = x + y
    a = z + 2
    b = 2 + a
    print(z)
    print(a)
    print(b)
    
    print('\n')
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