//
// Created by aparanj on 2022-05-16.
//

#include "Pivot.h"

Pivot::Pivot(sf::RenderWindow *window, sf::Vector2f shift) : pivot(14) {
    this->window = window;
    this->pos = shift;
    this->pivot.setFillColor(sf::Color::Black);
    this->pivot.setOrigin(14,14);
    this->pivot.setPosition(this->pos);

}

void Pivot::draw() {
    this->window->draw(pivot);
}

