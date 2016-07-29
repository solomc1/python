import goody

def read_fa(file):
    fa = dict()
    for line in file:
        desc = line.strip().split(';')
        fa[desc[0]] = dict(zip(desc[1::2],desc[2::2]))
    return fa

def print_fa(fa):
    print('\nFinite Automaton Description')
    for s in sorted(fa):
        print(' ',s,'transitions:',sorted(fa[s].items()))
        
def process(fa,state,inputs):
    result =[state]
    for i in inputs:
        if i not in fa[state]:
            result.append((i,None))
            return result
        else:
            state = fa[state][i]
            result.append((i,state))
    return result

def interpret(faresult):
    print('Start state =',faresult[0])
    for i in faresult[1:]:
        print('  Input = ',i[0],'; ',sep='',end='')
        if i[1] != None:
            print('new state =',i[1])
        else:
            print('illegal input; terminated')
    print('Stop state =',faresult[-1][1])


fa = read_fa(goody.safe_open('Enter file with finite automaton', 'r', 'Could not find that file',1))
print_fa(fa)
data = goody.safe_open('\nEnter file with start-states and inputs', 'r', 'Could not find that file')
for line in data:
    print('\nStarting new simulation')
    desc = line.strip().split(';')
    interpret(process(fa,desc[0],desc[1:]))
