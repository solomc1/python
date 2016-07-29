class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for i in terms:
            assert type(i[0]) in (int,float) 
            assert type(i[1]) == int, float
            assert i[1] >= 0
            assert i[1] not in self.terms.keys()
            if i[0] != 0:
                self.terms.update({i[1]:i[0]})
            
        
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
        new_str = ''
        for i in self.terms.items():
            new_str += str('(' +str(i[1]) +','+ str(i[0]) + ')')
        return 'Poly({})'.format(new_str)
            

    
    def __len__(self):
        new_list = [] 
        for i in self.terms.keys():
            new_list.append(i)
        if len(self.terms.keys()) > 0:
            return max(new_list)
        else:
            return 0
        
    
    def __call__(self,arg):
        count = 0
        for i in self.terms.items():
            count += (arg**i[0])*i[1]
        return count
            
    

    def __iter__(self):
        for i in sorted(self.terms.items(), reverse = True):
            yield (i[1],i[0])
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError
        elif index < 0 :
            raise TypeError
        return self.terms[index]
        
            

    def __setitem__(self,index,value):
        if type(index) == int and index > 0:
            self.terms.update({index:value})
            for i in self.terms.keys():
                if self.terms[i] == 0:
                    del self.terms[i] 
                    break
        else:
            raise TypeError

    def __delitem__(self,index):
        if type(index) == int and index >= 0:
            if index in self.terms.keys():
                del self.terms[index]
        else:
            raise TypeError
    
            
            

    def _add_term(self,c,p):
        if type(c) in (int,float) and type(p) == int:
            if p not in self.terms.keys() and c != 0:
                self.terms.update({p:c})
            elif p in self.terms.keys() and c != 0:
                self.terms.update({p:c + self.terms[p]})
            for i in self.terms.keys():
                if self.terms[i] == 0:
                    del self.terms[i] 
                    break

    def __add__(self,right):
        pass
#         new_dict = {}
#         for i in right.terms.items():
#             if i[1] in self.terms.keys():
#                 new_dict.update({i[1]})
                
                    
    

    
    def __radd__(self,left):
        pass

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        new_list = []
        if type(right) not in (int,str):
            for i,e in zip(self.terms.items(), right.terms.items()):
                if i[0] == e[0] and i[1] == e[1]:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return all(new_list)
        elif type(right) == int:
            if 1 not in self.terms.keys():
                if right in self.terms.values():
                    return True
            else:
                return False
        else:
            raise TypeError
                

    
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