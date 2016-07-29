

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        #print(terms)
        for c,p in terms:
            assert type(c)==int or type(c)==float, 'coefficent not numeric'
            assert type(p)==int and p>=0, 'power not numeric'
            if c!=0:
                assert not p in self.terms.keys(), 'in it'
                self.terms[p]=c
                #print("self.term",self.terms)
#         self.terms=sorted(self.terms, key= lambda x:x)
        
        
    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')
    
    def __repr__(self):
        result="Poly("
        for p,c in self.terms.items():
            result+="({co},{po})".format(co=c, po=p)
        result+=")"
        return result
    
    def __len__(self):
        if self.terms=={}:
            return 0
        else:
            powers=[]
            for p in self.terms.keys():
                powers.append(p)
            return max(powers)
    
    def __call__(self,arg):
        answer=0
        d=sorted
        for p,c in self.terms.items():
            answer+=c*(arg**p)
        return answer
        
            

    def __iter__(self):
        print(self.terms)
        for p,c in self.terms.items():
            yield (c,p)
            

    def __getitem__(self,index):
        if type(index)!=int:
            raise TypeError
        if index<0:
            raise TypeError
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index)!=int:
            raise TypeError
        if index<0:
            raise TypeError
        if value==0 and index in self.terms.keys():
            del self.terms[index]
        elif value!=0:
            self.terms[index]=value


    def __delitem__(self,index):
        if type(index)!=int:
            raise TypeError
        if index<0:
            raise TypeError
        if index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(c)!=int or type(c)!=float:
            raise TypeError
        if type(p)!=int:
            raise TypeError
        if not p>=0:
            raise TypeError
        if c!=0 and (p not in self.terms.keys()):
            self.terms[p]=c
        if c!=0 and p in self.terms.keys():
            if self.terms[p]+c==0:
                del self.terms[p]
            else:
                self.terms[p]+=c
        
        
       

    def __add__(self,right):
        if type(right)==int or type(right)==float:
            self.terms[0]+=right
        elif type(right)==type(self):
            for p,c in right.terms.items():
                for p1, c1 in self.terms.items():
                    if p==p1:
                        self.terms[p]=c+c1
                self.terms[p]=c
        return str(self)

    
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