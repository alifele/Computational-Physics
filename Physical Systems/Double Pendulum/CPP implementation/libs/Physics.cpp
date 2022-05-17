//
// Created by aparanj on 2022-05-17.
//

#include "Physics.h"

Physics::Physics() {
    this->PsiList.col(0) = this->Psi;
    std::cout << sizeof(this->m1) << std::endl;
    this->h = this->tList(1) - this->tList(0);
    this->Calculate();
}

Eigen::Array4d Physics::F(double t, Eigen::Array4d Psi_) {
    Eigen::Array4d result = {0,0,0,0};
    double th1 = Psi_(0);
    double th1D = Psi_(1);
    double th2 = Psi_(2);
    double th2D = Psi_(3);
    double A1, B1, C1, D1 = 0;
    double A2, B2, C2, D2 = 0;

    A1 = this->l1 * (this->m1 + this->m2);
    B1 = this->m2 * this->l2 * std::cos(th2 - th1);
    C1 = this->m2 * this->l2 * th2D*th2D * std::sin(th2 - th1);
    D1 = (this->m1+this->m2)*this->g*std::sin(th1);

    A2 = this->l2;
    B2 = this->l1*std::cos(th2-th1);
    C2 = -this->l1*th1D*th1D*std::sin(th2-th1);
    D2 = this->g*std::sin(th2);


    double f0 = Psi_(1);
    double f1 = (A2*(C1-D1)-B1*(C2-D2))/(A1*A2 - B1*B2);
    double f2 = Psi_(3);
    double f3 = (B2*(C1-D1)-A1*(C2-D2))/(B1*B2 - A1*A2);

    result = {f0,f1,f2,f3};


    return result;
}

void Physics::Calculate() {

    for (int i=0; i< this->N_t-1; ++i){
        Eigen::Array4d f0,f1,f2,f3 = {0,0,0,0};
        double t = this->tList(i);
        Eigen::Array4d Psi_ = PsiList.col(i);

        f0 = this->F(t, Psi_);
        f1 = this->F(t+this->h/2, Psi_+f0*this->h/2);
        f2 = this->F(t+this->h/2, Psi_+f1*this->h/2);
        f3 = this->F(t+this->h, Psi_+f2*this->h);

        Psi_ += this->h/6 * (f0 + 2*f1 + 2*f2 + f3);
        this->PsiList.col(i+1) = Psi_;
    }

//    const static Eigen::IOFormat CSVFormat(Eigen::FullPrecision, Eigen::DontAlignCols, ", ", "\n");
//
//    std::ofstream file("data.csv");
//    if (file.is_open())
//    {
//        file << this->PsiList.format(CSVFormat);
//        file.close();
//    }

}
