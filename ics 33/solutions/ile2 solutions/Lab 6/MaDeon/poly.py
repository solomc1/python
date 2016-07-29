class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for argument in terms:
            if argument[0] == 0:
                continue
            if type(argument[0]) not in [int, float]:
                raise AssertionError('Poly.__init__: illegal coefficient in {}'. format(argument))
            if type(argument[1]) != int or argument[1] < 0:
                raise AssertionError('Poly.__init__: illegal power in {}'.format(argument))
            if argument[1] in self.terms and self.terms[argument[1]] != argument[0]:
                raise AssertionError('Poly.__init__: illegal power in {}'.format(argument))
            self.terms[argument[1]] = argument[0]
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
        return 'Poly({})'.format(','.join(['({},{})'.format(v,k) for k,v in self.terms.items()]))

    
    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            return max([int(pow) for pow in self.terms.keys()])
    
    def __call__(self,arg):
        def evaluate(x: int):
            polynomial = []
            for k,v in self.terms.items():
                polynomial.append('{}*{}**{}'.format(v,x,k))
            return eval('{}'.format('+'.join(polynomial)))
        return evaluate(arg)
        
    

    def __iter__(self):
        poly = [(v,k) for k,v in self.terms.items()]
        for object in sorted(poly, key=lambda x: x[1], reverse=True):
            yield object
            

    def __getitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Poly.__getitem__: illegal index({})'.format(index))
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) != int or index<0:
            raise TypeError('Poly.__getitem__: illegal index({})'.format(index))        
        if value == 0:
            self.terms.pop(index)
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int or index<0:
            raise TypeError('Poly.__delitem__: illegal index({})'.format(index)) 
        if index in self.terms:
            self.terms.pop(index)        
            

    def _add_term(self,c,p):
        if type(c) not in [int, float]:
            raise TypeError('Poly._add_term: illegal coefficient({})'.format(c))
        if type(p) != int or p < 0:
            raise TypeError('Poly._add_term: illegal power({})'.format(p))
        if p not in self.terms:
            if p!= 0:
                self.terms[p] = c
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.terms.pop(p)        
       

    def __add__(self,right):
        if type(right) not in (int, Poly, float):
            raise TypeError('Poly.__add__:Unsupported operand + for type({})'.format(type(right)))
        newpoly = Poly()
        for k,v in self.terms.items():
            newpoly._add_term(v,k)
        if type(right) in (int, float):
            newpoly._add_term(right, 0)
            return newpoly
        else:
            for k,v in right.terms.items():
                newpoly._add_term(v,k)
            return newpoly
    
    def __radd__(self,left):
        if type(left) not in (int, Poly, float):
            raise TypeError('Poly.__add__:Unsupported operand + for type({})'.format(type(left)))
        newpoly = Poly()
        for k,v in self.terms.items():
            newpoly._add_term(v,k)
        if type(left) in (int, float):
            newpoly.addterms(left, 0)
            return newpoly
        else:
            for k,v in left.terms.items():
                newpoly._add_term(v,k)
            return newpoly
    

    def __mul__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__mul__:Unsupported operand * for type({})'.format(type(right)))
        newpoly = Poly()
        for k,v in self.terms.items():
            newpoly._add_term(v,k)
        if type(right) in (int, float):
            for k,v in newpoly.terms.items():
                newpoly.terms[k] = newpoly.terms[k] * right
            return newpoly
        else:
            newdict = {}
            for k,v in newpoly.terms.items():
                key = k
                value = v
                for x,y in right.terms.items():
                    key = key * x
                    value = value * y
                newdict[key] = value
            newpoly.terms = newdict
            return newpoly
            

    def __rmul__(self,left):
        if type(left) not in (int, float, Poly):
            raise TypeError('Poly.__rmul__:Unsupported operand * for type({})'.format(type(left)))
        newpoly = Poly()
        for k,v in self.terms.items():
            newpoly._add_term(v,k)
        if type(left) in (int, float):
            for k,v in newpoly.terms.items():
                newpoly.terms[k] = newpoly.terms[k] * left
            return newpoly
        else:
            newdict = {}
            for k,v in newpoly.terms.items():
                key = k
                value = v
                for x,y in left.terms.items():
                    key = key * x
                    value = value * y
                newdict[key] = value
            newpoly.terms = newdict
            return newpoly
    

    def __eq__(self,right):
        if type(right) not in (int, float, Poly):
            raise TypeError('Poly.__eq__:Unsupported operand + for type({})'.format(type(right)))
        if type(right) == Poly:
            checklist = [x for x in list(self.terms.items()) if x not in list(right.terms.items())]
            return checklist == []
        else:
            checklist = [x for object in self.terms.items() for x in object ]
            return right in checklist
    
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