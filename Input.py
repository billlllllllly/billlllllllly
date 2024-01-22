import re
import os

def getchidx(intxt):
    for i in range(len(intxt)):
        x = re.findall("[a-zA-Z()0-9;:#*+-=_\'\"\/.~\[\]]", intxt[i])
        if len(intxt[i]) != len(x):
            return i
        
def transform(inputfile, filename):
    try:
        inputfiledata = inputfile.readlines()
    except:
        print("file error")
        return 0
    path = 'C:/Users/sunfar/Desktop/billy/EVT/inputtemp'
    os.chdir(path)
    vocablistfile = open(filename, "x", encoding='utf-8')

    for i in range(len(inputfiledata)):
        try:
            word = inputfiledata[i].split()
            chidx = getchidx(word)
        except:
            print("error in line " + (i+1) + " " + word + '\n')

        else:
            vocablistfile.write("{\"English\":\"")
            for j in range(chidx-1):
                vocablistfile.write(word[j]+' ')
            vocablistfile.write(word[chidx-1])

            vocablistfile.write("\", \"Chinese\":\"")
            for j in range(chidx, len(word)-1):
                vocablistfile.write(word[j]+' ')
            vocablistfile.write(word[len(word)-1])

            vocablistfile.write("\", \"weight\":2}\n")

    vocablistfile.close()
    return 0


#main code
path = 'C:/Users/sunfar/Desktop/billy/EVT/forinput'
dirlist = os.listdir(path)

for file in dirlist:
    path = 'C:/Users/sunfar/Desktop/billy/EVT/forinput'
    os.chdir(path)
    inputfile = open(file, "r", encoding='utf-8')
    filename = file[:-4] + '-T.txt'
    #print(filename)
    transform(inputfile, filename)
    inputfile.close()
