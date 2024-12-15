#pragma once
#include "tools.h"
#include <string>
using namespace std;

string tolower1(string str);
string capitalize(string str);
void setNonCanonicalMode();
void restoreCanonicalMode();
void getFiles(vector<string>& files);
char getKBniput();