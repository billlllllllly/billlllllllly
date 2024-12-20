#pragma once
#include "rpg.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
#include <random>
#include <ctime>
#include <cstdlib>
using namespace std;

class RPG(aa){
    private:
    map<string, vector<string> > wordMap;
    string L = ".";
    void dumping(string& key, string& value);

    public:
    void begin(string fileName, int targetlength);
    void fileprocess(string fileName);
    string txtlineprocess(string str, string key);
    string wordGenerator(string key, int futher);
    void paragraphGenerator(int pLength, string outputFileName);
    void fileout(string str, string outputFileName);
    void wordMapFileout();
    void test();

    void sentenceGenerator();
};