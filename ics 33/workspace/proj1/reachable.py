# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.

def read_graph(file: str) -> dict:
    lines = file.readlines()
    dictionaries = {}
    for line in lines:
        result = line.split(';')
        if result[0] in dictionaries:
            dictionaries[result[0]].add(result[1].strip())
        else:
            dictionaries[result[0]] = {result[1].strip()}
    return dictionaries

def print_graph(graphdict: dict) -> None:
    print('Graph: source -> {destination} edges')
    keylist = [key for key in graphdict]
    keylist.sort()
    for key in keylist:
        print('  ', key, '->', graphdict[key])

def reachable(graphdict: dict, startnode: str) -> set:
    reachedset = set()
    reachedset.add(startnode)
    exploredlist = [node for node in graphdict[startnode]]
    while len(exploredlist) != 0:
        key = exploredlist[0]
        reachedset.add(exploredlist.pop(0))
        if key in graphdict:
            for node in graphdict[key]:
                exploredlist.append(node)
    return reachedset
            

if __name__ == '__main__':
    with open(input('Name of file: ')) as f:
        graphdict = read_graph(f)
        print_graph(graphdict)
        while True:
            stnode = input('Enter a starting node: ')
            if stnode == 'quit':
                break
            print('From ', stnode, 'the reachable nodes are ', reachable(graphdict, stnode))
    