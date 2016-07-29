class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
#         Fill in the rest of this method, using *terms to intialize self.terms
        for k,v in terms:
            if type(k) not in [int,float] or type(v) != int or v < 0:
                raise AssertionError("invalid argument {}".format(k,v))
            elif v in self.terms.keys():
                raise AssertionError("cannot reuse power {}".format(v))
            elif k != 0:
                self.terms[v] = k
              
#     I have written str(...) because it is used in the bsc.txt file and
#       it is a bit subtle to get correct. Notice that it assumes that
#       every Poly object stores a dict whose keys are powers and whose
#       associated values are coefficients. This function does not depend
#       on any other method in this class being written correctly.   
    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        string = "Poly("
        for k,v in self.terms.items():
            string += "({},{}),".format(v,k)
        string = string.strip(",")
        string += ")"
        return string

    
    def __len__(self):
        high = 0
        if self.terms =={}:
            return high
        else:
            for k in self.terms.keys():
                if k > high:
                    high = k
            return high
    
    def __call__(self,arg):
        total = 0
        for k,v in self.terms.items():
            result = (arg)**k
            total += v*result
        return total
    

    def __iter__(self):
        i = []
        i2 = []
        for k,v in self.terms.items():
            i2.append((k,v))
        i2 = sorted(i2, reverse = True)
        for tup in i2:
            i.append((tup[1], tup[0]))
        return iter(i)
            

    def __getitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError("Invalid index {}".format(index))
        elif index not in self.terms.keys():
            return 0
        else:
            return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError("Invalid index {}".format(index))
        elif value== 0:
            temp = {}
            for k,v in self.terms.items():
                if k != index:
                    temp[k] = v
            self.terms = temp
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError("Invalid index {}".format(index))
        elif index in self.terms.keys():
            temp = {}
            for k,v in self.terms.items():
                if k != index:
                    temp[k] = v
            self.terms = temp

    def _add_term(self,c,p):
        if type(c) not in [int, float] or type(p) !=int or p<0:
            raise TypeError("Invalid entry {},{}".format(c,p))
        elif p not in self.terms.keys() and c !=0:
            self.terms[p] = c
        elif c ==0:
            temp = {}
            for k,v in self.terms.items():
                if k != p:
                    temp[k] = v
            self.terms = temp
            
        else:
            test = self.terms[p] + c
            if test !=0:
                self.terms[p] = test
            else:
                temp = {}
                for k,v in self.terms.items():
                    if k != p:
                        temp[k] = v
                self.terms = temp
       

    def __add__(self,right):
        if type(right) == Poly:
            string = "Poly("
            for k,v in self.terms.items():
                if k in right.terms.keys():
                    string += "({},{}),".format(v+right.terms[k],k)
                else:
                    string += "({},{}),".format(v,k)
            for k,v in right.terms.items():
                if k not in self.terms.keys():
                    string += "({},{}),".format(v,k)
            string = string.strip(",")
            string += ")"
            return eval(string)
        elif type(right) not in (int,float):
            raise TypeError("inoperable types for +: Poly and {}".format(str(type(right))))
        else:
            if 0 not in self.terms.keys():
                string = "Poly("
                for k,v in self.terms.items():
                    string += "({},{}),".format(v,k)
                string += "({},0)".format(right)
                string += ")"
                return eval(string)
            else:
                string = "Poly("
                for k,v in self.terms.items():
                    if k!=0:
                        string += "({},{}),".format(v,k)
                    else:
                        string += "({},0),".format(right+v)
                string = string.strip(',')
                string += ")"
                return eval(string)

    
    def __radd__(self,left):
        return self +left
    

    def __mul__(self,right):
        if type(right) is Poly:
            string = "Poly"
            newstring = ''
            for k,v in self.terms.items():
                for nk, nv in right.terms.items():
                    string += "({},{}),".format(nv*v,k+nk)
            string = string.strip(",")
            string += ")"
            print(string)            
                    
        elif type(right) not in (int,float):
            raise TypeError("inoperable types for *: Poly and {}".format(str(type(right))))
        else:
            string = "Poly("
            for k,v in self.terms.items():
                string += "({},{}),".format(right*v,k)
            string = string.strip(",")
            string += ")"
            return eval(string)                
    

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right) ==Poly:
            if len(self.terms.keys())!= len(right.terms.keys()):
                return False
            else:
                for k,v in self.terms.items():
                    if k not in right.terms.keys() or v != right.terms[k]:
                        return False
                return True
        elif type(right) not in (int,float):
            raise TypeError("unorerable types: Poly and {}".format(str(type(right))))
        else:
            if 0 not in self.terms.keys() or len(self.terms.keys())>1 or self.terms[0] != right:
                return False
            return True
        
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    p1 = Poly((1,1),(2,0))
    p2 = Poly((3,2),(2,1),(1,0))
    print(p1*p2)
    
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