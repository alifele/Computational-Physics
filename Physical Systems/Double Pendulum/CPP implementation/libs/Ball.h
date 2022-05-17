//
// Created by aparanj on 2022-05-16.
//

#ifndef DOUBLEPENDULUM_BALL_H
#define DOUBLEPENDULUM_BALL_H

#include "SFML/Graphics.hpp"
#include "SFML/Window.hpp"


class Ball {
public:
    sf::RenderWindow *window;
    sf::CircleShape *ball;


    Ball(sf::RenderWindow *window);
    void setPos(sf::Vector2f pos);
    void draw();



};


#endif //DOUBLEPENDULUM_BALL_H
