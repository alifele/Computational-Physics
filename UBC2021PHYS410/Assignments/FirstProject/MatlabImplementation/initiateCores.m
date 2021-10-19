function [CoresTimeCut, CoresV0] = initiateCores(CoresTimeCut, CoresV0)
    
    CoresTimeCut(1,:) = [-1,1.6,0];
    CoresV0(1,:) = [0.24,0,0];


    CoresTimeCut(2,:) = [1,-1.6,0];
    CoresV0(2,:) = [-0.24,0,0,];


    

end

% ([-1,1.6,0], dtype='float')
%     CoresV0[0] = np.array([0.25,0,0]