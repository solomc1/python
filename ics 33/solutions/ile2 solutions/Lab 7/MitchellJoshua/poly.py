class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        
        # Fill in the rest of this method, using *terms to intialize self.terms
        for arg in terms:
            if arg[0]!=0:
                if (type(arg[0]) in (int,float)):
                    if type(arg[1])==int and (arg[1]>=0)  and (arg[1] not in self.terms.keys()):
                            self.terms[arg[1]]=arg[0]
                    else:
                        message= 'Poly.__init__: illegal power in: '+str(arg)
                        assert False,message
                else:
                    message= 'Poly.__init__: illegal coefficient in: '+ str(arg)
                    assert False, message
                

            
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
        dict_switch= {v:k for k,v in self.terms.items()}
        return 'Poly{}'.format(tuple(dict_switch.items()))

    
    def __len__(self):
        if len(self.terms)==0:
            return 0
        return max(self.terms.keys())
    
    def __call__(self,arg):
        if type(arg) in (int,float):
            replaced= self.__str__().replace('x','*{}'.format(arg))
            return eval(replaced.replace('^','**'))
    

    def __iter__(self):
        try:
            temp=self.terms
            while len(temp)!=0:
                maximum= max(temp.keys())
                yield (self.terms[maximum],maximum)
                del(temp[maximum])
        except StopIteration:    
            pass
            
            
            

    def __getitem__(self,index):
        if type(index)==int and index>=0:
            if index not in self.terms.keys():
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError

    def __setitem__(self,index,value):
        if type(index)==int and index>=0:
            if value!=0:
                self.terms[index]=value
            elif value==0 and index in self.terms.keys():
                del(self.terms[index])
        else:
            raise TypeError
            

    def __delitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                del(self.terms[index])
        else:
            raise TypeError
            

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p)==int and p>=0:
            if p not in self.terms.keys() and p!=0:
                self.terms[p]=c
            elif p in self.terms.keys():
                sums= self.terms[p]+c
                if sums!=0:
                    self.terms[p]=sums
                else:
                    del(self.terms[p])
        else:
            raise TypeError
       

    def __add__(self,right):
        pass

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(self)==Poly and type(right) in (Poly,int,float):
            if type(right) in (int,float):
                return list(self.terms.keys())[0]==right
            else:
                return self.terms.keys()==right.terms.keys()
        else:
            raise TypeError

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
#     print('Start simple tests')
#     p = Poly((3,2),(-2,1), (4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End simple tests\n')

    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()