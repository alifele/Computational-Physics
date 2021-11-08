function yout = rk4step(fcn, t0, dt, y0)
    F0 = fcn(t0,y0);
    F1 = fcn(t0+dt/2, y0+F0*dt/2);
    F2 = fcn(t0+dt/2, y0+F1*dt/2);
    F3 = fcn(t0+dt, y0+F2*dt);

    yout = y0 + dt/6 * (F0+2*F1+2*F2+F3);


end