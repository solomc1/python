'''
Created on Apr 25, 2014

@author: Solomon
'''

class Repeat:
    def __init__(self, iterable,max_times = None):
        self.iterable = iterable
        self.max_times = max_times
    
    def __iter__(self):
        class Repeat_iter:
            def __init__(self, iterable, max_times):
                self.iteraable = iterable
                self.max_times_left = max_times
                self.iterator = iter(iterable)
                
            def __next__(self):
                if self.max_times_left != None and self.max_times_left <= 0:
                    raise StopIteration
                else:
                    try:
                        return next(self.iterator)
                    except StopIteration:
                        if self.max_times_left != None:
                            self.max_times_left -= 1
                        self.iterator = iter(self.iterable)
                        return next(self)
        return Repeat_iter(self.iterable, self.max_times)
            
class psorted:
    def __init__(selfself, iterable, key = None, reverse = False):
        self.result= list(iterable)
        sel.fresult.sort(ley = key, reverse = reverse)
        
    def __inter__(self):
        return iter(self.result)
    
                    
for i in Filter('abasdlkfja;sfja;fja', lambda x: x not in 'richardpattis'):
    pass


#staticmethod
def _gen(bins):
    for i in range(10):
        yield bins[i]
        
        
def repeat(iterable, max_times = None):
    while max_times == None or max_times >0:
        for i in iterable:
            yield i
        max_times -=1
        


























