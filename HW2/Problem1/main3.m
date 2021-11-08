t0 = 0;
dt = 0.01;
tend = 15;
y0 = [1; -2];
reltol = 1.0e-5;

tspan = [t0:dt:tend];
[tout, yout] = rk4ad(@fcn, tspan, reltol, y0);

%plot(yout(1,:), yout(2, :))
plot(tspan, yout(2, :))