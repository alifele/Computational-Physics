% This program plots the heat map with X and Y corresponding to total
% amount of injected hot and cold molecules. The color values show the time
% integreated activity in tumor only

%-------------------------------

% To run the model:
% you need to open the project in simbiology model analyzer and then run
% the "HotColdAmount" program. Then import the last run results to matlab
% workspace as data1. Also you need to enter the number of steps for hot
% and cold amounts in the "hotAmountSteps" and  "coldAmountSteps"
% variables. Also you need to enter the number of steps of the different
% time amounts in the "timeIntervalSteps" variable.

%-------------------------------

% Interpretation and results
% Effect of injection time interval: with the same amout for the pare of 
% (hot, cold) but with different time intervals for injection,
% we can get higher TIA values. 
%--
% Nonlinearities and Competition: With higher amount of cold molecules,
% more activity needs to be injected in order to achieve the same amount of
% TIA

%-------------------------------

paramSweep = data1.samples.generate{:,:};

hotAmountSteps = 20;    
coldAmountSteps = 20;
timeIntervalSteps = 4;


hot = paramSweep(:,1);
cold = paramSweep(:,2);
interval = paramSweep(:,3);


Hot = reshape(hot, hotAmountSteps,hotAmountSteps,timeIntervalSteps);  % unit is nanomole
% Hot unit conversion to Activity = lambda*N
% A = Hot*1e-9(mol) * 6.022*1e23(#/mole) * lambda(1/min) * 1/60(min/sec) =
% Hot*0.72*1e9 (#/sec) = Hot*0.72 GBq
Hot = Hot * 72; % unit is GBq;
Cold = reshape(cold, coldAmountSteps,coldAmountSteps,timeIntervalSteps);


% Calculating total hot and total cold injected
Hot = Hot*5; %note that since we had 5 injections so we should *5
Cold = Cold*5; %note that since we had 5 injections so we should *5

Spec = Hot./(Cold+Hot);

Interval = reshape(interval, coldAmountSteps,coldAmountSteps,timeIntervalSteps); % we could
% also write: Interval = reshape(interval, hotAmountSteps,hotAmountSteps,4);


TINList = zeros(hotAmountSteps^2*timeIntervalSteps,1); % time integrated number of hot molecules
res = data1.results;

for i=1:length(res)
    TINList(i) = res(i).ScalarObservables{:,:};
end

TIN = reshape(TINList, coldAmountSteps,coldAmountSteps,timeIntervalSteps);
TIA = TIN * 7.23 * 1e-5;  % time integratede activity; A=N*lambda
% the unit of TIA is not #, it is nanomole. so it should be converted to #
% by multiplying at 6.023*10^23 * 10^(-9)
TIA = TIA * 6.023*1e23*1e-9;
TIA = TIA / 1e9; % the unit if TIA is now #bilion = GBq.sec





t = tiledlayout(2,2,'TileSpacing','Compact','Padding','Compact');
for i=1:timeIntervalSteps
    nexttile;
    contourf(Cold(:,:,i), Hot(:,:,i),TIA(:,:,i), 20);
    colormap("jet")
    caxis([1e5,9.5e5])
    %colorbar;
    title("time interval between injections: " + Interval(1,1,i) + " min", fontsize=14, FontWeight="normal");
    

end
cb = colorbar;
cb.Layout.Tile = 'east';
cb.Label.String = "TIA [GBq.second]";
cb.Label.FontSize = 10;
title(t, ["TIA in tumor: 5 equal injections"], fontsize=15)
xlabel(t, "total injected cold amount [nmol]", fontsize=15);
ylabel(t, "total injected activity [GBq]", fontsize=15);


