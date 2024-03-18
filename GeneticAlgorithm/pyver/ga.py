import random
import matplotlib.pyplot as plt
import numpy as np
import tools
import os

class GA:
    def __init__(self,
                 fitness_to_crossover=tools.f2c,
                 fitness_func=tools.method1,
                 gene_length=100, population_size=1000, generation=500, mutation_rate=0.01,
                 drawresult=False):
        self.f2c = fitness_to_crossover
        self.fitness_func = fitness_func
        self.gene_length = gene_length
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generation = generation
        self.population = self.initialize_population()
        self.history_best = []
        self.history_worst = []
        self.evolve()
        if drawresult == True:
            self.draw_result()

    def initialize_population(self):
        population = []
        for i in range(self.population_size):
            individual = []
            for j in range(self.gene_length):
                individual.append(random.randint(0, 10))
            population.append(individual)
        return population
    
    def mutation(self, individual):
        mutation_start_idx = random.randint(0, len(individual) - 3)
        mutation_length = random.randint(0, 3)
        for i in range(mutation_start_idx, mutation_start_idx+mutation_length, 1):
            individual[i] = random.randint(0, 10)
        return individual

    def crossover(self, in1, in2):
        target = random.randint(0, len(in1)-1)
        y1 = []
        y2 = []
        y1.extend(in1[0:target])
        y1.extend(in2[target:])
        y2.extend(in2[0:target])
        y2.extend(in1[target:])
        return [y1, y2]

    def fitness_ccalculate(self):
        rate=[]
        for p in self.population:
            fitness = self.fitness_func(p)
            rate.append(fitness)
        self.history_best.append(max(rate)/500)
        self.history_worst.append(min(rate)/500)
        rate = tools.normolization(rate)
        for i in range(len(rate)):
            rate[i] = int(np.floor(rate[i]*100))
        return rate

    def crossover_rate_calculation(self, populationfitness):
        crossover_rate = []
        for i in populationfitness:
            crossover_rate.append(self.f2c(i))
        return crossover_rate

    def reproduct(self, crossover_rate):
        offspring = []
        while len(offspring) < self.population_size:
            parent_target = random.choices(self.population, crossover_rate, k=2)
            oft = (self.crossover(parent_target[0], parent_target[1]))
            if self.mutation_rate > random.random():
                oft[0] = self.mutation(oft[0])
            if self.mutation_rate > random.random():
                oft[1] = self.mutation(oft[1])
            offspring.extend(oft)
        return offspring

    def evolve(self):
        for epoch in range(self.generation + 1):
            populationfitness = self.fitness_ccalculate()
            crossover_rate = self.crossover_rate_calculation(populationfitness)
            offspring = self.reproduct(crossover_rate)
            self.population = offspring
            tools.show_progress(epoch/self.generation)

    def draw_result(self):
        plt.plot(self.history_best, label='best')
        plt.plot(self.history_worst, label='worst')
        plt.xlabel('generation')
        plt.ylabel('fitness rate')
        plt.axis([0, self.generation, 0, 1])
        plt.suptitle("GA test")
        plt.legend()
        path = 'C:/Users/sunfar/Desktop/billy/genetic _algorithm/figure'
        plt.savefig(os.path.join(path, 'temp002.png'))
        plt.show()
