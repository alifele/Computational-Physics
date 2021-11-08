harmonic = 0;
VanderPol = 1;

% For simple harmonic motion
if harmonic
    y0 = [1; 0];
    reltolList = [1.0e-5,1.0e-7,1.0e-9,1.0e-11];
    %reltolList = [1.0e-11];
    reltolListNames = ["1.0e-5","1.0e-7","1.0e-9","1.0e-11"];
    tspan = linspace(0.0, 3.0 * pi, 65);
    
    for i = 1:4
        reltol = reltolList(i);
        [tout, yout] = rk4ad(@fcn_harmonic, tspan, reltol, y0);
        figure;
        hold on;
        plot(tspan, (yout(1,:)-cos(tspan)))
        title("reltol = "+reltolListNames(i));
        xlabel('time');
        ylabel('Sin(t) - x(t)')
        %plot(tspan, cos(tspan))
        
    end

end

% For Van der Pol
if VanderPol
    reltol = 1.0e-10;
    y0 = [1; -6];
    tspan = linspace(0.0, 100, 4097);
    [tout, yout] = rk4ad(@fcn_VanDerPol, tspan, reltol, y0);
    
    figure;
    plot(tspan, yout(1, :))
    xlabel('time');
    ylabel('x');
    title("x vs. t (reltol=1.0e-10)")

    figure;
    plot(yout(1,:), yout(2, :))
    xlabel("x");
    ylabel('velocity');
    title("Phase space (reltol=1.0e-10)")
end