#include "tools.h"
#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <random>
using namespace std;


list<int> randomchoiceidx(list<float> rate, int k){
    random_device rd;
    mt19937 gen(rd());
    discrete_distribution<> d(rate.begin(), rate.end());
    list<int> choosenidx;// = new list<int>();
    while(choosenidx.size()<k){
        int temp = d(gen);
        bool choosen = 0;
        for(int C : choosenidx){
            if(temp == C){
                choosen = 1;
                break;
            }
        }
        if(choosen == 0){
            choosenidx.push_back(temp);
        }
    }
    return choosenidx;
}



void showprogress(float progress){
    int P = floor(progress*20);
    printf("[");
    for(int i = 1; i <= P; i++){
        printf("#");
    }
    for(int j = 20-P; j > 0; j--){
        printf("-");
    }
    printf("]");
    printf("%6d\r", int(progress*100));
    if(floor(progress)==1){
        printf("[####################]  \033[93mDONE\033[0m\n");
    }
}
