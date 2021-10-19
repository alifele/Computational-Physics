function TypeX = initiateFirstTwoSteps(TypeX, TypeTimeCut, TypeV0, dt)
    shape = size(TypeX);
    n_type = shape(1);

    for type = 1:n_type
        TypeX(type,:,1) = TypeTimeCut(type,:);
        TypeX(type,:,2) = TypeX(type,:,1) + TypeV0(type,:)*dt;

    end



end


% 
% def initiateFirstTwoStepsStars(StarsX, StarsTimeCut, StarsV0,dt):
%     for star in range(StarsX.shape[0]):
%         StarsX[star,:,0] = StarsTimeCut[star,:]
%         StarsX[star,:,1] = StarsX[star,:,0] + StarsV0[star]*dt
