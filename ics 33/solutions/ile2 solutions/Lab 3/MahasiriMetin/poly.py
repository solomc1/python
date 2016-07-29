#Metin Mahasiri 25303756

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms!
#         for k,v in terms.items()
#             print('key',key)
#             print('value', value)
        print()
        self.terms = {}
        for i in terms:
            if type(i[0]) == int or type(i[0]) == float:
#                 if i[0] == 0:
#                     pass
                if (i[1]) >= 0:
                    if i[1] not in self.terms:
                        self.terms[i[1]] = i[0]
                else:
                    raise AssertionError
            else:
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
        string = 'Poly('
        print('repr')
        for i in self.terms:
            string+='('
            string+=str(self.terms[i])
            string+=','
            string+=str(i)
            string+=')'
        string+=')'
        return string

    
    def __len__(self):
        start = 0
        if self.terms == {}:
            return 0
        else:
            for item in self.terms:
                if item>start:
                    start = item
        return start
    
    def __call__(self,arg):
        answer = 0
        if type(arg) == int or type(arg) == float:
            for item in self.terms:
                answer = answer + (self.terms[item]*(arg**item))
                print(answer)
        return answer
                

    def __iter__(self):
        pass
#         self.term = (list(self.term))
#         print(self.term.sorted())
#         self.term.sorted(lambda x:x[1])
#         print(self.term)
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError
        else:
            try:
                return self.terms[index]
            except:
                return 0
            
            

    def __setitem__(self,index,value):
        if type(index) != int or index <0:
            raise TypeError
        elif value == 0:
            pass
        else:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index <0:
            raise TypeError
        try:
            del(self.terms[index])
        except:
            pass
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError
        elif type(p) != int:
            raise TypeError
        elif p <0:
            raise TypeError
        elif c == 0:
            pass
        elif p not in self.terms:
            self.terms[p] = c
        elif p in self.terms:
            if self.terms[p]+c != 0:
                self.terms[p]+=c
            else:
                del(self.terms[p])
            
    def __add__(self,right):
        self.answer = {}
        if type(right) == int:
            for i in self.terms:
                self.terms[i]+ right
            return self.terms
        if type(right) == Poly:
            for item in self.terms:
                for key in right.terms:
                    if item == key:
                        self.answer[item] = self.terms[item]+right.terms[key]
            return self.answer

                    

    
    def __radd__(self,left):
        self.answer = {}
        if type(left) == int:
            for i in self.terms:
                self.term[i]+ left
            return self.terms
        if type(left) == Poly:
            for item in self.terms:
                for key in left.terms:
                    if item == key:
                        self.answer[item] = self.terms[item]+left.terms[key]
            return self.answer
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right)!= int and type(right)!= float and type(right)!= Poly:
            raise TypeError
        if type(right == int) or type(right == float):
            self.terms>right
        else:
            pass

    
if __name__ == '__main__':
    print('test')
    p1 = Poly((1,1),(2,0))
    p2 = Poly((3,2),(2,1),(1,0))
    print(p1+p2)

    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
#     print('  list collecting iterator results:',[t for t in p])
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()