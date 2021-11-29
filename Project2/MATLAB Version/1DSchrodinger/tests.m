figure()
hold on;
for tt = 1:size(t,2)
    clf;
    plot(x,psimod(tt,:));
    java.lang.Thread.sleep(20);
    title(tt)
    ylim([-1,1])
    drawnow;
end