### These are those data that the corresponding parameters in other organs
### are based on these number. for Example lambda_int in spleen, liver, kidney is
### defined to be lambda_int_tu * 1.7
### So these data are kind of global data that all of the classes in
### organ_init.py file needs to have access to.


class Data:
    TumorData = {
        "lambda_int": 0.001     ## 1/min
    }

    MuscleData = {
        "k": 0.02   ## L/min/kg --> please see the important note bellow. In a nutshell, /kg is the right unit here
    }

    ## Important Note: In the table of Frenco 2021 paper, the units of k_i are in ml/min/g which is in fact
    ## the permeability surface area product per unit mass of organ. In order to get the permeability of the
    ## organ we need to multipy k_i at the mass of organ (1gr = 1ml). So the calculated PS value will be:
    ## PS = 1000 * k * V  (Note that V is in Litre). So PS will have the units of ml/min. Now to get the standard
    ## units of (L/min) we need to multiply it at 0.001. So PS with standard units (L/min) will be: PS = k*V

    LiverData = {
        "k": MuscleData["k"]*100    ### Used for redmarrow
        ## L/min/kg. See the notes in Data.py file under MuscleData
    }
