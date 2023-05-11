import random
import json
import time


#data loading
file = "all1.txt"
vocabfile = open(file, "r", encoding = 'utf-8')
print(f"\nusing file: \033[93m{file}\033[97m")
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

ansappeartime = [0,0,0,0]

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
    ansappeartime[correctanswerinsertidx] += 1
    answer.insert(correctanswerinsertidx,correctanswer)
    target_language = random.randint(0,1)
    
    if target_language == 0:
        print(vocablist[correctanswer]["English"])
        print("(1){0}\n(2){1}\n(3){2}\n(4){3}\n".format(vocablist[answer[0]]["Chinese"],vocablist[answer[1]]["Chinese"],vocablist[answer[2]]["Chinese"],vocablist[answer[3]]["Chinese"]))
    else:
        print(vocablist[correctanswer]["Chinese"])
        print("(1){0}\n(2){1}\n(3){2}\n(4){3}\n".format(vocablist[answer[0]]["English"],vocablist[answer[1]]["English"],vocablist[answer[2]]["English"],vocablist[answer[3]]["English"]))
    
    
    userinput = input()
    while userinput != '1' and userinput != '2' and userinput != '3' and userinput != '4' and userinput != '-1':
        print("\033[1;91m !!! INPUT ERROR !!!\033[0m")
        userinput = input()
    userinput = int(userinput)


    if (userinput == -1):
        keepgoing = -1
    elif (answer[userinput - 1] == correctanswer):
        weight[correctanswer] -= 2
        correctnum += 1
        totalnum += 1
    else:
        weight[correctanswer] += 2
        totalnum += 1
        print("\033[93m  {0} {1}\033[97m".format(vocablist[correctanswer]["English"],vocablist[correctanswer]["Chinese"]))
        print("\033[93m  {0} {1}\033[97m".format(vocablist[answer[userinput-1]]["English"],vocablist[answer[userinput-1]]["Chinese"]))
    print(f"--------------------------------------------------------\033[32m{correctnum}/{totalnum}\n \033[97m")

#funtion define (hand write)
def handwrite(i):
    global correctnum
    global totalnum
    word = vocablist[i]["English"]
    print("{0} {1}_____{2}".format(vocablist[i]["Chinese"], word[:1], word[-1:]))
    userinput = str(input())
    if(userinput == vocablist[i]["English"]):
        correctnum += 1
        totalnum += 1
        print(f"--------------------------------------------------------\033[32m{correctnum}/{totalnum}\n \033[97m")
    else:
        totalnum += 1
        print("\n\033[93m{}\033[97m".format(vocablist[i]["English"]))
        print(f"--------------------------------------------------------\033[32m{correctnum}/{totalnum}\n \033[97m")



#run
userinputmode = input("enter mode [mc/hw]  \033[32m")
print("\033[97m")
start_time = time.time()
if(userinputmode == "hw"):
    random.shuffle(vocablist)
    for i in range(len):    
        handwrite(i)
else:
    while (1 == keepgoing):
        mutiple_choice()
        if(weight.count(0) == len):
            break
    
end_time = time.time()
accuracy = str((correctnum/totalnum))[:5]
mtcpq = str((end_time - start_time)/totalnum)[:4]
ttc = str(end_time - start_time)[:4]
print(f"\033[93m-- accuracy: {accuracy} --\033[97m")
print(f"\033[93m-- mtcpq: {mtcpq} sec --\033[97m")
print(f"\033[93m-- ttc: {ttc} sec --\033[97m", end='\n\n\r')


"""
#keep/reset weight?
keepweight = input("keep weight? [y/n]")
if('y' == keepweight):
    with open("weight.txt", "w", encoding='utf-8') as file:
        for i in range(len):
            file.write(str(weight[i]))
            file.write("\n")
           
resetweight = input("reset weight? [y/n]")
if('y' == resetweight):
    with open("VocabM4-12.txt", "w", encoding='utf-8') as file:
        for i in range(len):
            vocablist[i]["weight"] = 2
            x = json.dumps(vocablist[i])
            file.write(x)
"""