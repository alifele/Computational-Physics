## Receptor Positive Organ Initiator
from initiator.Data import Data


def Tumor_init(Patient):
    if Patient.patient_info.tumorType == "NET":
        v_tu_int = 0.3
        v_tu_v = 0.1
        k_tu = 0.2  ## for PS calculation
    else:
        v_tu_int = 0.23
        v_tu_v = 0.11
        k_tu = 0.31  ## for PS calculation

    Patient.Tumor_param = {
        "V_total": Patient.patient_info.V_tu,
        "F": Patient.patient_info.f_tu * (1 - Patient.patient_info.H) * Patient.patient_info.V_tu,
        "V_v": v_tu_v * Patient.patient_info.V_tu,
        "PS": k_tu * Patient.patient_info.V_tu,
        "V_int": v_tu_int * Patient.patient_info.V_tu,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k_tu,
        "lambda_int": Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_TU,
        "lambda_phy": Patient.lambda_phy}

    Patient.Tumor_var["R"] = Patient.patient_info.R_tu_density * Patient.patient_info.V_tu


def Liver_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    k = Data.MuscleData["k"] * 100
    Patient.Liver_param = {
        "V_total": Patient.patient_info.V_L,
        "F": 0.065 * Patient.F,
        "V_v": 0.085 * Patient.patient_info.V_L,
        "PS": k * Patient.patient_info.V_L,
        "V_int": 0.2 * Patient.patient_info.V_L,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k,
        "lambda_int": lambda_int,
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy}

    Patient.Liver_var["R"] = Patient.patient_info.R_L_density * Patient.patient_info.V_L


def Spleen_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    k = Data.MuscleData["k"] * 100
    Patient.Spleen_param = {
        "V_total": Patient.patient_info.V_S,
        "F": 0.03 * Patient.F,
        "V_v": 0.12 * Patient.patient_info.V_S,
        "PS": k * Patient.patient_info.V_S,
        "V_int": 0.2 * Patient.patient_info.V_S,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k,
        "lambda_int": lambda_int,
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy}

    Patient.Spleen_var["R"] = Patient.patient_info.R_S_density * Patient.patient_info.V_S


def Kidney_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    Patient.Kidney_param = {
        "V_total": Patient.patient_info.V_K,
        "F": 0.19 * Patient.F,
        "V_v": 0.055 * Patient.patient_info.V_K,
        "V_int": 0.15 * Patient.patient_info.V_K,
        "V_intra": 0,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": lambda_int,
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy,
        "GFR": Patient.patient_info.GFR,
        "phi": 1.0,
        "f_exc": 0.98}

    V_intra = (Patient.patient_info.V_K - Patient.Kidney_param["V_int"] - Patient.Kidney_param["V_v"]) * 2 / 3
    Patient.Kidney_param["V_intra"] = V_intra

    Patient.Kidney_var["R"] = Patient.patient_info.R_K_density * Patient.patient_info.V_K


def ProstateUterus_init(Patient):
    if Patient.patient_info.gender == "male": ## Prostate
        V_total = 0.016 * Patient.patient_info.BW/71
        V_v = 0.04 * (1-Patient.patient_info.H) * V_total
        V_int = 0.25*V_total
        F = 0.18 * (1-Patient.patient_info.H) * V_total
        k = 0.1
        R_density = Patient.patient_info.R_K_density * 0.26

    if Patient.patient_info.gender == "female": ##Uterus
        V_total = 0.08 * Patient.patient_info.BW/71
        V_v = 0.07 * (1 - Patient.patient_info.H) * V_total
        V_int = 0.25 * 0.5
        F = 1 * (1-Patient.patient_info.H) * V_total
        k = 0.2
        R_density = Patient.patient_info.R_K_density * 0.092

    Patient.ProstateUterus_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.ProstateUterus_var["R"] = R_density * Patient.ProstateUterus_param["V_total"]



def Lungs_init(Patient):
    V_total = 1 * Patient.patient_info.BW/71
    V_v = 0.105 * Patient.V_p
    alpha = 5.5 ## interestitial to vascular ratio
    V_int = V_v*alpha
    F = Patient.F
    k = 100 * Data.MuscleData["k"]
    R_density = 0

    Patient.Lungs_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Lungs_var["R"] = R_density * Patient.Lungs_param["V_total"]


def Adrenals_init(Patient):
    V_total = 0.014*Patient.patient_info.BW/71
    V_v = 0.03*(1-Patient.patient_info.H) * V_total
    V_int = 0.24 * V_total
    f = 6
    F = f * (1-Patient.patient_info.BW) * V_total
    k = Data.MuscleData['k'] * 100
    R_density = Patient.patient_info.R_K_density * 1.65

    Patient.Adrenals_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.Adrenals_var["R"] = R_density * Patient.Adrenals_param["V_total"]

