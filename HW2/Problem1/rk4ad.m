function [tout, yout] = rkadd(fcn, tspan, reltol1, y0)
    min_timeStep = 1.0e-4;

    nout = size(tspan,2);
    yout = zeros(size(y0,1), nout);
    yout(:,1) = y0;

    for i = 1:nout-1
        
        t0 = tspan(i);
        t_next = tspan(i+1);
        dt = t_next - t0;


        y_fine = rk4step(@fcn, t0, dt/2, y0);
        y_fine = rk4step(@fcn, t0+dt/2, dt/2, y_fine);
        y_coarse = rk4step(@fcn, t0, dt, y0);

        DeltaY = norm(y_fine(1) - y_coarse(1));
        E_trunc = DeltaY * 16/15;
        C = 0.9 * (reltol1*y0(1)/E_trunc)^(1/5);

        if C >= 1
            y0 = rk4step(@fcn, t0, dt, y0);
            yout(:,i+1) = y0;
        end

        if C < 1
            while C < 1
                if C*dt<min_timeStep
                    dt = min_timeStep;
                end
                dt = C * dt;
                y0 = rk4step(@fcn, t0, dt, y0);
                t0 = t0 + dt;
                dt = t_next - t0; 

                y_fine = rk4step(@fcn, t0, dt/2, y0);
                y_fine = rk4step(@fcn, t0+dt/2, dt/2, y_fine);
                y_coarse = rk4step(@fcn, t0, dt, y0);
        
                DeltaY = norm(y_fine(1) - y_coarse(1));
                E_trunc = DeltaY * 16/15;
                C = 0.9 * (reltol1*y0(1)/E_trunc)^(1/5);
                
            end

            y0 = rk4step(@fcn, t0, dt, y0);
            yout(:,i+1) = y0;
        end
    
    end

    tout = tspan;
end



% 
%     nout = size(tspan);
%     nout = nout(2);
% 
%     yout = zeros(size(y0,1),nout);
%     yout(:,1) = y0;
% 
%     for i = 1:nout-1
%         
%         t0 = tspan(i);
%         dt = tspan(i+1) - t0;
%         y0 = rk4step(@fcn, t0, dt, y0);
%         yout(:,i+1) = y0;
% 
%     end
% 
%     
