# Kevin Wong, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

def transform(iterable,f):
    for x in iterable:
        yield f(x)


def running_count(iterable,p):
    count= 0 
    for x in iterable:
        if p(x):
            count += 1
        yield count
        
def n_with_pad(iterable,n,pad=None):
    i = iter(iterable)
    for j in range(n):
        try: 
            x = next(i)
            yield x
        except StopIteration:
            yield pad
        
def sequence(*args):
    for iterable in args:
        for x in iterable:
            yield x


def alternate(*args):
    iterables = []
    for x in args:
        iterables.append(iter(x))
    iterables_left = list(iterables)
    while len(iterables_left) > 0:
        for i in iterables:
            try:
                yield next(i)
            except StopIteration:
                if i in iterables_left:
                    iterables_left.remove(i)

                
if __name__ == '__main__':
    import driver
    driver.driver()
