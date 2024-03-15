class GAmodule{
    protected:
    virtual float f2c();
    virtual float fitness_func();
    void population_initialize();
    void mutation();
    void crossover();
    float fitness_caculate();
    float crossoverrate_caculate();
    void reproduct();
    void evolve();
}