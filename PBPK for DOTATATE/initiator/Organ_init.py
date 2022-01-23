## Receptor Positive Organ Initiator
from initiator.Data import Data


def Tumor_init(Patient):
    if Patient.patient_info.tumorType == "NET":
        v_tu_int = 0.3
        v_tu_v = 0.1
        k_tu = 0.2  ## for PS calculation ## L/min/Kg (See the comment in Data.py file under MuscleData
    else:
        v_tu_int = 0.23
        v_tu_v = 0.11
        k_tu = 0.31  ## for PS calculation  ## L/min/Kg (See the comment in Data.py file under MuscleData

    Patient.Tumor_param = {
        "V_total": Patient.patient_info.V_tu,                    # L
        "F": Patient.patient_info.f_tu * (1 - Patient.patient_info.H) * Patient.patient_info.V_tu,  # L/min
        "V_v": v_tu_v * Patient.patient_info.V_tu,              # L
        "PS": k_tu * Patient.patient_info.V_tu,                 # L/min
        "V_int": v_tu_int * Patient.patient_info.V_tu,          # L
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k_tu,  ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_int": Data.TumorData["lambda_int"],             # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_TU,       # 1/min
        "lambda_phy": Patient.lambda_phy}                       # 1/min

    Patient.Tumor_var["R"] = Patient.patient_info.R_tu_density * Patient.patient_info.V_tu


def Liver_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    k = Data.MuscleData["k"] * 100
    Patient.Liver_param = {
        "V_total": Patient.patient_info.V_L,        # L
        "F": 0.065 * Patient.F,                     # L/min
        "V_v": 0.085 * Patient.patient_info.V_L,    # L
        "PS": k * Patient.patient_info.V_L,         # L/min
        "V_int": 0.2 * Patient.patient_info.V_L,    # L
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_int": lambda_int,                                   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT,           # 1/min
        "lambda_phy": Patient.lambda_phy}                           # 1/min

    Patient.Liver_var["R"] = Patient.patient_info.R_L_density * Patient.patient_info.V_L


def Spleen_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    k = Data.MuscleData["k"] * 100
    Patient.Spleen_param = {
        "V_total": Patient.patient_info.V_S,                    # L
        "F": 0.03 * Patient.F,                                  # L/min
        "V_v": 0.12 * Patient.patient_info.V_S,                 # L
        "PS": k * Patient.patient_info.V_S,                     # L/min
        "V_int": 0.2 * Patient.patient_info.V_S,                # L
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_int": lambda_int,                               # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT,       # 1/min
        "lambda_phy": Patient.lambda_phy}                       # 1/min

    Patient.Spleen_var["R"] = Patient.patient_info.R_S_density * Patient.patient_info.V_S


def Kidney_init(Patient):
    lambda_int = 1.7 * Data.TumorData["lambda_int"]
    Patient.Kidney_param = {
        "V_total": Patient.patient_info.V_K,                    # L
        "F": 0.19 * Patient.F,                                  # L/min
        "V_v": 0.055 * Patient.patient_info.V_K,                # L
        "V_int": 0.15 * Patient.patient_info.V_K,               # L
        "V_intra": 0,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": lambda_int,                               # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT,       # 1/min
        "lambda_phy": Patient.lambda_phy,                       # 1/min
        "GFR": Patient.patient_info.GFR*1,
        "phi": 1.0,
        "f_exc": 0.98}

    V_intra = (Patient.patient_info.V_K - Patient.Kidney_param["V_int"] - Patient.Kidney_param["V_v"]) * 2 / 3
    Patient.Kidney_param["V_intra"] = V_intra

    Patient.Kidney_var["R"] = Patient.patient_info.R_K_density * Patient.patient_info.V_K


