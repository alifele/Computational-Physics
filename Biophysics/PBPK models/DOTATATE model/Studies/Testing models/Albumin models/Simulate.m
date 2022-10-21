function args = Simulate(model, cs, variantsStruct, dosesStruct)

% Initialize arguments.
args.input.model    = model;
args.input.cs       = cs;
args.input.variants = variantsStruct;
args.input.doses    = dosesStruct;

% Define StatesToLog cleanup code.
originalStatesToLog = get(cs.RuntimeOptions, 'StatesToLog');
cleanupStatesToLog  = onCleanup(@() restoreStatesToLog(cs, originalStatesToLog));

% Configure StatesToLog.
set(cs.RuntimeOptions, 'StatesToLog', {'Liver.Liver_P_v', 'Liver.Liver_P_int', 'Liver.Liver_P_bind', 'Liver.Liver_P_intern', 'Liver.Liver_Pl_v', 'Liver.Liver_Pl_int', 'Liver.Liver_Pl_bind', 'Liver.Liver_Pl_intern', 'Liver.Liver_R', 'Art.Art_P', 'Art.Art_Pl', 'Vein.Vein_P', 'Vein.Vein_Pl', 'Lungs.Lungs_P_v', 'Lungs.Lungs_P_int', 'Lungs.Lungs_Pl_v', 'Lungs.Lungs_Pl_int', 'Brain.Brain_P_v', 'Brain.Brain_P_int', 'Brain.Brain_Pl_v', 'Brain.Brain_Pl_int', 'Skin.Skin_P_v', 'Skin.Skin_P_int', 'Skin.Skin_Pl_v', 'Skin.Skin_Pl_int', 'Heart.Heart_P_v', 'Heart.Heart_P_int', 'Heart.Heart_Pl_v', 'Heart.Heart_Pl_int', 'Bone.Bone_P_v', 'Bone.Bone_P_int', 'Bone.Bone_Pl_v', 'Bone.Bone_Pl_int', 'Adipose.Adipose_P_v', 'Adipose.Adipose_P_int', 'Adipose.Adipose_Pl_v', 'Adipose.Adipose_Pl_int', 'GI.GI_P_v', 'GI.GI_P_int', 'GI.GI_P_bind', 'GI.GI_P_intern', 'GI.GI_Pl_v', 'GI.GI_Pl_int', 'GI.GI_Pl_bind', 'GI.GI_Pl_intern', 'GI.GI_R', 'Spleen.Spleen_P_v', 'Spleen.Spleen_P_int', 'Spleen.Spleen_P_bind', 'Spleen.Spleen_P_intern', 'Spleen.Spleen_Pl_v', 'Spleen.Spleen_Pl_int', 'Spleen.Spleen_Pl_bind', 'Spleen.Spleen_Pl_intern', 'Spleen.Spleen_R', 'Muscle.Muscle_P_v', 'Muscle.Muscle_P_int', 'Muscle.Muscle_P_bind', 'Muscle.Muscle_P_intern', 'Muscle.Muscle_Pl_v', 'Muscle.Muscle_Pl_int', 'Muscle.Muscle_Pl_bind', 'Muscle.Muscle_Pl_intern', 'Muscle.Muscle_R', 'RedMarrow.RedMarrow_P_v', 'RedMarrow.RedMarrow_P_int', 'RedMarrow.RedMarrow__bind', 'RedMarrow.RedMarrow_P_intern', 'RedMarrow.RedMarrow_Pl_v', 'RedMarrow.RedMarrow_Pl_int', 'RedMarrow.RedMarrow_Pl_bind', 'RedMarrow.RedMarrow_Pl_intern', 'RedMarrow.RedMarrow_R', 'Adrenal.Adrenal_P_v', 'Adrenal.Adrenal_P_int', 'Adrenal.Adrenal_P_bind', 'Adrenal.Adrenal_P_intern', 'Adrenal.Adrenal_Pl_v', 'Adrenal.Adrenal_Pl_int', 'Adrenal.Adrenal_Pl_bind', 'Adrenal.Adrenal_Pl_intern', 'Adrenal.Adrenal_R', 'ProUt.ProUt_P_v', 'ProUt.ProUt_P_int', 'ProUt.ProUt_P_bind', 'ProUt.ProUt_P_intern', 'ProUt.ProUt_Pl_v', 'ProUt.ProUt_Pl_int', 'ProUt.ProUt_Pl_bind', 'ProUt.ProUt_Pl_intern', 'ProUt.ProUt_R', 'Rest.Rest_P_v', 'Rest.Rest_P_int', 'Rest.Rest_P_bind', 'Rest.Rest_P_intern', 'Rest.Rest_Pl_v', 'Rest.Rest_Pl_int', 'Rest.Rest_Pl_bind', 'Rest.Rest_Pl_intern', 'Rest.Rest_R', 'Kidney.Kidney_P_v', 'Kidney.Kidney_P_int', 'Kidney.Kidney_P_bind', 'Kidney.Kidney_P_intern', 'Kidney.Kidney_Pl_v', 'Kidney.Kidney_Pl_int', 'Kidney.Kidney_Pl_bind', 'Kidney.Kidney_Pl_intern', 'Kidney.Kidney_R', 'Kidney.Kidney_P_intera', 'Kidney.Kidney_Pl_intera', 'Tumor1.Tumor1_P_v', 'Tumor1.Tumor1_P_int', 'Tumor1.Tumor1_P_bind', 'Tumor1.Tumor1_P_intern', 'Tumor1.Tumor1_Pl_v', 'Tumor1.Tumor1_Pl_int', 'Tumor1.Tumor1_Pl_bind', 'Tumor1.Tumor1_Pl_intern', 'Tumor1.Tumor1_R', 'Peptide_Protein.PeptideProtein_PPR', 'Peptide_Protein.PeptideProtein_PPRl'});

% Run simulation.
args = runSimulation(args);

end

% -------------------------------------------------------------------------
function args = runSimulation(args)

% Extract the input arguments.
input    = args.input;
model    = input.model;
cs       = input.cs;
variants = input.variants.modelStep;
doses    = input.doses.modelStep;

% Define StopTime cleanup code.
originalStopTime  = get(cs, 'StopTime');
originalTimeUnits = get(cs, 'TimeUnits');
cleanupStopTime   = onCleanup(@() restoreStopTime(cs, originalStopTime, originalTimeUnits));

% Configure StopTime.
set(cs, 'StopTime', 10000);
set(cs, 'TimeUnits', 'minute');

% Simulate the model
data = sbiosimulate(model, cs, variants, doses);

% Populate the output structure.
args.output.results = data;

end

% -------------------------------------------------------------------------
function restoreStatesToLog(cs, originalStatesToLog)

% Restore StatesToLog.
set(cs.RunTime, 'StatesToLog', originalStatesToLog);

end



% -------------------------------------------------------------------------
function restoreStopTime(cs, originalStopTime, originalTimeUnits)

% Restore StopTime.
set(cs, 'StopTime', originalStopTime);
set(cs, 'TimeUnits', originalTimeUnits);

end

