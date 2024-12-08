#include "rpg_v2.h"
#include "tools.h"

void RPG::set(){
    string userinput = "";
    cout << "\033[0m-Enter read in filename: \033[93m";
    getline(cin, userinput);
    if(userinput != ""){
        ifstream test(userinput.c_str());
        if(test){
            inputFileName = userinput;
        }else{
            cout << "\t\033[91mFILE NOT FOUND\n";
            cout << "\t\033[93mdefault using: " << inputFileName << '\n';
        }
        test.close();
    }else{
        cout << "\t\033[93mdefault using: " << inputFileName << '\n';
    }

    cout << "\033[0m\n-Enter target length: \033[93m";
    getline(cin, userinput);
    if(userinput != ""){
        int temp = -1;
        try{
            temp = stoi(userinput);
        }catch(invalid_argument){}
        if(temp <= 0){
            cout << "\t\033[91mINVALID ARGUMENT\n";
            cout << "\t\033[93mdefault using: " << targetLength << '\n';
        }else{
            targetLength = temp;
        }
    }else{
        cout << "\t\033[93mdefault using: " << targetLength << '\n';
    }

    cout << "\033[0m\n-Enter coherence level[1/2/3]: \033[93m";
    getline(cin, userinput);
    if(userinput != ""){
        int temp = -1;
        try{
            temp = stoi(userinput);
        }catch(invalid_argument){}
        if(temp<1 || temp>3){
            cout << "\t\033[91mINVALID ARGUMENT\n";
            cout << "\t\033[93mdefault using: " << coherenceLevel << '\n';
        }else{
            coherenceLevel  = temp;
        }
    }else{
        cout << "\t\033[93mdefault using: " << coherenceLevel << '\n';
    }
    //resteing terminal color
    cout << "\033[0m";
    return;
}

void RPG::begin(){
    set();
    fileprocess();
    srand(time(0));
    paragraphGenerator();
    return;
}

void RPG::fileprocess(){
    ifstream fileIn;
    fileIn.open(inputFileName.c_str());
    string str = "";
    vector<string> last3Word = {"", "", "."};
    while(getline(fileIn, str)){
        last3Word = txtprocess(str, last3Word);
    }
    return;
}

vector<string> RPG::txtprocess(string str, vector<string> keys){
    vector<string> result = split(str);
    for(int i=0; i<result.size(); i++){
        dumping(keys[2], result[i]);
        dumping(keys[1]+keys[2], result[i]);
        dumping(keys[0]+keys[1]+keys[2], result[i]);
        keys = {keys[1], keys[2], result[i]};
    }
    return keys;
}

string RPG::wordGenerator(vector<string> keys){
    string key = "";
    switch(cohrenceLevel){
        case 1:
            key = keys[2];
            break;
        case 2:
            key = keys[1] + keys[2];
            break;
        case 3:
            key = keys[0] + keys[1] + keys[2];
            break;
        default:
            key = keys[2];
            break;
    }
    int size = wordMap[key].size();
    int idx = rand()%size;
    string result = wordMap[key][idx];
    return result;
}

void RPG::paragraphGenerator(){
    vector<string> temp;
    for(int recentLength=0; recentLength<targetlength; ){
        temp = sentenceGenerator(recentLength);
        temp[0][0] = toupper(temp[0][0]);
        fileout(temp);
    }
    return;
}

vector<string> RPG::sentenceGenerator(int& recentLenth){
    vector<string> sentence;
    int randLength = rand()%10 + 5;
    //start
    vector<string> possibleStarters;
    for(auto ele : wordMap["."]){
        if(isNounOrPronoun(ele))
            possibleStarters.push_back(ele);
    }
    if(possibleStarters.size() == 0){
        possibleStarters = wordMap["."];
    }

    sentence.push_back(possibleStarters[(rand()%possibleStarters.size()) - 1]);
    while(sentence.size()<randLength-2){
        //get keys
        vector<string> keys;
        for(int c=0; c<3; c++){
            int idx = sentence.size() - 3 + c;
            if(idx > 0){
                keys.push_back(sentence[idx]);
            }else{
                if(c==2){
                    keys.push_back(".");
                }else{
                    keys.push_back("");
                }
            }
        }
        string word;
        //avoid same
        do{
            word = wordGenerator(keys);
        }while(word == sentence[sentence.size()-1]);
        sentence.push_back(word);
    }
    //ending the sentence
    while(1){

    }
    
    return ;
}

void RPG::fileout(vector<string> str){
    for()
    return;
}

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

vector<string> RPG::split(string target){
    vector<string> result;
    string word = "";
    string possible = "";
    target += " ";
    for(int i=0; i<target.length(); i++){
        if(target[i] == ' '){
            char delta = word[word.length()-1];
            if(delta=='.' || delta=='?' || delta=='!'){
                result.push_back(word.substr(0, word.length()-1));
                result.push_back(word.substr(word.length()-1, 1));
            }else{
                result.push_back(word);
            }
            word = "";
        }else{
            word += target[i];
        }
    }
    
    return result;
}

void RPG::dumping(string key, string value){
    bool duplicate = 0;
    for(string ele: wordMap[key]){
        if(ele == value){
            duplicate = 1;
            break;
        }
    }
    if(!duplicate) wordMap[key].push_back(value);
    return;
}

bool RPG::isNounOrPronoun(string str){
    vector<string> noun = {};
    vector<string> pronou
    return 1;
}