#pragma once
#include "tools.h"
#include <dirent.h> // For opendir, readdir, closedir
#include <cstring>  // For strerror
#include <cerrno>   // For errno
#include <termios.h>
#include <unistd.h>
#include <iostream>
#include <string>
using namespace std;

string tolower1(string str){
    string str2 = "";
    for(char a : str){
        if((a-'A'>=0) && (a-'A'<26)){
            a = a + ('a' - 'A');
        }
        str2 += a;
    }
    return str2;
}

string capitalize(string str){
    string temp="";
    if((str[0]-'a'>=0) && (str[0]-'a'<26)){
        temp += str[0] - ('a' - 'A');
    }
    for(int i=1; i<str.length(); i++){
        temp += str[i];
    }
    return (string)temp;
}

// Set terminal to non-canonical mode
void setNonCanonicalMode() {
    struct termios t;
    tcgetattr(STDIN_FILENO, &t); // Get current terminal settings
    t.c_lflag &= ~ICANON;        // Disable canonical mode
    t.c_lflag &= ~ECHO;          // Disable echo
    tcsetattr(STDIN_FILENO, TCSANOW, &t);
}

// Restore terminal to canonical mode
void restoreCanonicalMode() {
    struct termios t;
    tcgetattr(STDIN_FILENO, &t);
    t.c_lflag |= ICANON;
    t.c_lflag |= ECHO;
    tcsetattr(STDIN_FILENO, TCSANOW, &t);
}

void getFiles(vector<string>& files) {
    //provided by chat-GPT
    //get files in specific dictionary on linux
    string path = "/edahome/course/2024CPP/2024CPP076/final_project/";

    DIR *dir = opendir(path.c_str());
    if (dir == nullptr) {
        cerr << "Error opening directory: " << strerror(errno) << '\n';
        return;
    }
    struct dirent *entry;
    while ((entry = readdir(dir)) != nullptr) {
        // Ignore "." and ".." entries
        string fileName = string(entry->d_name);
        if (fileName != "." && fileName != ".." && fileName.substr(fileName.length()-4, 4)==".txt"){
            files.push_back(fileName);
        }
    }
    closedir(dir);
    return;
}

char getKBniput(){
    char ch;
    read(STDIN_FILENO, &ch, 1); // Read one character
    if(ch == '\033'){ // Escape sequence
        char seq[2];
        if(read(STDIN_FILENO, &seq, 2) == 2){ // Read the next two characters
            if(seq[0] == '['){
                string temp = to_string(seq[1]-'A');
                return temp[0];
            }
        }
    }else{
        //normal kb input, including enter key 
        return ch;
    }
}