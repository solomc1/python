import goody
from goody import irange
import prompt
from random import choice
#from collections import defaultdict

def read_corpus(os,file):
    corpus = dict() # defaultdict(list)
    key =[next(file) for i in irange(os)]
    for w in file:
        if tuple(key) not in corpus or w not in corpus[tuple(key)]:# w not in corpus[tuple(key)]:
            corpus.setdefault(tuple(key),list()).append(w)
        key.pop(0)
        key.append(w)
    return corpus


def print_corpus(corpus):
    print('Corpus')
    mins,maxs=-1,-1
    for k in sorted(corpus):
        print(' ',k,'can be followed by any of', corpus[k])
        mins = len(corpus[k]) if mins == -1 or len(corpus[k]) < mins else mins
        maxs = len(corpus[k]) if maxs == -1 or len(corpus[k]) > maxs else maxs
        if len(corpus[k]) == 46:
            print (k,corpus[k])
    print('min/max =',str(mins)+'/'+str(maxs)) 


def produce_text(corpus,text,count):
    os = len(text)
    for i in irange(count):
        key = tuple(start[-os:])
        if key not in corpus:
            text.append(None)
            return text
        start.append(choice(corpus[key]))
    return start    



os = prompt.for_int('Enter order statistic',is_legal=lambda x : x >= 1)
corpus = read_corpus(os, goody.read_file_values(goody.safe_open('Enter file to process', 'r', 'Cannot find that file')))
print_corpus(corpus)

print('\nEnter '+str(os)+' words to start with')
start = [prompt.for_string('Enter word '+str(i)) for i in irange(os)]
how_many = prompt.for_int('Enter # of words to generate',is_legal=lambda x : x > 0)
text = produce_text(corpus,start,how_many)
print('Random text =',text)