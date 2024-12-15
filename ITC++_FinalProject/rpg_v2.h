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
#include <unistd.h> //sleep()

#define OPTION 5

using namespace std;

class RPG{
    private:
    string inputFileName = "alice.txt";
    string outputFileName = "final.txt";
    int targetLength = 500;
    int coherenceLevel = 3;
    int changeLineFlag = 80;
    int changeLineCounter = 0;
    vector<vector<string> > Choice = {
        {},
        {"final.txt", "generated.txt", ""},
        {"100", "200", "500", ""},
        {"1", "2", "3"},
        {"60", "80", "100", ""}
    };
    vector<string> paragraph;
    vector<string> Value = {"alice.txt", "final.txt", "500", "3", "80"};
    vector<string> Title = {"input file", "output file", "desired length", "coherence level", "line length"};
    unordered_map<string, vector<string> > wordMap;
    //unordered_map<string, int> wordConut;

    void dumping(string key, string value);
    vector<string> split(string target);
    vector<string> sentenceGenerator(int recentLength);
    vector<string> txtprocess(string str, vector<string> key);
    bool wordGenerator(vector<string> keys, string& result);
    void warpAndFileOut(vector<string> str);
    void wordMapFileOut();
    bool isNounOrPronoun(string str);
    void clearAndTitle();
    void wordModify(string& str);
    bool checkValible(int idx, string input);
    void printSettingList(int highlight, int expand, int expandHighlight);
    void paragraphToTerminal();
    void setting2(int& label1Idx);

    public:
    void setting1();
    void begin();
    void fileprocess();
    void paragraphGenerator();
    void test();
    void textanalysis();
    
};