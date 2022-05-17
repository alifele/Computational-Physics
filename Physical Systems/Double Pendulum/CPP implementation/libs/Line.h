//
// Created by aparanj on 2022-05-16.
//

#ifndef DOUBLEPENDULUM_LINE_H
#define DOUBLEPENDULUM_LINE_H

#include "SFML/Graphics.hpp"
#include "SFML/Window.hpp"
#include <cmath>



class Line {
public:
    sf::RenderWindow *window = nullptr;
    sf::RectangleShape *line = nullptr;

    int width = 10;
    sf::Vector2f pivotPosition = {0,0};
    sf::Vector2f objectPosition = {0,0};

    Line(sf::RenderWindow *window);
    void draw();
    void setValues(sf::Vector2f objectPos, sf::Vector2f pivot);

};


#endif //DOUBLEPENDULUM_LINE_H
