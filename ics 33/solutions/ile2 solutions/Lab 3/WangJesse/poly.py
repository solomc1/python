class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for c,p in terms:
            if type(p) != int or type(c) != int and type(c) != float:
                raise AssertionError("Power must be an int, Coefficient must be int or float ")
            if c != 0:
                if p >= 0:
                    if p in self.terms:
                        raise AssertionError("A power cannot appear as a later term if it appears as an earlier term")
                    else:
                        self.terms[p] = c
                else:
                    raise AssertionError("Power must be >=0")

        #print(self.terms)
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
        term_list = []
        for i in self.terms:
            term_list.append('(' + str(self.terms[i]) + ',' + str(i)  + ')')
        term_str = ','.join(term_list)
        return 'Poly(' + term_str +')'
         
    def __len__(self):
        spl = [] #sorterpowerlist
        for i in self.terms:
            spl.append(i)
        sorted(spl)
        if spl == []:
            return 0
        else:
            return spl[-1]
        pass
    
    def __call__(self,arg):
        result = 0
        for i in self.terms:        
            result += self.terms[i]*(arg**i)        
        return result
        pass

    def __iter__(self):
        power_list = []
        co_list = []
        for i in self.terms:
            power_list.append(i)
        power_list.sort(reverse=True)
        for i in power_list:
            co_list.append(self.terms[i])
        powers = iter(power_list)
        coeff = iter(co_list)
        for i in self.terms:
            yield (next(coeff),next(powers))
        pass
            

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError("power must be an int")
        elif index < 0:
            raise TypeError("Power must be >0")
        else:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]
        pass
            

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError("power must be an int")
        elif index < 0:
            raise TypeError("Power must be >0")
        else:
            if value == 0 and index in self.terms:
                self.terms.pop(index)
            elif value != 0:
                self.terms[index] = value
        pass
            

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError("power must be an int")
        elif index < 0:
            raise TypeError("Power must be >0")
        else:
            if index in self.terms:
                self.terms.pop(index)
        pass
            

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError("power must be an int")
        elif p < 0:
            raise TypeError("Power must be >0")
        if type(c) != int and type(c) != float:
            raise TypeError("Coefficient must be an int or a float")
        if c != 0 and p not in self.terms:
            self.terms[p] = c
        elif p in self.terms:
            added_term = self.terms[p] + c
            if added_term == 0:
                self.terms.pop(p)
            else:
                self.terms[p] = added_term
        pass
       

    def __add__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("invalid use of operand")
        if type(right) == int or type(right) == float:
            print(self,right)
            added_term = self.terms[0] + right
            result = self
            result.terms[0] = added_term
            return result
        if type(right) == Poly:
            added_term_list = []
            for i in self.terms:
                if i in right.terms:
                    added_term_list.append(('(' + str(self.terms[i] + right.terms[i]) + ',' + str(i) + ')'))
                else:
                    added_term_list.append(('(' + str(self.terms[i]) + ',' + str(i)+ ')'))
            for i in right.terms:
                if i not in self.terms:
                    added_term_list.append(('(' + str(right.terms[i]) + ',' + str(i)+ ')'))
            print(added_term_list)
            thingie = ','.join(added_term_list)
            print(thingie)
            return eval('Poly' + '(' + thingie +')' )
                    
                
                
        pass

    
    def __radd__(self,left):
        if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError("invalid use of operand")
        if type(left) == int or type(left) == float:
            added_term = self.terms[0] + left
            result = self
            result.terms[0] = added_term
            return result
        if type(left) == Poly:
            added_term_list = []
            for i in self.terms:
                if i in left.terms:
                    added_term_list.append(('(' + str(self.terms[i] + left.terms[i]) + ',' + str(i) + ')'))
                else:
                    added_term_list.append(('(' + str(self.terms[i]) + ',' + str(i)+ ')'))
            for i in left.terms:
                if i not in self.terms:
                    added_term_list.append(('(' + str(left.terms[i]) + ',' + str(i)+ ')'))
            print(added_term_list)
            thingie = ','.join(added_term_list)
            print(thingie)
            return eval('Poly' + '(' + thingie +')' )
        pass
    

    def __mul__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("invalid use of operand")
        if type(right) == int or type(right) == float:
            print(self,right)
            added_term = self.terms[0] + right
            result = self
            result.terms[0] = added_term
            return result
        if type(right) == Poly:
            added_term_list = []
            for i in self.terms:
                if i in right.terms:
                    added_term_list.append(('(' + str(self.terms[i]*right.terms[i]) + ',' + str(i) + ')'))
                else:
                    added_term_list.append(('(' + str(self.terms[i]) + ',' + str(i)+ ')'))
            for i in right.terms:
                if i not in self.terms:
                    added_term_list.append(('(' + str(right.terms[i]) + ',' + str(i)+ ')'))
            print(added_term_list)
            thingie = ','.join(added_term_list)
            print(thingie)
            return eval('Poly' + '(' + thingie +')' )
        pass
    

    def __rmul__(self,left):
         if type(left) != Poly and type(left) != int and type(left) != float:
            raise TypeError("invalid use of operand")
        if type(left) == int or type(left) == float:
            added_term = self.terms[0] * left
            result = self
            result.terms[0] = added_term
            return result
        if type(left) == Poly:
            added_term_list = []
            for i in self.terms:
                if i in left.terms:
                    added_term_list.append(('(' + str(self.terms[i] * left.terms[i]) + ',' + str(i) + ')'))
                else:
                    added_term_list.append(('(' + str(self.terms[i]) + ',' + str(i)+ ')'))
            for i in left.terms:
                if i not in self.terms:
                    added_term_list.append(('(' + str(left.terms[i]) + ',' + str(i)+ ')'))
            print(added_term_list)
            thingie = ','.join(added_term_list)
            print(thingie)
            return eval('Poly' + '(' + thingie +')' )
        pass
    

    def __eq__(self,right):
        if type(right) != Poly and type(right) != int and type(right) != float:
            raise TypeError("invalid use of operand")
        if type(right) == int or type(right) == float:
            return self.__call__(0) == right
        elif type(right) == Poly:
            return self == Poly
        pass

    
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    #===========================================================================
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    # print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    #print('  p(2):',p(2))
    # print('  list collecting iterator results:',[t for t in p])
    # print('  p+p:',p+p)
    # print('  p+2:',p+2)
    # print('  p*p:',p*p)
    # print('  p*2:',p*2)
    # print('End simple tests\n')
    #===========================================================================

    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()