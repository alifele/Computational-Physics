//
// Created by aparanj on 2021-10-22.
//

#ifndef LOGISTICMAP_MAP_H
#define LOGISTICMAP_MAP_H


class Map {
public:
    int iterate;
    double lastValues[500] = {0};
    double r;
    double seed;
    double x;

    Map(double r, double seed, int iterate);
    void run();
};


#endif //LOGISTICMAP_MAP_H
