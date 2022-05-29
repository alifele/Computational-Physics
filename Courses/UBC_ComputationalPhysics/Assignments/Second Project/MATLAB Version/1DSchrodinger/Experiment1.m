VisualizationRun = 0;
CalculationRun = 1;

if VisualizationRun == 1
    
    idtype = 1;
    vtype = 1;
    idpar = [0.4,0.075,0];
    vpar = [0.6,0.8,5500];
    tmax = 0.1;
    lambda = 0.01;
    level = 8;
    
    
    [x, t, psi, psire, psiim, psimod, prob, v] = sch_1d_cn(tmax, level, lambda, ...
        idtype, idpar, vtype, vpar);
    
end

if CalculationRun == 1
    nv = 251;
    V_powerList = linspace(-2,5,nv);
    Fe_List = zeros(1,nv);
    idtype = 1;
    vtype = 1;
    idpar = [0.4,0.075,20];
    tmax = 0.1;
    lambda = 0.01;
    level = 9;
    
    i = 1;
    for V = V_powerList
        vpar = [0.6,0.8,exp(V)];
        [x, t, psi, psire, psiim, psimod, prob, v] = sch_1d_cn(tmax, level, lambda, ...
        idtype, idpar, vtype, vpar);
        P_bar = mean(prob, 1);
        P_bar = P_bar / P_bar(end);
        [tra,x1] = min(x<0.8);
        Fe_List(1,i) = (P_bar(end) - P_bar(x1))/(0.2);
        
        i = i+1
    end

end
    


