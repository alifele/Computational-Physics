idtype = 1;
vtype = 0;
idpar = [0.5,0.075,0.0];
vpar = [4];
tmax = 0.25;
lambda = 0.1;
level = 9;


[x, t, psi, psire, psiim, psimod, prob, v] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);




