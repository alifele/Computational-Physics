idtype = 0;
vtype = 0;
%idpar = [0.5,0.075,0];
idpar = [3];
vpar = [0.25,0.75,-2500];
tmax = 0.25;
lambda = 0.1;
level = 6;

[x_0, t_0, psi_0, psire_0, psiim_0, psimod_0, prob_0, v_0] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_1, t_1, psi_1, psire_1, psiim_1, psimod_1, prob_1, v_1] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_2, t_2, psi_2, psire_2, psiim_2, psimod_2, prob_2, v_2] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);

level = level+1;
[x_3, t_3, psi_3, psire_3, psiim_3, psimod_3, prob_3, v_3] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);


t_0 = t_0(1:end-1);
x_0 = x_0(1:end-1);

[X,T] = meshgrid(x_0, t_0);
exact = exact_1d_sch(idpar(1),X,T);
psi_0 = psi_0(1:end-1,1:end-1);
psi_1 = psi_1(1:2:end-1,1:2:end-1);
psi_2 = psi_2(1:4:end-1,1:4:end-1);
psi_3 = psi_3(1:8:end-1,1:8:end-1);


% imagesc(abs(dpsi));
% colorbar();



