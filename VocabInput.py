inputfile = open("VocabInput.txt", "r", encoding='utf-16')
vocablistfile = open("VocabM4-12", "w", encoding='utf-16')

inputfiledata = inputfile.readlines()
for i in range(len(inputfiledata)):
    vocablistfile.write("{\"English\":\"")
    vocablistfile.write(inputfiledata[i].split()[0])
    vocablistfile.write("\", \"Chinese\":\"")
    vocablistfile.write(inputfiledata[i].split()[1])
    vocablistfile.write("\", \"weight\":5}\n")


inputfile.close()
vocablistfile.close()