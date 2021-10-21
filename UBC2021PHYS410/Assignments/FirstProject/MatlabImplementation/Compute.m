function [StarsX, CoresX] = Compute(l, tmax)
    
    
    
    N_timeSteps = 2^l+1;
    
    dt = tmax/(N_timeSteps-1);

    % Galaxy Collision Initial Condition for Stars
    % Number of stars for the original simulation of the interaction of
    % two cores with stars orbiting them

    NStars1 = 20000;
    NStars2 = 20000;
    NStars = NStars1 + NStars2;
    NCores = 2;

    % Two Body Initial Condition of Stars
    % For the convergence test of the two body problem, we should set the 
    % number of stars to be zero. we need to evaluate simulation for two
    % interacting cores with out any stars.

%     NStars1 = 0;
%     NStars2 = 0;
%     NStars = NStars1 + NStars2;
%     NCores = 2;

    % Single Moving Galaxy Initial Condition
%     NStars1 = 500;
%     NStars2 = 0;
%     NCores = 1;
%     NStars = NStars1 + NStars2;



    
    StarsX = zeros(NStars,3,N_timeSteps);
    CoresX = zeros(NCores,3,N_timeSteps);
    
     StarsV0 = zeros(NStars, 3);
     CoresV0 = zeros(NCores, 3);
     
     StarsTimeCut = zeros(NStars,3);
     CoresTimeCut = zeros(NCores,3);
     
     
     [CoresTimeCut, CoresV0] = initiateCores(CoresTimeCut, CoresV0);
     [StarsTimeCut, StarsV0] = initiateStars(StarsTimeCut, StarsV0, CoresTimeCut, NStars1, NStars2, CoresV0);
%     
%     
%     for t = 1:N_timeSteps
%         
%         for star = 1:NStars
%             StarsX(star,:,t) = rand(1,3);
%         
%         end
% 
%     end
    
     StarsX = initiateFirstTwoSteps(StarsX, StarsTimeCut, StarsV0, dt);
     CoresX = initiateFirstTwoSteps(CoresX, CoresTimeCut, CoresV0, dt);
     
     for t= 2:N_timeSteps-1
         StarsX = moveStars(StarsX, CoresX, dt,t, NStars, NCores);
         CoresX = moveCores(CoresX, dt,t, NCores);
     
     end
% 
%     fprintf("Calculatoin Done!")
%     


end