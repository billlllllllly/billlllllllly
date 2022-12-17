import random

def mutation(x):
    targexcromosome = random.randint()%x.len()
    msi = random.randint()%x[targexcromosome].len()
    mei = random.randint()%x[targexcromosome].len()
    for i in range(msi, mei, 1):
        x[targexcromosome][i] = random.randint()
    return x

def crossover(x1, x2):
    targetcromosome = random.randint()%x1.len()
    y1 = x1[targetcromosome]
    y2 = x1[targetcromosome]
    x1[targetcromosome] = y2
    x1[targetcromosome] = y1
    return x1, x2

def fitness():
    a
