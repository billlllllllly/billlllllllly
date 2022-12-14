import random

def mutation(individual):
    msi = random.randint(0, len(individual) - 3)
    mei = msi + 3
    for i in range(msi, mei, 1):
        individual[i] = random.randint(0, 10)
    return individual

def crossover(x1, x2):
    target = random.randint(0, len(x1)-1)
    y1 = []
    y2 = []
    y1.extend(x1[0:target])
    y1.extend(x2[target:])
    y2.extend(x2[0:target])
    y2.extend(x1[target:])
    offspring = [y1, y2]
    return offspring

def fitness_caculate(parent):
    rate = []
    for i in range(len(parent)):
        temp = 0
        for j in parent[i]:
            temp += j
        rate.append(temp**2)
    return rate

def offspring_making(rate, parents, population = 100, wanttomutate = 1):
    offspring = []
    for i in range(population//2):
        parent_target = random.choices(parents, rate, k = 2)
        oft = (crossover(parent_target[0], parent_target[1]))
        if wanttomutate == 1:
            ifmutate = random.randint(0, 5)
            if ifmutate == 1:
                oft[0] = mutation(oft[0])
            elif ifmutate == 2:
                oft[1] = mutation(oft[1])
        offspring.extend(oft)
    return offspring


#main
generation = 10000
population = 100
neuro = 20
parent = []
for i in range(population):
    individual = []
    for j in range(neuro):
        individual.append(random.randint(0, 10))
    parent.append(individual)
offspring = []
rate = []
bestofgeneration = []
for i in range(generation + 1):
    rate = fitness_caculate(parent)
    offspring = offspring_making(rate, parent, population)
    bestidx = 0
    for j in range(len(rate)):
        if rate[j] > rate[bestidx]:
            bestidx = j
    if i % 50 == 0:
        best = sum(parent[bestidx])
        print(f"[{i}] ----- {best}")
    parent = offspring   
print("\033[93m----END----\033[97m")
