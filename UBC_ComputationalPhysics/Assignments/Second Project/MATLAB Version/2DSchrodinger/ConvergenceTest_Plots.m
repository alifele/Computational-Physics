ScaledPlot = 1;


dpsi6 = psi_7 - psi_6;
dpsi6_norm = reshape(mean(mean(abs(dpsi6).^2,1),2).^0.5,1,[]);

dpsi7 = psi_8 - psi_7;
dpsi7_norm = reshape(mean(mean(abs(dpsi7).^2,1),2).^0.5,1,[]);

dpsi8 = psi_9 - psi_8;
dpsi8_norm = reshape(mean(mean(abs(dpsi8).^2,1),2).^0.5,1,[]);

xlabel("t")
ylabel("||d\psi^l||")
grid on;

if ScaledPlot == 0

    hold on;
    plot(t0,(dpsi6_norm.'),'--', 'LineWidth',3);
    plot(t0,1*(dpsi7_norm.'),'-.', 'LineWidth',3);
    plot(t0,1*(dpsi8_norm.'), ':', 'LineWidth',3);
    legend(["||d\psi^6||","||d\psi^7||","||d\psi^8||"])

end

if ScaledPlot == 1

    hold on;
    plot(t0,(dpsi6_norm.'),'--', 'LineWidth',3);
    plot(t0,4*(dpsi7_norm.'),'-.', 'LineWidth',3);
    plot(t0,16*(dpsi8_norm.'), ':', 'LineWidth',3);
    legend(["||d\psi^6||","4||d\psi^7||","16||d\psi^8||"])


end
