function ConvergenceTest(tmax)
    clf;

    l=6;
    N_timeSteps6 = 2^l+1;
    dt6 = tmax/(N_timeSteps6-1);
    [StarsX, CoresX6] = Compute(l, tmax);


    l=7;
    N_timeSteps7 = 2^l+1;
    dt7 = tmax/(N_timeSteps7-1);
    [StarsX, CoresX7] = Compute(l, tmax);


    l=8;
    N_timeSteps8 = 2^l+1;
    dt8 = tmax/(N_timeSteps8-1);
    [StarsX, CoresX8] = Compute(l, tmax);



    l=9;
    N_timeSteps9 = 2^l+1;
    dt9 = tmax/(N_timeSteps9-1);
    [StarsX, CoresX9] = Compute(l, tmax);

    CoresX7 = CoresX7(:,:,1:2:end)
    CoresX8 = CoresX8(:,:,1:4:end);
    CoresX9 = CoresX9(:,:,1:8:end);
    
    delta67 = CoresX6 - CoresX7;
    delta78 = CoresX7 - CoresX8;
    delta89 = CoresX8 - CoresX9;

    delta89 = 8*delta89;
    delta78 = 4*delta78;
    
    hold on;
    plot(reshape(delta67(1,1,:),1,[]))
    plot(reshape(delta78(1,1,:),1,[]))
    plot(reshape(delta89(1,1,:),1,[]))

    legend( 'delta67' ,'4*delta78', '8*delta89')
    title("Error Analysis of two body problem")
    xlabel('time')
    ylabel('Error')



    fprintf('done')


end

