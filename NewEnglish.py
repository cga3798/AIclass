import nltk
from nltk import word_tokenize
from nltk.util import ngrams
text = open('../AICLASS/doyle-27.txt', 'r').read()
word1dDict = {}
word2Dict = {}

token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)

for b in trigrams:
    if (b[0] not in word1dDict):
        word1dDict[b[0]] = [(b[1], [(b[2], 1)])]
    else:
        temp = word1dDict.get(b[0])
        found = False
        for n in temp:
            if n[0] == b[1]:
                found = True
                found1 = False
                for k in n[1]:
                    if (k[0] == b[2]):
                        n[1].append((b[2],k[1] + 1))                        
                        n[1].remove(k)
                        found1 = True
                if not found1:
                    n[1].append((b[2], 1))

        if not found:
            temp.append((b[1], [(b[2], 1)]))        

for n in word1dDict:
    for k in word1dDict.get(n):
        for l in k[1]:
            word2Dict[n] = [(k[0], [(l[0], l[1]/len(k[1]))])]