def ProstateUterus_init(Patient):
    if Patient.patient_info.gender == "male": ## Prostate
        V_total = 0.016 * Patient.patient_info.BW/71    # L
        V_v = 0.04 * (1-Patient.patient_info.H) * V_total   # L
        V_int = 0.25*V_total    # L
        F = 0.18 * (1-Patient.patient_info.H) * V_total
        k = 0.1
        R_density = Patient.patient_info.R_K_density * 0.26

    if Patient.patient_info.gender == "female": ##Uterus
        V_total = 0.08 * Patient.patient_info.BW/71 # L
        V_v = 0.07 * (1 - Patient.patient_info.H) * V_total # L
        V_int = 0.25 * 0.5  # L
        F = 1 * (1-Patient.patient_info.H) * V_total
        k = 0.2
        R_density = Patient.patient_info.R_K_density * 0.092

    Patient.ProstateUterus_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k*V_total,                                    #L/min
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,                                             # L/min
        "k": k,                                             # L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.ProstateUterus_var["R"] = R_density * Patient.ProstateUterus_param["V_total"]



def Lungs_init(Patient):
    V_total = 1 * Patient.patient_info.BW/71    # L
    V_v = 0.105 * Patient.V_p   # L
    alpha = 5.5 ## interestitial to vascular ratio
    V_int = V_v*alpha   # L
    F = Patient.F
    k = 100 * Data.MuscleData["k"]
    R_density = 0

    Patient.Lungs_param = {
        "V_total": V_total,                 # L
        "V_v": V_v,                         # L
        "V_int": V_int,                     # L
        "PS": k*V_total,                    # L/min
        "F": F,                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy    # 1/min
    }
    Patient.Lungs_var["R"] = R_density * Patient.Lungs_param["V_total"]


def Adrenals_init(Patient):
    V_total = 0.014*Patient.patient_info.BW/71  # L
    V_v = 0.03*(1-Patient.patient_info.H) * V_total # L
    V_int = 0.24 * V_total  # L
    f = 6
    F = f * (1-Patient.patient_info.BW) * V_total
    k = Data.MuscleData['k'] * 100
    R_density = Patient.patient_info.R_K_density * 1.65

    Patient.Adrenals_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k*V_total,                                    # L/min
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.Adrenals_var["R"] = R_density * Patient.Adrenals_param["V_total"]

def GI_init(Patient):
    V_total = (0.385+0.548+0.104+0.15) * Patient.patient_info.BW / 71   # L
    V_v = 0.076 * V_total   # L
    alpha = 8.8  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.16*Patient.F
    k = Data.MuscleData['k']
    R_density = Patient.patient_info.R_K_density * 0.16

    Patient.GI_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k*V_total,                                    # L/min
        "F": F,                                             # L/min
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.GI_var["R"] = R_density * Patient.GI_param["V_total"]

def Skin_init(Patient):
    V_total = 3.408 * Patient.patient_info.BW / 71  # L
    V_v = 0.03 * V_total    # L
    alpha = 8.9  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.05 *Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Skin_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k*V_total,                                     # L/min,
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy    # 1/min
    }
    Patient.Skin_var["R"] = R_density * Patient.Skin_param["V_total"]

def Adipose_init(Patient):
    V_total = 13.465 * Patient.patient_info.BW / 71 # L
    V_v = 0.05 * V_total    # L
    alpha = 15.5  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.05 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Adipose_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k*V_total,                                    # L/min
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy                    # 1/min
    }
    Patient.Adipose_var["R"] = R_density * Patient.Adipose_param["V_total"]



def RedMarrow_init(Patient):
    V_total = 1.1 * Patient.patient_info.BW / 71    # L
    V_v = 0.04 * V_total    # L
    alpha = 3.7  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.03 * Patient.F
    k = Data.LiverData['k']
    R_density = Patient.patient_info.R_K_density * 0.028

    Patient.RedMarrow_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "PS": k * V_total,                                  # L/min
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.RedMarrow_var["R"] = R_density * Patient.RedMarrow_param["V_total"]


def Bone_init(Patient):
    V_total = 10.165 * Patient.patient_info.BW / 71 - Patient.RedMarrow_param['V_total']    # L
    V_v = 0.07 * V_total - Patient.RedMarrow_param["V_v"]                                   # L
    alpha = 9.3  ## interestitial to vascular ratio
    V_int = alpha * V_v                                                                     # L
    F = 0.05 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Bone_param = {
        "V_total": V_total,                 # L
        "V_v": V_v,                         # L
        "V_int": V_int,                     # L
        "PS": k * V_total,                  # L/min
        "F": F,                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy    # 1/min
    }
    Patient.Bone_var["R"] = R_density * Patient.Bone_param["V_total"]



