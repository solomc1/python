# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.

from collections import defaultdict

def print_dict(title:str, d:dict, f = None, b:bool = False)->None:
    print(title)
    keylist = [key for key in d]
    keylist.sort(key = f)
    for key in keylist:
        print("  ", key, "->", d[key])
    

def read_voter_preferences(f:str)->dict:
    d = defaultdict(list)
    for line in f.readlines():
        result = line.split(';')
        for item in range(len(result)-1):
            d[result[0]].append((result[item+1][0]))
    return dict(d)
                                
def evaluate_ballot(d:dict, s:set)-> dict:
    candidates = defaultdict(int)
    for voter in d:
        for pref in d[voter]:
            if pref in s:
                candidates[pref]+=1
                break
    return dict(candidates)

def remaining_candidates(d:dict)->set:
    if len(d) == 2 and list(d.values())[0] == list(d.values())[1]:
        return set()
    lowestcandidate = ''
    lowestvote = 1000
    for candidate in d:
        if d[candidate] < lowestvote:
            lowestcandidate = candidate
            lowestvote = d[candidate]
    del d[lowestcandidate]
    return(set(d.keys()))
        
    
    


if __name__ == '__main__':
    with open(input("Enter file with voter preferences: ")) as f:
        read = read_voter_preferences(f)
        print_dict("Voter Preferences", read)
        r = set(read[list(read.keys())[0]])
        readcount = 0
        while len(r) > 1:
            readcount += 1
            votes = evaluate_ballot(read, r)
            print("\nVote count on ballot #{} with candidates (alphabetically) =".format(readcount), r)
            for key in sorted(list(votes.keys())):
                print("  ", key, "->", votes[key])
            print("\nVote count on ballot #{} with candidates (numerically) =".format(readcount), r)
            for key in sorted(list(votes), key = lambda key: votes[key], reverse = True):
                print("  ", key, "->", votes[key])
            r = remaining_candidates(votes)
            
        if r == set():
            print("\nNo one wins!")
        else:
            print("\n"+list(r)[0], 'is the winner!')