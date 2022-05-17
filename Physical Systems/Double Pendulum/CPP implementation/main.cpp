#include <iostream>
#include "SFML/Graphics.hpp"
#include "SFML/Window.hpp"

#include "libs/Sketch.h"


int main()
{

    Sketch sketch(new sf::RenderWindow(sf::VideoMode(1000,1000), "SFML window"));

    sketch.window->setFramerateLimit(120);

    while (sketch.window->isOpen())
    {
        sf::Event event{};
        while (sketch.window->pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                sketch.window->close();
        }

        sketch.draw();
    }

    return 0;

}