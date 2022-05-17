//
// Created by aparanj on 2022-05-16.
//

#ifndef DOUBLEPENDULUM_SKETCH_H
#define DOUBLEPENDULUM_SKETCH_H

#include "SFML/Graphics.hpp"
#include "SFML/Window.hpp"
#include "iostream"
#include "Pivot.h"
#include "Line.h"
#include "Ball.h"
#include "Physics.h"

class Sketch {
public:
    sf::RenderWindow *window;
    sf::RectangleShape *border;
    sf::Vector2f shift = {0.0,0.0};
    Pivot *pivot = nullptr;
    Line *line1 = nullptr;
    Line *line2 = nullptr;
    Ball *ball1 = nullptr;
    Ball *ball2 = nullptr;
    Ball *tail1 = nullptr;
    Ball *tail2 = nullptr;
    Eigen::Matrix4Xd VisPsi;
    Eigen::Matrix4Xd Pos;
    sf::Vector2f pos = {100,500};
    sf::Vector2f pos2 = {400,800};
    int counter = 0;

    Physics *physics = nullptr;


    Sketch(sf::RenderWindow *window);
    void draw();
    void Transform();
};


#endif //DOUBLEPENDULUM_SKETCH_H
