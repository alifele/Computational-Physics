
function CoresX = moveCores(CoresX,dt,t, NCores)
    m=1;

    for core_i = 1:NCores
        X = CoresX(core_i,:,t);
        Xpre = CoresX(core_i,:,t-1);

        acceleration = 0;

        for core_j =1:NCores
            if core_i ~= core_j
                Xj = CoresX(core_j,:,t);
                r = Xj - X + 0.01*0;
                acceleration = acceleration + m * (r/(norm(r)^3 + 0.005));
            end
            XNew = acceleration * dt^2 + 2*X - Xpre;
            CoresX(core_i,:,t+1) = XNew;
        end


    end

end




% def moveCores(CoresX, params,t):
%     m=1
%     for core_i in range(CoresX.shape[0]):
%         X = CoresX[core_i, :, t]
%         Xpre = CoresX[core_i, :, t - 1]
%         acceleration = 0
%         for core_j in range(CoresX.shape[0]):
%             if core_i != core_j:
%                 Xj = CoresX[core_j, :, t]
%                 r = Xj - X + 0.01
%                 acceleration += m*((r) / (np.linalg.norm(r) ** 3+0.005))
% 
%         XNew = acceleration * params['dt'] ** 2 + 2 * X - Xpre
%         CoresX[core_i, :, t + 1] = XNew
