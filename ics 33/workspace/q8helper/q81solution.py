import random
from goody         import irange
from priorityqueue import PriorityQueue
from performance   import Performance




def setup(size):
    global pq_new
    pq_new = PriorityQueue([i for i in range(size)])
    
def code(merges):
    global pq_new
    for i in range(merges):
        pq_new.remove()
        
for i in irange(0,8):
    size = 10000 * 2**i
    p = Performance(lambda : code(10000), lambda:setup(size),5,'\n\nPriorityQueue Class of size ' + str(size))
    p.evaluate()
    p.analyze()