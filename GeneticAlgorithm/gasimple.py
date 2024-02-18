import random
import numpy as np
import matplotlib.pyplot as plt
import tools

def mutation(individual):
    msi = random.randint(0, len(individual) - 3)
    mei = random.randint(msi, len(individual) - 1)
    
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
    for p in parent:
        fitness = tools.method1(p)
        rate.append(fitness)
    
    best = max(rate)/500
    worst = min(rate)/500
    rate = tools.normolization(rate)
    
    for i in range(len(rate)):
        rate[i] = int(np.floor(rate[i]*100))
    return rate, best, worst
    
def offspring_making(rate, parents, population, mutaterate=0.01):
    offspring = []
    for i in range(population//2):
        parent_target = random.choices(parents, rate, k = 2)
        oft = (crossover(parent_target[0], parent_target[1]))
        if mutaterate > random.random():
            oft[0] = mutation(oft[0])
        if mutaterate > random.random():
            oft[1] = mutation(oft[1])
        offspring.extend(oft)
    return offspring

#main
def main(generation=1000, population=1000, neuro=100, mutaterate=0.01):
    parent = []
    for i in range(population):
        individual = []
        for j in range(neuro):
            individual.append(random.randint(0, 10))
        parent.append(individual)
    offspring = []
    bestofgeneration = []
    worstofgeneration = []
    x = []
    for i in range(generation + 1):
        rate, best, worst = fitness_caculate(parent)
        offspring = offspring_making(rate, parent, population, mutaterate)
        if i % 10 == 0:
            bestofgeneration.append(best)
            worstofgeneration.append(worst)
            x.append(i)
        parent = offspring
        tools.show_progress(progress=(i/generation))
    return [x, bestofgeneration, worstofgeneration]



for i in range(1, 11):
    print(f'...........\033[93mtest--{i}\033[0m...........')
    [x, best, worst] = main(mutaterate = i*0.01)
    plt.plot(x, best, label='mr={}'.format(i*0.01))
plt.show()


'''
[x, best, worst] = main(mutaterate=0.01)
plt.plot(x, best, label="best")
plt.plot(x, worst, label="worst")

plt.xlabel('generation')
plt.ylabel('fitness rate')
plt.axis([0, 1000, 0, 1])
os.chdir("C:/Users/sunfar/Desktop/billy/cssg/genetic _algorithm/figure")
plt.suptitle("fitness = sum")
plt.legend()
#plt.savefig('temp.png')
'''