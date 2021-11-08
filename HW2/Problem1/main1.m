t0 = 0;
dt = 0.01;
y0 = [1; -2];

y = zeros(2,100);
for i=1:9000
    y(:,i) = rk4step(@fcn, t0, dt, y0);
    t0 = t0 + dt;
    y0 = y(:,i);
end


plot(y(1,:),y(2,:))