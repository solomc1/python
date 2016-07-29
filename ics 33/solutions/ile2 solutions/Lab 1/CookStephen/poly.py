from goody import type_as_str

class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        #coefficient = i[0]
        #power = i[1]
        for i in terms:
            assert(type(i[0]) == int or type(i[0]) == float)
            assert(type(i[1]) == int)
            assert(i[1] >= 0)
            if i[1] in self.terms.keys() and self.terms[i[0]] != 0:
                assert False
            if i[0] != 0:
                self.terms[i[1]] = i[0]
        
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
        result = ''
        r_list = []
        for k in self.terms.items():
            r_list.append(str(k))
        return 'Poly(' + ','.join(r_list) + ')'

    
    def __len__(self):
        highest = 0
        for k in self.terms.keys():
            if k > highest:
                highest = k
        return highest
        
        
    
    def __call__(self,arg):
        assert(type(arg) == int or type(arg) == float)
        result = 0
        for k,v in self.terms.items():
            if v != 0:
                result += pow(arg,k) * v
            else:
                result += v
        return result
    

    def __iter__(self):
        count = 0
        tuples = []
        for k,v in self.terms.items():
            tuples.append((v,k))
        for i in sorted(tuples, key=lambda x : x[1], reverse=True):
            if count <= len(self.terms):
                yield i
                count+=1
        
            

    def __getitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be a valid integer >= 0')
        if index not in self.terms.keys():
            return 0
        return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError('Index must be a valid integer >= 0')
        if value == 0:
            if 0 in self.terms.values():
                pass
        elif value != 0:
            self.terms[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError('Index must be a valid integer >= 0')
        if index in self.terms.keys():
            self.terms.pop(index)       
            

    def _add_term(self,c,p):
        if type(c) != int and type(c) != float:
            raise TypeError('Coefficient must be type int or float')
        if type(p) != int or p < 0:
            raise TypeError('Power must be an integer value >= 0')
        if p not in self.terms.keys() and c != 0:
            self.terms[p] = c
        elif p in self.terms.keys():
            if self.terms[p] + c != 0:
                self.terms[p] += c

    def __add__(self,right):
        pass
#
    
    def __radd__(self,left):
        pass
    

    def __mul__(self,right):
        pass
    

    def __rmul__(self,left):
        pass
    

    def __eq__(self,right):
        for k in self.terms.items():
            if k in right.items():
                continue
            else:
                return False
        return True

    
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