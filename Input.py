import re

def getchidx(intxt):
    for i in range(len(intxt)):
        x = re.findall("[a-zA-Z()0-9\'\"\/.~\[\]]", intxt[i])
        if len(intxt[i]) != len(x):
            print(i)
            return i


inputfile = open("VocabInput.txt", "r", encoding='utf-8')
vocablistfile = open("temp.txt", "w", encoding='utf-8')

inputfiledata = inputfile.readlines()
for i in range(len(inputfiledata)):
    word = inputfiledata[i].split()
    print(word , end='  ')
    chidx = getchidx(word)

    vocablistfile.write("{\"English\":\"")
    for j in range(chidx-1):
        vocablistfile.write(word[j]+' ')
    vocablistfile.write(word[chidx-1])

    vocablistfile.write("\", \"Chinese\":\"")
    for j in range(chidx, len(word)-1):
        vocablistfile.write(word[j]+' ')
    vocablistfile.write(word[len(word)-1])

    vocablistfile.write("\", \"weight\":2}\n")

inputfile.close()
vocablistfile.close()
