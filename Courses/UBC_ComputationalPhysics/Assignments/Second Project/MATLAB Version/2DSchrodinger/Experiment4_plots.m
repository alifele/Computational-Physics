ShowdoubleSlit = 0;
GenerateVidoe = 1;
crossSection = 1;


if crossSection
    plot(x,psimod(:,240,150));
    
end

if ShowdoubleSlit ==1
    imagesc(v)
end

if ShowdoubleSlit==0 & crossSection == 0

    figure()
    hold on;
    
    if GenerateVidoe == 1
        avifilename = '2D_DoubleSlit.avi';
        aviobj = VideoWriter(avifilename);
        open(aviobj);
    end
    
    colormap cool;
    for tt = 1:1:size(t,2)
        clf;
        contourf(psimod(:,:,tt),7);
    %     hold on;
    %     contourf(v/vpar(end));
    %     hold off;
        
        caxis([0,1]);
        axis square;
        colorbar;
        
        title("Frame:", tt)
        
        if GenerateVidoe == 1
            writeVideo(aviobj, getframe(gcf));
        end
        drawnow;
        pause(0.1);
    end
    
    if GenerateVidoe ==1 
        close(aviobj);
    end
    close;

end