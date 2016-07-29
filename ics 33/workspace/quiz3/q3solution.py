import prompt,re
import math
from goody import type_as_str

def expand_re(pat_dict:{str:str}):

    for key, val in pat_dict.items():
        hash_pat = re.compile(r"#(\w+)#")
        match = hash_pat.search(val)
        if match:
            key_to_replace = match.group(1)
            print(key_to_replace)
            val_to_replace = pat_dict[key_to_replace]
            pat_dict[key] = hash_pat.sub('(' + val_to_replace + ')', val)
            return expand_re(pat_dict)
    return pat_dict


            
class Point:
    
    def __init__(self,x,y):
        if type(x) == int and type(y) == int:
            self.x = x
            self.y = y
        else:
            raise AssertionError('Input is not a valid integer')
        

    def __repr__(self):
        return ('Point('+str(self.x)+','+str(self.y)+')')
            


    def __str__(self):
        return ('(x='+str(self.x)+','+'y='+str(self.y)+')')
    

    def __bool__(self):
        return not (self.x == 0 and self.y==0)
        

    def __add__(self,right):
        if type(right) == Point:
            newx= self.x+ right.x
            newy = self.y+ right.y
            return (Point(newx,newy))
        else:
            raise TypeError("invalid input try again")
        

    def __mul__(self,left):
        if type(left) == int:
            newx= self.x* left
            newy = self.y* left
            return (Point(newx,newy))
        else:
            raise TypeError("invalid input try again")
        
        

    def __rmul__(self,left):
        return self.__mul__(left)
        

    def __getitem__(self,index):
        if type(index) in [str,int]:
            if index == 0 or index == 'x':
                return self.x
            elif index == 1 or index =='y':
                return self.y
            else:
                raise IndexError('not a valid input')
        else:
            raise IndexError('not a valid input')

    def __lt__(self,right):
        if type(right) is Point:
            return self.distance()<right.distance()
        elif type(right) in (int,float):
            return self.distance()<right

        else:
            raise TypeError('Invalid input, please try again')
            
    def distance(self):
        return math.sqrt(((self.y)**2+(self.x)**2))    
        
    def __call__(self,x,y):
        if type(x) == int and type(y)== int:
            self.x=x
            self.y=y
        else:
            raise AssertionError('not an integer, please try again')
        


from collections import defaultdict
class History:
    def __init__(self):
        self.history = defaultdict(list)
        
    def __getattr__(self,name):
        history_count = name.count("_prev")
        attr_name = re.sub("_prev+","",name)
        if attr_name in self.history.keys():
            history_total = len(self.history[attr_name])
            if history_count < history_total:
                return self.history[attr_name][history_total - history_count - 1]
            return None
        else:
            raise NameError(name + " does not exist.")
       
    def __setattr__(self,name,value):
        if '_prev' in name:
            raise NameError("not a string please try again")
        if 'history' in self.__dict__:
            self.history[name].append(value)
        self.__dict__[name] = value
            

    def __getitem__(self,index):
        if index > 0:
            raise IndexError("The index is negative or 0 please try again.")
        i = abs(index)
        history_dict = {}
        for key, history_list in self.history.items():
            history_total = len(history_list)
            history_dict[key] = history_list[history_total - i - 1] if i < history_total else None 
        return history_dict    

if __name__ == '__main__':
    
    if prompt.for_bool('Test expand?',True):
        pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
        expand_re(pd)
        print('result =',pd)
        # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
        
        pd = dict(integer       =r'[+-]?\d+',
                  integer_range =r'#integer#(..#integer#)?',
                  integer_list  =r'#integer_range#(?,#integer_range#)*',
                  integer_set   =r'{#integer_list#?}')
        expand_re(pd)
        print('result =',pd)
        # produces/prints the dictionary 
        # {'integer'      : '[+-]?\\d+',
        #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
        #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
        #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
        # }
        
        pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
        expand_re(pd)
        print('result =',pd)
        # produces/prints the dictionary 
        # {'d': '(((correct)))',
        #  'c': '((correct))',
        #  'b': '(correct)',
        #  'a': 'correct',
        #  'g': '((((((correct))))))',
        #  'f': '(((((correct)))))',
        #  'e': '((((correct))))'
        # }
    
    import driver
    driver.driver()
    
    
