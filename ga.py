import random
import numpy as np


class ga:
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

    #need to alter
    def fitness_caculate(testaccuracy):
        rate = []
        for i in testaccuracy:
            rate.append(i**2)
        return rate

    def offspring_making(rate, parents, population = 100, wanttomutate = 1):
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

    
