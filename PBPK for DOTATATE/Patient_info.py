class Patient_info:

    gender = "male"     ## male or female
    BSA = 1.94      ## Body Surface Area -- m^2
    BW = 80         ## Body Weight -- kg
    H = 0.1

    V_body = BW*1000  ## Based on 1g==1ml assumption
    V_tu = 0.087    ## litre
    V_L = 1.811     ## litre
    V_S = 0.198     ## litre
    V_K = 0.193     ## litre

    R_tu_density = 15   ## nmol/L
    R_L_density = 1.4   ## nmol/L
    R_S_density = 8.7   ## nmol/L
    R_K_density = 6.5   ## nmol/L
    R_rest_density = 0.5    ## nmol/L

    lambda_rel_NT = 0.7 * 1e-4      ## 1/min
    lambda_rel_TU = 1.1 * 1e-4      ## 1/min

    tumorType = "NET"   #NET or MEN
    f_tu = 0.1 * 0.001  #L/min/g
    k_pr = 4.7 * 1e-4   #1/min
    GFR = 0.11  #L/mi



