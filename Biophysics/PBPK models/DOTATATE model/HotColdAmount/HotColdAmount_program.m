function args = HotColdAmount_program(model, cs, variantsStruct, dosesStruct)

% Initialize arguments.
args.input.model    = model;
args.input.cs       = cs;
args.input.variants = variantsStruct;
args.input.doses    = dosesStruct;

% Define StatesToLog cleanup code.
originalStatesToLog = get(cs.RuntimeOptions, 'StatesToLog');
cleanupStatesToLog  = onCleanup(@() restoreStatesToLog(cs, originalStatesToLog));

% Configure StatesToLog.
set(cs.RuntimeOptions, 'StatesToLog', {'Vein.Vein_Pl', 'Tumor1.Tumor1_Pl_bind'});

% Generate samples.
args = runGenerateSamples(args);

% Run simulation.
args = runSimulation(args);


end

% -------------------------------------------------------------------------
function args = runGenerateSamples(args)

samples1 = SimBiology.Scenarios();
add(samples1, 'cartesian', 'dose_hot Amount', linspace(10,400,10));
add(samples1, 'cartesian', 'dose_cold Amount', linspace(0,100,10));

% Configure RandomSeed to a unique value.
seeds = typecast(now, 'uint32');
samples1.RandomSeed = seeds(1);
generate(samples1);

% Populate the output structure.
args.output.samples = samples1;


end
% -------------------------------------------------------------------------
function args = runSimulation(args)

% Extract the input arguments.
input    = args.input;
model    = input.model;
cs       = input.cs;
variants = input.variants.modelStep;
doses    = input.doses.modelStep;

% Extract samples to simulate.
samples = args.output.samples;

% Construct doses.
dose1        = sbioselect(model, 'Type', 'repeatdose', 'Name', 'dose_hot');
value1       = dose1.Amount;
unit1        = dose1.AmountUnits;
param1       = addparameter(model, 'dose_hot Amount', 'ValueUnits', unit1);
cleanupDose1 = onCleanup(@() restoreDose(param1, dose1, 'Amount', value1));
dose1.Amount = 'dose_hot Amount';
dose2        = sbioselect(model, 'Type', 'repeatdose', 'Name', 'dose_cold');
value2       = dose2.Amount;
unit2        = dose2.AmountUnits;
param2       = addparameter(model, 'dose_cold Amount', 'ValueUnits', unit2);
cleanupDose2 = onCleanup(@() restoreDose(param2, dose2, 'Amount', value2));
dose2.Amount = 'dose_cold Amount';

% Turn off observables.
observables        = model.Observables;
activateState      = get(observables, {'Active'});
cleanupObservables = onCleanup(@() restoreObservables(observables, activateState));
set(observables, 'Active', false);

% Turn on observables.
obsNames    = {'integral'};
observables = sbioselect(model.Observables, 'Name', obsNames);
set(observables, 'Active', true);

% Get list of observables.
states          = cs.RuntimeOptions.StatesToLog;
observables     = sbioselect(model.Observables, 'Active', true);
observableNames = cell(1, length(states)+length(observables));
for i = 1:length(states)
    observableNames{i} = states(i).PartiallyQualifiedName;
end
for i = 1:length(observables)
    observableNames{i+length(states)} = observables(i).Name;
end

% Convert doses.
if ~isempty(doses)
    dosesTable = getTable(doses);
else
    dosesTable = [];
end

% Simulate the model.
f    = createSimFunction(model, samples, observableNames, doses, variants, 'AutoAccelerate', false);
data = f(samples, cs.StopTime, dosesTable);

% Populate the output structure.
args.output.results = data;

end

% -------------------------------------------------------------------------
function restoreStatesToLog(cs, originalStatesToLog)

% Restore StatesToLog.
set(cs.RunTime, 'StatesToLog', originalStatesToLog);

end

% -------------------------------------------------------------------------
function restoreDose(param, dose, property, value)

set(dose, property, value);
delete(param);

end

% -------------------------------------------------------------------------
function restoreObservables(observables, active)

for i = 1:length(observables)
    set(observables(i), 'Active', active{i});
end

end

