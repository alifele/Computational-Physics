//
// Created by aparanj on 2021-10-22.
//

#include <iostream>
#include "Map.h"

Map::Map(double r, double seed, int iterate){
    this->r = r;
    this->seed = seed;
    this->x = seed;
    this->iterate = iterate;
}

void Map::run() {
    this->x = this->seed;
    for (int i = 0; i < this->iterate; ++i) {
        this->x = this->r * this->x * (1-this->x);
        if (i >= 50){
            this->lastValues[i-50] = this->x;
        }
    }

}
