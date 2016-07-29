import goody
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[0])==int or type(term[0])==float,"Coefficient must be int or float"
            assert type(term[1])==int and term[1]>=0,"Power must be an integer greater than or equal to 0"
            assert term[1] not in self.terms.keys(),"Multiple coefficients for the same power are not allowed"
            if term[0]!=0:
                self.terms[term[1]]=term[0]
        
        
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
        return 'Poly{}'.format(tuple((x,y) for (y,x) in self.terms.items()))
    
    def __len__(self):
        if len(self.terms.keys())==0:
            return 0
        else:
            return max(self.terms.keys())
    
    def __call__(self,arg):
        result=0
        for item in self.terms.items():
            result+=item[1]*(arg**item[0])
        return result
    

    def __iter__(self):
        for item in sorted(self.terms.items(),reverse=True):
            yield (item[1],item[0])
            

    def __getitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                return self.terms[index]
            else:
                return 0
        else:
            raise TypeError("Power must be an integer greater than or equal to 0")
            

    def __setitem__(self,index,value):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                if value==0:
                    del self.terms[index]
                else:
                    self.terms[index]=value
            else:
                if value!=0:
                    self.terms[index]=value
        else:
            raise TypeError("Power must be an integer greater than or equal to 0")

    def __delitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            raise TypeError("Power must be an integer greater than or equal to 0")
            

    def _add_term(self,c,p):
        assert type(c)==int or type(c)==float,"Coefficient must be int or float"
        assert type(p)==int and p>=0, "Power must be an integer greater than or equal to 0"
        if p in self.terms.keys():
            self.terms[p]+=c
            if self.terms[p]==0:
                del self.terms[p]
        else:
            if c!=0:
                self.terms[p]=c
       

    def __add__(self,right):
        result=eval(repr(self))
        if type(right)==int or type(right)==float:
            result._add_term(right,0)
        elif type(right)==Poly:
            for item in right.terms.items():
                result._add_term(item[1],item[0])
        else:
            raise TypeError("Unsupported operand for +, {} and {}".format(goody.type_as_str(self),goody.type_as_str(right)))
        return result
            

    
    def __radd__(self,left):
        return self+left

    def __mul__(self,right):
        result=Poly()
        if type(right)==int or type(right)==float:
            for key in self.terms.keys():
                result[key]=right*self.terms[key]
        elif type(right)==Poly:
            for item in self.terms.items():
                for rItem in right.terms.items():
                    result._add_term(item[1]*rItem[1],item[0]+rItem[0])
        else:
            raise TypeError("Unsupported operand for *, {} and {}".format(goody.type_as_str(right),goody.type_as_str(self)))
        return result

    def __rmul__(self,left):
        return self*left
    

    def __eq__(self,right):
        if type(right)==int or type(right)==float:
            if len(self.terms.keys())==1 and 0 in self.terms.keys():
                return self.terms[0]==right
            else:
                return False
        elif type(right)==Poly:
            selfIter=iter(self)
            rIter=iter(right)
            for i in selfIter:
                if next(rIter)!=i:
                    return False
            return True
        else:
            raise TypeError("Uncomparable types, {} and {}".format(goody.type_as_str(right),goody.type_as_str(self)))

    
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