def Heart_init(Patient):
    V_total = 0.341 * Patient.patient_info.BW / 71  # L
    V_v = 0.01 * V_total                            # L
    alpha = 3.7  ## interestitial to vascular ratio
    V_int = alpha * V_v                             # L
    F = 0.04 * Patient.F
    k = Data.MuscleData['k']
    R_density = 0

    Patient.Heart_param = {
        "V_total": V_total,                 # L
        "V_v": V_v,                         # L
        "V_int": V_int,                     # L
        "PS": k * V_total,                  # L/min
        "F": F,                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy    # 1/min
    }
    Patient.Heart_var["R"] = R_density * Patient.Heart_param["V_total"]


def Brain_init(Patient):
    V_total = 1.45 * Patient.patient_info.BW / 71   # L
    V_v = 0.012 * V_total   # L
    alpha = 0  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.04 * Patient.F
    k = 0
    R_density = 0

    Patient.Brain_param = {
        "V_total": V_total,                     # L
        "V_v": V_v,                             # L
        "V_int": V_int,                         # L
        "PS": k * V_total,                      # L/min
        "F": F,                                 # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy        # 1/min
    }
    Patient.Brain_var["R"] = R_density * Patient.Brain_param["V_total"]



def Muscle_init(Patient):
    V_total = 30.078 * Patient.patient_info.BW / 71 # L
    V_v = 0.14 * V_total    # L
    alpha = 5.9  ## interestitial to vascular ratio
    V_int = alpha * V_v # L
    F = 0.17 * Patient.F
    k = Data.MuscleData['k']
    R_density = Patient.patient_info.R_K_density * 0.0056

    Patient.Muscle_param = {
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "V_int": V_int,                                     # L
        "PS": k * V_total,                                  # L/min
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.Muscle_var["R"] = R_density * Patient.Muscle_param["V_total"]


def Art_init(Patient):
    V_total = (0.06 + 0.045)*Patient.V_p                    # L
    F = Patient.F

    Patient.Art_param = {
        "V_total": V_total,                                 # L
        "F": F,                                             # L/min
        "lambda_phy": Patient.lambda_phy                    # 1/min
    }
    Patient.Art_var["P_labeled"] = 0
    Patient.Art_var["P_unlabeled"] = 0


def Vein_init(Patient):
    V_total = (0.18 + 0.045) * Patient.V_p  # L
    F = Patient.F

    Patient.Vein_param = {
        "V_total": V_total,                             # L
        "F": F,                                         # L/min
        "lambda_phy": Patient.lambda_phy                # 1/min
    }
    Patient.Vein_var["P_labeled"] = 0.5 * 1e-5
    Patient.Vein_var["P_unlabeled"] = 0.5 * 1e-5


def Rest_init(Patient):
    V_body = Patient.patient_info.BW   ## 1kg = 1 lit   # L
    V_total_organs = 0.0    # L
    V_v_organs = 0.0    # L
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
        "V_total": V_total,                                 # L
        "V_v": V_v,                                         # L
        "V_int": V_int,                                     # L
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "PS": k * V_total,                                  # L/min
        "F": F,                                             # L/min
        "k": k, ## L/min/Kg (See the comment in Data.py file under MuscleData
        "lambda_phy": Patient.lambda_phy,                   # 1/min
        "lambda_int": 1.7 * Data.TumorData["lambda_int"],   # 1/min
        "lambda_rel": Patient.patient_info.lambda_rel_NT    # 1/min
    }
    Patient.Rest_var["R"] = R_density * Patient.Rest_param["V_total"]


def BloodProteinComplex_init(Patient):
    Patient.BloodProteinComplex_param = {
        "K_pr": Patient.patient_info.k_pr * 0,  # 1/min
        "lambda_phy": Patient.lambda_phy    # 1/min
    }





























