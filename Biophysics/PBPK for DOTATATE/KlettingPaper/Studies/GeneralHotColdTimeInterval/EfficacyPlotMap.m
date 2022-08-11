close all
xx = 0.2:0.01:1.8;
yy = 0.2:0.01:1.8;


[XX,YY] = meshgrid(xx,yy);

a = YY-XX;
b = YY+XX;


bmax = max(b(:));
amax = max(a(:));

% val = a + 50*a./real(((bmax/2).^2-(b-bmax/2).^2).^1.2);.


% val = a + 50*a./abs((9-(b-3).^2).^1.1);


% val = a + 0.2*a./exp((-(b-2).^2)/0.45);

val1 = 1*a./exp((-(b-2).^2)/2);

val2 = 1*(b-2)./exp((-(a).^2)/2) ;

val_1 = val1*1./(val2.^2+0.5);
val_1 = val_1./abs(min(val_1(:)));



val_2 = val2*1./(val1.^2+0.5);
val_2 = val_2./abs(min(val_2(:)));



% 
% contourf(XX,YY,val1,20)
% colormap("jet")
% colorbar()
% % caxis([-1,1])
% 
% figure()
% 
% contourf(XX,YY,1./(val2.^2+1),20)
% colormap("jet")
% colorbar()
% % caxis([-1,1])
% 
% figure()

contourf(XX,YY,val_1,20)
colormap("jet")
cb = colorbar();
caxis([-1,1])

xlabel("NTIA for OAR")
ylabel("NTIA for tumor")
cb.Label.String = "Efficacy"
cb.Label.FontSize= 13;




xline(1)
yline(1)