# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.
from collections import defaultdict

def read_fa(file: 'open file') -> dict:
    fa_dict = defaultdict(dict)
    for l in file.readlines():
        splitlist = l.split(';')
        x = 1
        while x < len(splitlist):
            fa_dict[splitlist[0]][splitlist[x]] = splitlist[x+1].split('\n')[0]
            x += 2
    return dict(fa_dict)
        

def print_fa(d: dict) -> None:
    print("Finite Automation")
    for i in list(d.keys()):
        print('  '+i+' transitions:', sorted([(k, d[i][k]) for k in d[i].keys()]))
    print()
        

def process(d: dict, s: str, l: list) -> []:
    processlist = [s]
    state = s
    for number in l:
        try:
            processlist.append((number.split('\n')[0], d[state][number.split('\n')[0]]))
            state = d[state][number.split('\n')[0]]
        except:
            processlist.append((number.split('\n')[0], None))
    return processlist

def interpret(l: list) -> None:
    print('Starting new simulation')
    print("Starting state = ", l[0])
    for element in range(len(l)-1):
        if l[element+1][1] == None:
            print("  Input = ", l[element+1][0], "; illegal input: terminated")
            break
        print("  Input = ", l[element+1][0], "; new state = ", l[element+1][1])
    print("Stop state = ", l[-1][1],'\n')
        
        

if __name__ == '__main__':
    with open(input('Enter file with finite automaton: ')) as f:
        print()
        fadict = read_fa(f)
        print_fa(fadict)
    with open(input('Enter file with finite automaton: ')) as f:
        print()
        for line in f.readlines():
            splitlines = line.split(';')
            interpret(process(fadict, splitlines[0], splitlines[1:]))
            