import goody
#from collections import defaultdict

def read_ndfa(file):
    ndfa = dict()
    for line in file:
        trans = dict() #defaultdict(set)
        desc = line.strip().split(';')
        for (s,d) in zip(desc[1::2],desc[2::2]):
            trans.setdefault(s,set()).add(d) #trans[s].add(d)
        ndfa[desc[0]] = trans
    return ndfa

def print_ndfa(fa):
    print('\nNon-Deterministic Finite Automaton')
    for s in sorted(fa):
        print(' ',s,'transitions:',sorted(fa[s].items()))
        
def process(ndfa,state,inputs):
    result =[state]
    states = set([state])
    for i in inputs:
        # Thanks to a suggestion by Max Kim
        states = {ns for s in states if i in ndfa[s] for ns in ndfa[s][i]}
        result.append((i,states))
#        new_states = set()
#        for s in states:
#            if i in ndfa[s]:
#                new_states |= ndfa[s][i]
#        result.append((i,new_states))
#        states = new_states
    return result

def interpret(result):
    print('Start state =',result[0])
    for i in result[1:]:
        print('  Input =',i[0],';','new possible states =',i[1])
    print('Stop state(s) =',result[-1][1])


ndfa = read_ndfa(goody.safe_open('Enter file with non-deterministic finite automaton', 'r', 'Could not find that file'))
print_ndfa(ndfa)
data = goody.safe_open('\nEnter file with start-state and input', 'r', 'Could not find that file')
for line in data:
    print('\nStarting new simulation')
    desc = line.strip().split(';')
    interpret(process(ndfa,desc[0],desc[1:]))
