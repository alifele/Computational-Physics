ScaledPlot = 1;

[X,Y,T] = meshgrid(x0,y0,t0);
psi_exact = Exact_2d_sch(idpar(1),idpar(2),X,Y,T);



dpsi6 = psi_exact - psi_6 ;
dpsi6_norm = reshape(mean(mean(abs(dpsi6).^2,1),2).^0.5,1,[]);

dpsi7 = psi_exact - psi_7;
dpsi7_norm = reshape(mean(mean(abs(dpsi7).^2,1),2).^0.5,1,[]);

dpsi8 = psi_exact - psi_8;
dpsi8_norm = reshape(mean(mean(abs(dpsi8).^2,1),2).^0.5,1,[]);
% 
dpsi9 = psi_exact - psi_9;
dpsi9_norm = reshape(mean(mean(abs(dpsi9).^2,1),2).^0.5,1,[]);


xlabel("t")
ylabel("||E(\psi^l)||")
grid on;

if ScaledPlot == 0

    hold on;
    plot(t0,(dpsi6_norm.'),'--', 'LineWidth',3);
    plot(t0,1*(dpsi7_norm.'),'-.', 'LineWidth',3);
    plot(t0,1*(dpsi8_norm.'), ':', 'LineWidth',3);
    plot(t0,1*(dpsi9_norm.'), '--', 'LineWidth',3);
    legend(["||E(\psi^6)||","||E(\psi^7)||","||E(\psi^8)||","||E(\psi^9)||"])

end

if ScaledPlot == 1

    hold on;
    plot(t0,(dpsi6_norm.'),'--', 'LineWidth',3);
    plot(t0,4*(dpsi7_norm.'),'-.', 'LineWidth',3);
    plot(t0,16*(dpsi8_norm.'), ':', 'LineWidth',3);
    plot(t0,64*(dpsi9_norm.'), '--', 'LineWidth',3);
    legend(["||E(\psi^6)||","4||E(\psi^7)||","16||E(\psi^8)||","64||E(\psi^9)||"])


end
