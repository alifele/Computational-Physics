## Receptor Positive Organ Initiator
from Data import Data


def Tumor_init(Patient):
    if Patient.patient_info.tumorType == "NET":
        v_tu_int = Data.TumorData["v_int_NET"]
        v_tu_v = Data.TumorData["u_v_NET"]
        k_tu = Data.TumorData["k_NET"]  ## for PS calculation
    else:
        v_tu_int = Data.TumorData["v_int_menin"]
        v_tu_v = Data.TumorData["v_v_menin"]
        k_tu = Data.TumorData["k_menin"]  ## for PS calculation

    Patient.Tumor_param = {
        "F": Patient.patient_info.f_tu * (1 - Patient.patient_info.H) * Patient.patient_info.V_tu,
        "V_v": v_tu_v * Patient.patient_info.V_tu,
        "PS": k_tu * Patient.patient_info.V_tu,
        "V_int": v_tu_int * Patient.patient_info.V_tu,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": Data.TumorData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel,
        "lambda_phy": Patient.lambda_phy}

    Patient.Tumor_var["R"] = Patient.patient_info.R_tu_density * Patient.patient_info.V_tu


def Liver_init(Patient):
    Patient.Liver_param = {
        "F": 0.065 * Patient.F,
        "V_v": Data.LiverData["v_v"] * Patient.patient_info.V_L,
        "PS": Data.LiverData["k"] * Patient.patient_info.V_L,
        "V_int": Data.LiverData["v_int"] * Patient.patient_info.V_L,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": Data.LiverData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy}

    Patient.Liver_var["R"] = Patient.patient_info.R_L_density * Patient.patient_info.V_L


def Spleen_init(Patient):
    Patient.Liver_param = {
        "F": 0.03 * Patient.F,
        "V_v": Data.SpleenData["v_v"] * Patient.patient_info.V_S,
        "PS": Data.SpleenData["k"] * Patient.patient_info.V_S,
        "V_int": Data.SpleenData["v_int"] * Patient.patient_info.V_S,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": Data.SpleenData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy}

    Patient.Spleen_var["R"] = Patient.patient_info.R_S_density * Patient.patient_info.V_S


def Kidney_init(Patient):
    Patient.Kidney_param = {
        "F": 0.19 * Patient.F,
        "V_v": Data.KidneyData["v_v"] * Patient.patient_info.V_K,
        "V_int": Data.KidneyData["v_int"] * Patient.patient_info.V_K,
        "V_intra": 0,
        "k_on": Patient.k_on,
        "k_off": Patient.k_off,
        "lambda_int": Data.KidneyData["lambda_int"],
        "lambda_rel": Patient.patient_info.lambda_rel_NT,
        "lambda_phy": Patient.lambda_phy,
        "GFR": 0,
        "theta": 0,
        "f_ecx": 0}

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

    if Patient.patient_info.gender == "female" ##Uterus
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
        "F": F,
        "k": k,
    }
    Patient.xx_var["R"] = R_density * Patient.ProstateUterus_param["V_total"] #TODO is it V_total?
