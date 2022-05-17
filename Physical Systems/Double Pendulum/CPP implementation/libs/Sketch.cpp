//
// Created by aparanj on 2022-05-16.
//

#include "Sketch.h"


Sketch::Sketch(sf::RenderWindow *window) {

    this->physics = new Physics();
    this->VisPsi = Eigen::MatrixXd::Zero(4, this->physics->N_t);
    this->Pos = Eigen::MatrixXd::Zero(4, this->physics->N_t);

    this->window = window;
    this->shift.x = window->getSize().x;
    this->shift.y = window->getSize().y;
    this->shift.x /= 2;
    this->shift.y /= 15;
    this->border = new sf::RectangleShape(sf::Vector2f(this->window->getSize().x-10, this->window->getSize().y-10));
    this->border->setFillColor(sf::Color::Transparent);
    this->border->setPosition(5,5);
    this->border->setOutlineThickness(10);

    this->pivot = new Pivot(this->window, this->shift);
    this->line1 = new Line(this->window);
    this->line2 = new Line(this->window);
    this->ball1 = new Ball(this->window);
    this->ball2 = new Ball(this->window);

    this->tail1 = new Ball(this->window);
    this->tail1->ball->setRadius(4);
    this->tail1->ball->setOrigin(4,4);
    this->tail1->ball->setFillColor(sf::Color(174,255,173));
    this->tail1->ball->setOutlineThickness(0);


    this->tail2 = new Ball(this->window);
    this->tail2->ball->setRadius(4);
    this->tail2->ball->setOrigin(4,4);
    this->tail2->ball->setFillColor(sf::Color(250,255,90));
    this->tail2->ball->setOutlineThickness(0);

    this->Transform();


}


void Sketch::draw() {
    this->pos.x = this->Pos.col(counter%physics->N_t)(0);
    this->pos.y = this->Pos.col(counter%physics->N_t)(1);
    this->pos2.x = this->Pos.col(counter%physics->N_t)(2);
    this->pos2.y = this->Pos.col(counter%physics->N_t)(3);

    this->window->clear(sf::Color(144,144,144));
    this->window->draw(*this->border);

    if (counter<= 200){
        for (int j=0; j<counter; ++j){
            this->pos.x = this->Pos.col(j)(0);
            this->pos.y = this->Pos.col(j)(1);
            this->tail1->setPos(this->pos);
            this->tail1->draw();
        }

        for (int j=0; j<counter; ++j){
            this->pos2.x = this->Pos.col(j)(2);
            this->pos2.y = this->Pos.col(j)(3);
            this->tail2->setPos(this->pos2);
            this->tail2->draw();
        }
    }else{
        for (int j=counter-200; j<counter; ++j){
            this->pos.x = this->Pos.col(j)(0);
            this->pos.y = this->Pos.col(j)(1);
            this->tail1->setPos(this->pos);
            this->tail1->draw();
        }

        for (int j=counter-200; j<counter; ++j){
            this->pos2.x = this->Pos.col(j)(2);
            this->pos2.y = this->Pos.col(j)(3);
            this->tail2->setPos(this->pos2);
            this->tail2->draw();
        }
    }



    this->line1->setValues(this->pos, this->shift);
    this->line1->draw();
    this->line2->setValues(this->pos2, this->pos);
    this->line2->draw();
    this->ball1->setPos(this->pos);
    this->ball1->draw();
    this->ball2->setPos(this->pos2);
    this->ball2->draw();
    this->pivot->draw();

    this->counter += 1;

//    std::cout << (this->window->getSize()) << std::endl;

    this->window->display();
}

void Sketch::Transform() {
    float scale = 200;
    Eigen::Array2d shift = {this->shift.x, this->shift.y};
    this->VisPsi = this->physics->PsiList;
    Eigen::ArrayXd th1 = this->physics->PsiList.array().row(0);
    Eigen::ArrayXd th2 = this->physics->PsiList.array().row(2);
//    this->VisPsi.row(0) = scale * this->physics->PsiList.row(0);
//    this->VisPsi.row(1) = -scale * this->physics->PsiList.row(0);
//    this->VisPsi.row(0) = this->VisPsi.row(0).array() + shift(0);
//    this->VisPsi.row(1) = this->VisPsi.row(1).array() + shift(1);
    this->Pos.row(0) = this->physics->l1*th1.sin();
    this->Pos.row(1) = -this->physics->l1*th1.cos();
    this->Pos.row(2) = this->physics->l1*th1.sin() + this->physics->l2*th2.sin();
    this->Pos.row(3) = -this->physics->l1*th1.cos() - this->physics->l2*th2.cos();

    this->Pos *= scale;
    this->Pos.row(1) *= -1;
    this->Pos.row(3) *= -1;

    this->Pos.row(0) = this->Pos.array().row(0) + shift(0);
    this->Pos.row(1) = this->Pos.array().row(1) + shift(1);
    this->Pos.row(2) = this->Pos.array().row(2) + shift(0);
    this->Pos.row(3) = this->Pos.array().row(3) + shift(1);
}