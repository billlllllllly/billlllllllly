#include "rpg_v2.h"
#include "tools.h"

void RPG::begin(){
    setting1();
    fileprocess();
    //cout << "f0\n";
    wordMapFileOut();
    //cout << "f1\n";
    srand(time(0));
    clearAndTitle();
    paragraphGenerator();
    paragraphToTerminal();
    cout << "\n\n";
    //cout << "f2\n";
    return;
}

void RPG::test(){
    setting1();
    fileprocess();
    wordMapFileOut();
    srand(time(0));
    vector<string> temp = sentenceGenerator(0);
    for(auto ele : temp){
        cout << ele << ' ';
    }
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
    vector<string> temp = split(str);
    vector<string> result = {};
    for(int i=0; i<temp.size(); i++){
        string T = "";
        for(int j=0; j<temp[i].length(); j++){
            char C = tolower(temp[i][j]);
            if(((C-'a'>=0)&&(C-'a'<26)) || (C=='\''))
                T += C;
        }
        //error on puncuations
        if(T!="")
            result.push_back(T);
        if(temp[i]=="." || temp[i]=="?" || temp[i]=="!")
            result.push_back(temp[i]);
    }
    for(int i=0; i<result.size(); i++){
        dumping(keys[2], result[i]);
        dumping(keys[1]+keys[2], result[i]);
        dumping(keys[0]+keys[1]+keys[2], result[i]);
        keys = {keys[1], keys[2], result[i]};
    }
    return keys;
}

