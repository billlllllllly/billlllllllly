#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <windows.h>
using namespace std;

void showprogress(int progress){
    int P = progress/10;
    int target = progress%20;
    printf("  loading... [");
    for(int j=1; j<=P; j++){
        if(j == target){
            printf("\033[1;92m#\033[0m");
        }else{
            printf("\033[2;0m#\033[0m");
        }
    }
    for(int k=P+1; k<=20; k++){
        if(k == target){
            printf("\033[1;92m-\033[0m");
        }else{
            printf("\033[2;0m-\033[0m");
        }
    }
    printf("]\r");
}

void loadingbar(){
    int totalprogress = 200;
    for(int i=0; i<=totalprogress; i++){
        showprogress(i);
        Sleep(50);
    }
}

void showtxt(string target, int prespace=0, int countmax = 12){  
    for(int i=0; i<target.size(); i++){
        int count = 0;
        int toprint;
        while(true){
            printf("\r");
            for(int l=0; l<prespace; l++){
                printf(" ");
            }
            for(int j=0; j<i; j++){
                printf("%c", target[j]);
            }
            toprint = rand()%94 + 32;
            if(count >= countmax){
                printf("%c", target[i]);
                break;
            }
            printf("%c", toprint);
            Sleep(40);
            count++;
        }
    }

}

void showpic(){
    string pic[] = 
                 {"                                      --------------                                    ",                             
                  "                                 ----:::::::....:::::::---=                             ",                             
                  "                              --::::....            ....::::--                          ",                              
                  "                           --:::...                      ...:::--                       ",                              
                  "                         --::..                              ..:::-                     ",                              
                  "                       --:...                                  ...:--                   ",                              
                  "                     --:...                                      ...:--                 ",                              
                  "                    -::..                                          ..::-                ",                             
                  "                   -:...                  .--==-:.                  ...:-               ",                              
                  "                  -:...              -+***        ***+:              ...:-              ",                              
                  "                 -:...            -*+:               .=*+             ...:-             ",                              
                  "                -:...            =                       --            ...:-            ",                              
                  "               -::..                                                    ..:--           ",                              
                  "               -:..                                                      ..:-           ",                             
                  "               ::..                                                      ..::           ",                             
                  "              -:..                                                        ..:-          ",                            
                  "              -:..                                                        ..:-          ",                           
                  "              ::..                                                        ..::          ",                          
                  "              -:..                -##*:              :*##-                ..:-          ",                         
                  "              -::..              -*+=+*-            :*+=+*=              ...:-          ",                        
                  "              =::..              +====+=            =+====+              ..::=          ",                       
                  "               ::...             ===-===            -+=-==+             ...::           ",                      
                  "               -::..              *===*              *===*             ..::-           ",                     
                  "                -:..                                                   ...:-            ",                    
                  "                 ::..                                                  ..::             ",                   
                  "                  ::..                                                ..::              ",                  
                  "                   ::..                                              ..::               ",                 
                  "                    ::..                                            ..::                ",                
                  "                     -::..                                        ..::-                 ",               
                  "                       ::...                                    ...::                   ",              
                  "                         :::..                                ...::                     ",             
                  "                           -::...                          ...::-                       ",            
                  "                              :::....                  ....:::                          ",           
                  "                                 ::::::..............::::::                             ",          
                  "                                       :::::::::::::-                                   "};

    for(string s : pic){
        for(char c : s){
            printf("%c", c);
            
        }
        Sleep(50);
        printf("\n");
    }
}

void singnature(string name){
    for(int i=0; i<12; i++){
        Sleep(50);
        printf("\n");
    }
    showtxt(name, 2, 8);

}

int main(){
    cin.ignore();
    loadingbar();
    printf("\r                                                  \n\n");
    Sleep(2000);
    showtxt("Jun. 29, 2024", 70);
    printf("\n\n");
    Sleep(2000);
    printf("\r");
    showtxt("!!!HAPPY BIRTHDAY, SANDY CHEN!!!", 2);
    printf("\n\n\n");
    Sleep(2000);
    printf("\r");
    showpic();
    Sleep(2000);
    singnature("Billy Fan");
    cin.ignore();
    return 0;
}
