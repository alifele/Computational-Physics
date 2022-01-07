class Data:
    TumorData = {
        "v_int_NET": 0.3,
        "v_v_NET": 0.1,
        "k_NET": 0.2,
        "v_int_menin": 0.23,
        "v_v_menin": 0.11,
        "k_menin": 0.31,
        "lambda_int": 0.001
    }

    MuscleData = {
        "v_v": 0,
        "v_int": 0,
        "k": 0.02,
    }

    KidneyData = {
        "v_v": 0.055,
        "v_int": 0.15,
        "lambda_int": 1.7 * TumorData["lambda_int"]
    }

    ## k_L = 100*k_mu and this equation is included in Organ_init.py
    LiverData = {
        "v_v": 0.085,
        "v_int": 0.2,
        "k": MuscleData["k_mu"] * 100,
        "lambda_int": KidneyData["lambda_int"]
    }

    SpleenData = {
        "v_v": 0.12,
        "v_int": 0.2,
        "k": MuscleData["k_mu"] * 100,
        "lambda_int": KidneyData["lambda_int"]
    }





