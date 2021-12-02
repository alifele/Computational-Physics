
figure()
hold on;

% avifilename = 'schrodinger1D.avi';
% aviobj = VideoWriter(avifilename);
% open(aviobj);
colormap cool;

hold on;
for tt = 1:3:size(t,2)
    clf;
    plot(x,psimod(tt,:));
    java.lang.Thread.sleep(0.5);
    title(tt)
    ylim([0,1]);
%     writeVideo(aviobj, getframe(gcf));

    drawnow;
end

close(aviobj);
% 
% for tt = 1:size(x,2)-1
%     clf;
%     plot(t,psimod(:,tt));
%     java.lang.Thread.sleep(20);
%     title(tt)
%     ylim([0,1]);
% %     writeVideo(aviobj, getframe(gcf));
% 
%     drawnow;
% end
%close;