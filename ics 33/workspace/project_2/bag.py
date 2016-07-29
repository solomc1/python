# Kevin Wong, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
from goody import type_as_str

class Bag:
    
    def __init__(self, values = []):
        self.bag = defaultdict(int)
        for x in values:
            self.bag[x] += 1
            
    def __repr__(self):
        result = []
        for k,v in self.bag.items():
            for i in range(v):
                result.append(k)
        return 'Bag('+str(result)+')'
    
    def __str__(self):
        result_list = []
        for k,v in self.bag.items():
            result_list.append(k + '['+str(v)+']')
        result_str = ''
        for x in result_list:
            result_str += x+','
        return 'Bag('+result_str[:-1]+')'
    
    def __len__(self):
        result = 0
        for v in self.bag.values():
            result+=v
        return result
    
    def unique(self):
        return len(self.bag.keys())
    
    def __contains__(self, value):
        return value in self.bag.keys()
    
    def count(self, key):
        if key not in self.bag.keys():
            return 0
        return self.bag[key]
    
    def add(self, key):
        if key in self.bag.keys():
            self.bag[key] += 1
        else:
            self.bag[key] = 1
            
    def remove(self, key):
        if key in self.bag.keys():
            self.bag[key] -= 1
            if self.bag[key] == 0:
                self.bag.pop(key)
        else:
            raise ValueError(str(key)+ " is not in the Bag")
        
    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError("Cannot compare Bag with " + type_as_str(other))
        return self.bag == other.bag
    
    def __iter__(self):
        copy_dict = self.bag
        for k in copy_dict.keys():
            for x in range(copy_dict[k]):
                yield k
    
    
if __name__ == '__main__':

    import driver
    driver.driver()   
