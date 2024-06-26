import random
import json
import time
import os

filepath = 'C:/Users/sunfar/Desktop/billy/EVT/out'
files = os.listdir(filepath)
print(f"path: \033[93m{filepath}\033[0m")
print("file: \033[93m", end = '')
print(*files, sep = ', ', end = '')
print("\033[0m")

vocablist = []
weight = []
for file in files:
    vocabfile = open(os.path.join(filepath, file), "r", encoding = 'utf-8')
    x = vocabfile.readlines()
    for i in range(len(x)): 
        vocablist.append(json.loads(x[i]))
        weight.append(vocablist[i]["weight"])
    
l = len(vocablist)

#accuracy
totalnum = 0
wrongnum = 0
correctnum = 0
accuracy = 0.0
keepgoing = 1

ansappeartime = [0,0,0,0]

#funtion define (choice)
def mutiple_choice():
    global correctnum
    global totalnum
    global wrongnum
    global keepgoing
    global weight
    global keepgoing
    correctanswer = random.choices([i for i in range(0,l)], weights=weight, k=1)[0]
    anserror = 1
    while (anserror == 1):
        answer = random.choices([i for i in range(0,l)], k=3)
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
        return
    elif (answer[userinput - 1] == correctanswer):
        weight[correctanswer] -= 2
        correctnum += 1
        totalnum += 1
    else:
        weight[correctanswer] += 2
        wrongnum += 1
        totalnum += 1
        print("\033[93m  {0} {1}\033[0m".format(vocablist[correctanswer]["English"],vocablist[correctanswer]["Chinese"]))
        print("\033[93m  {0} {1}\033[0m".format(vocablist[answer[userinput-1]]["English"],vocablist[answer[userinput-1]]["Chinese"]))
    print("--------------------------------------------------------", end = '')
    print("\033[92m%d\033[0m/\033[91m%d\033[0m/\033[96m%d\033[0m/%d\n" % (correctnum, wrongnum, totalnum, len(vocablist)))

#funtion define (hand write)
def handwrite():
    global correctnum
    global totalnum
    global wrongnum
    global weight
    global keepgoing
    wordidx = random.choices([i for i in range(0,l)], weights=weight, k=1)[0]
    word = vocablist[wordidx]["English"]
    if word[:1] == '#':
        weight[wordidx] -= 2
        return
    print(vocablist[wordidx]["Chinese"], end = ' ')
    iscomment = 0
    focus = ""
    if word[0] == '*':
        focus = word[1:]
        for s in focus.split():
            print("{0}_____".format(s[0]), end = ' ')
    else:
        for L in word.split():
            if L[:1]=="[" or iscomment==1:
                print(L, end = ' ')
                iscomment = 1
                if L[-1:]==']':
                    iscomment = 0
            else:
                focus = L
                print("{0}_____{1}".format(L[:1], L[-1:]), end = ' ')
    userinput = str(input("\n"))
    if userinput == "-1":
        keepgoing = -1
        return
    if(userinput == focus):
        correctnum += 1
        totalnum += 1
        weight[wordidx] -= 2
    else:
        totalnum += 1
        wrongnum += 1
        print("\033[93m{}\033[0m".format(focus))
        userinput = str(input())
    print("--------------------------------------------------------", end = '')
    print("\033[92m%d\033[0m/\033[91m%d\033[0m/\033[96m%d\033[0m/%d\n" % (correctnum, wrongnum, totalnum, len(vocablist)))


#run
userinputmode = input("enter mode [mc/hw]  \033[92m")
print("\033[0m")
start_time = time.time()
if(userinputmode == "hw"):
    while (1 == keepgoing):
        handwrite()
        if(weight.count(0) == l):
            break
else:
    while (1 == keepgoing):
        mutiple_choice()
        if(weight.count(0) == l):
            break
    
end_time = time.time()
accuracy = (correctnum/totalnum)
mtcpq = (end_time - start_time)/totalnum
print("\033[93m=================================")
print("accuracy  : %d/%d" % (correctnum, totalnum))
print("            %03.2f" % accuracy)
print("per q.    : %0.2f sec" % mtcpq)
print("=================================\033[0m")


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
