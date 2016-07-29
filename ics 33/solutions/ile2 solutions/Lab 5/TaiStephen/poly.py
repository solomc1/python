class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for term in terms:
            assert type(term[1])==int and term[1]>=0, "illegal power in ({},{})".format(*term)
            assert type(term[0]) in (int,float), "illegal coefficient in ({},{})".format(*term)
            assert term[1] not in self.terms
            if term[0]!=0:self.terms[term[1]] = term[0]
        
        
        
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
        argstring=''
        for term in self.terms:
            argstring+="({},{}),".format(self.terms[term],term)
        return "Poly("+argstring[:-1]+")"

    
    def __len__(self):
        if self.terms=={}:
            return 0
        return max(self.terms)
    
    def __call__(self,arg):
        result = 0
        for term in self.terms:
            result += self.terms[term]*(arg**term)
        return result
    

    def __iter__(self):
        ordered_powers = sorted(self.terms.keys(),reverse=True)
        for i in ordered_powers:
            yield (self.terms[i],i)
            
            

    def __getitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError("negative or non-integer index")
        if index not in self.terms:
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!=int or index<0:
            raise TypeError("negative or non-integer index")
        if value==0:
            if index in self.terms:
                self.terms.pop(index)
        else:
            self.terms[index]=value
            
            

    def __delitem__(self,index):
        if type(index)!=int or index<0:
            raise TypeError("negative or non-integer index")
        if index in self.terms:
            self.terms.pop(index)
            

    def _add_term(self,c,p):
        self[p]=self[p]+c
       

    def __add__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unsupported operand types")
        result = Poly()
        for term in self.terms:
            result[term]=self.terms[term]
        if type(right)==Poly:
            for term in right.terms:
                result._add_term(right.terms[term],term)
        else:
            result._add_term(right,0)
        return result

    
    def __radd__(self,left):
        if type(left) not in (int,float):
            raise TypeError("unsupported operand types")
        result = Poly()
        for term in self.terms:
            result[term]=self.terms[term]
        result._add_term(left,0)
        return result

    def __mul__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unsupported operand types")
        result = Poly()
        if type(right)==Poly:
            for sterm in self.terms:
                for rterm in right.terms:
                    result._add_term(self.terms[sterm]*right.terms[rterm],sterm+rterm)
        else:
            for term in self.terms:
                result._add_term(self.terms[term]*right,term)
        return result


    def __rmul__(self,left):
        if type(left) not in (int,float):
            raise TypeError("unsupported operand types")
        result = Poly()
        for term in self.terms:
            result._add_term(self.terms[term]*left,term)
        return result

    def __eq__(self,right):
        if type(right) not in (Poly,int,float):
            raise TypeError("unsupported operand types")
        if type(right) in (int,float):
            for term in self.terms:
                if term!=0:return False
            return right == self[0]
        return self.terms==right.terms

    
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
#     
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()