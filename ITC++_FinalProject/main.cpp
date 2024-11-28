#include "rpg.h"
#include "tools.h"
#include <string>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]){
    string fileName = (string)argv[1];
    int targetLength = stoi(argv[2]);
    RPG p1;
    //p1.fileprocess(fileName);
    srand(time(0));
    p1.begin(fileName, targetLength);
    //p1.wordMapFileout();
    return 0;
}