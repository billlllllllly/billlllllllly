import re
import os
from googletrans import Translator

def getchidx(wordarr):
    """
    notice that googletrans must be the version: 3.1.0a0 or there should be errors
    use ''python -m pip install googletrans==3.1.0a0''
    or use the commented code below
    """
    for i in range(len(wordarr)):
        result = Translator().detect(wordarr[i]).lang
        if result != 'en':
            return i
        """
        x = re.findall("[a-zA-Z()0-9;:#*+-=_\'\"\/.~\[\]]", wordarr[i])
        if len(wordarr[i]) != len(x):
            return i
        """
        
def transform(inputvocab, filename, outpath):
    try:
        inputvocabdata = inputvocab.readlines()
    except:
        print("file error")
        return
    
    #new the output file
    j=1
    while j >= 0:
        try:
            vocablistfile = open(os.path.join(outpath, filename), "x", encoding='utf-8')
            j=-1
        except:
            j += 1
            if j <= 2:
                filename = filename[:-4] + '(' + str(j) + ').txt'
            else:
                filename = filename[:-7] + '(' + str(j) + ').txt'

    i=0
    #transfom into json's format
    for i in range(len(inputvocabdata)):
        try:
            wordarr = inputvocabdata[i].split()
            chidx = getchidx(wordarr)
        except:
            print("error in line " + (i+1) + " " + wordarr + '\n')

        else:
            vocablistfile.write("{\"English\":\"")
            for j in range(chidx-1):
                vocablistfile.write(wordarr[j]+' ')
            vocablistfile.write(wordarr[chidx-1])

            vocablistfile.write("\", \"Chinese\":\"")
            for j in range(chidx, len(wordarr)-1):
                vocablistfile.write(wordarr[j]+' ')
            vocablistfile.write(wordarr[len(wordarr)-1])

            vocablistfile.write("\", \"weight\":2}\n")

    vocablistfile.close()
    return 0

def main(inpath='C:/Users/sunfar/Desktop/billy/EVT/in',
         outpath='C:/Users/sunfar/Desktop/billy/EVT/out'):
    filelist = os.listdir(inpath)
    for file in filelist:
        inputvocab = open(os.path.join(inpath, file), "r", encoding='utf-8')
        filename = file[:-4] + '-T.txt'
        #print(filename)
        transform(inputvocab, filename, outpath)
        inputvocab.close()



main()

"""
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
"""
