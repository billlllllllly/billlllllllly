#include "rpg_v2.cpp"
#include "tools.cpp"
#include "textAnalysis.cpp"

using namespace std;

int main(){
    RPG rpg;
    rpg.begin();
    textAnalysis("alice.txt", "alice_analysis.txt");
    textAnalysis("final.txt", "final_analysis.txt");
    return 0;
}