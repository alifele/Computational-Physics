function [CoresTimeCut, CoresV0] = initiateCores(CoresTimeCut, CoresV0)
    
    %% Initial condition for galaxy collision
    % The following inital conditions are fine tuned to generate visually 
    % decent outputs for the interaction of cores with stars orbiting
    % around them

    CoresTimeCut(1,:) = [-1,1.6,0];
    CoresV0(1,:) = [0.24,0,0];

    CoresTimeCut(2,:) = [1,-1.6,0];
    CoresV0(2,:) = [-0.24,0,0,];

    %% Initial condition for two body test
    % The following initial condition are fine tuned to generate the result
    % for two cores orbiting each other without any stars around them. You
    % sould uncomment the following initial conditions in the case the you
    % want to generate the result of the main galaxy collision.

    r = 2
    CoresTimeCut(1,:) = [0.5*r,0,0];
    CoresV0(1,:) = [0,1/r,0];

    CoresTimeCut(2,:) = [-0.5*r,0,0];
    CoresV0(2,:) = [0,-1/r,0,];

    %% Initial condition for Single Stationary Galaxy
    % The initial condition of the single core with orbiting stars around
    % it. In this section we will have only singe core Stationary core
    CoresTimeCut(1,:) = [0,0,0];
    CoresV0(1,:) = [0.1,0,0];


    %% Initial condition for Single moving Galaxy
    

end

% ([-1,1.6,0], dtype='float')
%     CoresV0[0] = np.array([0.25,0,0]