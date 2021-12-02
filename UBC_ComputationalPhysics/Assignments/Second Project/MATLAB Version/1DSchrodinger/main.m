idtype = 1;
vtype = 1;
idpar = [0.5,0.075,0];
vpar = [0.25,0.75,-2500];
tmax = 0.01;
lambda = 0.01;
level = 9;


[x, t, psi, psire, psiim, psimod, prob, v] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);




