ScaledPlot = 1;

dpsi0 = exact - psi_0;
dpsi0_norm = mean(abs(dpsi0).^2,2).^0.5;

dpsi1 = exact - psi_1;
dpsi1_norm = mean(abs(dpsi1).^2,2).^0.5;

dpsi2 = exact - psi_2;
dpsi2_norm = mean(abs(dpsi2).^2,2).^0.5;

dpsi3 = exact - psi_3;
dpsi3_norm = mean(abs(dpsi3).^2,2).^0.5;

if ScaledPlot ~= 1

    hold on;
    plot(t_0,(dpsi0_norm.'),':', 'LineWidth',3);
    plot(t_0,(dpsi1_norm.'),'--', 'LineWidth',3);
    plot(t_0,1*(dpsi2_norm.'),'-.', 'LineWidth',3);
    plot(t_0,1*(dpsi3_norm.'), ':', 'LineWidth',3);
    
    legend(["||E(\psi^6)||","||E(\psi^7)||","||E(\psi^8)||","||E(\psi^9)||"])

end

if ScaledPlot == 1

    hold on;
    plot(t_0,(dpsi0_norm.'),':', 'LineWidth',3);
    plot(t_0,4*(dpsi1_norm.'),'--', 'LineWidth',3);
    plot(t_0,16*(dpsi2_norm.'),'-.', 'LineWidth',3);
    plot(t_0, 64*(dpsi3_norm.'), ':', 'LineWidth',3);
    
    legend(["||E(\psi^6)||","4||E(\psi^7)||","16||E(\psi^8)||","64||E(\psi^9)||"])

end