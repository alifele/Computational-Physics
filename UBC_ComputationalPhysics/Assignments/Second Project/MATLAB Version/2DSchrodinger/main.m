idtype = 1;
vtype = 0;
idpar = [0.5,0.5,0.07,0.07,0,0];
vpar = [4];
tmax = 0.1;
lambda = 0.01;
level = 7;


[x, y, t, psi, psire, psiim, psimod, v] = sch_2d_adi(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);



figure()
hold on;

% avifilename = 'GalaxyCollisionCenterofMass.avi';
% aviobj = VideoWriter(avifilename);
% open(aviobj);
colormap cool;


for tt = 1:size(t,2)
    clf;
    contourf(psimod(:,:,tt),7);
    java.lang.Thread.sleep(1);
    caxis([0,1]);
    colorbar;
    title(tt)
    drawnow;
%     writeVideo(aviobj, getframe(gcf));

end

% close(aviobj);
close;