import random

def mutation(individual):
    msi = random.randint(0, 10)
    mei = msi + 5
    for i in range(msi, mei, 1):
        individual[i] = random.randint(0, 9)
    return individual

def crossover(x1, x2):
    target = random.randint(0, len(x1)-1)
    y1 = []
    y2 = []
    y1 = x1[0:target]
    y1.append(x2[target:])
    y2 = x2[0:target]
    y2.append(x1[target:])
    offspring = [y1, y2]
    return offspring

def fitness_caculate(parent):
    rate = []
    temp = 0.0
    for i in range(len(parent)):
        temp = 0.0
        for j in parent[i]:
            temp += parent[i][j]
        rate.append(temp)
    return rate

def offspring_making(rate, parents, population = 100):
    offspring = []
    for i in range(population//2):
        parent_target = random.choices(parents, rate, k = 2)
        oft = (crossover(parent_target[0], parent_target[1]))
        ifmutate = random.randint(0, 5)
        if ifmutate == 1:
            oft[0] = mutation(oft[0])
        elif ifmutate == 2:
            oft[1] = mutation(oft[1])
            offspring.append(oft)
    return offspring


#main
generation = 100
population = 100
neuro = 20
parent = []
for i in range(population):
    individual = []
    for j in range(neuro):
        individual.append(random.randint(0, 9))
        parent.append(individual)
offspring = []
rate = []
for i in range(generation):
    rate = fitness_caculate(parent)
    offspring = offspring_making(rate, parent, population)
    best = 0
    for j in rate:
        if rate[j] > best:
            best = rate[j]
    print(f"best --- {best}")
    parent = offspring   
print("\033[93m----END----\033[97m")