#include "tools.h"

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