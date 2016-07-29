#Helper functions for testing (both in this module and in bsc)
from predicate import is_prime
def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1
         
def lets(string):
    for let in string:
        yield let
        

def in_a_row(n,iterable):
    if n < 2:
        raise AssertionError('number must be greater than 2')
    hidden = iter(iterable)
    temp = []
    for z in range(n):
        temp.append(None)
    result = set()
    try:
        while True:
            for num in range(n-1):
                temp[num]= temp[num+1]
            temp[-1]= next(hidden)
            if not any(item != temp[0] for item in temp):    
                result.add(temp[0])
    except StopIteration:
        pass
    return result
                                
 
 
class Permutation:
    def __init__(self,p,start):
        self.p     = p
        self.start = start
        
    def __iter__(self):
        class P_iter:
            def __init__(self, p, start):
                self.result_list = p
                self.end = False
                self.current = start
                self.start = start
            
            def __next__(self): 
                if self.end == False:
                    self.end = True
                    return self.start 
                else:
                    if self.result_list[self.current] != self.start:
                        self.current = self.result_list[self.current]
                    else:
                        raise StopIteration
                return self.current
            
        return P_iter(self.p,self.start)
        
    
class Permutation2:
    def __init__(self,p,start):
        self.result_list     = p
        self.start = start
        
    def __iter__(self):
        for i in range(len(self.result_list)):
            self.current = self.start
            self.start = self.result_list[self.start]
            yield self.current
        
            
                
    
def differences(it1,it2):
    hidden1 = iter(it1)
    hidden2 = iter(it2)
    item1 = []
    item2 = []
    index = []
    lst_recorder = []
    try:
        while True:
            a = next(hidden1)
            b = next(hidden2)
            if a != b:
                item1.append(a)
                item2.append(b)
                index.append(len(lst_recorder))
            lst_recorder.append(a)
            
    except StopIteration:
        pass
    return tuple(zip(index, item1, item2))

def skipper(iterable,n=0):
        hidden = iter(iterable)
        try:
            while True:
                result = []
                for i in range(n+1):
                    try:
                        result.append(next(hidden))
                    except:
                        pass                          
                try:
                    yield result[0]
                except:
                    raise StopIteration
        except StopIteration:
            pass
        

if __name__ == '__main__':
    import driver

    
    driver.driver() # type quit in driver to return and execute code below
    
    # Test in_a_row; add your own test cases
    print('Testing in_a_row')
    print(in_a_row(2,[4,4,2,6,6,9,6,7,7,3,2,2]))
    print(in_a_row(3,[5,3,7,7,7,2,3,8,5,4,4,4,6]))
    print(in_a_row(4,[5,5,5]))
    for i in range(5,1,-1):
        print('for',i,'=',in_a_row(i,map(lambda x : x.rstrip(),open('in_a_row.txt'))))
    
    
    # Test Permutation/Permuation2; add your own test cases
    print('\nTesting Permutation')
    for i in Permutation([4,0,3,1,2],0):
        print(i,end='')
    print()
    
    for i in Permutation([4,0,3,1,2],3):
        print(i,end='')
    print()
    
    for i in Permutation([0],0):
        print(i,end='')
    print()
    

    print('\nTesting Permutation2')
    for i in Permutation2([4,0,3,1,2],0):
        print(i,end='')
    print()
    
    for i in Permutation2([4,0,3,1,2],3):
        print(i,end='')
    print()
    
    for i in Permutation2([0],0):
        print(i,end='')
    print()
    

        
    # Test differences; add your own test cases
    print('\nTesting differences')
    for i in differences('abcdefghijklmnopqrstuvwxyz',
                         'abc#efghij;lmnopq;stuvwxyz/'):
        print(i,end='')
    print()
    
    for i in differences(lets('abcdefghijklmnopqrstuvwxyz///'),
                         lets('abc1ef2hijk3mnopqr4tuvwxyz')):
        print(i,end='')
    print()
    
    
    # Test skipper; add your own test cases
    print('\nTesting skipper')
    for i in skipper('abcdefghijklmnopqrstuvwxyz'):
        print(i,end='')
    print()

    for i in skipper('abcdefghijklmnopqrstuvwxyz',1):
        print(i,end='')
    print()

    for i in skipper('abcdefghijklmnopqrstuvwxyz',2):
        print(i,end='')
    print()

    # Primes 1-50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
    # Skipping 2 : 2 7 17 29 41 
    for i in skipper(primes(50),2):
        print(i,end=' ')
    print()

