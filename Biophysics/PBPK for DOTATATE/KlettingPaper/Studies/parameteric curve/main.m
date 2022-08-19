
paramSweep = data1.samples.generate{:,:};


res = data1.results;

TINnamesList = res(1).ScalarObservables.Properties.VariableNames; % to get 
% the name of columns each of which correspond to TIN value for an specific
% organ or tumor. With current version of the *.sbproj file, the order is:
% {'SpleenTIN'} {'KidneyTIN'} {'LiverTIN'} {'RedMarrowTIN'} {'TumorTIN'}
organsName = ["Spleen", "Kidney", "Liver", "RedMarrow", "Tumor"];
organsChannelIndex = [1,2,3,4,5];
organsChannelDictionary = containers.Map(organsName,organsChannelIndex);

hotAmountSteps = 1;    
coldAmountSteps = 1;
timeIntervalSteps = 9;
numberOfOrgansforTIN = 5;


 
% to extract the values of TIN (time integreated number of hots)
% in each scenario:
TINValues = zeros(length(res), numberOfOrgansforTIN);
for i=1:length(res)
    TINValues(i,:) = res(i).ScalarObservables{:,:};
end


%%%---------------------------------------------%%%
%%%% Reshapings and Reunitings


paramSweep = reshape(paramSweep,hotAmountSteps,coldAmountSteps,timeIntervalSteps,3);
% paramSweep now has 4 book channels. first book is hot, second is cold,
% third is hot time interval, and fourth is cold time interval. 
% Data of hot and cold books is Hot and Cold meshgrid. and data of time
% interval books is the time intervals. first page corresponding to 10 min
% second page 100 min, third page 500 min and fourth page 1000 min.
paramNames = ["Cold","Hot","n_repeat"];
paramChannelIndex = [1,2,3];
paramChannelDictionary = containers.Map(paramNames,paramChannelIndex);

% Hot unit conversion to Activity = lambda*N
% A = Hot*1e-9(mol) * 6.022*1e23(#/mole) * lambda(1/min) * 1/60(min/sec) =
% Hot*0.72*1e9 (#/sec) = Hot*0.72 GBq
paramSweep(:,:,:,1) = paramSweep(:,:,:,1) * 0.72; % unit is GBq;

clear cold;
clear hot;
clear interval;

% TINValues is a n*5 element matrix in which each column correspond to a
% TIN values of an specific organ. What I want to do is to put each organ
% at different channel in 4th dimension. In my terminology (see the "How
% multidimensional matrices work here:git/alifele/Computational-Physics/GreatNotes)
% I want to put them in diffenet books. So I first need to convert that
% into a single column and then convert that into a matrix with size equal
% to (20,20,4,5)

% TINValues = reshape(TINValues, [],1);
TINValues = reshape(TINValues, hotAmountSteps,coldAmountSteps, ...
    timeIntervalSteps,numberOfOrgansforTIN); % each channel of the 4th dimension
% corresponds to the TIAN value for an specific organ

TIA = TINValues * 7.23 * 1e-5;  % time integratede activity; A=N*lambda
% the unit of TIA is not #, it is nanomole. so it should be converted to #
% by multiplying at 6.023*10^23 * 10^(-9)
TIA = TIA * 6.023*1e23*1e-9;
TIA = TIA / 1e9; % the unit if TIA is now #bilion = GBq.sec





%%

close all;
NTIA = TIA ./ TIA(:,:,1,:);


% NTIA_Tumor = NTIA;
% 
% for i=1:5
%     NTIA_Tumor(:,:,:,i) = NTIA_Tumor(:,:,:,5);
% end

% Efficacy = NTIA ./ NTIA(:,:,:,5);

plot(reshape(NTIA(3,1,2:end,5),[],1),reshape(NTIA(3,1,2:end,1:4),[],4), ...
    "LineWidth",3);
% plot(reshape(NTIA(1,1,2:end,5),[],1),reshape(NTIA(1,1,2:end,2),[],1), ...
%     "LineWidth",3, "Marker","o");

xlabel("Tumor NTIA");
ylabel("Organ at Risk NTIA");
legend(["Spleen", "Kidney", "Liver", "RedMarrow"])
grid("on");

% i=3;
% comet( reshape(NTIA(1,1,2:end,i),[],1), reshape(NTIA(1,1,2:end,5),[],1));
% hold on;
% plot( reshape(NTIA(1,1,2:end,i),[],1), reshape(NTIA(1,1,2:end,5),[],1),'o');


%%

