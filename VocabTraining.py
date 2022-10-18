import random
import json

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
totalnum = 0
correctnum = 0
accuracy = 0.0

#run
keepgoing = 1
while (1 == keepgoing):
    answer = random.choices([i for i in range(0,len)], weights=weight, k=4)
    #while(answer.copy().sort()[0]==answer.copy().sort()[1] or answer.copy().sort()[1]==answer.copy().sort()[2] or answer.copy().sort()[2]==answer.copy().sort()[3]):
    #    answer = random.choices([i for i in range(0,len)], weights=weight, k=4)
    target_language = random.randint(0,1)
    correctanswer = random.randint(0,3)
    
    if target_language == 0:
        print(vocablist[answer[correctanswer]]["English"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(vocablist[answer[0]]["Chinese"],vocablist[answer[1]]["Chinese"],vocablist[answer[2]]["Chinese"],vocablist[answer[3]]["Chinese"]))
    else:
        print(vocablist[answer[correctanswer]]["Chinese"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(vocablist[answer[0]]["English"],vocablist[answer[1]]["English"],vocablist[answer[2]]["English"],vocablist[answer[3]]["English"]))
    
    userinput = int(input())
    
    if (userinput == -1):
        keepgoing = -1
    elif (userinput - 1 == correctanswer):
        correctnum += 1
        totalnum += 1
    else:
        totalnum += 1
        print("  {0} {1}".format(vocablist[answer[correctanswer]]["English"],vocablist[answer[correctanswer]]["Chinese"]))
        print("  {0} {1}".format(vocablist[answer[userinput-1]]["English"],vocablist[answer[userinput-1]]["Chinese"]))
    print(f"--------------------------------------------------------{correctnum}/{totalnum}\n")
    
    
    #keep/reset weight?
ksweight = input("keep or reset weight? [k/r/n]")
if('y' == ksweight):
    for i in range(len(x)):
        vocablist[i]["weight"] = weight[i]
        vocabfile.write(vocablist[i])
elif('s' == ksweight):
    for i in range(len(x)):
        vocablist[i]["weight"] = 5
        vocabfile.write(vocablist[i])
