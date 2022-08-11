sfunction result = k_pr_ParameterSweep(k_prList)
% this function will return the time integerated activity value
% corresponding to each value of k_pr in k_prList.

args = load("args.mat");
Args = args.args;
rules = Args{1}.rules;

for i = 1:size(rules,1)
    rule = rules(i);
    if strfind(rule.Rule, "k_pr")
        k_pr_index = i;
        break;
    end
end

result = zeros()


for k = 1:size(k_prList,2)

    k_pr = k_prList(k);
    coeff_str = string(k_pr);
    newValue = "k_pr = " + coeff_str + "*" + "4.7" + "*1e-4";
    Args{1}.rules(k_pr_index).rule = newValue;

    % Running the simulation 
    simulationResult = Simulate(Args{:});
    results = simulationResult.output.results;
    data = results.Data;
    tList = results.time;
    dataNames = results.dataNames;

    if k == 1
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
        result = zeros(size(labeledIndexList,2),size(k_prList,2));
    end

    result(:,k) = integral_array(data(:, labeledIndexList), tList);



end



end

