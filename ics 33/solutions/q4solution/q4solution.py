#Helper functions for testing (both in this module and in bsc)
#Each is a generator of values (primes and characters in a string)
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
    assert n >=2,'q4solution.in_a_row: n('+str(n)+') not >= 2'
    answer = set()
    it = iter(iterable)
    try:
        past = []
        for _ in range(n-1):
            past.append(next(it))
        while True:
            past.append(next(it))
            if all(v==past[0] for v in past):
                answer.add(past[0])
            past.pop(0)
    except StopIteration:
        return answer
 
# Using no list: more efficient in time and space, but more complex logic
# Technically doesn't work if n-1 None values appear first in the list
# def in_a_row(n,iterable):
#     assert n >=2,'q4solution.in_a_row: n('+str(n)+') not >= 2'
#     answer = set()
#     it = iter(iterable)
#     prev = None
#     count = 0
#     try:
#         while True:
#             current = next(it)
#             if prev == current:
#                 count += 1
#             else:
#                 count = 1
#                 prev = current
#             if count == n:
#                 answer.add(current)
#     except StopIteration:
#         return answer
 
 
class Permutation:
    def __init__(self,p,start):
        self.p     = p
        self.start = start
        
    def __iter__(self):
        class P_iter:
            def __init__(self,p,start):
                self.p     = p 
                self.start = start
                self.i     = start
                self.done  = False
                
            def __next__(self):
                if self.done:
                    raise StopIteration
                answer = self.i
                self.i = self.p[self.i]
                self.done = self.i == self.start
                return answer 
        return P_iter(self.p,self.start)       

    
class Permutation2:
    def __init__(self,p,start):
        self.p     = p
        self.start = start
        
    def __iter__(self):
        k = self.start
        while True:
            yield k
            k = self.p[k]
            if k == self.start:
                raise StopIteration
    
    
def differences(it1,it2):
    for n,(i1,i2) in enumerate(zip(it1,it2)):
        if i1 != i2:
            yield (n, i1, i2)
            
            
def skipper(iterable,n=0):
    it = iter(iterable)
    yield(next(it))
    while True:
        for _ in range(n):
            next(it)
        yield next(it)
 
# Alternative version using one loop/if with % operations       
# def skipper(iterable,n=0):
#     for i,v in enumerate(iterable,0):        #continue iteration
#         if i%(n+1) == 0:
#             yield v
        

if __name__ == '__main__':
    import driver
    
    driver.driver() # type quit in driver to return and execute code below
    
    # Test increases; add your own test cases
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
