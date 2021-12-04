idtype = 1;
vtype = 1;
idpar = [0.5,0.075,0];
vpar = [0.25,0.75,-2500];
tmax = 0.1;
lambda = 0.01;
level = 8;


[x, t, psi, psire, psiim, psimod, prob, v] = sch_1d_cn(tmax, level, lambda, ...
    idtype, idpar, vtype, vpar);




figure()
hold on;

% avifilename = 'schrodinger1D.avi';
% aviobj = VideoWriter(avifilename);
% open(aviobj);
colormap cool;
xlabel('x')
ylabel('|\psi|')

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
