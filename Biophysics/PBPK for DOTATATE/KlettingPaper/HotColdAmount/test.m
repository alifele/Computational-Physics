samples1 = SimBiology.Scenarios();
add(samples1, 'cartesian', 'dose_hot Amount', linspace(10,400,10));
add(samples1, 'cartesian', 'dose_cold Amount', linspace(0,100,10));

% Configure RandomSeed to a unique value.
seeds = typecast(now, 'uint32');
samples1.RandomSeed = seeds(1);
generate(samples1);



%% This script computes a heat map with following features:
% x-> amount of injected cold
% y-> amount of injected hot
% colormap -> time integrated activity

% inputs:
% Integral --> this contains the time integrated activity values. It shoudl
% be imported from the simbiology model analyzer.
integral = Integral(:,2);
integral = integral{:,:};
integral = reshape(integral, 10,10);
cold = parameterSweep(:,3);
hot = parameterSweep(:,2);

Hot = reshape(hot, 10,10);
Cold = reshape(cold, 10,10);
Spec = (Cold);



%contourf(Cold, Hot, integral, 20);
contourf(Spec, Hot, integral, 20);
xlabel("Cold");
ylabel("Hot");

hold on;


SpecList = [0.1:0.1:1];
%SpecList=logspace(-0.5,0,10);
cold_x = Cold(1,:);

for spec=SpecList
plot(cold_x, cold_x/(1/spec - 1), 'red', LineWidth=3);
end

ylim([50,400]);