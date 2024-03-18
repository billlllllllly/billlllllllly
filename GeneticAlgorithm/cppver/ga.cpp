#include "ga.h"
#include "tools.h"
#include <algorithm>
using namespace std;

void GAmodule::population_initialize(){
    for(int i = 1; i <= population_size; i++){
        list<int> individual_gene;
        for(int j = 1; j<= gene_size; j++){
            individual_gene.push_back(randint(0, 10));
        }
        population.push_back(individual_gene);
    }
}

void GAmodule::mutation(list<float>* individual){
    int mutation_start_idx = rand()%gene_size;
    int mutate_length = 1;
    do{
        mutate_length++;
        individual[mutation_start_idx] = randint(0, 10);
        if(float()(rand()%1 != 1)) || (mutation_start_idx+1 > gene_size){
            return;
        } 
    }
    while(mutate_length <= 3);
}

void GAmodule::crossover(list<float>[2]* parent, list<list<int>>* child){
    int cidx = rand();
    swap_ranges((*parent[0]).rbegin()+cidx, (*parent[0]).rend(), (*parent[1]).rbegin()+cidx);
}

void GAmodule::fitness_calculate(list<float>* populationfitness){
    for(list<int> P : population){
        float individual_fitness = fitness_func(P);
        (*populationfitness).push_back(individual_fitness);
    }
    return;
}

void GAmodule::crossoverrate_calculate(list<float>* populationfitnesss, list<float>* crossover_rate){
    for(float P : populationfitnesss){
        (*crossover_rate).push_back(f2c(P));
    }
    return;
}

void GAmodule::reproduce(list<list<int>>* child, list<float>* crossover_rate){
    list<int> parent_target = randomchoiceidx((*crossover_rate), 2);
    crossover([&population[parent_target[0]], &population[parent_target[1]]]);
    return; 
}

void GAmodule::evolve(){
    for(int epoch = 0; epoch <= generation; epoch++){
        list<float> populationfitnesss; 
        fitness_calculate(&populationfitnesss);
        history_best.push_back(max(populationfitnesss));
        list<float> crossover_rate; 
        crossoverrate_calculate(&crossover_rate, &populationfitnesss);
        list<list<int>> offspring;
        while(offspring.size() < population.size()){
            list<list<int>> child; 
            reproduce(&child, &crossover_rate);
            offspring.insert(offspring.end(), child.begin(), child.end());
        }
        population = offspring;
    }
    return;
}
