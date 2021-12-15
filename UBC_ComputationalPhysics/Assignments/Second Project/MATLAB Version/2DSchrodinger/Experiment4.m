b = 7/100;
d = 3/100;
s = 0.5 -b/2 -d;


idtype = 1;
vtype = 2;
idpar = [0.1,0.5,0.07,0.07,40,0];
vpar = [s,s+d,s+d+b,s+2*d+b,100];
tmax = 0.01;
lambda = 0.01;
level = 8;


[x, y, t, psi, psire, psiim, psimod, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);






