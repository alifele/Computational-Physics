//
// Created by aparanj on 2022-05-16.
//

#include "Ball.h"

Ball::Ball(sf::RenderWindow *window) {
    this->window = window;
    this->ball = new sf::CircleShape(20);
    this->ball->setFillColor(sf::Color(154,50,234));
    this->ball->setOutlineThickness(4);
    this->ball->setOrigin(20,20);
}

void Ball::setPos(sf::Vector2f pos) {
    this->ball->setPosition(pos);
}

void Ball::draw() {
    this->window->draw(*this->ball);
}
