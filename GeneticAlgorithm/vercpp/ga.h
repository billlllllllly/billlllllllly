#ifndef GA_h
#define GA_h

#include <list>
using namespace std;

class GAmodule{
    public:
    list<float> history_best;
    list<float> history_worst;

    protected:
    unsigned int population_size;
    unsigned int gene_size;
    unsigned float mutation_rate;
    unsigned int generation;
    list<list<int>> population;

    protected:
    virtual float f2c()=0;
    virtual float fitness_func()=0;
    void population_initialize();
    void mutation(list<float>* individual);
    void crossover(list<float>[2]* parent);
    void fitness_calculate(list<float>* populationfitness);
    void crossoverrate_calculate(list<float>* populationfitnesss, list<float>* crossover_rate);
    void reproduce(list<int>* child, list<float>* crossover_rate);
    void evolve();
}

#endif
