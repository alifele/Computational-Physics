idtype = 1;
vtype = 1;
idpar = [0.5,0.075,0];
vpar = [0.25,0.75,-2500];
tmax = 0.01;
lambda = 0.01;
level = 9;


[x_7, t_7, psi_7, psire_7, psiim_7, psimod_7, prob_7, v_7] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);


level = level+1;

[x_8, t_8, psi_8, psire_8, psiim_8, psimod_8, prob_8, v_8] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

psi_7 = psi_7(1:end-1,1:end-1);


dpsi = psi_8(1:2:end-1,1:2:end-1) - psi_7;
dpsi_norm = sum(abs(dpsi).^2,2).^0.5;

% imagesc(abs(dpsi));
% colorbar();

plot(t_7(1,1:end-1),(dpsi_norm.'))


