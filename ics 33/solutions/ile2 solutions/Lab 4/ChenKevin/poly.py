class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for x in terms:
            assert type(x[0]) != int or float,"coefficient is not a valid entry"
            assert type(x[1]) != int or float,"Exponent is not a valid entry"
            if type(x[1]) != int:
                print( AssertionError)
            if x[0] != 0:
                self.terms[x[0]] = x[1]
#             for x in self.terms:
#                 if terms[1] == self.terms[x[0]]:
#                     print ( AssertionError )
        print(self.terms)
        
        
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
        data_list = []
        for x in self.terms:
            data_list.append((x, self.terms[x]))
        print (data_list)
        return str(data_list)
        
    
    def __len__(self):
        data_list = []
        i = 0
        for x in self.terms:
            data_list.append(self.terms[x])
        print(data_list)
        for x in data_list:
            if i < x:
                i = x
        return i
    
    def __call__(self,arg):
        data1 = []
        i = 0
        data2 = []
        data_tab = []
        for x in self.terms:
            data1.append(x)
            data2.append(self.terms[x])
        print(data1)
        print(data2)

        for x in data1:
            value = x
            print(x)
            print('test1')
            for y in data2:
                while i < y:
                    i+= 1
                    value *= arg
                    print(value)
                    print("***************")
            data_tab.append(value)
        print("here")
        print(data_tab)
        
        print("here")
        z = 0
        for x in data_tab:
            z += x
        return z
    def __iter__(self):
        old_l = []
        large_l = []
        new_l = []
        final_l = []
        for x in self.terms:
            old_l.append((x,self.terms[x]))
        print("here123")
        print(old_l)
        print("here123")
        for x in old_l:
            largest = old_l[2][1]
            if x[1] > largest:
                largest = x[1]
                large_l.append(x)
        i = 0
        print(len(old_l))
        while i < len(old_l):
            if old_l[i][1] > old_l[i+1][1]:
                new_l.append(old_l[i])
                i += 1
#         for x in old_l:
#             largest = old_l[1][1]
#             if x[1] < largest:
#                 new_l.append(x)
#         for x in large_l:
#             final_l.append(x)
#         for x in new_l:
#             final_l.append(x)
        print(new_l)
        print("testtesttest")
        return old_l
                
        
            

    def __getitem__(self,index):
        return self.terms[index]
            

    def __setitem__(self,index,value):
        self.terms[index] = value
            

    def __delitem__(self,index):
        self.terms[index] = None
            

    def _add_term(self,c,p):
        data_list = []
        if c != 0:
            if type(p) == int or float:
                for x in self.terms:
                    data_list.append(self.items[x])
                    if p not in data_list:
                        self.terms[c] = p
            else:
                return AssertionError
        else:
            return AssertionError

    def __add__(self,right):
        data = []
        for x in self.terms
            if right[1] == self.terms[x]:
                return self.terms[x+right[0]] = right[1]

    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        if type(right) is Poly or float or int:
            i = 0
            z = 0
            data = []
            for y in right:
                data.append(y)
            for x in self.terms:
                if self.terms[x] = right[x]:
                    i += 1
                    if x = data[i]:
                        x = 0
                    else:
                        z = 1
                    if z = 0:
                        return True
        else:
            return TypeError
    
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