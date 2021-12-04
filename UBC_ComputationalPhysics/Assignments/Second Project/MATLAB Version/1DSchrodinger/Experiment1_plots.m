showAnimation = 0;
saveVideo = 0;
CalculationPlots = 1;



if showAnimation ==1
    
    
    figure()
    hold on;
    if saveVideo == 1
        avifilename = 'Potentiel Barrier.avi';
        aviobj = VideoWriter(avifilename);
        open(aviobj);
    end
    colormap cool;
    
    
    hold on;
    for tt = 1:4:size(t,2)
        clf;
        plot(x,psimod(tt,:));
        java.lang.Thread.sleep(0.5);
        title("Frame: ", tt)
        ylim([0,1]);
        xlabel("x")
        ylabel("|\psi|")
        drawnow;
        if saveVideo == 1
            writeVideo(aviobj, getframe(gcf));
        end
    end
    

    if saveVideo == 1
        close(aviobj);
    end

end


if CalculationPlots == 1
    hold on;
    plot(V_powerList,log(Fe_List), "LineWidth",3)
    xlabel("ln(V)");
    ylabel("ln(F_e)");
    title("ln(F_e) Vs. ln(V)");
    grid on;

end




% %plot(x(1:end-1), P_bar)
% 
% mat = P_bar - P_bar.';
% DX = x(1:end-1) - x(1:end-1)';
% 
% MAT = mat ./ (DX + 0.00001);
% %MAT = mean(MAT,1);
% %plot(x(1:end-1),MAT);
% imagesc(MAT(1:1:end,1:1:end));
% colorbar();
% 
