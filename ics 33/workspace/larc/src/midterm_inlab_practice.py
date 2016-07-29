import goody
import prompt
from collections import defaultdict


def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        s,d = line.strip().split(';'))
        graph[s].add(d)
    return graph

def print_graph(graph):
    for s,d in sorted(graph.items(), key = lambda x: x[1], x[2]):
        print(s,d)
        
def reachable(graph,start):
    reached = set() 
    exploring = [start]
    while exploring:
        s = exploring.pop(0)
        reached.add(s)
        for d in graph[s]:
            if d not in reached:
                exploring.append(d)
    return reached
   
def print_dict(title,d,key=None,reverse=False):
    for k in sorted(d, key = key, reverse = reverse):
        print(' ', k, ' -_>')
    


def read_voter_preferences(file):
    votes = dict()
    for line in file:
        entry = line.rstrip().split(';')
        votes[entry[0]]= entry[1:]
    return votes
    


def evaluate_ballot(vp,cie):
    vd = {c: 0 for c in cie}
    for clist in vp.values():
        for c in clist:
            if c in cie:
                vd[c ] +=1
                break
    return vd



def remaining_candidates(vd):
    needed_votes = min(vd.values())
    return {c for c in vd if (vd[c]> needed_votes)}


