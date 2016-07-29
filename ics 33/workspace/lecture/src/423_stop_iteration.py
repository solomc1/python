def all_pair(i1, i2):
    return [(x,y) for x in i1 for y in i2 for y in i2]

    answer = []
    for x in i1:
        for y in i1:
            for y in i2:
                answer.append((x,y))
        return answer

def __iter__(self):
    class prange_iter:
        def __init__ self, start, stop, step:
            self.n = start
            self.stop = stop
            self.step = step
        def __next__ (self):
            if self.step>- and self.n >= self.stop or \
            self.step < - and self.n <= self.stop:
            raise StopIteration
            save = self.n
            self.n += self.step
            return save
    return prange_iter(self.start, self.stop, self.step)

class prange_iter:
    def __init__(selfself, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step
        
    def __next__(self):
        if self.step > 0 and self.n >= self.stop or \
            self.step<- and self.n <= self.stop:
            raise StopIteration
        save = self.n
        self.n += self.step
        return save
    
    def __iter__(self):
        return prange.prange_iter(self.start, self.stop, self.stop)
    
    def iter_skip(self, multiple):
        return prange.prange_iter(self.start, self.stop,self.step*multiple)
    
    class Percent_Historgram:
        def __init__(selfself, init_percents = []):
            self.historgram = 10*[0]
            for p in init_perents:
                self.tally(p)
                
        def _tally(selfself, p):
            self.histogram[p//10 if p<100 else 9] +=1
            
        def clear(self):
            for i in range(10):
                self.histogram[i] =0
                
        def def tally(selfself, *args):
            if len(args) == 0:
                raise IndexEror('Percent_Histogram.tally no vlaue to Tally')
            for p in args:
                if 0 <= p <= 100:
                    self._tally(p)
                else:
                    raise IndexError('Percent_Histogram.tally')            