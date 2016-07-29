class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for coe,pow in terms:
            if type(coe) not in (int,float):
                raise AssertionError('Poly.__init__: illegal coefficient in :{}'.format((coe,pow)))
            if type(pow) is not int or pow < 0:
                raise AssertionError('Poly.__init__: illegal power in: {}'.format((coe,pow)))
            if coe == 0:
                pass
            elif pow in self.terms.keys():
                raise AssertionError()
            else:
                self.terms[pow] = coe
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
        fin = []
        for k,v in self.terms.items():
            fin.append((v,k))
        return 'Poly' + str(tuple(fin))

    
    def __len__(self):
        if list(self.terms.keys()) == []:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            total += v*arg**k
        return total
    

    def __iter__(self):
        def _gen(bin):
            for k,v in bin:
                yield (v,k)



        return _gen(self.terms.items())
            

    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: illegal power : {}'.format(index))
        if index not in self.terms.keys():
            return 0
        else:
            return self.terms.get(index)
            

    def __setitem__(self,index,value):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__setitem__: illegal power : {}'.format(index))
        if value == 0:
            try:
                self.terms.pop(index)
            except:
                pass
        else:
            self.terms[index] = value           

    def __delitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__delitem__: illegal power : {}'.format(index))
        if index not in self.terms.keys():
            pass
        else:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        if type(c) not in (int,float):
            raise TypeError()
        if type(p) is not int or p <0:
            raise TypeError()
        elif p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if c + self.terms.get(p) == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = c + self.terms.get(p)


       

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__add__: illegal operand:{}'.format(right))
        if type(right) is Poly:
            for k,v in self.terms.items():
                for a,b in right.terms.items():
                    if k == a:
                        pass
#             print(self.terms.items(), right.terms.items())
        elif type(right) in (int,float):
            pass
        return self.terms.items()
    
    def __radd__(self,left):
        return self + left
    

    def __mul__(self,right):
        check = []
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__mul__: illegal operand:{}'.format(right))
#         if type(right) is Poly:
#             for k,v in self.terms.items():
#                 for a,b in right.terms.items():
#                     check.append((k*a, v*b))
        if type(right) in (int,float):
            for k,v in self.terms.items():
                
                check.append((k*right,v*right))
        elif type(right) is Poly:
            check.append(self.terms.items())

#         return Poly(tuple(check))  
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError('Poly.__eq__: illegal operand:{}'.format(right))
        if type(right) is Poly:
            for k,v in self.terms.items():
                for a,b in right.terms.items():
                    if k == a and v == b:
                        return True
                    else:
                        return False   
        elif type(right) in (int,float):
            for k,v in self.terms.items():
                if k == right or v == right:
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