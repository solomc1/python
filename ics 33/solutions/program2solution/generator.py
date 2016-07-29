# A generator for iterating through any iterable (mostly used to
#  iterate through the letters in a string).
# It is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(lets(string)), so the generator functions you write should not
#   call len on their parameters

def lets(string):
    for i in range(len(string)):
        yield string[i]

def transform(iterable,f):
    for i in iterable:
        yield f(i)

def running_count(iterable,p):
    answer = 0
    for i in iterable:
        if p(i):
            answer += 1
        yield answer
        
def n_with_pad(iterable,n,pad=None):
    it = iter(iterable)
    for i in range(n):
        try:
            yield(next(it))
        except StopIteration:
            yield pad
        
def sequence(*args):
    for a in args:
        for i in a:
            yield i

def alternate(*args):
    args = [iter(a) for a in args]
    while args:
        left = []
        for i in range(len(args)):
            try:
                yield next(args[i])
                left.append(args[i])
            except StopIteration:
                pass
        args = left
                


if __name__ == '__main__':
    import driver
    driver.driver()
