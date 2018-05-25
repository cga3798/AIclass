import nltk
import random
from nltk import word_tokenize
from nltk.util import ngrams
text = open('../AICLASS/doyle-27.txt', 'r').read()
text += "\n"
text += open('../AICLASS/alice-27.txt', 'r').read()
text += "\n"
text += open('../AICLASS/doyle-case-27.txt', 'r').read()
text += "\n"
text += open('../AICLASS/london-call-27.txt', 'r').read()
text += "\n"
text += open('../AICLASS/melville-billy-27.txt', 'r').read()
text += "\n"
text += open('../AICLASS/twain-adventures-27.txt', 'r').read()

text = text.lower()

word1dDict = {}
word2Dict = {}




token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)

for b in trigrams:
    if (b[0] not in word1dDict.keys()):
        word1dDict[b[0]] = ([((b[1], 1), [(b[2], 1)])], 1)
    else:
        temp = word1dDict.get(b[0])[0]
        found = False 
        word1List = []
        for n in temp:
            if n[0][0] == b[1]:
                found = True 
                found1 = False
                tempList = []
                for k in n[1]:
                    if (k[0] == b[2]):
                        tempList.append((b[2],k[1] + 1))                        
                        found1 = True
                    else:
                        tempList.append(k)
                if not found1:
                    tempList.append((b[2], 1))
                temp1 = (n[0][0], n[0][1] + 1)
                number = word1dDict.get(b[0])[1]
                word1List.append((temp1, tempList))
                break
            else:
                word1List.append(n)
        if not found:
            word1List.append(((b[1], 1), [(b[2], 1)]))      
        newTemp = word1dDict.get(b[0])
        word1dDict[b[0]] = ( word1List ,newTemp[1] + 1)

for word1 in word1dDict:
    w1G = word1dDict.get(word1)
    tempList2 = []
    for word2 in w1G[0]:
        tempList = []
        for word3 in word2[1]:
            temp = (word3[0], word3[1]/ len(word2[1]))
            tempList.append(temp)
        tempList = sorted(tempList,key=lambda x: x[1], reverse = True )
        temp = ( (word2[0][0], len(word2[1]) / w1G[1])  ,tempList)
        tempList2.append(temp)
    tempList2 = sorted(tempList2,key=lambda x: x[0][1], reverse = True )
    word1dDict[word1] = (tempList2, w1G[1])
        

options = list(word1dDict.keys())
choice= random.choice(options)
story = choice + " "
repeat = []
count = 0
while (len(story) < 1000):
    count = count + 1
    temp = word1dDict.get(choice)[0]
    story += temp[0][0][0] + " " + temp[0][1][0][0] + " "
    temp2 = choice + " " + temp[0][0][0] + " " + temp[0][1][0][0] + " "
    repeat.append(temp2)
    choice = temp[0][1][0][0]
    temp = word1dDict.get(choice)[0]
    temp3 = choice + " " + temp[0][0][0] + " " + temp[0][1][0][0] + " "
    
    if temp3 in repeat:
        options = list(word1dDict.keys())
        choice= random.choice(options)
    if len(repeat) > 5:
        repeat.remove(repeat[0])
    if (count > 20):
        count = 0
        story += "\n"
f = open("AllBooks.txt", "w")
f.write(story)
f.close()
print(story)