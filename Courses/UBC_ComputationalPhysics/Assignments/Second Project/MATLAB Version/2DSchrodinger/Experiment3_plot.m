GenerateVidoe = 0;

figure()
hold on;

if GenerateVidoe == 1
    avifilename = '2D_PotentialBarrier.avi';
    aviobj = VideoWriter(avifilename);
    open(aviobj);
end

colormap cool;
for tt = 1:4:size(t,2)
    clf;
    contourf(psimod(:,:,tt),7);
    java.lang.Thread.sleep(1);
    caxis([0,1]);
    axis square;
    colorbar;
    title("Frame:", tt)
    drawnow;
    if GenerateVidoe == 1
        writeVideo(aviobj, getframe(gcf));
    end
    
end

if GenerateVidoe ==1 
    close(aviobj);
end
close;