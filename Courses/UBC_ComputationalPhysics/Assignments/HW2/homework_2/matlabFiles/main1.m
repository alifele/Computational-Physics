t0 = 0;
dt = 0.01;
y0 = [0; 1];

yout = rk4step(@fcn_1, t0, dt, y0);

yout(1,:)
sin(dt)
yout - sin(dt)



% 
% y = zeros(2,100);
% for i=1:9000
%     y(:,i) = rk4step(@fcn_VanDerPol, t0, dt, y0);
%     t0 = t0 + dt;
%     y0 = y(:,i);
% end
% 
% 
% plot(y(1,:))