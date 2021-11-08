function [tout, yout] = rk4(fcn, tspan, y0)
    nout = size(tspan);
    nout = nout(2);

    yout = zeros(size(y0,1),nout);
    yout(:,1) = y0;

    for i = 1:nout-1
        
        t0 = tspan(i);
        dt = tspan(i+1) - t0;
        y0 = rk4step(@fcn, t0, dt, y0);
        yout(:,i+1) = y0;

    end

    tout = tspan;


end