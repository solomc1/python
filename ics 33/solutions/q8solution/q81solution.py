import random
from goody import irange
from performance import Performance
from priorityqueue import PriorityQueue

def setup(size):
    global pq
    alist = [i for i in range(size)]
    random.shuffle(alist)
    pq = PriorityQueue(alist)
    
def code(removes):
    global pq
    for i in range(removes):
        pq.remove()
        
for i in irange(0,8):
    size = 10000 * 2**i
    p = Performance(lambda : code(10000), lambda:setup(size),5,'\n\nPriority Queue of size ' + str(size))
    p.evaluate()
    p.analyze()