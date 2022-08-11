% this script will generate the metric plots. the X and Y axis of metric
% plot is hot and cold amount. But the color values of the heatmap is this
% quantity --> (TIA_tumor(s1)/TIA_tumor(s0))/(TIA_OAR(s1)/TIA(OAR(s0)). In
% other words we actually want to devide the normalized TIA heat map of
% tumor by normalized TIA heat map of the OARs.

paramSweep = data1.samples.generate{:,:};


res = data1.results;

TINnamesList = res(1).ScalarObservables.Properties.VariableNames; % to get 
% the name of columns each of which correspond to TIN value for an specific
% organ or tumor. With current version of the *.sbproj file, the order is:
% {'SpleenTIN'} {'KidneyTIN'} {'LiverTIN'} {'RedMarrowTIN'} {'TumorTIN'}
organsName = ["Spleen", "Kidney", "Liver", "RedMarrow", "Tumor"];
organsChannelIndex = [1,2,3,4,5];
organsChannelDictionary = containers.Map(organsName,organsChannelIndex);

hotAmountSteps = 30;    
coldAmountSteps = 30;
timeIntervalSteps = 5;
numberOfOrgansforTIN = 5;

paramSweep = data1.samples.generate{:,:};

 

% % % hot = paramSweep(:,1);
% % % cold = paramSweep(:,2);
% % % interval = paramSweep(:,3);


% to extract the values of TIN (time integreated number of hots)
% in each scenario:
TINValues = zeros(length(res), 5);
for i=1:length(res)
    TINValues(i,:) = res(i).ScalarObservables{:,:};
end


%%%---------------------------------------------%%%
%%%% Reshapings and Reunitings


paramSweep = reshape(paramSweep,hotAmountSteps,coldAmountSteps,timeIntervalSteps,4);
% paramSweep now has 4 book channels. first book is hot, second is cold,
% third is hot time interval, and fourth is cold time interval. 
% Data of hot and cold books is Hot and Cold meshgrid. and data of time
% interval books is the time intervals. first page corresponding to 10 min
% second page 100 min, third page 500 min and fourth page 1000 min.
paramNames = ["Hot","Cold","HotInterval","ColdInterval"];
paramChannelIndex = [1,2,3,4];
paramChannelDictionary = containers.Map(paramNames,paramChannelIndex);

% Hot unit conversion to Activity = lambda*N
% A = Hot*1e-9(mol) * 6.022*1e23(#/mole) * lambda(1/min) * 1/60(min/sec) =
% Hot*0.72*1e9 (#/sec) = Hot*0.72 GBq
paramSweep(:,:,:,1) = paramSweep(:,:,:,1) * 0.72; % unit is GBq;

clear cold;
clear hot;
clear interval;

% TINValues is a 1600*5 element matrix in which each column correspond to a
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

normalizedTIA = TIA(:,:,:,:)./TIA(:,:,1,:); %TIA(:,:,1,:) corresponds to 10
% min injection interval. we consider that as the base line strategy

X = normalizedTIA(:,:,:,1:4); %for OARs
X(X>=2) = 2;
y = normalizedTIA(:,:,:,5); %for tumor
Y = y;
Y(:,:,:,2)=y;
Y(:,:,:,3)=y;
Y(:,:,:,4)=y;


% kidneyNTIA = normalizedTIA(:,:,2,2); %NTIA for 1000 min kidney
% tumorNTIA = normalizedTIA(:,:,2,5); %NTIA for 1000 min tumor
% 
% kidneyMetricPlot = zeros(size(kidneyNTIA));
% % kidneyMetricPlot((kidneyNTIA<1 & tumorNTIA>1)) = 1;
% % kidneyMetricPlot((kidneyNTIA>1 & tumorNTIA<1)) = -1;
% 
% 
% kidneyMetricPlot((tumorNTIA./kidneyNTIA>1)&kidneyNTIA>1) = 0.5;
% kidneyMetricPlot((tumorNTIA./kidneyNTIA<1)&kidneyNTIA>1) = -0.5;
% kidneyMetricPlot((tumorNTIA./kidneyNTIA<1)&kidneyNTIA<1) = -0.5;
% kidneyMetricPlot((tumorNTIA./kidneyNTIA>1)&kidneyNTIA<1) = 0.5;


metricValues = zeros(size(Y));



% metricValues(Y./X>1) = -0.5;
% metricValues(Y./X<1) = +0.5;
% metricValues(Y>1 & X<1) = metricValues(Y>1 & X<1)-0.5;
% metricValues(Y<1 & X>1) = metricValues(Y<1 & X>1)+0.5;


% metricValues(Y./X>1) = Y./X;
% metricValues(Y./X<1) = Y./X;
% metricValues(Y>1 & X<1) = metricValues(Y>1 & X<1)-0.5;
% metricValues(Y<1 & X>1) = metricValues(Y<1 & X>1)+0.5;
% metricValues = Y./X;



% metricValues((OrganDivTumor>1))




% 
% contourf(paramSweep(:,:,1,paramChannelDictionary("Cold")), ...
%     paramSweep(:,:,1,paramChannelDictionary("Hot")), ...
%     metricValues(:,:,2,2),1)
% colorbar
% caxis([-1,1])

% myColorMap = [204, 0, 0;255, 166, 77;0, 230, 230;57, 230, 0];

% myColorMap = [201, 47, 8 ;201, 122, 8;161, 201, 8 ;56, 201, 8 ];

a = Y-X;
b = Y+X;

% val = a + 50*a./abs((9-(b-3).^2));
% val = val./abs(min(val(:)));

val = a + 0.03*a./exp((-(b-2).^2)/0.5);

val = val./abs(min(val(:)));


val1 = 1*a./exp((-(b-2).^2)/2);

val2 = 1*(b-2)./exp((-(a).^2)/2);

val = val1*1./(val2.^2+0.5);
val = val./abs(max(val(:)));




% contourf(X(:,:,2,2),Y(:,:,2,2),Y(:,:,2,2));
% contourf(paramSweep(:,:,2,paramChannelDictionary("Cold")), ...
%             paramSweep(:,:,2,paramChannelDictionary("Hot")), ...
%             val(:,:,2,organIndex), 5);
% 
% colormap("jet")
% colorbar();
% caxis([-1,1]);



for organIndex=1:4
    organFigure = figure(organIndex); set(organFigure, "Position", ...
        [500+10*organIndex,500+10*organIndex,1000,600])
    timeTiles = tiledlayout(2,2,'TileSpacing','Compact','Padding','Compact');
    for i=2:timeIntervalSteps
        nexttile;
%         contourf(paramSweep(:,:,i,paramChannelDictionary("Cold")), ...
%             paramSweep(:,:,i,paramChannelDictionary("Hot")), ...
%             metricValues(:,:,i,organIndex), 2);

%         contourf(paramSweep(:,:,i,paramChannelDictionary("Cold")), ...
%             paramSweep(:,:,i,paramChannelDictionary("Hot")), ...
%             colorVal(:,:,i,organIndex),5);

        contourf(paramSweep(:,:,2,paramChannelDictionary("Cold")), ...
            paramSweep(:,:,2,paramChannelDictionary("Hot")), ...
            val(:,:,i,organIndex), 5);

        colormap("jet");
%         colormap(myColorMap/255);
        caxis([-1,1]);
%         colorbar;
        title("infusion rate: " + paramSweep(1,1,i,3) + "nanomole/min", fontsize=14, FontWeight="normal");
    end

 
    cb = colorbar;
    cb.Layout.Tile = 'east';
    cb.Label.String = "Efficacy";
    cb.Label.FontSize = 10;
    title(timeTiles, ["Efficacy in "+organsName(organIndex)+": constant rate infusion"], fontsize=15)
    xlabel(timeTiles, "total injected cold amount [nmol]", fontsize=15);
    ylabel(timeTiles, "total injected activity [GBq]", fontsize=15);


end
