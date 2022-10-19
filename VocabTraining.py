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
    correctanswer = random.choices([i for i in range(0,len)], weights=weight, k=1)[0]
    answer = random.choices([i for i in range(0,len)], k=3)
    correctanswerinsertidx = random.randint(0,3)
    answer.insert(correctanswerinsertidx,correctanswer)
    target_language = random.randint(0,1)
    
    if target_language == 0:
        print(vocablist[correctanswer]["English"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(vocablist[answer[0]]["Chinese"],vocablist[answer[1]]["Chinese"],vocablist[answer[2]]["Chinese"],vocablist[answer[3]]["Chinese"]))
    else:
        print(vocablist[correctanswer]["Chinese"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(vocablist[answer[0]]["English"],vocablist[answer[1]]["English"],vocablist[answer[2]]["English"],vocablist[answer[3]]["English"]))
    
    userinput = int(input())
    
    if (userinput == -1):
        keepgoing = -1
        accuracy = (correctnum/totalnum)*100
        print(f"\nacccuracy:{accuracy}%\n")
    elif (answer[userinput - 1] == correctanswer):
        weight[correctanswer] -= 1
        weight[answer[userinput-1]] -= 1
        correctnum += 1
        totalnum += 1
    else:
        weight[correctanswer] += 2
        totalnum += 1
        print("  {0} {1}".format(vocablist[correctanswer]["English"],vocablist[correctanswer]["Chinese"]))
        print("  {0} {1}".format(vocablist[answer[userinput-1]]["English"],vocablist[answer[userinput-1]]["Chinese"]))
    print(f"--------------------------------------------------------{correctnum}/{totalnum}\n")

#keep/reset weight?
keepweight = input("keep weight? [y/n]")
if('y' == keepweight):
    for i in range(len):
        vocablist[i]["weight"] = weight[i]
        vocabfile.write(vocablist[i])

resetweight = input("reset weight? [y/n]")
if('y' == resetweight):
    with open("VocabM4-12.txt", "w", encoding='utf-8') as file:
        for i in range(len):
            vocablist[i]["weight"] = 2
            file.write()
