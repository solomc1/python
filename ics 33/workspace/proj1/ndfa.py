# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.
from collections import defaultdict
def read_ndfa(file:'open file')-> dict:
    ndfa_dict = defaultdict(dict)
    for l in file.readlines():
        splitlist = l.split(';')
        if len(splitlist) == 1:
            ndfa_dict[splitlist[0]] = dict()
        x = 1
        while x < len(splitlist):
            if splitlist[x] in ndfa_dict[splitlist[0]].keys():
                ndfa_dict[splitlist[0]][splitlist[x]].add(splitlist[x+1].split('\n')[0])
            else:
                ndfa_dict[splitlist[0]][splitlist[x]] = {splitlist[x+1].split('\n')[0]}
            x += 2
    return dict(ndfa_dict)

def print_ndfa(d:dict)->None:
    print("Non-Deterministic Finite Automation")
    for i in list(d.keys()):
        print('  '+i+' transitions:', sorted([(k, d[i][k]) for k in d[i].keys()]))
    print()

def process(d:dict, s:str, l:list)->[()]:
    processlist = [s]
    state = {s}
    for n in l:
        newset = set()
        for s in state:
            try:
                newset.update(d[s][n.split('\n')[0]])
            except:
                pass
        processlist.append((n.split('\n')[0], newset))
        state = newset
    return processlist

def interpret(l:[])->None:
    print('Starting new simulation')
    print("Starting state = ", l[0])
    for element in range(len(l)-1):
        if l[element+1][1] == None:
            print("  Input = ", l[element+1][0], "; illegal input: terminated")
            break
        print("  Input = ", l[element+1][0], "; new state = ", l[element+1][1])
    print("Stop state = ", l[-1][1],'\n')

if __name__ == '__main__':
    with open(input('Enter file with non-deterministic finite automaton: ')) as f:
        print()
        ndfadict = read_ndfa(f)
        print_ndfa(ndfadict)
    with open(input('Enter file with start-state and input: ')) as f:
        print()
        for line in f.readlines():
            splitlines = line.split(';')
            interpret(process(ndfadict, splitlines[0], splitlines[1:]))

