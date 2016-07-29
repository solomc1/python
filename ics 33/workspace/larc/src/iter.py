try:
    _hidden = iter(range(10))
    while True:
        num = next(_hidden)
        print(num)
        print(num**2)
except StopIteration:
    pass
    
class Candy_Bag:
    def __init__ (self, list_of_candy:list):
        self.contents = list_of_candy
    
    def __iter__(self):
        return iter(self.contents)
    
myBag = Candy_Bag(['snickers','chocolate','gum'])
    
for candy in myBag:
    print(candy)
    
import re
wrongName = "Sindy"
pattern = 'S'
compiled_pattern = re.compile(pattern)
Correctstring = re.sub(compiled_pattern)

#def __setattr__(self, name, value):
    #write code that saves the value to some sort of data structure
    
counts = {}

class Count_Num_Access:
    def __init__(self):
        pass

    def __getattr__(self, name):
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1
        print(counts)
        

    def __setattr__(self, name, value):
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1
        print(counts)
        




a = Count_Num_Access()


a.b
a.c
a.b = 5
