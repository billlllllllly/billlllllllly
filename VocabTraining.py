import random
import json

#data loading
vocabfile = open("VocabM4-12", "r")
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
    answer = random.choices(vocablist, weights=weight, k=4)
    target_language = random.randint(0,1)
    correctanswer = random.randint(0,3)
    
    if target_language == 0:
        print(answer[correctanswer]["English"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(answer[0]["Chinese"],answer[1]["Chinese"],answer[2]["Chinese"],answer[3]["Chinese"]))
    else:
        print(answer[correctanswer]["Chinese"])
        print("(1){0}  (2){1}  (3){2}  (4){3}\n".format(answer[0]["English"],answer[1]["English"],answer[2]["English"],answer[3]["English"]))
    
    userinput = int(input())

    if (userinput - 1 == correctanswer):
        correctnum += 1
        totalnum += 1
    else:
        totalnum += 1
        print("  {0} {1}".format(answer[correctanswer]["English"],answer[correctanswer]["Chinese"]))
        print("  {0} {1}".format(answer[userinput-1]["English"],answer[userinput-1]["Chinese"]))
    print(f"--------------------------------------------------------{correctnum}/{totalnum}\n")