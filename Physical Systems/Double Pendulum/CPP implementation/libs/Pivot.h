//
// Created by aparanj on 2022-05-16.
//

#ifndef DOUBLEPENDULUM_PIVOT_H
#define DOUBLEPENDULUM_PIVOT_H

#include "SFML/Graphics.hpp"
#include "SFML/Window.hpp"
//#include "Sketch.h"


class Pivot {
public:
    sf::RenderWindow *window;
    sf::CircleShape pivot;

    sf::Vector2f pos = {0,0};


    Pivot(sf::RenderWindow *window, sf::Vector2f shift);
    void draw();

};


#endif //DOUBLEPENDULUM_PIVOT_H
