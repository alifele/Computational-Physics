### These are those data that the corresponding parameters in other organs
### are based on these number. for Example lambda_int in spleen, liver, kidney is
### defined to be lambda_int_tu * 1.7
### So these data are kind of global data that all of the classes in
### organ_init.py file needs to have access to.


class Data:
    TumorData = {
        "lambda_int": 0.001
    }

    MuscleData = {
        "k": 0.02,
    }

    LiverData = {
        "k": MuscleData["k"]*100    ### Used for redmarrow
    }
