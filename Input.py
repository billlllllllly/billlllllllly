inputfile = open("VocabInput.txt", "r", encoding='utf-8')
vocablistfile = open("temp.txt", "w", encoding='utf-8')

inputfiledata = inputfile.readlines()
for i in range(len(inputfiledata)):
    word = inputfiledata[i].split()

    vocablistfile.write("{\"English\":\"")
    for j in range(len(word)-2):
        vocablistfile.write(word[j]+' ')
    vocablistfile.write(word[len(word)-2])

    vocablistfile.write("\", \"Chinese\":\"")
    vocablistfile.write(word[len(word)-1])

    vocablistfile.write("\", \"weight\":2}\n")

inputfile.close()
vocablistfile.close()
