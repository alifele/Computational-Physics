
How to run the mode:
    first you need to open the .sbproj file with the simbiology
    model analyzer and then run the program and then export the results of 
    the last run to the matlab work space with name data1
    After this you can run any of the *.m files and generate the results




This folder contains the following files:


GeneralHotColdTimeInterval.sbproj:
    The project file of the simbiology. You need to open this file in the
    simbiology model analyzer and then run the program in order to generate
    the approporate data. Then you need to import data of last run into matlab
    workspace with name data1

Heatmap_original.m:
    Generates heatmap which its X and Y values are different amounts of hot
    and cold values. the color value is the time integrated activity. This
    program will generate these curves for five organs: Liver, Spleen, 
    Kidney, Redmarrow, Tumor. For each organ one figure will be generated
    in each of which we will have four different heatmaps corresponding to 
    0.5, 500, 1000, 1500, and 2000 min time interval between injections


Heatmap_normalized.m:
    This also will generate the similar figures and subplots to the 
    Heatmap_original.m file. But the color value will be TIA(s_i)/TIA(s_0);
    in which TIA(s_i) is the strategy s_i which correspods to an specific 
    injectioin time interval. TIA(s_0) is the time integrated activity for 
    the baseline strategy (which in this case is the 0.5 minute injection).

    I introduce the quantitiy normalized time integrated activity or 
    NTIA(s_i) = TIA(s_i)/TIA(s_0)


metricplots.m:
    I define the following variable as metric
    metric(s_i) = NTIA_OAR(s_i)/NTIA_tumor(s_i)
    I categorize the values of metric into four numerical categories:

    -1 --> NTIA_OAR(s_i)>1 & NTIA_tumor(s_i)<1
    +1 --> NTIA_OAR(s_i)>1 & NTIA_tumor(s_i)<1

    -0.5 --> metric(s_i)>1 & NTIA_OAR(s_i)<1;
    -0.5 --> metric(s_i)>1 & NTIA_tumor>1;

    +0.5 --> metric(s_i)<1 & NTIA_OAR(s_i)>1;
    +0.5 --> metric(s_i)<1 & NTIA_tumor<1;


     NTIA_OAR(s_i)
                 y=x
        |    :-.5/  
        |    :  /   
        | -1 : / .5 
        |    :/     
        |..../......
        |-.5/:
        |  / :  +1  
        | /.5:      
        |/___:______ NTIA_tumor(s_i)

    





