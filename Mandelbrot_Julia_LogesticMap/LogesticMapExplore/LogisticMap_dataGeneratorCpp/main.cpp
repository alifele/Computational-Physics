#include <iostream>
#include "Map.h"
#include <fstream>


void creatRList(double* rList,int N, double step, double first);


int main() {
    double r = 3;
    double seed = 0.5;
    int iterate = 500;

    double first=3.4;
    double last = 3.7;
    double step = 0.0000005;
    int N = (int) ((last-first)/step);
    double rList[N]={};

    creatRList(rList,N, step, first);

    std::ofstream myfile;
    myfile.open("data.csv");


    for (int i = 0; i < N; ++i) {

        Map myMap(*(rList+i),seed,iterate);
        myMap.run();
        myfile<<*(rList+i)<<',';

        for (double lastValue : myMap.lastValues) {
            myfile<<lastValue<<',';
        }
        myfile<<'\n';
    }

    myfile.close();
    std::cout << "DONE!" << std::endl;






}


void creatRList(double* rList, int N, double step, double first){
    double x =first;
    for (int i = 0; i < N; ++i) {
        *(rList+i)=x;
        x += step;
    }
    std::cout <<"hello";
}
