import random
import json
from symbol import annassign

#data loading
vocabfile = open("VocabM4-12.txt", "r", encoding='utf-8')
x = vocabfile.readlines()
vocablist = []
weight = []
for i in range(len(x)):
    vocablist.append(json.loads(x[i]))
    weight.append(vocablist[i]["weight"])
len = len(vocablist)

#accuracy
correctnum = 0
totalnum = 0
accuracy = 0.0

#run
wronglist = []
random.shuffle(vocablist)
for i in range(len):
    anserror = 1
    while (anserror == 1):
        answer = random.choices([i for i in range(0,len)], k=3)
        if(answer.count(answer[0]) == 1 and answer.count(answer[1]) == 1 and answer.count(i) == 0):
            anserror = 0
    insertidx = random.randint(0,3)
    answer.insert(insertidx,i)
    print(vocablist[i]["Chinese"])
    print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(vocablist[answer[0]]["English"],vocablist[answer[1]]["English"],vocablist[answer[2]]["English"],vocablist[answer[3]]["English"]))
    userinput = int(input())
    totalnum += 1
    if(answer[userinput-1] != i):
        wronglist.append(i)
    else:
        correctnum += 1

#result
print("--------------------accuracy:{0}%".format(correctnum*100/totalnum))
for i in range (len(wronglist)):
    print("  {0} {1}".format(vocablist[wronglist[i]]["English"],vocablist[wronglist[i]]["Chinese"]))