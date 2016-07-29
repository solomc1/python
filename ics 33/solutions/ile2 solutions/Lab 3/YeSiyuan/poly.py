class Poly:
    
    def __init__(self,*terms):
        # __str__ uses the name self.terms for the dictionary of terms
        # So __init__ should build this dictionary from terms
        self.terms = {}
        for numbers in terms:
            assert type(numbers[0]) is (int or float), "Poly.__init__: illegal powers in : (" + str(*terms) + ")"
            assert type(numbers[1]) is int and numbers[1] >= 0, "Poly.__init__: illegal powers in : (" + str(*terms) + ")"
            assert type(numbers[1]) not in self.terms, "Poly.__init__: illegal powers in : (" + str(*terms) + ")"
            if numbers[0] != 0:
                self.terms[numbers[1]] = numbers[0]
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
        answer = 'Poly('
        for i in self.terms:
            answer += '(' + str(self.terms[i]) + ', ' + str(i) + '), '
        if self.terms != {}:
            answer = answer[:-2]
        answer += ')'
        return answer
    
    def __len__(self):
        answer = 0
        for i in self.terms:
            if i > answer:
                answer = i
        return answer
    
    def __call__(self,arg):
        answer = 0
        for power in self.terms:
            answer += self.terms[power]**power
        return answer
    

    def __iter__(self):
        answer = list(self.terms.items())
        answer.sort(reverse = True)
        return iter(answer)
            

    def __getitem__(self,index):
        if index < 0 or type(index) != int:
            raise TypeError("Sorry, " + str(index) + " must be an integer greater than 0.")
        else:
            if index not in self.terms:
                return 0
            else:
                return self.terms[index]
            

    def __setitem__(self,index,value):
        if type(index) != int or index < 0:
            raise TypeError("Sorry, " + str(index) + " must be an integer greater than 0.")
        else:
            if value == 0:
                self.terms.__delitem__(value)
            else:
                self.__dict__[index] = value
            

    def __delitem__(self,index):
        if type(index) != int or index < 0:
            raise TypeError("Sorry, " + str(index) + " must be an integer greater than 0.")
        else:
            if index in self.terms:
                self.terms.__delitem__(index)
            
    
    def _add_term(self,c, p):
        if type(c) != (int or float):
            raise TypeError("Sorry, " + str(c) + " must be an int or float")
        if type(p) != int or p < 0:
            raise TypeError("Sorry, " + str(p) + " must be a non-negative int")
        if p not in self.terms:
            self.terms[p] = c
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                self.terms.__delitem__(p)
    

    def __add__(self,right):
        if type(self) != Poly:
            if type(self) is not (int or float):
                print(type(self))
                raise TypeError("Sorry " + str(self) + " must be a Polynomial or int or float")
        if type(right) != Poly:
            if type(right) is not (int or float):
                raise TypeError("Sorry " + str(right) + " must be a Polynomial or int or float")
        if type(right) is (int or float) and type(self) == (int or float):
            raise TypeError("Sorry, one of the variables must be a polynomial")
        if type(self) is (int or float):
            self, right = right, self
        if type(right) is (int or float):
            answer = self.terms[0]
            answer += right
            return answer
        else:
            answer = {}
            answer2 = {}
            for i in self.terms:
                answer[self.terms[i]] = i
            for i in right.terms:
                answer2[right.terms[i]] = i
            for i in answer:
                if i in answer2:
                    answer[i] += answer2[i]
            for i in answer2:
                if i not in answer:
                    answer[i] = answer2[i]
            realanswer = {}
            for i in answer:
                realanswer[answer[i]] = i
            answer = Poly(answer)
            realanswer = Poly(realanswer)
            #return Poly(realanswer)

    
    def __radd__(self,left):
        if type(self) != Poly:
            if type(self) is not (int or float):
                print(type(self))
                raise TypeError("Sorry " + str(self) + " must be a Polynomial or int or float")
        if type(left) != Poly:
            if type(left) is not (int or float):
                raise TypeError("Sorry " + str(left) + " must be a Polynomial or int or float")
        if type(left) is (int or float) and type(self) == (int or float):
            raise TypeError("Sorry, one of the variables must be a polynomial")

    def __mul__(self,right):
        if type(self) != Poly:
            if type(self) is not (int or float):
                print(type(self))
                raise TypeError("Sorry " + str(self) + " must be a Polynomial or int or float")
        if type(right) != Poly:
            if type(right) is not (int or float):
                raise TypeError("Sorry " + str(right) + " must be a Polynomial or int or float")
        if type(right) is (int or float) and type(self) == (int or float):
            raise TypeError("Sorry, one of the variables must be a polynomial")
    

    def __rmul__(self,left):
        if type(self) != Poly:
            if type(self) is not (int or float):
                print(type(self))
                raise TypeError("Sorry " + str(self) + " must be a Polynomial or int or float")
        if type(left) != Poly:
            if type(left) is not (int or float):
                raise TypeError("Sorry " + str(left) + " must be a Polynomial or int or float")
        if type(left) is (int or float) and type(self) == (int or float):
            raise TypeError("Sorry, one of the variables must be a polynomial")

    def __eq__(self,right):
        if type(self) != Poly:
            if type(self) is not (int or float):
                print(type(self))
                raise TypeError("Sorry " + str(self) + " must be a Polynomial or int or float")
        if type(right) != Poly:
            if type(right) is not (int or float):
                raise TypeError("Sorry " + str(right) + " must be a Polynomial or int or float")
        if type(right) is (int or float) and type(self) == (int or float):
            raise TypeError("Sorry, one of the variables must be a polynomial")
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