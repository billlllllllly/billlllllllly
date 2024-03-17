class GAmodule{
    protected:
    virtual float f2c();
    virtual float fitness_func();
    void population_initialize();
    void mutation();
    void crossover();
    float fitness_calculate();
    float crossoverrate_calculate();
    void reproduct();
    void evolve();
}
