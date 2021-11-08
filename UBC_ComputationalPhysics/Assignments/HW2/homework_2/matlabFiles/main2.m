xPlot = 0;
phasePlot = 0;
errorPlots = 0;
vanDerPolPlots = 1;


% This configuration is used to generate the x-t and phase plots
if xPlot | phasePlot
    t0 = 0;
    dt = 0.01;
    tend = 3*pi;
    y0 = [0; 1];
    tspan = [t0:dt:tend];
    [tout, yout] = rk4(@fcn_harmonic, tspan, y0);
end


% This section calculates the errors
if errorPlots
    l6 = 6;
    l7 = 7;
    l8 = 8;
    y0 = [0; 1];
    
    N_timeSteps6 = 2^l6+1;   
    tspan6 = linspace(0,3*pi, N_timeSteps6);
    [tout, yout6] = rk4(@fcn_harmonic, tspan6, y0);
    
    N_timeSteps7 = 2^l7+1;   
    tspan7 = linspace(0,3*pi, N_timeSteps7);
    [tout, yout7] = rk4(@fcn_harmonic, tspan7, y0);
    
    N_timeSteps8 = 2^l8+1;   
    tspan8 = linspace(0,3*pi, N_timeSteps8);
    [tout, yout8] = rk4(@fcn_harmonic, tspan8, y0);
    
    Err67 = yout6(1,:) - yout7(1,1:2:end);
    Err78 = yout7(1,1:2:end) - yout8(1,1:4:end);
end


% Van der Pol
if vanDerPolPlots
    l = 12;
    y0 = [1;-6];
    N_timeSteps = 2^l+1;   
    tspan = linspace(0,100, N_timeSteps);
    [tout, yout] = rk4(@fcn_VanDerPol, tspan, y0);
    
end

if vanDerPolPlots
    figure;
    plot(tspan, yout(1, :))
    xlabel('time');
    ylabel('x');
    title("x vs. t")
    
    figure;
    plot(yout(1,:), yout(2, :))
    xlabel("x");
    ylabel('velocity');
    title("Phase space")

end

if errorPlots
    figure;
    hold on;
    plot(tspan6, Err67);
    plot(tspan6, 16*Err78);
    legend("x(level6) - x(level7)","16*(x(level7) - x(level8))")
    title('Error Analysis')
    xlabel('time');
    ylabel('Error')
end


if xPlot
    figure;
    plot(tspan, yout(1, :))
    xlabel('time');
    ylabel('x');
    title("x vs. t")
end

if phasePlot
    figure;
    plot(yout(1,:), yout(2, :))
    xlabel("x");
    ylabel('velocity');
    title("Phase space")

end


