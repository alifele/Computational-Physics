idtype = 1;
vtype = 1;
idpar = [0.5,0.5,0.07,0.07,0,0];
vpar = [0.35,0.65,0.35,0.65,50];
tmax = 0.02;
lambda = 0.001;
level = 7;


[x, y, t, psi, psire, psiim, psimod, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);



