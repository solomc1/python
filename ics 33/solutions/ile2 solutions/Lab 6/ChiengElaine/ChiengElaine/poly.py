class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        try:
            self.terms = {}
            for term in terms:
                assert (type(term[0]) in [int,float]), 'coefficient is not an int or a float'
                assert (type(term[1])== int), 'power is not an int'
                assert (term[1]>=0), 'power is negative'
                if term[0] !=0:
                    if term[1] not in self.terms.keys():
                        self.terms[term[1]]=term[0]
                    else:
                        assert (term[1] not in self.terms.keys()), 'the same power is already in the dictionary'
        except:
            raise AssertionError
        
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
        sortedpowers=[]
        sortedtuples=''
        for k in self.terms.keys():
            sortedpowers.append(k)
        for p in range(len(sorted(sortedpowers, reverse=True))):
            for k,v in self.terms.items():
                if k==sorted(sortedpowers, reverse=True)[p]:
                    if sorted(sortedpowers, reverse=True)[p]==sorted(sortedpowers, reverse=True)[-1]:
                        sortedtuples+=str(((k,v)))
                    else:
                        sortedtuples+=str(((k,v)))+','
        return 'Poly('+sortedtuples+')'

    
    def __len__(self):
        if self.terms=={}:
            return 0
        else:
            sortedpowers=[]
            for k in self.terms.keys():
                sortedpowers.append(k)
            return max(sortedpowers)
    
    def __call__(self,arg):
        try:
            assert (type(arg) in [int,float]), 'argument is not an int or float'
            answer=0
            for k,v in self.terms.items():
                if k!=0:
                    answer+=v*arg**k
                else:
                    answer+=v
            return answer
        except AssertionError:
            pass
    

    def __iter__(self):
        sortedpowers=[]
        sortedtuples=[]
        for k in self.terms.keys():
            sortedpowers.append(k)
        for p in sorted(sortedpowers, reverse=True):
            for k,v in self.terms.items():
                if k==p:
                    sortedtuples.append(((v,k)))
        for pair in sortedtuples:
            yield pair
            

    def __getitem__(self,index):
        if type(index)!= int or index<0:
            raise TypeError('Index is not an int or is negative')
        elif index not in self.terms.keys():
            return 0
        else:
            for key in self.terms.keys():
                if key==index:
                    return self.terms[key]
            

    def __setitem__(self,index,value):
        if type(index)!= int or index<0:
            raise TypeError('Index is not an int or is negative')
        else:
            if index not in self.terms.keys():
                self.terms[index]=value
            for k,v in self.terms.items():
                if index==k:
                    self.terms[index]=value
                elif v==0:
                    del self.term[k]
            
            
    def __delitem__(self,index):
        if type(index)!= int or index<0:
            raise TypeError('Index is not an int or is negative')
        elif index in self.terms.keys():
            del self.terms[index]
            

    def _add_term(self,c,p):
        if type(p)!= int or p<0:
            raise TypeError('power is not an int or is negative')
        elif (type(c) not in [int, float]):
            raise TypeError('Index is not an int or is negative')
        else:
            if p not in self.terms.keys() and c !=0:
                self.terms[p]=c
            elif p in self.terms.keys():
                for k,v in self.terms.items():
                    if p==k:
                        nv=v+c
                        self.terms[k]=nv
            for key,val in self.terms.items():
                if val==0:
                    del self.terms[key]
       

    def __add__(self,right):
        if type(right) not in [int, float, Poly]:
            raise TypeError('right is not an int, float, or Poly')
        if type(right) in [int, float]:
            if 0 in self.terms.keys():
                self.terms[0]+=right
                if self.terms[0]==0:
                    del self.terms[0]
            else:
                self.terms[0]=right
            return self.__str__()
        elif type(right)==Poly:
            for k,v in right.terms.items():
                self._add_term(v,k)
            return self.__str__()

    
    def __radd__(self,left):
        if type(left) not in [int, float, Poly]:
            raise TypeError('right is not an int, float, or Poly')
        if type(left) in [int, float]:
            if 0 in self.terms.keys():
                self.terms[0]+=left
                if self.terms[0]==0:
                    del self.terms[0]
            else:
                self.terms[0]=left
            return self.__str__()
        elif type(left)==Poly:
            for k,v in left.terms.items():
                self._add_term(v,k)
            return self.__str__()
    

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