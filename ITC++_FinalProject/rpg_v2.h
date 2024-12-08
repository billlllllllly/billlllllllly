#pragma once
#include "rpg_v2.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <iomanip>
#include <unordered_map>
#include <random>
#include <ctime>
#include <cstdlib>
using namespace std;

class RPG{
    private:
    string inputFileName = "alice.txt";
    string outputFileName = "final.txt";
    int targetLength = 500;
    int coherenceLevel = 2;
    int changeLineCounter = 0;
    unordered_map<string, vector<string> > wordMap;
    unordered_map<string, int> wordConut;

    void dumping(string key, string value);
    vector<string> split(string target);
    vector<string> sentenceGenerator(int& recentLength);
    bool isNounOrPronoun(string str);
    vector<string> txtprocess(string str, vector<string> key);
    string wordGenerator(vector<string> keys);
    void fileout(vector<string> str);
    void wordMapFileout();

    public:
    void set();
    void begin();
    void fileprocess();
    void paragraphGenerator();
    void test();
    void textanalysis();
    
};