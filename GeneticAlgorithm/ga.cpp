#include <ga.h>
#include <list>
#include <random>

class GAmodule{
    protected:
    int population_size;
    int gene_size;
    float mutation_rate;
    int generation;
    float GAmodule::f2c(){
        return 0.0f;
    }
    float GAmodule::fitness_func(){
        return 0.0f;
    }
    void GAmodule::population_initialize(){};
    void GAmodule::mutation(){};
    void GAmodule::crossover(){};
    float GAmodule::fitness_caculate(){};
    float GAmodule::crossoverrate_caculate(){};
    void GAmodule::reproduct(){
        int offspring[];
    };
    void GAmodule::evolve(){
        for(int epoch = 0; epoch <= generation; epoch++){
            float populationfitnesss = fitness_caculate();
            float crossover_rate = crossoverrate_caculate();
            int offspring = reproduct();
            int population = offspring;
        }
    };
}