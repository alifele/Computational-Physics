## Chain of Particles connected with Spring

In this code I have solved the differential equations of a system of 1D particles connected to each other with springs. You can find the theory and derivation in the Theory folder. 

I have used RK-45 to solve the ODEs. You can also see the algorithm in the Theory folder. 

In the Physics.py file, by chaning the value of "TheEndsConnectedToWall" variable, you can set that the two ending particles are free or connected to walls with springs.

Also in the sketch.py file, you can change the values of following variables:
```python
self.L0
self.L
```

So that you can achieve the desired output. Note that L0 is the distance from the left most well to the first partcle and L is the length of spring.

Note by commenting/uncommening codes on the Box.draw( ) method you can visualise the particles and their velocities. By visualizing the speeds only, some very beautiful patterns emerge.

In the following images you can find some of the outputs:

20 Particles visualized with their velocities:
![enter image description here](https://github.com/alifele/Computational-Physics/blob/main/Physical%20Systems/Spring%20Chain/Images/20ParticlesMoving.png?raw=true)

![enter image description here](https://github.com/alifele/Computational-Physics/blob/main/Physical%20Systems/Spring%20Chain/Images/20%20Particles.png?raw=true)

100 Particles with Velocities:
![enter image description here](https://github.com/alifele/Computational-Physics/blob/main/Physical%20Systems/Spring%20Chain/Images/100ParticlesWithSquares.png?raw=true)

100 Particles without the particles (velocities only):
![enter image description here](https://github.com/alifele/Computational-Physics/blob/main/Physical%20Systems/Spring%20Chain/Images/100Particles.png?raw=true)



