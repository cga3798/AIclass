import nltk
from nltk import word_tokenize
from nltk.util import ngrams
text = open('../AICLASS/doyle-27.txt', 'r').read()
dict = {}
token = nltk.word_tokenize(text)
print(token)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
for b in bigrams:
    print(b)

for b in trigrams:
    if (b[0] not in dict):
        dict[b[0]] = [[b[1]], [b[2]]]
    else:
        for (word in dict.get(b[0])):
            if (b[1] not in word[0]):
                
