//
// Created by aparanj on 2022-05-16.
//

#include "Line.h"

Line::Line(sf::RenderWindow *window) {
    this->window = window;
    this->line = new sf::RectangleShape(sf::Vector2f(1, this->width)); // I will replace the 1 with actual value later;
    this->line->setFillColor(sf::Color(47,47,85));
    this->line->setOrigin(0, this->line->getSize().y/2);
//    this->line->setPosition(this->pivotPosition);
}

void Line::draw() {
    this->window->draw(*(this->line));
}

void Line::setValues(sf::Vector2f objectPos, sf::Vector2f pivot) {
    this->pivotPosition.x = pivot.x; this->pivotPosition.y = pivot.y;
    this->line->setPosition(this->pivotPosition);

    sf::Vector2f D =  objectPos - this->pivotPosition;
    this->line->setSize(sf::Vector2f(std::sqrt(D.x*D.x+D.y*D.y), this->width));
    if (D.y >= 0){
        float theta = std::atan(D.x/D.y);
        this->line->setRotation(90-theta/3.14 * 180 );
    }else{
        float theta = std::atan(D.x/D.y);
        this->line->setRotation(-(90+theta/3.14 * 180));

    }

//    this->line->setRotation(-5);
}

