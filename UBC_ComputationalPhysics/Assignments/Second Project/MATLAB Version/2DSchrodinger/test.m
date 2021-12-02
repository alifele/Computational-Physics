figure()
hold on;

avifilename = 'GalaxyCollisionCenterofMass.avi';
aviobj = VideoWriter(avifilename);
open(aviobj);
colormap cool;


for tt = 1:size(t,2)
    clf;
    contourf(psimod(:,:,tt),7);
    java.lang.Thread.sleep(5);
    caxis([0,1]);
    colorbar;
    title(tt)
    %drawnow;
    writeVideo(aviobj, getframe(gcf));

end

close(aviobj);
close;