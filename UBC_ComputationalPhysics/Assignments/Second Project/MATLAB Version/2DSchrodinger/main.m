idtype = 1;
vtype = 0;
idpar = [0.5,0.5,0.07,0.07,0,0];
vpar = [4];
tmax = 0.1;
lambda = 0.01;
level = 7;


[x, y, t, psi, psire, psiim, psimod, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);



