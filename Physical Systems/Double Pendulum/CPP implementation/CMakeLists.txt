cmake_minimum_required(VERSION 3.20)
project(DoublePendulum)

set(CMAKE_CXX_STANDARD 14)

add_executable(DoublePendulum main.cpp libs/Sketch.cpp libs/Sketch.h libs/Pivot.cpp libs/Pivot.h libs/Line.cpp libs/Line.h libs/Ball.cpp libs/Ball.h libs/Physics.cpp libs/Physics.h)


find_package (SFML REQUIRED system window graphics network audio)
target_link_libraries(DoublePendulum sfml-audio sfml-graphics sfml-network sfml-system)

find_package (Eigen3 REQUIRED NO_MODULE)
target_link_libraries (DoublePendulum Eigen3::Eigen)