% The following code will multiply the value of k_pr at coeff
clear;
args = load("args.mat");
Args = args.args;
rules = Args{1}.rules;
% Finding the index of k_pr
for i = 1:size(rules,1)
    rule = rules(i);
    if strfind(rule.Rule, "k_pr")
        k_pr_index = i;
        break;
    end
end

coeff = 1000;
coeff_str = string(coeff);
newValue = "k_pr = " + coeff_str + "*" + "4.7" + "*1e-4";
Args{1}.rules(k_pr_index).rule = newValue;

% Running the simulation 
simulationResult = Simulate(Args{:});
results = simulationResult.output.results;
data = results.Data;
tList = results.time;
dataNames = results.dataNames;



% Extracting the labeled variables
labeledIndexList = [];  % index of labeled variables in data
labeledNamesList = [];  % name of labeld variables 
j = 1;
for i = 1:size(data,2)
    name = dataNames(i);
    name = name{1};
    if (size(strfind(name, "Pl")) + size(strfind(name, "PeptideProtein_PPRl")))
        labeledIndexList(j) = i;
        j=j+1;
    end
end
labeledNamesList = dataNames(labeledIndexList);



% Plotting
% plot(tList(1:50), data(1:50,labeledIndexList))


% Numerical Calculation
integ = integral_array(data(:, labeledIndexList), tList);



