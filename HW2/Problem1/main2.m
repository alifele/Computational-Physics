t0 = 0;
dt = 0.01;
tend = 15;
y0 = [1; -2];

tspan = [t0:dt:tend];
[tout, yout] = rk4(@fcn, tspan, y0);

%plot(yout(1,:), yout(2, :))
plot(tspan, yout(2, :))