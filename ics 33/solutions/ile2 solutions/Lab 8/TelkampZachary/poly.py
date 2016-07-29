#Zachary Telkamp Lab 8 50161646
from goody import type_as_str
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            if self.correct(i):
                if i[1] in self.terms.keys():
                    raise AssertionError('Poly.__init__: illegal power in ' + str(i))
                self.terms[i[1]] = i[0]
        
        
    
    def correct(self,tuples):
        if type_as_str(tuples[0]) != 'int' and type_as_str(tuples[0]) != 'float':
            raise AssertionError('Poly.__init__: illegal Coeff in ' + str(tuples))
        elif type_as_str(tuples[1]) != 'int':
            raise AssertionError('Poly.__init__: illegal power in ' + str(tuples))
        elif (int(tuples[1]) < 0):
            raise AssertionError('Poly.__init__: illegal power in ' + str(tuples))
        else:
            if tuples[0] == 0:
                return False
            return True



            
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
        newstr = ''
        for i in self.terms.keys():
            newstr += '({},{}),'.format(self.terms[i],i)
        newstr = newstr[:-1]
        return 'Poly({})'.format(newstr)

    
    def __len__(self):
        if len(self.terms.keys()) == 0:
            return 0
        
        num = 0
        for i in self.terms.keys():
            if int(i) > num:
                num = int(i)
        return num
    
    def __call__(self,arg):
        num = 0
        if type_as_str(arg) != 'int' and type_as_str(arg) != 'float':
            raise TypeError
        else:
            for i in self.terms.keys():
                newnum = arg**i
                newnum = newnum * self.terms[i]
                num += newnum
        return num
                
    

    def __iter__(self):
        for i in sorted(self.terms.keys(), reverse = True):
            yield (self.terms[i],i)
            

    def __getitem__(self,index):
        if type_as_str(index) != 'int' or int(index) < 0:
            raise TypeError('Poly.__getitem__: illegal index')
        
        if index in self.terms.keys():
            return self.terms[index]
        else:
            return 0
            

    def __setitem__(self,index,value):
        if type_as_str(index) != 'int' or int(index) < 0:
            raise TypeError('Poly.__setitem__: illegal index')
        
        if int(value) == 0:
            if index in self.terms.keys():
                self.terms = self._createnewdict(index)
            else:
                return
        
        elif index not in self.terms.keys():
            self.terms[index] = value
        else:
            self.terms[index] = value
        
        
    def _createnewdict(self,num):  
        newdict = {}
        for i in self.terms.keys():
            if i != num:
                newdict[i] = self.terms[i]
        return newdict     
    
    def _refreshdict(self):
        for i in self.terms.keys():
            if int(self.terms[i]) == 0:
                self.terms = self._createnewdict(i)
                

    def __delitem__(self,index):
        if type_as_str(index) != 'int' or int(index) < 0:
            raise TypeError('Poly.__setitem__: illegal index')
        self.terms = self._createnewdict(index)
            

    def _add_term(self,c,p):
        if self.correct((c,p)):
            if p in self.terms.keys():
                self.terms[p] = self.terms[p] + c
                self._refreshdict()
            else:
                self.terms[p] = c
       

    def _addhelper(self, tupler):
        p = Poly()
        for i in self.terms.keys():
            p._add_term(self.terms[i],i)
        
        
        if type_as_str(tupler) == 'int':
            p.terms[0] = p.terms[0] + tupler
        else:
            for i in tupler.terms.keys():
                p._add_term(tupler.terms[i],i)
        return p
        
    def __add__(self,right):
        x = self._addhelper(right)
        return x
        

    
    def __radd__(self,left):
        x = self._addhelper(left)
        return x
    
    def _mulhelper(self,tupler):
        
        p = Poly()
        z = Poly()
        if type_as_str(tupler) == 'int':
            for i in self.terms.keys():
                p._add_term(self.terms[i] * tupler,i)
            return p

        for i in self.terms.keys():
            p._add_term(self.terms[i],i)
        for i in sorted(tupler.terms.keys(), reverse = True):
            for j in sorted(p.terms.keys(), reverse = True):
                z._add_term((tupler[i] * p[j]),(i + j))
        return z
            

    def __mul__(self,right):
        x = self._mulhelper(right)
        return x
    

    def __rmul__(self,left):
        x = self._mulhelper(left)
        return x
    

    def __eq__(self,right):
        if type_as_str(right) == 'int':
            try:
                if int(str(self)) == right:
                    return True
                else:
                    return False
            except:
                return False
        elif type_as_str(right) == type_as_str(self):
            for i in right.terms.keys():
                if i not in self.terms.keys():
                    return False
                else:
                    if right[i] != self[i]:
                        return False
            return True
        else:
            raise TypeError('Poly.__eq__: object is not a Poly or an Int')

    
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