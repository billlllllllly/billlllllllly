#include "rpg.h"
#include "tools.h"

string RPG::txtlineprocess(string str, string key){
    string value = "";
    str = tolower1(str);
    bool flag = 0;
    for(int i=0; i<str.length(); i++){
        if((str[i]-'a'>=0)&&(str[i]-'a'<26)){
            flag = 1;
            value+=str[i];
            continue;
        }
        if(flag==1 && str[i]=='\''){
            flag = 1;
            value+=str[i];
            continue;
        }
        if(flag==1 && ((str[i]==',')||(str[i]==' '))){
            flag = 0;
            dumping(key, value);
            continue;
        }
        if((str[i]=='.')||(str[i]=='?')||(str[i]=='!')){
            flag = 0;
            dumping(key, value);
            value = {str[i]};
            dumping(key, value);
        }      
    }
    return key;
}
//finished?

void RPG::dumping(string& key, string& value){
    bool duplicate = 0;
    for(string ele: wordMap[key]){
        if(ele == value){
            duplicate = 1;
            break;
        }
    }
    if(!duplicate) wordMap[key].push_back(value);
    key = value;
    value = "";
    return;
}
//finished

void RPG::fileprocess(string fileName){
    ifstream fileIn;
    fileIn.open(fileName.c_str());
    string str = "";
    string lastWord = ".";
    while(getline(fileIn, str)){
        lastWord = txtlineprocess(str, lastWord);
    }
    return;
}
//finished

string RPG::wordGenerator(string key, int futher){
    int size = wordMap[key].size();
    //srand(788);
    int idx = rand()%size;
    //cout << idx << '\n';
    string result = wordMap[key][idx];
    return result;
}
//finished

void RPG::paragraphGenerator(int pLength, string outputFileName){
    string W = wordGenerator(".", 1);
    bool newline = 1;
    string sentence = "";
    for(int i=1; i<pLength; i++){
        if(W!="." && W!="?" && W!="!" && newline!=1)
            sentence += " ";
        sentence += W;
        newline = 0;
        W = wordGenerator(W, 1);
        if(i%20 == 0){
            if(W=="." || W=="?" || W=="!"){
                sentence += W;
                W = wordGenerator(W, 1);
            }
            newline = 1;
            fileout(sentence, outputFileName);
            sentence = "";
        }
    }
    return;
}
//finished

void RPG::fileout(string str, string outputFileName){
    ofstream fileout2;
    fileout2.open(outputFileName, ios::app);
    fileout2 << "\n" << str;
    fileout2.flush();
    fileout2.close();
    return;
}
//finished

void RPG::begin(string fileName, int targetlength){
    fileprocess(fileName);
    
    //write title
    ofstream fileout2;
    fileout2.open("finalout.txt");
    fileout2 << "-----FINAL GENERATED TEXT-----";
    fileout2.flush();
    fileout2.close();

    paragraphGenerator(targetlength, "finalout.txt");
    return;
}
//finished

void RPG::wordMapFileout(){
    ofstream fileout1;
    fileout1.open("wordmap.txt");
    for(const auto element : wordMap){
        fileout1 << "|" << setw(8) << element.first << ": ";
        for(string value : element.second){
            fileout1 << value << " / ";
        }
        fileout1 << "\n";
        fileout1.flush();
    }
    fileout1.close();
    return;
}
//finished

void RPG::sentenceGenerator(){
    vector<string> sentence;
    string W = wordGenerator(".", 1);
    //while (){
    //}
    return;
}



void RPG::test(){
    return;
}