load('HotColdAmount_args.mat');
result = HotColdAmount_program(HotColdAmount_args{:});

% When we run the program, the result object contains inputs and outputs.
% inputs is simply the model description and output contains the samples of
% scenarios and the results

% scenario --> when we perform parameter sweep in matlab, the results is
% called scenario. The parameter sweep is saved in form of scenarion
% object. You can search simbiology scenarios in the help bar and find the
% documentations. scenario object also contains some methods amoung which
% the generate method is important to us

% Inorder to use the method of the class we should write
% (method(scenario)) or scenario.generate. For example generate(scenario)
% or scenario.generate.


scenarios = result.output.samples;  % to get the scenarios
parametersTable = scenarios.generate(); % to get the table of different values per scenario
parametersTable = parametersTable{:,:}; % to convert table to matrix

nEntry = scenarios.NumberOfEntries % 2 entries in this case: amount of hot 
% and amount of cold
nameOfEntries = {};

for i=1:nEntry;  % iterate over entries to get the name of entries
    nameOfEntries{end+1} = scenarios.getEntry(i).Name;
end

% if you check the the nameOfEntries list, you will find out that the first
% name is Hot and the second is Cold. So the first column of
% parametersTable of Hot and the second is Cold


% extracting the hot and cold list
hotList = parametersTable(:,1);
coldList = parametersTable(:,2);

% Converting into a mesh grind format by resizing:
% since each of parameters have 10 samples, so by reshaping the hot and
% cold lists we will have meshgrid like structures
Hot = reshape(hotList, 10,10);
Cold = reshape(coldList, 10,10);


% Extracting the values of time integrated activity which were defind as a
% observable in the model

TIAList = zeros(100,1);
res = result.output.results;
for i=1:length(res)
    TIAList(i) = res(i).ScalarObservables{:,:};
end

TIA = reshape(TIAList,10,10); % reshaping TIAList to get the same format as
% and Cold (which were in form of meshgird

contourf(Cold, Hot, TIA, 20);
xlabel("Cold");
ylabel("Hot");
title("receptor binded compartmetn of tumor");









