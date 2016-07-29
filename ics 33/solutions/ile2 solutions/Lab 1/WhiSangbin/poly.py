class Poly:

    def __init__(self,*terms):
        self.terms = {}
        for i in terms:
            if type(i[0]) not in (int, float):
                raise AssertionError
            if type(i[1]) != int:
                raise AssertionError
            if i[1] < 0:
                raise AssertionError
            if i[1] in self.terms:
                raise AssertionError
            if i[0] == 0:
                pass
            else:
                self.terms[i[1]] = i[0]

    def __str__(self):
        def term(c,p,var):
            return (str(c) if p == 0 or c != 1 else '') +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for p,c in sorted(self.terms.items(),reverse=True)]).replace('+ -','- ')

    def __repr__(self):
        string = ''
        for i in self.terms:
            string += '({},{}),'.format(self.terms[i], i)
        return 'Poly({})'.format(string.rstrip(','))

    def __len__(self):
        if self.terms == {}:
            return 0
        else:
            max_val = 0
            for i in self.terms:
                if i > max_val:
                    max_val = i
            return max_val

    def __call__(self,arg):
        sum_val = 0
        for i in self.terms:
            sum_val += (arg**i)*self.terms[i]
        return sum_val

    def __iter__(self):
        for i in sorted(self.terms, reverse = True):
            yield (self.terms[i], i)

    def __getitem__(self,index):
        if type(index) != int:
            raise TypeError
        if index < 0:
            raise TypeError
        if index not in self.terms:
            return 0
        else:
            return self.terms[index]

    def __setitem__(self,index,value):
        if type(index) != int:
            raise TypeError
        if type(value) not in (int, float):
            raise TypeError
        if index < 0:
            raise TypeError
        if value == 0:
            try:
                del self.terms[index]
            except KeyError:
                pass
        else:
            self.terms[index] = value

    def __delitem__(self,index):
        if type(index) != int:
            raise TypeError
        if index < 0:
            raise TypeError
        if index in self.terms:
            del self.terms[index]

    def _add_term(self,c,p):
        if type(p) != int:
            raise TypeError
        if type(c) not in (int, float):
            raise TypeError
        if p < 0:
            raise TypeError
        if p not in self.terms:
            if c != 0:
                self.terms[p] = c
        else:
            self.terms[p] += c
            if self.terms[p] == 0:
                del self.terms[p]

    def __add__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) in (int, float):
            new = Poly()
            for i in self.terms:
                new._add_term(self.terms[i], i)
            new._add_term(right, 0)
            return new
        if type(right) == Poly:
            new = Poly()
            for i in self.terms:
                new._add_term(self.terms[i], i)
            for j in right.terms:
                new._add_term(right.terms[j], j)
            return new

    def __radd__(self,left):
        return self.__add__(left)

    def __mul__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) in (int, float):
            new = Poly()
            for i in self.terms:
                new._add_term(self.terms[i]*right, i)
            return new
        if type(right) == Poly:
            new = Poly()
            for i in self.terms:
                for j in right.terms:
                    new._add_term(self.terms[i]*right.terms[j], i+j)
            return new

    def __rmul__(self,left):
        return self.__mul__(left)

    def __eq__(self,right):
        if type(right) not in (Poly, int, float):
            raise TypeError
        if type(right) in (int, float):
            return self.__getitem__(0) == right
        if type(right) == Poly:
            try:
                for i in self.terms:
                    if self.terms[i] != right[i]:
                        return False
                for i in right.terms:
                    if self.terms[i] != right[i]:
                        return False
            except KeyError:
                return False
            return True

if __name__ == '__main__':
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
    driver.driver()