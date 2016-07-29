from collections import defaultdict
class History:
    def __init__(self):
        self.history = defaultdict(list)
        
    def __getattr__(self,name):
        myname = re.sub("_prev+","",name)
        if myname in self.history.keys():
            return self.__getitem__(-name.count("_prev"))[myname]
        elif myname not in self.history.keys():
            raise NameError('Attribute is not in the dictionary')

    def __setattr__(self,name,value):
        if '_prev' in name:
            raise NameError("not a string please try again")
        if 'history' in self.__dict__:
            self.history[name].append(value)
        self.__dict__[name] = value
            

    def __getitem__(self,index):
        if index> 0:
            raise IndexError('the length of the key must be an integer')
        for key, value in self.history.items():
            if len(value) >= abs(index):
                return (key,(value[-1+index]))
                
            else:
                 return None
