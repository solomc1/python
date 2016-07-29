import goody

def print_dict(title,d,key=None,reverse=False):
    print('\n',title,sep='')
    for k in sorted(d,key=key,reverse=reverse):
        print(' ',k,' -> ', d[k])


def read_voter_preferences(file):
    votes = dict()
    for line in file:
        entry = line.rstrip().split(';')
        votes[entry[0]] = entry[1:]
    return votes


def evaluate_ballot(vp,cie):
    vd = {c : 0 for c in cie} # defaultdict(int)
    for clist in vp.values():
        for c in clist:
            if c in cie:
                vd[c] += 1
                break
    return vd


def remaining_candidates(vd):
    needed_votes = min(vd.values())
    return {c for c in vd if (vd[c] > needed_votes)}       


vp = read_voter_preferences(goody.safe_open('Enter file with voter preferences', 'r', 'Could not find that file'))
print_dict('Voter Preferences',vp,None,False)
cie = {c for cs in vp.values() for c in cs}     

ballot = 1
while len(cie) > 1:
    vd = evaluate_ballot(vp,cie)
    print_dict ('Vote count on ballot #' +str(ballot) + ' with candidates (alphabetically) = ' + str(cie),vd)
    print_dict ('Vote count on ballot #' +str(ballot) + ' with candidates (numerical) = ' + str(cie),vd,lambda x : vd[x],True)
    cie = remaining_candidates(vd)
    ballot += 1
if len(cie) == 1:
    print('\nWinner is ',cie)
else:
    print('\nNo winner: election is a tie among candidate remaining on the last ballot')