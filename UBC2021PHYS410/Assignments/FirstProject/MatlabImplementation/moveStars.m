

function StarsX = moveStars(StarsX, CoresX, dt,t, NStars, NCores)
    
    m = 1;

    for star = 1:NStars
        X = StarsX(star,:,t);
        Xpre = StarsX(star,:,t-1);
        acceleration = 0;

        for core = 1:NCores
            Xj = CoresX(core, :,t);
            r = Xj - X + 0.01;
            acceleration = acceleration + m*(r/(norm(r)^3 + 0.005));
        
        end

        XNew = acceleration * dt^2 + 2*X - Xpre;
        StarsX(star,:,t+1) = XNew;


    end
    



end



% 
% def moveStars(StarsX, CoresX, params,t):
%     m = 1
%     for star in range(StarsX.shape[0]):
%         X = StarsX[star, :, t]
%         Xpre = StarsX[star, :, t - 1]
%         acceleration = 0
%         for core in range(CoresX.shape[0]):
%             Xj = CoresX[core, :, t]
%             r = Xj - X + 0.01
%             acceleration += m*((r) / (np.linalg.norm(r)**3+0.005))
% 
%         XNew = acceleration * params['dt'] ** 2 + 2 * X - Xpre
%         StarsX[star, :, t + 1] = XNew