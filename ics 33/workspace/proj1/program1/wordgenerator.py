# Adam Peter, Lab 6
# Solomon Chan, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming.
import goody
from collections import defaultdict
import random

def read_corpus(order_stas, file:'open file') -> dict:
    corpusdict = defaultdict(list)
    g = goody.read_file_values(f)
    prereadwords = []
    for x in range(eval(order_stas)):
        prereadwords.append(next(g))
    for i in g:
        if i not in corpusdict[tuple(prereadwords)]:
            corpusdict[tuple(prereadwords)].append(i)
        prereadwords = prereadwords[1:]
        prereadwords.append(i)
    return dict(corpusdict)
        

def print_corpus(d:dict)->None:
    print('Corpus')
    min = 10000
    max = -1
    for i in sorted(d.keys()):
        if len(d[i]) < min:
            min = len(d[i])
        if len(d[i]) > max:
            max = len(d[i])
        print(i, 'can be followed by any of ',d[i])
    print('min/max = {}/{}'.format(min, max))

def produce_text(d:dict, l:list, num:int)-> [str]:
    n_words = l
    new_words= []
    for i in range(num):
        w = random.choice(d[tuple(n_words)])
        n_words.remove(n_words[0])
        n_words.append(w)
        new_words.append(w)
    return new_words
    

if __name__ == '__main__':
    order = input('Enter order statistic: ')
    with open(input('Enter file to process: ')) as f:
        corpusdict = read_corpus(order, f)
        print_corpus(corpusdict)
        print()
        print("Enter", order,"words to start with")
        words = []
        for i in range(eval(order)):
            words.append(input("Enter word {}: ".format(i+1)))
            
        word_num = input("Enter # of words to generate: ")
        print("Random text = ", produce_text(corpusdict, words, eval(word_num)))
        