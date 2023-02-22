import random
import numpy as np

class ga(individual):

    

    def mutation(individual):
        for cro in individual:
            for gene in cro:
                if random.randint(1, 100) == 1:
                    gene = random.randint(1, 10)
        return individual
    #ok

    def crossover(in1, in2):
        target = random.randint(0, len(in1)-1)
        y1 = []
        y2 = []
        y1.extend(in1[0:target])
        y1.extend(in2[target:])
        y2.extend(in2[0:target])
        y2.extend(in1[target:])
        offspring = [y1, y2]
        return offspring

    #need to fix
    def fitness_caculate(testaccuracy):
        rate = []
        for i in testaccuracy:
            rate.append(i**2)
        return rate

    def reproduct(rate, parents, population = 100, wanttomutate = 1):
        offspring = []
        for i in range(population//2):
            parent_target = random.choices(parents, rate, k = 2)
            oft = (ga.crossover(parent_target[0], parent_target[1]))
            if wanttomutate == 1:
                ifmutate = random.randint(0, 5)
                if ifmutate == 1:
                    oft[0] = ga.mutation(oft[0])
                elif ifmutate == 2:
                    oft[1] = ga.mutation(oft[1])
            offspring.extend(oft)
        return offspring

    def ans(v):
        max = 0
        idx = 0
        for i in range(len(v)):
            if v[i] > max:
                idx = i
        return idx

