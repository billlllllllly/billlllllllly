import random
import json


#data loading
vocabfile = open("M4-19.txt", "r", encoding='utf-8')
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
keepgoing = 1

#funtion define (choice)
def mutiple_choice():
    global correctnum
    global totalnum
    global keepgoing
    correctanswer = random.choices([i for i in range(0,len)], weights=weight, k=1)[0]
    anserror = 1
    while (anserror == 1):
        answer = random.choices([i for i in range(0,len)], k=3)
        if(answer.count(answer[0]) == 1 and answer.count(answer[1]) == 1 and answer.count(correctanswer) == 0):
            anserror = 0
    correctanswerinsertidx = random.randint(0,3)
    answer.insert(correctanswerinsertidx,correctanswer)
    target_language = random.randint(0,1)
    
    if target_language == 0:
        print(vocablist[correctanswer]["English"])
        print("(1){0}\n(2){1}\n(3){2}\n(4){3}\n".format(vocablist[answer[0]]["Chinese"],vocablist[answer[1]]["Chinese"],vocablist[answer[2]]["Chinese"],vocablist[answer[3]]["Chinese"]))
    else:
        print(vocablist[correctanswer]["Chinese"])
        print("(1){0}\n(2){1}\n(3){2}\n(4){3}\n".format(vocablist[answer[0]]["English"],vocablist[answer[1]]["English"],vocablist[answer[2]]["English"],vocablist[answer[3]]["English"]))
    
    userinput = input()
    if userinput != '1' and userinput != '2' and userinput != '3' and userinput != '4':
        print("\033[1;91m !!! INPUT ERROR !!!\033[0m")
        userinput = input()
    userinput = int(userinput)


    
    if (userinput == -1):
        keepgoing = -1
        print(f"\nacccuracy:{accuracy}%\n")
    elif (answer[userinput - 1] == correctanswer):
        weight[correctanswer] -= 1
        weight[answer[userinput-1]] -= 1
        correctnum += 1
        totalnum += 1
    else:
        weight[correctanswer] += 2
        totalnum += 1
        print("\033[93m  {0} {1}\033[0m".format(vocablist[correctanswer]["English"],vocablist[correctanswer]["Chinese"]))
        print("\033[93m  {0} {1}\033[0m".format(vocablist[answer[userinput-1]]["English"],vocablist[answer[userinput-1]]["Chinese"]))
    print(f"--------------------------------------------------------\033[32m{correctnum}/{totalnum}\n \033[0m")

#funtion define (hand write)
def handwrite(i):
    global correctnum
    global totalnum
    print("{0} {1}_____".format(vocablist[i]["Chinese"], vocablist[i]["English"][:2]))
    userinput = str(input())
    if(userinput == vocablist[i]["English"]):
        correctnum += 1
        totalnum += 1
        print(f"--------------------------------------------------------{correctnum}/{totalnum}\n")
    else:
        totalnum += 1
        print("\n  {}".format(vocablist[i]["English"]))
        print(f"--------------------------------------------------------{correctnum}/{totalnum}\n")



#run
userinputmode = input("enter mode [mc/hw]  \033[32m")
print("\033[0m")
if(userinputmode == "mc"):
    while (1 == keepgoing):
        mutiple_choice()
        if(weight.count(0) == len):
            break
else:
    random.shuffle(vocablist)
    for i in range(len):    
        handwrite(i)

accuracy = (correctnum/totalnum)*100
print(f"accuracy:{accuracy}")


"""
#keep/reset weight?
keepweight = input("keep weight? [y/n]")
if('y' == keepweight):
    with open("VocabM4-12.txt", "w", encoding='utf-8') as file:
        for i in range(len):
            vocablist[i]["weight"] = weight[i]
            x = json.dumps(vocablist[i])
            file.write(x)
resetweight = input("reset weight? [y/n]")
if('y' == resetweight):
    with open("VocabM4-12.txt", "w", encoding='utf-8') as file:
        for i in range(len):
            vocablist[i]["weight"] = 2
            x = json.dumps(vocablist[i])
            file.write(x)
"""
