from copy import copy
class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        if terms==None:
            self.terms={0:0}
        for term in terms:
            assert type(term[0]) in (int,float)
            assert type(term[1])==int and term[1]>=0
            if term[1] in self.terms:
                if term[0]!=0:
                    raise AssertionError
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
        results=[]
        for k,v in self.terms.items():
            results.append(str((v,k)))
        return 'Poly({})'.format(','.join(results))

    
    def __len__(self):
        return max(self.terms) if len(self.terms)>0 else 0
    
    def __call__(self,arg):
        results=0
        for k,v in self.terms.items():
            results+=v*(arg)**k
        return results
    

    def __iter__(self):
        for k in sorted(self.terms,reverse=True):
            yield(self.terms[k],k)
            
            

    def __getitem__(self,index):
        if type(index)==int and index>=0:
            return self.terms[index] if index in self.terms else 0
        raise TypeError
            

    def __setitem__(self,index,value):
        if type(index)==int and index>=0:
            if value==0:
                if index in self.terms:
                    del self.terms[index]
                else:
                    pass
            else:
                self.terms[index]=value
        else:
            raise TypeError
                
            

    def __delitem__(self,index):
        if type(index)==int and index>=0:
            if index in self.terms:
                del self.terms[index]
        else:
            raise TypeError
            

    def _add_term(self,c,p):
        if type(p)==int and p>=0 and type(c) in (int,float):
            if p not in self.terms and c!=0:
                self.terms[p]=c
            else:
                if p in self.terms:
                    if self.terms[p]+c!=0:
                        self.terms[p]=self.terms[p]+c 
                    else:
                        del self.terms[p]
        else:
            raise TypeError
                
       

    def __add__(self,right):
        values=[[v,k] for k,v in self.terms.items()]
        if type(right) in (int,float):
            for value in values:
                if value[1]==0:
                    if value[0]+right!=0:
                        value[0]=value[0]+right
                    else:
                        values.remove(value)
        elif type(right)==Poly:
            for k,v in right.terms.items():
                if k in [value[1] for value in values]:
                    for value in values:
                        if value[1]==k:
                            if value[0]+right.terms[k]!=0:
                                value[0]=value[0]+right.terms[k]
                            else:
                                values.remove(value)
                else:
                    values.append((v,k))
        else:
            raise TypeError
        results=[str(value) for value in values]
        return eval('Poly({})'.format(','.join(results)))

    
    def __radd__(self,left):
        values=[[v,k] for k,v in self.terms.items()]
        if type(left) in (int,float):
            for value in values:
                if value[1]==0:
                    if value[0]+left!=0:
                        value[0]=value[0]+left
                    else:
                        values.remove(value)
        elif type(left)==Poly:
            for k,v in left.terms.items():
                if k in [value[1] for value in values]:
                    for value in values:
                        if value[1]==k:
                            if value[0]+left.terms[k]!=0:
                                value[0]=value[0]+left.terms[k]
                            else:
                                values.remove(value)
                else:
                    values.append((v,k))
        else:
            raise TypeError
        results=[str(value) for value in values]
        return eval('Poly({})'.format(','.join(results)))
    

    def __mul__(self,right):
        values=[[v,k] for k,v in self.terms.items()]
        if type(right) in (int,float):
            if right==0:
                return 0
            else:
                for value in values:
                    value[0]=right*value[0]
        results=[str(value) for value in values]
        if type(right)==Poly:
            temp=[]
            for k,v in right.terms.items():
                for value in values:
                    if k+value[1] in [t[1] for t in temp]:
                        for t in temp:
                            if t[1]==k+value[1]:
                                temp.append((v*value[0]+t[0],t[1]))
                                temp.remove(t)
                    else:
                        temp.append((v*value[0],k+value[1]))
        results=[str(i) for i in temp]
        return eval('Poly({})'.format(','.join(results)))            
        
                
    

    def __rmul__(self,left):
        values=[[v,k] for k,v in self.terms.items()]
        if type(left) in (int,float):
            if left==0:
                return 0
            for value in values:
                value[0]=left*value[0]
        results=[str(value) for value in values]
        return eval('Poly({})'.format(','.join(results)))
    

    def __eq__(self,right):
        if type(right) in (int,float):
            if len(self.terms)==1 and 0 in self.terms:
                return self.terms[0]==right
            else:
                return False
        elif type(right)==Poly:
            results=True
            for k,v in right.terms.items():
                if k not in self.terms and v!=0:
                    return False
                results=results*(self.terms[k]==right.terms[k])
            return results
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
#     p[2] = 0
#     print(str(p))
#     p[10] = 0
#     p1 = Poly((1,1),(2,0))
#     p2 = Poly((3,2),(2,1),(1,0))
#     p3 = Poly((3,5),(-2,2),(-4,0))
#     print(p1+p2)
#     print(p2+p3)
#     print(p1+p3)
#     p3*2
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()