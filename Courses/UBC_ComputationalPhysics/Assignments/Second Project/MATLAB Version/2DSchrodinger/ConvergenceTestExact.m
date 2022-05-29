clear all;
idtype = 0;
vtype = 0;
idpar = [2,3];
vpar = [4];
tmax = 0.05;
lambda = 0.05;
level = 6;


[x_6, y_6, t_6, psi_6, psire_6, psiim_6, psimod_6, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_7, y_7, t_7, psi_7, psire_7, psiim_7, psimod_7, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_8, y_8, t_8, psi_8, psire_8, psiim_8, psimod_8, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_9, y_9, t_9, psi_9, psire_9, psiim_9, psimod_9, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

% 
t0 = t_6(1:end-1);
x0 = x_6(1:end-1);
y0 = y_6(1:end-1);


% 
% 
psi_6 = psi_6(1:end-1,1:end-1,1:end-1);
psi_7 = psi_7(1:2:end-1,1:2:end-1,1:2:end-1);
psi_8 = psi_8(1:4:end-1,1:4:end-1,1:4:end-1);
psi_9 = psi_9(1:8:end-1,1:8:end-1,1:8:end-1);