bool RPG::wordGenerator(vector<string> keys, string& result){
    string key = "";
    switch(coherenceLevel){
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
    if(size == 0) return 0;
    int idx = rand()%size;
    result = wordMap[key][idx];
    return 1;
}

void RPG::paragraphGenerator(){
    vector<string> temp;
    int recentLength = 0;
    while(recentLength<targetLength){
        temp = sentenceGenerator(recentLength);
        recentLength += (temp.size()-1);
        temp[0][0] = toupper(temp[0][0]);
        warpAndFileOut(temp);
    }
    return;
}

vector<string> RPG::sentenceGenerator(int recentLenth){
    vector<string> sentence;
    int randLength = rand()%8 + 7;
    if(targetLength - recentLenth < 15)
        randLength = targetLength - recentLenth;
    if(randLength < 6){
        vector<string> temp;
        randLength++;
        while(randLength--){
            temp.push_back("");
        }
        return temp;
    }
    
    vector<string> possibleStarters = {};
    for(auto ele : wordMap["."]){
        if(isNounOrPronoun(ele))
            possibleStarters.push_back(ele);
    }
    if(possibleStarters.size() == 0){
        possibleStarters = wordMap["."];
    }

    sentence.push_back(possibleStarters[rand()%possibleStarters.size()]);
    recentLenth++;

    while(sentence.size()<randLength-1){
        //get keys error
        vector<string> keys = {"", "", "."};
        for(int c=coherenceLevel-1; c>=0; c--){
            int idx = sentence.size() - coherenceLevel + c;
            if(idx >= 0){
                keys[c+3-coherenceLevel] = (sentence[idx]);
            }
        }
        //cout << "keys: " << keys[0] << keys[1] << keys[2] << '\n';
        string word = "";
        if(!wordGenerator(keys, word)){
            break;
        }
        /*
        do{
            if(!wordGenerator(keys, word)){
                break;
            }
        }while(word == sentence[sentence.size()-1]);
        */
        sentence.push_back(word);
        if(word=="." || word=="?" || word=="!")
            return sentence;
        recentLenth++;
    }
    //ending the sentence
    sentence.push_back(".");
    //cout << "sentence size: " << sentence.size() << '\n';   
    return sentence;
}

void RPG::warpAndFileOut(vector<string> str){
    ofstream fileOut(outputFileName, ios::app);
    for(int i=0; i<str.size(); i++){
        wordModify(str[i]);
    }
    //word process
    str[str.size()-2] += str[str.size()-1];
    str.pop_back();
    paragraph.insert(paragraph.end(), str.begin(), str.end());

    for(string word : str){
        if(changeLineCounter + word.length() + 1 > changeLineFlag){
            changeLineCounter = 0;
            fileOut << '\n';
        }
        fileOut << word << " ";
        changeLineCounter += word.length()+1;
        fileOut.flush();
    }
    fileOut.flush();
    fileOut.close();
    return;
}

void RPG::wordMapFileOut(){
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

vector<string> pronouns = {
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", 
    "us", "them", "my", "your", "his", "its", "our", "their", "mine", 
    "yours", "ours", "theirs", "who", "whom", "whose", "which", "that"
};

vector<string> commonNouns = {
    "time", "way", "day", "man", "thing", "woman", "child", "world", "school", "state",
    "family", "student", "group", "country", "problem", "hand", "part", "place", "case",
    "week", "company", "system", "program", "question", "work", "government", "number",
    "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact",
    "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue",
    "side", "kind", "head", "house", "service", "friend", "father", "power", "hour",
    "game", "line", "end", "member", "law", "car", "city", "community", "name", "president",
    "team", "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others",
    "level", "office", "door", "health", "person", "art", "war", "history", "party", "result",
    "change", "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher",
    "force", "education", "foot", "boy", "age", "policy", "process", "music", "market", "sense",
    "nation", "plan", "college", "interest", "death", "experience", "effect", "use", "class",
    "control", "care", "field", "development", "role", "effort", "rate", "heart", "drug",
    "show", "leader", "light", "voice", "wife", "police", "mind", "price", "report", "decision",
    "son", "view", "relationship", "town", "road", "arm", "difference", "value", "building",
    "action", "model", "season", "society", "tax", "director", "position", "player", "record",
    "paper", "space", "ground", "form", "event", "official", "matter", "center", "couple",
    "site", "project", "activity", "star", "table"
};

bool RPG::isNounOrPronoun(string str){
    string lowerWord = tolower1(str);

    // Check in pronouns or common nouns
    for(string ele : pronouns){
        if(ele == lowerWord) return true;
    }
    for(string ele : commonNouns){
        if(ele == lowerWord) return true;
    }
    
    // Additional heuristic (e.g., if it starts with a capital letter, it might be a proper noun)
    if (std::isupper(str[0])) {
        return true;
    }

    return false;
}

void RPG::clearAndTitle(){
    ofstream fileOut(outputFileName.c_str());
    fileOut << "---GENERATED TEXT---\n";
    fileOut.flush();
    fileOut.close();
    return;
}

void RPG::paragraphToTerminal(){
    changeLineCounter = 0;
    for(string word : paragraph){
        if(changeLineCounter + word.length() + 1 > changeLineFlag){
            changeLineCounter = 0;
            cout << '\n';
        }
        cout << word << " ";
        changeLineCounter += word.length()+1;
        //sleep(2.0);
    }
    return;
}

void RPG::wordModify(string& str){
    int idxOfLastChar = str.length()-1;
    int idxOfFirstChar = 0;
    while(str[idxOfLastChar]==' ' || str[idxOfLastChar]=='\''){
        idxOfLastChar--;
    }
    while(str[idxOfFirstChar]==' ' || str[idxOfFirstChar]=='\''){
        idxOfFirstChar++;
    }
    try{
        str = str.substr(idxOfFirstChar, idxOfLastChar-idxOfFirstChar+1);
    }catch(out_of_range){} 
    return;
}

void RPG::printSettingList(int highlight, int expand, int expandHighlight){
    cout << "\033[2J\033[H\033[0m"; //clear terminal
    cout << "=======================================\n";
    cout << "               settings                \n";
    cout << "=======================================\n";
    for(int i=0; i<Title.size(); i++){
        cout << "\033[0m";
        if(i==highlight) cout << "\033[93m";
        cout << setw(2) << i+1 << ". " << Title[i] << ": \r\t\t\t" << Value[i] << "\033[0m\n";
        if(i==highlight && expand==1){
            for(int j=0; j<Choice[i].size(); j++){
                cout << "      ";
                if(j==expandHighlight) cout << "\r    >>";
                    cout << "(" << j+1 << "). " << Choice[i][j] << "\033[0m\n";
            }
        }
    }
    cout << "\033[0m" << flush;
    return;
}

bool RPG::checkValible(int idx, string userinput){
    bool success = 0;
    switch(idx){
    case 0:
        if(userinput != ""){
            ifstream test(userinput.c_str());
            if(test){
                inputFileName = userinput;
                Value[idx] = userinput;
                success = 1;
            }
            test.close();
        }
        break;
    case 1:
        if(userinput != ""){
            ofstream test(userinput.c_str());
            if(test){
                outputFileName = userinput;
                Value[idx] = outputFileName;
                success = 1;
            }
            test.close();
        }
        break;
    case 2:
        if(userinput != ""){
            int temp = -1;
            try{
                temp = stoi(userinput);
            }catch(invalid_argument){}
            if(temp > 0){
                targetLength = temp;
                Value[idx] = to_string(targetLength);
                success = 1;
            }
        }
        break;
    case 3:
        if(userinput != ""){
            int temp = -1;
            try{
                temp = stoi(userinput);
            }catch(invalid_argument){}
            if(temp>=1 && temp<=3){
                coherenceLevel  = temp;
                Value[idx] = to_string(coherenceLevel);
                success = 1;
            }
        }
        break;
    case 4:
        if(userinput != ""){
            int temp = -1;
            try{
                temp = stoi(userinput);
            }catch(invalid_argument){}
            if(temp > 0){
                changeLineFlag = temp;
                Value[idx] = to_string(changeLineFlag);
                success = 1;
            }
        }
        break;

    }
    return success;
}

void RPG::setting1(){
    getFiles(Choice[0]);
    cout << "\033[2J\033[H\033[0m";
    Choice[0].push_back("");
    setNonCanonicalMode();
    //enter to select
    //q to quit
    //up down to change file
    //right left to change dir
    string str = "";
    int label1Idx = 0;
    char control = ' ';
    string input;
    do{
        switch(control){
            case '0':
                //up
                if(label1Idx>0)
                    label1Idx--;
                break;

            case '1':
                //down
                if(label1Idx<Title.size()-1)
                    label1Idx++;
                break;

            case '2':
                //left
                setting2(label1Idx);
                break;

            case '\n':
                cout << " input >>\033[92m ";
                restoreCanonicalMode();
                getline(cin, input);
                cout << "\033[0m ";
                checkValible(label1Idx, input);
                setNonCanonicalMode();
                break;

            default:
                break;
        }
        //print setting menu
        printSettingList(label1Idx, 0, 0);
        control = getKBniput();
    }while(control!='s');
    cout << "\033[2J\033[H\033[0m---GENERATED TEXT---\n";
    restoreCanonicalMode();
    return;
}

void RPG::setting2(int& label1Idx){
    string str = "";
    int label2Idx = 0;
    char control = ' ';
    string input;
    do{
        switch(control){
            case '0':
                //up
                if(label2Idx>0){
                    label2Idx--;
                }else{
                    return;
                }
                break;

            case '1':
                //down
                if(label2Idx<Choice[label1Idx].size()-1){
                    label2Idx++;
                }else{
                    label1Idx++;
                    label1Idx %= Title.size();
                    return;
                }
                break;

            case '\n':
                if(Choice[label1Idx][label2Idx] != ""){
                    checkValible(label1Idx, Choice[label1Idx][label2Idx]);
                }else{
                    cout << " input >>\033[92m ";
                    restoreCanonicalMode();
                    getline(cin, input);
                    cout << "\033[0m ";
                    if(checkValible(label1Idx, input)){
                        Choice[label1Idx][label2Idx] = input;
                        Choice[label1Idx].push_back("");
                    }
                    setNonCanonicalMode();
                }
                break;

            default:
                break;
        }
        //print setting menu
        printSettingList(label1Idx, 1, label2Idx);
        control = getKBniput();
    }while(control!='3');
    return;
}