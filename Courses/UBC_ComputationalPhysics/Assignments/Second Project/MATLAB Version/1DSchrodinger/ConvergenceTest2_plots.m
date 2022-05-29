ScaledPlot = 1;


dpsi1 = psi_1 - psi_0;
dpsi1_norm = mean(abs(dpsi1).^2,2).^0.5;

dpsi2 = psi_2 - psi_1;
dpsi2_norm = mean(abs(dpsi2).^2,2).^0.5;

dpsi3 = psi_3 - psi_2;
dpsi3_norm = mean(abs(dpsi3).^2,2).^0.5;

xlabel("t^n");
ylabel("||d\psi^l||")

if ScaledPlot ~= 1

    hold on;
    plot(t_0,(dpsi1_norm.'),'--', 'LineWidth',3);
    plot(t_0,1*(dpsi2_norm.'),'-.', 'LineWidth',3);
    plot(t_0,1*(dpsi3_norm.'), ':', 'LineWidth',3);
    
    legend(["||d\psi^6||","||d\psi^7||","||d\psi^8||"])

end

if ScaledPlot == 1

    hold on;
    plot(t_0,(dpsi1_norm.'),'--', 'LineWidth',3);
    plot(t_0,4*(dpsi2_norm.'),'-.', 'LineWidth',3);
    plot(t_0,16*(dpsi3_norm.'), ':', 'LineWidth',3);
    
    legend(["||d\psi^6||","4||d\psi^7||","16||d\psi^8||"])

end
