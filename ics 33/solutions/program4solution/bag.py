from collections import defaultdict
from goody import type_as_str
class Bag:
    def __init__(self,values=[]):
        self.counts = defaultdict(int)
        for v in values:
            self.counts[v] += 1
    
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'

    def __repr__(self):
        param = []
        for k,v in self.counts.items():
            param += v*[k]
        return 'Bag('+str(param)+')'

    def __len__(self):
        return sum(self.counts.values())
        
    def unique(self):
        return len(self.counts)
        
    def __contains__(self,v):
        return v in self.counts
    
    def count(self,v):
        return self.counts[v] if v in self.counts else 0

    def add(self,v):
        self.counts[v] += 1
    
    def remove(self,v):
        if v in self.counts:
            self.counts[v] -= 1
            if self.counts[v] == 0:
                del self.counts[v]
        else:
            raise ValueError('Bag.remove('+str(v)+'): not in Bag')
        
    def __eq__(self,right):
        if type(right) is not Bag or len(self) != len(right):
            return False
        else:
            for i in self.counts:
                # check not it to avoid creating count of 0 via defaultdict
                if i not in right or self.counts[i] != right.counts[i]:
                    return False
            return True
        
    @staticmethod
    def _gen(x):
        for k,v in x.items():
            for i in range(v):
                yield k  
                
    def __iter__(self):
        return Bag._gen(dict(self.counts))
    
    def x__check_annotation__(self, check, param, value, check_history):
        def name_as_str (x): return "'"+str(x)+"'"
        def value_as_str(x): return "'"+str(x)+"'"
        
        assert isinstance(value,Bag), name_as_str(param)+' failed annotation check(wrong type): value = '+value_as_str(value)+\
                                       '\n  was type '+type_as_str(value)+' ...should be type Bag\n'+check_history  
                                                      
        assert len(self) == 1, name_as_str(param)+' annotation inconsistency: Bag should have 1 value but had '+str(len(self))+\
                              '\n  annotation = '+str(self)+'\n'+check_history 
                                              
        for annot_v in self.counts: # get first and only
            pass
        for v in value.counts: # not use regular iterator to avoid duplicates
            check(param,annot_v,v, check_history+'Bag value check: '+str(annot_v)+'\n')