def GI_init(Patient):
    V_total = (0.385+0.548+0.104+0.15) * Patient.patient_info.BW / 71
    V_v = 0.076 * V_total
    alpha = 8.8  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.16*Patient.F
    k = Data.MuscleData['k']
    R_density = Patient.patient_info.R_K_density * 0.16

    Patient.GI_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "F": F,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.GI_var["R"] = R_density * Patient.GI_param["V_total"]

def Skin_init(Patient):
    V_total = 3.408 * Patient.patient_info.BW / 71
    V_v = 0.03 * V_total
    alpha = 8.9  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.05 *Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Skin_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Skin_var["R"] = R_density * Patient.Skin_param["V_total"]

def Adipose_init(Patient):
    V_total = 13.465 * Patient.patient_info.BW / 71
    V_v = 0.05 * V_total
    alpha = 15.5  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.05 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Adipose_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k*V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Adipose_var["R"] = R_density * Patient.Adipose_param["V_total"]



def RedMarrow_init(Patient):
    V_total = 1.1 * Patient.patient_info.BW / 71
    V_v = 0.04 * V_total
    alpha = 3.7  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.03 * Patient.F
    k = Data.LiverData['k']
    R_density = Patient.patient_info.R_K_density * 0.028

    Patient.RedMarrow_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k * V_total,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.RedMarrow_var["R"] = R_density * Patient.RedMarrow_param["V_total"]


def Bone_init(Patient):
    V_total = 10.165 * Patient.patient_info.BW / 71 - Patient.RedMarrow_param['V_total']
    V_v = 0.07 * V_total - Patient.RedMarrow_param["V_v"]
    alpha = 9.3  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.05 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Bone_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k * V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Bone_var["R"] = R_density * Patient.Bone_param["V_total"]



def Heart_init(Patient):
    V_total = 0.341 * Patient.patient_info.BW / 71
    V_v = 0.01 * V_total
    alpha = 3.7  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.04 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Heart_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k * V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Heart_var["R"] = R_density * Patient.Heart_param["V_total"]


def Brain_init(Patient):
    V_total = 1.45 * Patient.patient_info.BW / 71
    V_v = 0.012 * V_total
    alpha = 0  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.04 * Patient.F
    k = 0
    R_density = 0

    Patient.Brain_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "PS": k * V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Brain_var["R"] = R_density * Patient.Brain_param["V_total"]



def Muscle_init(Patient):
    V_total = 30.078 * Patient.patient_info.BW / 71
    V_v = 0.14 * V_total
    alpha = 5.9  ## interestitial to vascular ratio
    V_int = alpha * V_v
    F = 0.17 * Patient.F
    k = Data.MuscleData['k']
    R_density = Patient.patient_info.R_K_density * 0.0056

    Patient.Muscle_param = {
        "V_total": V_total,
        "V_v": V_v,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "V_int": V_int,
        "PS": k * V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.Muscle_var["R"] = R_density * Patient.Muscle_param["V_total"]


def Art_init(Patient):
    V_total = (0.06 + 0.045)*Patient.V_p
    F = Patient.F

    Patient.Art_param = {
        "V_total": V_total,
        "F": F,
        "lambda_phy": Patient.lambda_phy
    }


def Vein_init(Patient):
    V_total = (0.18 + 0.045) * Patient.V_p
    F = Patient.F

    Patient.Vein_param = {
        "V_total": V_total,
        "F": F,
        "lambda_phy": Patient.lambda_phy
    }
    Patient.Vein_var["P_labeled"] = 100
    Patient.Vein_var["P_unlabeled"] = 100


def Rest_init(Patient):
    V_body = Patient.patient_info.BW   ## 1kg = 1 lit
    V_total_organs = 0.0
    V_v_organs = 0.0
    F_organs = 0.0
    for organ in Patient.OrgansList:
        if organ.name == "Tumor" or "BloodProteinComplex":
            continue
        V_total_organs += organ.parameters["V_total"]
        V_v_organs += organ.parameters["V_v"]
        F_organs += organ.parameters["F"]

    V_total = V_body - V_total_organs
    V_v = Patient.V_p - V_v_organs
    alpha = 3.7 ## interestitial to vascular volume
    V_int = alpha * V_total
    F = Patient.F - F_organs
    k = Data.MuscleData['k']
    R_density = Patient.patient_info.R_rest_density


    Patient.Rest_param = {
        "V_total": V_total,
        "V_v": V_v,
        "V_int": V_int,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "PS": k * V_total,
        "F": F,
        "k": k,
        "lambda_phy": Patient.lambda_phy,
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT
    }
    Patient.Rest_var["R"] = R_density * Patient.Rest_param["V_total"]


def BloodProteinComplex_init(Patient):
    Patient.BloodProteinComplex_param = {
        "K_pr": Patient.patient_info.k_pr,
        "lambda_phy": Patient.lambda_phy
    }





























