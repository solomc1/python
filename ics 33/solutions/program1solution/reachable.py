import goody
import prompt
from collections import defaultdict


def read_graph(file):
    graph = defaultdict(set)
    for line in file:
        s,d = line.strip().split(';')
        graph[s].add(d)
    return graph


def print_graph(graph):
    print('\nGraph: source -> {destination} edges')
    for s,d in sorted(graph.items()):
        print('  ',s,'->',d)

        
def reachable(graph,start):
    reached, exploring = set(), [start]
    while exploring:
        s = exploring.pop(0)
        reached.add(s)
        for d in graph[s]:
            if d not in reached:
                exploring.append(d)
    return reached


graph = read_graph(goody.safe_open('Enter file with graph', 'r', 'Could not find that file'))
print_graph(graph)
while True:
    start = prompt.for_string('\nEnter starting node', None, (lambda x : x in graph or x == 'quit'), 'Not a source node')
    if start == 'quit':
        break
    print('From',start,'the reachable nodes are',reachable(graph,start))