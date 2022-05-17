//
// Created by aparanj on 2022-05-17.
//

#ifndef DOUBLEPENDULUM_PHYSICS_H
#define DOUBLEPENDULUM_PHYSICS_H

#include "cmath"
#include "Eigen/Dense"
#include "iostream"
#include "fstream"


class Physics {
public:

    double m1 = 1.0;
    double m2 = 1.0;
    double l1 = 1.0;
    double l2 = 0.9;
    double g = 10.0;


    int level = 14;
    int N_t = std::pow(2,level);
    double h;
    Eigen::ArrayXd tList = Eigen::ArrayXd::LinSpaced(N_t, 0, 100);
    Eigen::Matrix4Xd PsiList = Eigen::Matrix4Xd::Zero(4, N_t);
    Eigen::Array4d Psi = {3.14/2,1,-3.14/3,-1};

//
    Physics();
    Eigen::Array4d F(double t, Eigen::Array4d Psi);
    void Calculate();

};


#endif //DOUBLEPENDULUM_PHYSICS_H
