t = results.Time;
data = results.Data;

% % t_min = t(1);
% % t_max = t(end);
% % 
% % t_new = linspace(t_min,t_max,3000);
% % 
% % 
% % data_new = interp1(t,data,t_new, "cubic");
% % 
% % plot(t_new(1:500), data_new(1:500,1:20),LineWidth=2)hold on
% % plot(t(1:end), data(1:end,1:20),LineWidth=2,Marker="o", LineStyle="none")

intg = integral_array(data, t)

